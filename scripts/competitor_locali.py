#!/usr/bin/env python3
"""Trova i competitor locali di un'attività con Google Places API (New).

Fa UNA sola ricerca testuale ("categoria a luogo") e stampa la classifica
dei risultati ordinata per forza della reputazione: valutazione media
moltiplicata per il logaritmo del numero di recensioni (così 4,5 stelle
con 800 recensioni batte 5,0 stelle con 3 recensioni).

Limite rigido: massimo 1 chiamata API per esecuzione.

Chiave richiesta: GOOGLE_PLACES_API_KEY (variabile d'ambiente o file .env
nella cartella principale del progetto), con "Places API (New)" attiva.
Attivazione: https://console.cloud.google.com/google/maps-apis

Uso:
    python3 competitor_locali.py --categoria "ristorante" --luogo "Vicenza" [--max 15] [--json]
"""

import argparse
import json
import math
import os
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path

URL_API = "https://places.googleapis.com/v1/places:searchText"
URL_REGISTRAZIONE = "https://console.cloud.google.com/google/maps-apis"
MAX_CHIAMATE = 1
COSTO_PER_CHIAMATA_EURO = 0.03  # SKU Enterprise Text Search, stima

# Solo i campi necessari: la FieldMask determina anche il costo della chiamata.
FIELD_MASK = (
    "places.displayName,places.rating,places.userRatingCount,"
    "places.formattedAddress,places.websiteUri,places.priceLevel"
)

LIVELLI_PREZZO = {
    "PRICE_LEVEL_FREE": "gratis",
    "PRICE_LEVEL_INEXPENSIVE": "€",
    "PRICE_LEVEL_MODERATE": "€€",
    "PRICE_LEVEL_EXPENSIVE": "€€€",
    "PRICE_LEVEL_VERY_EXPENSIVE": "€€€€",
}


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


def punteggio(posto):
    """Reputazione = valutazione x log(recensioni + 1)."""
    voto = posto.get("rating") or 0.0
    recensioni = posto.get("userRatingCount") or 0
    return voto * math.log(recensioni + 1)


def tronca(testo, massimo=45):
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


def main():
    parser = argparse.ArgumentParser(
        description="Trova i competitor locali di un'attività con Google Places "
        "API (New). Massimo 1 chiamata API per esecuzione."
    )
    parser.add_argument("--categoria", required=True, help='tipo di attività (es. "ristorante")')
    parser.add_argument("--luogo", required=True, help='città o zona (es. "Vicenza")')
    parser.add_argument(
        "--raggio-m", type=int, default=10000,
        help="raggio in metri (accettato per compatibilità: la ricerca testuale "
        "usa il luogo nel testo, non le coordinate)",
    )
    parser.add_argument("--max", type=int, default=15, help="numero massimo di risultati (default 15, tetto 20)")
    parser.add_argument("--json", action="store_true", help="stampa la risposta API in JSON grezzo")
    args = parser.parse_args()

    chiave = carica_chiave("GOOGLE_PLACES_API_KEY")
    if not chiave:
        print("Manca la chiave API di Google Places (variabile GOOGLE_PLACES_API_KEY).")
        print("Impostala nell'ambiente oppure aggiungi la riga GOOGLE_PLACES_API_KEY=...")
        print("al file .env nella cartella principale del progetto.")
        print(f"Puoi crearla (attivando \"Places API (New)\") qui: {URL_REGISTRAZIONE}")
        sys.exit(1)

    corpo = json.dumps({
        "textQuery": f"{args.categoria} a {args.luogo}",
        "pageSize": max(1, min(args.max, 20)),
        "languageCode": "it",
        "regionCode": "IT",
    }).encode("utf-8")

    richiesta = urllib.request.Request(
        URL_API,
        data=corpo,
        headers={
            "Content-Type": "application/json",
            "X-Goog-Api-Key": chiave,
            "X-Goog-FieldMask": FIELD_MASK,
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
            with urllib.request.urlopen(richiesta, timeout=30, context=contesto) as risposta:
                dati = json.loads(risposta.read().decode("utf-8", errors="replace"))
        except urllib.error.HTTPError as errore:
            corpo_errore = errore.read().decode("utf-8", errors="replace")[:500]
            try:
                messaggio = json.loads(corpo_errore).get("error", {}).get("message", corpo_errore)
            except (json.JSONDecodeError, AttributeError):
                messaggio = corpo_errore
            print(f"Errore dall'API Google Places (HTTP {errore.code}): {messaggio}")
            if errore.code in (401, 403):
                print("Controlla che la chiave sia valida e che \"Places API (New)\" sia attiva sul progetto.")
            sys.exit(1)
        except (urllib.error.URLError, TimeoutError, OSError) as errore:
            print(f"Errore di rete verso places.googleapis.com: {errore}")
            sys.exit(1)

        if args.json:
            print(json.dumps(dati, ensure_ascii=False, indent=2))
            return

        posti = dati.get("places", [])
        if not posti:
            print(f"Nessun risultato per \"{args.categoria}\" a {args.luogo}.")
            return

        posti.sort(key=punteggio, reverse=True)
        righe = []
        for posto in posti:
            voto = posto.get("rating")
            righe.append((
                tronca(posto.get("displayName", {}).get("text", "-"), 35),
                f"{voto:.1f}" if voto is not None else "-",
                posto.get("userRatingCount", "-"),
                LIVELLI_PREZZO.get(posto.get("priceLevel"), "-"),
                tronca(posto.get("websiteUri", "-"), 40),
                tronca(posto.get("formattedAddress", "-"), 45),
            ))

        print(f"Competitor locali per \"{args.categoria}\" a {args.luogo} "
              "(ordinati per valutazione x log recensioni)")
        stampa_tabella(
            ("Nome", "Valutazione", "Recensioni", "Prezzo", "Sito", "Indirizzo"),
            righe,
        )
    finally:
        costo = "fascia gratuita" if chiamate == 0 else \
            ("€{:.2f}".format(chiamate * COSTO_PER_CHIAMATA_EURO)).replace(".", ",")
        print(f"\nChiamate API effettuate: {chiamate} (costo stimato: {costo})")


if __name__ == "__main__":
    main()
