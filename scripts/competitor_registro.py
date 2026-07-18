#!/usr/bin/env python3
"""Trova i competitor di un'azienda italiana nel registro imprese (Openapi).

Partendo da una partita IVA (o da un dominio, da cui la P.IVA viene
estratta gratis con estrai_piva.py) recupera il profilo aziendale da
company.openapi.com e poi cerca le aziende con lo stesso codice ATECO
nella stessa provincia.

Limite rigido: massimo 2 chiamate API per esecuzione
(1 profilo + 1 ricerca), per tenere i costi sotto controllo.

Chiave richiesta: OPENAPI_TOKEN (variabile d'ambiente o file .env nella
cartella principale del progetto). Registrazione: https://console.openapi.com/

Uso:
    python3 competitor_registro.py --piva 01234567890 [--provincia VI] [--max 10] [--json]
    python3 competitor_registro.py --dominio esempio.it [--provincia VI] [--max 10] [--json]
"""

import argparse
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# Rende importabile estrai_piva.py dalla stessa cartella.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from estrai_piva import estrai_piva, valida_piva  # noqa: E402

BASE_API = "https://company.openapi.com"
# Con OPENAPI_SANDBOX=1 (ambiente o .env) si usa l'ambiente di test di Openapi:
# credito virtuale e dati fittizi, utile finche' il KYC di produzione non e' approvato.
BASE_API_SANDBOX = "https://test.company.openapi.com"
URL_REGISTRAZIONE = "https://console.openapi.com/"
MAX_CHIAMATE = 2
COSTO_PER_CHIAMATA_EURO = 0.10  # stima prudente, dipende dal listino Openapi

CHIAVI_DENOMINAZIONE = ["companyName", "denominazione", "businessName", "ragioneSociale"]
CHIAVI_ATECO = ["atecoCode", "codiceAteco", "ateco"]
CHIAVI_PROVINCIA = ["province", "provincia", "provinceCode"]
CHIAVI_COMUNE = ["municipality", "comune", "town", "city"]
CHIAVI_DIPENDENTI = ["employees", "dipendenti", "numberOfEmployees"]
CHIAVI_FATTURATO = ["turnover", "fatturato", "revenue"]
CHIAVI_PIVA = ["vatCode", "vatNumber", "piva", "taxCode"]


class ContatoreChiamate:
    """Conta le chiamate API e blocca l'esecuzione oltre il limite."""

    def __init__(self, massimo):
        self.massimo = massimo
        self.effettuate = 0

    def registra(self):
        if self.effettuate >= self.massimo:
            raise RuntimeError(
                f"Limite rigido di {self.massimo} chiamate API per esecuzione raggiunto."
            )
        self.effettuate += 1


def carica_chiave(nome):
    """Legge una chiave dall'ambiente o dal file .env alla radice del progetto.

    Il valore non viene mai stampato.
    """
    valore = os.environ.get(nome, "").strip()
    if valore:
        return valore
    percorso_env = Path(__file__).resolve().parent.parent / ".env"
    if percorso_env.is_file():
        try:
            for riga in percorso_env.read_text(encoding="utf-8").splitlines():
                riga = riga.strip()
                if not riga or riga.startswith("#") or "=" not in riga:
                    continue
                chiave, _, val = riga.partition("=")
                if chiave.strip() == nome:
                    val = val.strip().strip("'\"")
                    return val or None
        except OSError:
            pass
    return None


def chiama_api(url, token, contatore):
    """Esegue una GET autenticata verso Openapi e restituisce il JSON."""
    contatore.registra()
    richiesta = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "User-Agent": "team-marketing-ai/1.0",
        },
    )
    try:
        contesto = ssl.create_default_context()
        with urllib.request.urlopen(richiesta, timeout=30, context=contesto) as risposta:
            return json.loads(risposta.read().decode("utf-8", errors="replace"))
    except urllib.error.HTTPError as errore:
        corpo = errore.read().decode("utf-8", errors="replace")[:500]
        try:
            messaggio = json.loads(corpo).get("message", corpo)
        except (json.JSONDecodeError, AttributeError):
            messaggio = corpo
        print(f"Errore dall'API Openapi (HTTP {errore.code}): {messaggio}")
        if errore.code in (401, 403):
            print("Controlla che il token OPENAPI_TOKEN sia valido e abbia lo scope 'company'.")
        sys.exit(1)
    except (urllib.error.URLError, TimeoutError, OSError) as errore:
        print(f"Errore di rete verso company.openapi.com: {errore}")
        sys.exit(1)


