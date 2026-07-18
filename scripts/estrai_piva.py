#!/usr/bin/env python3
"""Estrae e valida la partita IVA italiana dal sito web di un'azienda.

Scarica la homepage e, se la P.IVA non è lì, prova le pagine dove di
solito compare (privacy, contatti, chi siamo, note legali). Ogni numero
candidato viene validato con l'algoritmo ufficiale della cifra di
controllo (formula di Luhn: cifre in posizione dispari sommate così come
sono, cifre in posizione pari raddoppiate sottraendo 9 se il doppio
supera 9, totale divisibile per 10).

Non usa nessuna API a pagamento: solo richieste HTTP alle pagine del sito.

Uso:
    python3 estrai_piva.py https://www.esempio.it [--json]
"""

import argparse
import json
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)

# Pagine tipiche in cui i siti italiani riportano la partita IVA.
PAGINE_EXTRA = [
    "/privacy",
    "/privacy-policy",
    "/contatti",
    "/contact",
    "/chi-siamo",
    "/note-legali",
]

# Numero di 11 cifre vicino a un'etichetta tipo "P.IVA", "Partita IVA", "VAT".
RE_CON_ETICHETTA = re.compile(
    r"(?:p\.?\s*iva|partita\s+iva|piva|vat(?:\s*(?:number|no\.?|id|reg\.?))?)"
    r"[^0-9]{0,25}(\d{11})",
    re.IGNORECASE,
)

# Numero di 11 cifre con il prefisso paese "IT" (es. IT01234567890).
RE_PREFISSO_IT = re.compile(r"\bIT\s?(\d{11})\b")


def valida_piva(piva):
    """Verifica la cifra di controllo di una partita IVA italiana.

    Algoritmo ufficiale (Luhn): X = somma delle cifre in posizione dispari
    (1ª, 3ª, ... contando da 1); Y = somma dei doppi delle cifre in
    posizione pari, sottraendo 9 quando il doppio supera 9. Il numero è
    valido se (X + Y) è divisibile per 10.
    """
    if not re.fullmatch(r"\d{11}", piva or ""):
        return False
    totale = 0
    for indice, carattere in enumerate(piva):
        cifra = int(carattere)
        if indice % 2 == 0:  # posizioni dispari contando da 1
            totale += cifra
        else:  # posizioni pari contando da 1
            doppio = cifra * 2
            totale += doppio - 9 if doppio > 9 else doppio
    return totale % 10 == 0


def normalizza_url(url):
    """Aggiunge lo schema https:// se manca."""
    url = url.strip()
    if "://" not in url:
        url = "https://" + url
    return url


def scarica(url):
    """Scarica una pagina (max 2 MB) fingendosi un browser. None se fallisce."""
    richiesta = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept-Language": "it-IT,it;q=0.9,en;q=0.6",
        },
    )
    try:
        contesto = ssl.create_default_context()
        with urllib.request.urlopen(richiesta, timeout=15, context=contesto) as risposta:
            grezzo = risposta.read(2_000_000)
    except (urllib.error.URLError, TimeoutError, ssl.SSLError, OSError, ValueError):
        return None
    return grezzo.decode("utf-8", errors="replace")


def estrai_testo(html):
    """Toglie script, style e tag HTML per cercare la P.IVA nel testo visibile."""
    testo = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", html)
    testo = re.sub(r"<[^>]+>", " ", testo)
    return re.sub(r"\s+", " ", testo)


def trova_candidate(html):
    """Restituisce i numeri candidati in ordine di affidabilità, senza doppioni."""
    testo = estrai_testo(html)
    candidate = []
    for espressione in (RE_CON_ETICHETTA, RE_PREFISSO_IT):
        for fonte in (testo, html):
            for numero in espressione.findall(fonte):
                if numero not in candidate:
                    candidate.append(numero)
    return candidate


def estrai_piva(url):
    """Cerca una partita IVA valida sul sito. Restituisce un dict o None.

    Il dict ha le chiavi: url, piva, pagina_fonte.
    """
    url = normalizza_url(url)
    parti = urllib.parse.urlsplit(url)
    base = f"{parti.scheme}://{parti.netloc}"
    pagine = [url]
    for percorso in PAGINE_EXTRA:
        pagina = base + percorso
        if pagina not in pagine:
            pagine.append(pagina)
    for pagina in pagine:
        html = scarica(pagina)
        if not html:
            continue
        for candidata in trova_candidate(html):
            if valida_piva(candidata):
                return {"url": url, "piva": candidata, "pagina_fonte": pagina}
    return None


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
        description="Estrae la partita IVA italiana dal sito di un'azienda "
        "(nessuna API a pagamento, nessuna chiave richiesta)."
    )
    parser.add_argument("url", help="URL del sito aziendale (es. https://www.esempio.it)")
    parser.add_argument("--json", action="store_true", help="stampa il risultato in JSON grezzo")
    args = parser.parse_args()

    esito = estrai_piva(args.url)

    if esito is None:
        print("Nessuna partita IVA valida trovata sul sito indicato.")
        print("Ho controllato la homepage e le pagine tipiche (privacy, contatti, note legali).")
        print("\nChiamate API effettuate: 0 (costo stimato: fascia gratuita)")
        sys.exit(1)

    if args.json:
        print(json.dumps(esito, ensure_ascii=False, indent=2))
    else:
        stampa_tabella(
            ("Campo", "Valore"),
            [
                ("Sito", esito["url"]),
                ("Partita IVA", esito["piva"]),
                ("Pagina fonte", esito["pagina_fonte"]),
            ],
        )
        print("\nPartita IVA valida secondo l'algoritmo ufficiale della cifra di controllo.")

    print("\nChiamate API effettuate: 0 (costo stimato: fascia gratuita)")


if __name__ == "__main__":
    main()
