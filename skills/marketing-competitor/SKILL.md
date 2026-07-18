---
name: marketing-competitor
description: Trova i concorrenti VERI di una PMI italiana partendo dal suo sito. Si attiva con /marketing competitor <url>, o quando l'utente chiede chi sono i suoi concorrenti, un confronto con la concorrenza, un'analisi competitiva. Usa registro imprese (openapi.com), Google Places per le attività locali, ricerca web come riserva.
---

# /marketing competitor: i concorrenti veri, non quelli immaginati

Chiunque può chiedere a un'AI "chi sono i miei concorrenti" e ricevere nomi plausibili. Questa skill fa una cosa diversa: legge la P.IVA dal sito, interroga il registro imprese e risponde con aziende che esistono davvero, stessa attività, stessa zona, con sede, dipendenti e fatturato. Per i negozi e i locali usa Google Places: chi fa la stessa cosa nel raggio di pochi chilometri.

## Procedura

### 1. Inquadra l'attività
WebFetch della homepage. Stabilisci: tipo di attività (vedi la regia in `marketing`), città o provincia, cosa vende esattamente. Se l'utente ha passato un nome invece di un URL, prima trova il sito con una ricerca web.

### 2. Scegli la strada giusta

| Situazione | Strada | Script |
|---|---|---|
| Attività locale con vetrina fisica (ristorante, palestra, studio, negozio) | Google Places: stessa categoria nella stessa zona | `competitor_locali.py --categoria "<cat>" --luogo "<città>"` |
| Azienda italiana (e-commerce, B2B, produzione, servizi) | Registro imprese: stesso ATECO, stessa provincia | `estrai_piva.py <url>` poi `competitor_registro.py --piva <piva>` |
| Azienda estera, progetto solo digitale, P.IVA introvabile | Ricerca web: query tipo "alternative a X", "X concorrenti", categorie di prodotto | WebSearch |

Per le attività locali vale la pena fare ANCHE il passaggio dal registro quando la P.IVA c'è: Places dice chi ti ruba i clienti in zona, il registro dice quanto è grosso.

### 3. Tetto di spesa, non negoziabile
Massimo una esecuzione per script in questa skill: una di `competitor_registro.py` (2 chiamate API) e una di `competitor_locali.py` (1 chiamata). Ogni script dichiara da solo il costo a fine run: riportalo nel report. Se un run fallisce, non ritentare a raffica: leggi l'errore, correggi i parametri, un solo nuovo tentativo.

### 4. Guarda in faccia i concorrenti
Dalla lista ottenuta scegli i 3-5 più rilevanti (per vicinanza di attività e dimensione) e apri i loro siti con WebFetch. Per ognuno annota: come si presentano in una riga, prezzi visibili sì o no, punti di forza dichiarati, recensioni e numeri mostrati, cosa fanno meglio del nostro utente e cosa peggio.

### 5. Scrivi ANALISI-COMPETITOR.md

## Struttura del report

```markdown
# Analisi della concorrenza: [nome attività]
Sito: [url] | Data: [data] | Tipo: [tipo attività]
Fonte dati: [registro imprese / Google Places / ricerca web]

## La tua carta d'identità (dal registro imprese)
P.IVA [numero] | ATECO [codice e descrizione] | Sede [comune (provincia)]
Dipendenti: [n] | Fatturato: [ultimo disponibile, se presente]

## Chi c'è in campo
| Concorrente | Comune | Dipendenti | Fatturato | Sito |
|---|---|---|---|---|
[dalla fonte dati: aziende reali, mai inventate. Se un dato manca, cella vuota, non un numero di fantasia]

## Confronto a colpo d'occhio (i 3-5 più vicini a te)
| | Tu | [Conc. 1] | [Conc. 2] | [Conc. 3] |
|---|---|---|---|---|
| Promessa in homepage | | | | |
| Prezzi visibili | | | | |
| Recensioni mostrate | | | | |
| Punto di forza percepito | | | | |

## Dove vinci già
[2-3 punti concreti, con la prova: cosa c'è sul tuo sito che i loro non hanno]

## Dove stai perdendo
[2-3 punti concreti, con la prova presa dai loro siti]

## Le 5 mosse per staccarti
[azioni ordinate per impatto/sforzo: cosa fare, dove, perché funziona contro QUESTI concorrenti]
```

A fine lavoro apri il file e riepiloga a terminale in massimo 10 righe: fonte dati, quanti concorrenti reali trovati, le prime 2 mosse.

## Casi particolari

- **P.IVA non trovata sul sito**: chiedila all'utente prima di passare alla ricerca web, la sa a memoria.
- **Chiave mancante** (lo script lo dice da solo): prosegui con la ricerca web e scrivi nel report che la lista non viene dal registro; suggerisci di configurare la chiave per la prossima volta.
- **Zero concorrenti in provincia**: rilancia allargando alla regione, poi al nazionale; dillo nel report, essere soli in provincia è già un'informazione di posizionamento.
- **Troppi risultati** (ATECO generico): restringi al codice ATECO completo o filtra per fascia di dipendenti simile a quella dell'utente.
- **Nomi da Places senza sito**: tienili comunque in tabella, per un locale il concorrente senza sito ma con 800 recensioni è il più pericoloso di tutti.
