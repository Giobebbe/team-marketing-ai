---
name: marketing-report
description: Genera il report cliente in PDF professionale (REPORT-CLIENTE.pdf) dai report della directory corrente, in stile editoriale di fascia alta - copertina full-bleed, pagella a barre, analisi area per area, radar cliente-vs-concorrente, matrice impatto/sforzo, piano 90 giorni. Impaginato con reportlab (serif Cormorant + DM Sans, carta avorio, accento verde pino). Pensato per consulenti e agenzie. Si attiva con /marketing report seguito dal nome del cliente, oppure "preparami il report per il cliente", "documento da consegnare", "report presentabile", "report PDF", "report con i grafici".
---

# /marketing report [nome cliente]

Il deliverable da presentare a un cliente pagante. Prende i report tecnici della directory corrente, li impacchetta in un **PDF professionale** con grafici veri e li impagina con `scripts/generate_pdf_report.py` (reportlab, brand Gentes). Un titolare di PMI lo legge in dieci minuti e capisce da solo dov'è messo e cosa fare.

Il flusso è quello provato: tu **assembli un JSON** con i dati, lo script lo **stampa in PDF**. Tu non impagini a mano: riempi i campi, lo script fa la grafica sempre uguale.

## Quando si attiva

- `/marketing report Trattoria Dal Moro` (o un altro nome cliente)
- "prepara il documento per il cliente", "report PDF", "report con i grafici", "devo consegnarlo lunedì"

## Cosa legge

I report della suite presenti nella directory corrente: `PAGELLA-MARKETING.md` (necessario per i grafici), `MAPPA-OPPORTUNITA.md`, `ANALISI-COMPETITOR.md`, `PIANO-90-GIORNI.md`, e gli altri se presenti (`PIANO-SEO.md`, `SEQUENZE-EMAIL.md`, `CALENDARIO-SOCIAL.md`, `CAMPAGNE-ADS.md`).

Se non c'è nessun report: "Non c'è niente da impacchettare. Parti da `/marketing analisi`, poi torna qui." Se manca solo la Pagella, avvisa che senza di essa il report esce senza grafici.

## Procedura

1. **Nome cliente e autore.** Prendili dal comando; se mancano, chiedili. Mai segnaposto vuoti in un documento da consegnare. L'autore di default è "Gentes AI".
2. **Leggi i report** presenti e prendi: tipo business, fotografia as-is, i 5 voti della Pagella + Voto Finale, **l'analisi per area** (cosa funziona/manca/fare, con le evidenze citate) dai blocchi degli agenti, **i problemi che costano di più**, la stima del concorrente principale sulle 5 aree, i concorrenti reali trovati, le mosse della Mappa opportunità (con impatto/sforzo/pertinenza), le fasi del piano 90 giorni.
3. **Assembla il JSON** secondo lo schema qui sotto. Scrivi tono da consulente: frasi corte, niente gergo, mai cifre in euro inventate.
4. **Controlla reportlab**: `python3 -c "import reportlab" 2>/dev/null || pip3 install reportlab`.
5. **Genera il PDF**: scrivi il JSON in un file temporaneo e lancia lo script.
   ```bash
   python3 scripts/generate_pdf_report.py /tmp/report_data.json REPORT-CLIENTE.pdf
   ```
6. **Apri il file**: `open REPORT-CLIENTE.pdf` (su mac). Se `open` non c'è, stampa il path.
7. **Pulisci** il JSON temporaneo e consegna all'utente il nome del file e due righe su cosa contiene.

## Schema del JSON (quello che lo script si aspetta)

```json
{
  "cliente": "Trattoria Dal Moro",
  "autore": "Gentes AI",
  "data": "20/07/2026",
  "sottotitolo": "Ristorazione · attività locale · Verona",
  "verdetto": "Una riga netta: la tesi del report (es. 'Cucinate benissimo, non lo sa nessuno').",
  "voto_finale": 5.6,
  "cover_image": "assets/cover-hero.jpg",
  "executive_summary": "2-4 frasi: com'è messo il marketing oggi, le 1-2 leve che pesano di più, il primo passo.",
  "as_is": {
    "cosa_vende": "Cosa vende e a chi, con le parole del sito.",
    "canali": "Da dove arrivano i clienti oggi (solo canali reali).",
    "dove_perde": "Il punto più debole del percorso, in una riga."
  },
  "aree": [
    {"nome": "Messaggio", "voto": 7.5, "nota": "Una riga sul perché di questo voto",
     "analisi": {
       "funziona": "Cosa funziona in quest'area, con l'evidenza citata dal sito.",
       "manca": "Cosa manca, con l'evidenza citata (tra virgolette il testo vero del sito).",
       "fare": ["Azione concreta, con la riscrittura vera dove serve", "...", "..."]}},
    {"nome": "Trovabilità", "voto": 4.0, "nota": "...", "analisi": {"funziona": "...", "manca": "...", "fare": ["..."]}},
    {"nome": "Conversione", "voto": 6.0, "nota": "...", "analisi": {"funziona": "...", "manca": "...", "fare": ["..."]}},
    {"nome": "Concorrenza", "voto": 5.5, "nota": "...", "analisi": {"funziona": "...", "manca": "...", "fare": ["..."]}},
    {"nome": "Crescita",    "voto": 5.0, "nota": "...", "analisi": {"funziona": "...", "manca": "...", "fare": ["..."]}}
  ],
  "problemi": [
    {"titolo": "Il problema detto come lo direbbe il cliente",
     "oggi": "Cosa succede oggi, con l'evidenza.",
     "costa": "Cosa costa, in clienti o occasioni perse (mai euro inventati).",
     "sistema": "Come si sistema, chi lo fa, in quanto tempo."}
  ],
  "competitor_principale": {
    "nome": "Osteria Al Ponte",
    "voti": [6.0, 7.0, 5.0, 6.0, 6.0],
    "lettura": "2-3 frasi: dove il concorrente è avanti e dove no. È una stima dichiarata."
  },
  "competitors": [
    {"nome": "...", "dove": "Verona", "fonte": "Registro imprese", "note": "..."}
  ],
  "opportunita": [
    {"n": 1, "mossa": "...", "impatto": "alto", "sforzo": "basso", "pertinente": "Sì, perché ..."}
  ],
  "piano": {
    "quick":      ["Azione settimana 1-2", "..."],
    "medio":      ["Azione mese 1-2", "..."],
    "strategico": ["Azione mese 2-3", "..."]
  },
  "decisione": {"titolo": "Una cosa sola per partire", "testo": "Il primo passo che il cliente deve approvare."},
  "fonti_dati": ["Registro imprese (openapi.com): ...", "Google Places: ...", "DataForSEO: ..."],
  "nota_esempio": "(solo per report dimostrativi: dichiara che i dati sono illustrativi)"
}
```

