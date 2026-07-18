# CLAUDE.md

Guida per lavorare su questa repo con Claude Code.

## Cos'e' il progetto

Team Marketing AI: suite di skill Claude Code in italiano per il marketing delle PMI italiane. Un comando `/marketing` con sottocomandi (analisi, seo, contenuti, email, social, ads, competitor, piano, report), sei agenti specializzati e script Python che portano dati reali (registro imprese via openapi.com, Google Places, volumi di ricerca DataForSEO). Il modello di valutazione e' la Pagella Marketing: 5 aree (Messaggio, Trovabilita', Conversione, Concorrenza, Crescita), voto da 1 a 10 con semaforo.

## Struttura

```
skills/       una cartella per comando, ognuna con il suo SKILL.md
squadra/      i 6 agenti (stratega-marketing, analista-competitor, specialista-seo,
              copywriter-pmi, esperto-conversioni, media-buyer)
scripts/      estrai_piva.py, competitor_registro.py, competitor_locali.py,
              volumi_ricerca.py (Python 3, solo libreria standard)
install.sh    copia skill, agenti e script in ~/.claude
uninstall.sh  rimuove esattamente cio' che install.sh ha copiato
```

## Come testare gli script

```bash
python3 scripts/estrai_piva.py <url-sito>
```

Nessuna dipendenza da installare: girano con Python 3 puro. Senza chiavi in `.env` stampano un messaggio chiaro e lo script che li invoca ripiega sulla ricerca web.

## Regole

- Stile italiano concreto, frasi che si direbbero a voce. MAI em-dash, ne' come trattino lungo ne' come doppio trattino usato da inciso.
- Mai committare `.env` o chiavi API in nessun file.
- Ogni script mantiene il tetto di 1 o 2 chiamate API per esecuzione e la riga finale con il costo stimato del run. Se modifichi uno script, quel tetto e quella riga restano.