def cerca_campo(oggetto, nomi):
    """Cerca in ampiezza la prima chiave tra `nomi` dentro dict/list annidati."""
    coda = [oggetto]
    while coda:
        corrente = coda.pop(0)
        if isinstance(corrente, dict):
            for nome in nomi:
                if nome in corrente and corrente[nome] not in (None, "", [], {}):
                    return corrente[nome]
            coda.extend(corrente.values())
        elif isinstance(corrente, list):
            coda.extend(corrente)
    return None


def appiattisci(valore):
    """Riduce a testo un campo che può essere un dict annidato (es. ateco)."""
    if valore is None:
        return "-"
    if isinstance(valore, dict):
        for chiave in ("code", "codice", "value", "number", "amount", "description"):
            if valore.get(chiave) not in (None, "", [], {}):
                return str(valore[chiave])
        return "-"
    if isinstance(valore, list):
        return appiattisci(valore[0]) if valore else "-"
    return str(valore)


def tronca(testo, massimo=40):
    testo = str(testo)
    return testo if len(testo) <= massimo else testo[: massimo - 1] + "…"


def stampa_tabella(intestazioni, righe):
    """Stampa una tabella allineata su stdout."""
    larghezze = [len(voce) for voce in intestazioni]
    for riga in righe:
        for indice, cella in enumerate(riga):
            larghezze[indice] = max(larghezze[indice], len(str(cella)))
    formato = "  ".join("{:<" + str(l) + "}" for l in larghezze)
    print(formato.format(*intestazioni))
    print(formato.format(*("-" * l for l in larghezze)))
    for riga in righe:
        print(formato.format(*(str(cella) for cella in riga)))


def costo_stimato(chiamate):
    if chiamate == 0:
        return "fascia gratuita"
    return ("€{:.2f}".format(chiamate * COSTO_PER_CHIAMATA_EURO)).replace(".", ",")