Note sui campi:
- `voto_finale` e i `voti` sono su scala **1-10** (una cifra decimale). Semaforo/stato: solido ≥ 8, da rafforzare 5-7.9, critico < 5. Lo script colora da solo.
- **`aree[].analisi`** è la sostanza del report (2 pagine): per ogni area *cosa funziona / cosa manca* con **l'evidenza citata dal sito** (testo vero tra virgolette) e *cosa fare* con **riscritture concrete** (l'H1 riscritto, i titoli, le email). Senza `analisi` l'area finisce solo nella pagella. Prendila dai blocchi degli agenti nella Pagella.
- **`problemi`** = i 2-4 problemi che costano di più, ognuno con oggi/costa/sistema. È la sezione "I problemi che costano di più".
- **`cover_image`** = percorso a una foto per la copertina full-bleed (per la demo `assets/cover-hero.jpg`). Sostituiscila con un'immagine adatta al cliente; se manca, la copertina usa uno sfondo scuro. Deve essere un'immagine con licenza d'uso (Unsplash, foto del cliente, ecc.).
- `competitor_principale.voti` = i 5 voti stimati del concorrente, nell'ordine Messaggio, Trovabilità, Conversione, Concorrenza, Crescita (per il radar). Prendili dalla tabella "Confronto col concorrente principale (stima)" della Pagella. Se non ci sono, ometti `competitor_principale`.
- `opportunita[].impatto` e `sforzo` ∈ {alto, medio, basso} (guidano la matrice). "alto impatto / basso sforzo" = quadrante "Fai subito".
- Ogni campo mancante viene saltato: niente `aree[].analisi` → niente pagine di analisi; niente `problemi` → niente sezione problemi; ecc.

## Cosa produce il PDF

Un documento A4 multipagina in **stile editoriale di fascia alta** (serif Cormorant + DM Sans, carta avorio, accento verde pino), impaginato dallo script. Sezioni numerate I-VII:
- **Copertina** full-bleed con `cover_image`, verdetto in serif e Voto grande.
- **I · Sommario** — executive summary + fotografia as-is + **pagella a barre**.
- **II · Analisi area per area** — la sostanza: per ogni area cosa funziona / cosa manca (con evidenza) / cosa fare (con riscritture). Da `aree[].analisi`.
- **III · I problemi che costano di più** — da `problemi`.
- **IV · Voi e i concorrenti** — **radar** cliente vs concorrente (stima) + tabella dei concorrenti reali.
- **V · Le priorità** — **matrice impatto/sforzo** + tabella delle mosse.
- **VI · Il piano a 90 giorni** — tre fasi + box "decisione richiesta".
- **VII · Metodologia e fonti dei dati** — le 5 aree e le fonti reali (registro imprese, Places, DataForSEO): è ciò che distingue questo report da un'analisi tirata a indovinare.

## Tono (per tutto il testo del JSON)

- Frasi corte, una frase un concetto. Niente gergo da agenzia ("funnel", "friction", "lead gen" → "il percorso", "l'attrito", "raccolta contatti").
- Mai promettere risultati ("l'obiettivo è", non "otterrete"). Mai cifre in euro inventate: valgono solo se nei report con la fonte.
- Del cliente si parla con rispetto anche nei problemi.

## Casi particolari

- **reportlab non installabile**: avvisa l'utente che il PDF richiede reportlab (`pip3 install reportlab`) e fermati; non ripiegare su un formato diverso senza dirlo.
- **Manca la Pagella**: genera un PDF ridotto (copertina + eventuali sezioni disponibili) e avvisa che con `/marketing analisi` escono pagella e radar.
- **Manca la stima concorrente**: ometti `competitor_principale`; il radar mostra solo il cliente.
- **Manca la Mappa opportunità**: ometti `opportunita`; salta la matrice.
- **Report dimostrativo** (azienda ipotetica): compila `nota_esempio` per dichiararlo. Per una prova rapida senza dati: `python3 scripts/generate_pdf_report.py` genera `REPORT-CLIENTE-esempio.pdf`.
- **Numeri in euro**: solo se già nei report con la fonte; ogni stima chiesta dall'utente entra dichiarata come ipotesi.
