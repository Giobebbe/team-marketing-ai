#!/usr/bin/env python3
"""Volumi di ricerca Google (Italia) per una lista di keyword, via DataForSEO.

Interroga l'endpoint live Search Volume di Google Ads
(/v3/keywords_data/google_ads/search_volume/live) con location Italia
(location_code 2380) e lingua italiana, e stampa per ogni keyword il
volume medio mensile, il livello di concorrenza e il CPC.

Limite rigido: massimo 1 chiamata API per esecuzione, massimo 10 keyword
(le eccedenti vengono ignorate con un avviso).

Credenziali richieste: DATAFORSEO_LOGIN e DATAFORSEO_PASSWORD (variabili
d'ambiente o file .env nella cartella principale del progetto).
Registrazione: https://app.dataforseo.com/register

Uso:
    python3 volumi_ricerca.py --keywords "agenzia web vicenza,siti web vicenza" [--json]
"""

import argparse
import base64
import json
import os
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path

URL_API = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
URL_REGISTRAZIONE = "https://app.dataforseo.com/register"
MAX_CHIAMATE = 1
MAX_KEYWORD = 10
COSTO_PER_CHIAMATA_EURO = 0.05
CODICE_ITALIA = 2380  # location_code DataForSEO per l'Italia

CONCORRENZA_IT = {"HIGH": "alta", "MEDIUM": "media", "LOW": "bassa"}


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


def formatta_volume(valore):
    """Formatta un volume con il punto come separatore delle migliaia."""
    if valore is None:
        return "-"
    return f"{int(valore):,}".replace(",", ".")


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


def main():
    parser = argparse.ArgumentParser(
        description="Volumi di ricerca Google in Italia per una lista di keyword "
        "(DataForSEO, 1 chiamata API, massimo 10 keyword)."
    )
    parser.add_argument(
        "--keywords", required=True,
        help='keyword separate da virgola (es. "agenzia web vicenza,siti web vicenza")',
    )
    parser.add_argument("--json", action="store_true", help="stampa la risposta API in JSON grezzo")
    args = parser.parse_args()

    login = carica_chiave("DATAFORSEO_LOGIN")
    password = carica_chiave("DATAFORSEO_PASSWORD")
    if not login or not password:
        print("Mancano le credenziali DataForSEO (variabili DATAFORSEO_LOGIN e DATAFORSEO_PASSWORD).")
        print("Impostale nell'ambiente oppure aggiungile al file .env nella cartella")
        print("principale del progetto (una per riga, formato CHIAVE=valore).")
        print(f"Puoi creare un account qui: {URL_REGISTRAZIONE}")
        sys.exit(1)

    keywords = [parola.strip() for parola in args.keywords.split(",") if parola.strip()]
    if not keywords:
        print("Nessuna keyword valida: passa una lista separata da virgole con --keywords.")
        sys.exit(1)
    if len(keywords) > MAX_KEYWORD:
        print(f"Attenzione: massimo {MAX_KEYWORD} keyword per esecuzione; "
              f"considero solo le prime {MAX_KEYWORD} ({len(keywords) - MAX_KEYWORD} scartate).")
        keywords = keywords[:MAX_KEYWORD]

    credenziali = base64.b64encode(f"{login}:{password}".encode("utf-8")).decode("ascii")
    corpo = json.dumps([{
        "keywords": keywords,
        "location_code": CODICE_ITALIA,
        "language_code": "it",
    }]).encode("utf-8")

    richiesta = urllib.request.Request(
        URL_API,
        data=corpo,
        headers={
            "Authorization": f"Basic {credenziali}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    chiamate = 0
    try:
        # Limite rigido: 1 sola chiamata per esecuzione.
        if chiamate >= MAX_CHIAMATE:
            raise RuntimeError(f"Limite rigido di {MAX_CHIAMATE} chiamata API raggiunto.")
        chiamate += 1
        try:
            contesto = ssl.create_default_context()
            with urllib.request.urlopen(richiesta, timeout=60, context=contesto) as risposta:
                dati = json.loads(risposta.read().decode("utf-8", errors="replace"))
        except urllib.error.HTTPError as errore:
            corpo_errore = errore.read().decode("utf-8", errors="replace")[:500]
            print(f"Errore dall'API DataForSEO (HTTP {errore.code}): {corpo_errore}")
            if errore.code == 401:
                print("Controlla login e password DataForSEO.")
            sys.exit(1)
        except (urllib.error.URLError, TimeoutError, OSError) as errore:
            print(f"Errore di rete verso api.dataforseo.com: {errore}")
            sys.exit(1)

        if dati.get("status_code") != 20000:
            print(f"Errore DataForSEO: {dati.get('status_message', 'risposta inattesa')}")
            sys.exit(1)
        compito = (dati.get("tasks") or [{}])[0]
        if compito.get("status_code") != 20000:
            print(f"Errore nel task DataForSEO: {compito.get('status_message', 'risposta inattesa')}")
            sys.exit(1)

        if args.json:
            print(json.dumps(dati, ensure_ascii=False, indent=2))
            return

        risultati = compito.get("result") or []
        if not risultati:
            print("Nessun dato di volume restituito per le keyword indicate.")
            return

        risultati.sort(key=lambda voce: voce.get("search_volume") or 0, reverse=True)
        righe = []
        for voce in risultati:
            concorrenza = CONCORRENZA_IT.get(voce.get("competition"), voce.get("competition") or "-")
            indice = voce.get("competition_index")
            if indice is not None:
                concorrenza = f"{concorrenza} ({indice})"
            cpc = voce.get("cpc")
            righe.append((
                voce.get("keyword", "-"),
                formatta_volume(voce.get("search_volume")),
                concorrenza,
                f"{cpc:.2f}" if cpc is not None else "-",
            ))

        print("Volumi di ricerca Google in Italia, lingua italiana")
        stampa_tabella(("Keyword", "Volume medio mensile", "Concorrenza", "CPC"), righe)
    finally:
        costo = "fascia gratuita" if chiamate == 0 else \
            ("€{:.2f}".format(chiamate * COSTO_PER_CHIAMATA_EURO)).replace(".", ",")
        print(f"\nChiamate API effettuate: {chiamate} (costo stimato: {costo})")


if __name__ == "__main__":
    main()