def main():
    parser = argparse.ArgumentParser(
        description="Trova i competitor di un'azienda italiana (stesso ATECO, "
        "stessa provincia) tramite l'API Company di Openapi. Massimo 2 chiamate API."
    )
    gruppo = parser.add_mutually_exclusive_group(required=True)
    gruppo.add_argument("--piva", help="partita IVA dell'azienda (11 cifre, con o senza prefisso IT)")
    gruppo.add_argument("--dominio", help="dominio del sito aziendale da cui estrarre la P.IVA (gratis)")
    parser.add_argument("--provincia", help="sigla provincia per la ricerca (es. VI); default: quella dell'azienda")
    parser.add_argument("--max", type=int, default=10, help="numero massimo di competitor (default 10)")
    parser.add_argument("--json", action="store_true", help="stampa le risposte API in JSON grezzo")
    args = parser.parse_args()

    token = carica_chiave("OPENAPI_TOKEN")
    base_api = BASE_API
    if carica_chiave("OPENAPI_SANDBOX") == "1":
        base_api = BASE_API_SANDBOX
        print("ATTENZIONE: ambiente SANDBOX attivo, i dati restituiti sono di test.\n")
    if not token:
        print("Manca la chiave API di Openapi (variabile OPENAPI_TOKEN).")
        print("Impostala nell'ambiente oppure aggiungi la riga OPENAPI_TOKEN=... al file .env")
        print("nella cartella principale del progetto.")
        print(f"Puoi creare un account e generare il token qui: {URL_REGISTRAZIONE}")
        sys.exit(1)

    if args.dominio:
        print(f"Estraggo la partita IVA dal sito {args.dominio} (nessun costo)...")
        esito = estrai_piva(args.dominio)
        if esito is None:
            print("Non sono riuscito a trovare una partita IVA valida sul sito indicato.")
            print("Riprova passando direttamente --piva.")
            sys.exit(1)
        piva = esito["piva"]
        print(f"Partita IVA trovata: {piva} (fonte: {esito['pagina_fonte']})\n")
    else:
        piva = re.sub(r"^\s*IT\s*", "", args.piva.strip(), flags=re.IGNORECASE)
        if not valida_piva(piva):
            print(f"'{args.piva}' non è una partita IVA italiana valida (cifra di controllo errata).")
            sys.exit(1)

    contatore = ContatoreChiamate(MAX_CHIAMATE)
    try:
        # Chiamata 1: profilo aziendale dalla P.IVA.
        risposta_profilo = chiama_api(f"{base_api}/IT-advanced/{piva}", token, contatore)
        profilo = risposta_profilo.get("data", risposta_profilo)
        if isinstance(profilo, list):
            profilo = profilo[0] if profilo else {}

        denominazione = appiattisci(cerca_campo(profilo, CHIAVI_DENOMINAZIONE))
        ateco = appiattisci(cerca_campo(profilo, CHIAVI_ATECO))
        provincia = args.provincia or appiattisci(cerca_campo(profilo, CHIAVI_PROVINCIA))
        comune = appiattisci(cerca_campo(profilo, CHIAVI_COMUNE))
        dipendenti = appiattisci(cerca_campo(profilo, CHIAVI_DIPENDENTI))
        fatturato = appiattisci(cerca_campo(profilo, CHIAVI_FATTURATO))

        # Chiamata 2: ricerca competitor con stesso ATECO nella stessa provincia.
        # dataEnrichment e' OBBLIGATORIO per avere i dati: senza, tornano solo gli id.
        # "start" = dataset base (denominazione, ATECO, sede); "advanced" costa di piu'.
        parametri = {
            "limit": max(1, min(args.max, 50)),
            "dataEnrichment": "start",
            "activityStatus": "ATTIVA",
        }
        if ateco != "-":
            parametri["atecoCode"] = ateco
        if provincia != "-":
            parametri["province"] = provincia
        if "atecoCode" not in parametri and "province" not in parametri:
            print("Il profilo non contiene né codice ATECO né provincia: impossibile cercare competitor.")
            sys.exit(1)

        url_ricerca = f"{base_api}/IT-search?{urllib.parse.urlencode(parametri)}"
        risposta_ricerca = chiama_api(url_ricerca, token, contatore)
        elenco = risposta_ricerca.get("data", risposta_ricerca)
        if not isinstance(elenco, list):
            elenco = [elenco] if elenco else []

        if args.json:
            print(json.dumps(
                {"profilo": risposta_profilo, "competitor": risposta_ricerca},
                ensure_ascii=False, indent=2,
            ))
            return

        print("Profilo azienda")
        stampa_tabella(
            ("Campo", "Valore"),
            [
                ("Denominazione", denominazione),
                ("Partita IVA", piva),
                ("Codice ATECO", ateco),
                ("Comune", comune),
                ("Provincia", provincia),
                ("Dipendenti", dipendenti),
                ("Fatturato", fatturato),
            ],
        )

        righe = []
        for azienda in elenco:
            piva_azienda = appiattisci(cerca_campo(azienda, CHIAVI_PIVA))
            if piva_azienda == piva:
                continue  # esclude l'azienda di partenza dai competitor
            righe.append((
                tronca(appiattisci(cerca_campo(azienda, CHIAVI_DENOMINAZIONE))),
                appiattisci(cerca_campo(azienda, CHIAVI_ATECO)),
                appiattisci(cerca_campo(azienda, CHIAVI_COMUNE)),
                appiattisci(cerca_campo(azienda, CHIAVI_DIPENDENTI)),
                appiattisci(cerca_campo(azienda, CHIAVI_FATTURATO)),
            ))

        print(f"\nCompetitor trovati: {len(righe)}")
        if righe:
            stampa_tabella(("Denominazione", "ATECO", "Comune", "Dipendenti", "Fatturato"), righe)
    finally:
        print(f"\nChiamate API effettuate: {contatore.effettuate} "
              f"(costo stimato: {costo_stimato(contatore.effettuate)})")


if __name__ == "__main__":
    main()
