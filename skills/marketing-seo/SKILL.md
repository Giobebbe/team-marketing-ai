---
name: marketing-seo
description: Audit SEO on-page di una pagina e piano contenuti a 8 settimane con volumi di ricerca reali per l'Italia (DataForSEO). Si attiva con /marketing seo <url>, oppure quando l'utente dice "audit seo", "perché non mi trovano su Google", "che keyword devo usare", "ottimizza questa pagina", "piano seo". Per le attività locali include la sezione dedicata alla scheda Google Business Profile.
---

# /marketing seo

Prende una pagina, controlla come è fatta agli occhi di Google, trova le parole che i clienti usano davvero per cercare (con i volumi veri, non a sensazione) e consegna un piano contenuti di 8 settimane. Pensata per la PMI che dice "su Google non mi trova nessuno".

## Quando si attiva

- `/marketing seo <url>`
- Frasi tipo: "perché non compaio su Google", "fammi l'audit seo", "su cosa devo scrivere per farmi trovare", "sistemami la SEO di questa pagina".
- Utile anche dopo un rifacimento del sito, per controllare di non aver perso le pagine che portavano traffico.

Se manca l'url, chiedilo. Se l'utente indica anche la zona geografica o il servizio principale, usali per orientare le keyword.

## Procedura

1. **Leggi la pagina.** WebFetch dell'url indicato. Se è la homepage, leggi anche 1-2 pagine di servizio o prodotto: spesso la homepage è generica e il potenziale SEO sta nelle pagine interne.

2. **Rileva il tipo di business** (attività locale, e-commerce, servizi B2B, studio professionale, formazione/creator) con gli stessi segnali della skill di analisi. Cambia tutto: per lo Studio dentistico Bianchi di Monza la partita si gioca su "dentista monza" e sulla scheda Google, per Oro del Salento si gioca sulle schede prodotto e sulle ricerche di chi vuole comprare olio online.

3. **Checklist on-page.** Compila la tabella della sezione "Checklist di valutazione" voce per voce, citando il testo reale trovato (il title vero, l'H1 vero), non giudizi astratti.

4. **Intento di ricerca.** Per ogni pagina letta, chiediti cosa sta cercando chi dovrebbe arrivarci: informazione ("come si conserva l'olio"), confronto ("miglior gestionale per officine"), o acquisto ("dentista monza prenota"). Una pagina che vuole vendere ma risponde a un intento informativo non convertirà mai, e va detto.

5. **Keyword candidate.** Costruisci 15-20 keyword candidate mescolando: categoria + città (per le locali), problema del cliente, nome del prodotto, domande frequenti. Nota importante: il pubblico italiano sui temi tech e digitali cerca sia in italiano sia in inglese ("crm per pmi" ma anche "crm tool"), quindi vanno considerate entrambe le lingue tra le candidate.

6. **Volumi VERI.** `python3 scripts/volumi_ricerca.py` con le keyword candidate: torna i volumi di ricerca mensili reali in Italia via DataForSEO. Se lo script stampa che manca la chiave, segui le istruzioni che stampa, prosegui col fallback (stima ragionata via WebSearch e suggerimenti di autocompletamento) e scrivi CHIARAMENTE nel report che i volumi sono stime, non dati misurati.

7. **Sezione locale** (solo se attività locale): valuta la scheda Google Business Profile con la checklist dedicata qui sotto. Per una Trattoria Dal Moro la scheda vale più del sito.

8. **Scrivi `PIANO-SEO.md`** nella directory corrente dell'utente, col template della sezione "Struttura del report". A terminale: i 3 problemi on-page più gravi, le 3 keyword migliori con volume, e il nome del file.

Regola d'oro dei numeri: MAI inventare stime di fatturato o di impatto in euro derivanti dalla SEO. Il traffico si stima, i soldi no: se l'utente non ha dato i suoi numeri, l'impatto si descrive a parole e le ipotesi si dichiarano.

## Checklist di valutazione

On-page, da compilare con quello che c'è davvero sulla pagina:

| Voce | Cosa controllare | Com'è fatta bene |
|-|-|-|
| Title | Presente, unico, sotto i 60 caratteri | Keyword principale + differenza ("Pizzeria a Verona con forno a legna"), non solo il nome dell'azienda |
| Meta description | Presente, sotto i 155 caratteri | Invita al click, contiene la keyword, promette qualcosa di concreto |
| H1 | Uno solo per pagina | Dice cosa offre la pagina, non "Benvenuti" |
| H2 | Struttura logica dei contenuti | Ogni H2 risponde a una domanda che il cliente si fa davvero |
| Alt delle immagini | Presenti e descrittivi | "bottiglia olio extravergine salento 750ml", non "IMG_0234" |
| URL | Corti, leggibili, con la keyword | /olio-extravergine-salento, non /prodotto?id=17 |
| Link interni | Le pagine si linkano tra loro | Dalla pagina servizio al blog e ritorno, con testo del link parlante |
| Contenuto | Quantità e utilità del testo | Risponde alla domanda del cliente meglio dei risultati già in prima pagina, senza muri di testo scritti per Google |

Google Business Profile (solo attività locali):

| Voce | Cosa controllare |
|-|-|
| Categoria | Quella giusta e più specifica (Studio dentistico, non Medico generico) |
| Recensioni | Quante, che media, se il titolare risponde (anche a quelle negative) |
| Foto | Recenti, fatte dal titolare, non solo quelle caricate dai clienti |
| Post | Almeno uno recente: una scheda ferma da mesi sembra un'attività chiusa |
| NAP coerente | Nome, indirizzo e telefono IDENTICI tra sito, scheda Google e directory |

## Struttura del report

```markdown
# Piano SEO

**Pagina analizzata:** www.esempio.it
**Data:** 18 luglio 2026
**Tipo di business:** e-commerce
**Volumi di ricerca:** dati reali DataForSEO / stime (indicare quale)

## Audit on-page

| Voce | Stato | Trovato sulla pagina | Da fare |
|-|-|-|-|
| Title | 🔴 | "Home" | Riscrivere: "Olio extravergine del Salento, spedito in 48 ore" |
| Meta description | 🟡 | ... | ... |
| H1 | ... | ... | ... |
| H2 | ... | ... | ... |
| Alt immagini | ... | ... | ... |
| URL | ... | ... | ... |
| Link interni | ... | ... | ... |
| Contenuto | ... | ... | ... |

## Intento di ricerca

[Per ogni pagina letta: chi ci deve arrivare, cosa sta cercando, se la pagina risponde a quell'intento]

## Le 10 keyword

| # | Keyword | Volume mensile (Italia) | Intento | Dove usarla |
|-|-|-|-|-|
| 1 | ... | ... | acquisto / confronto / informazione | pagina esistente o contenuto nuovo |

[Includere sia keyword in italiano sia in inglese dove il pubblico cerca in entrambe le lingue]

## Scheda Google Business Profile (solo attività locali)

| Voce | Stato | Da fare |
|-|-|-|
| Categoria | ... | ... |
| Recensioni | ... | ... |
| Foto | ... | ... |
| Post | ... | ... |
| NAP coerente | ... | ... |

## Piano contenuti 8 settimane

| Settimana | Contenuto | Keyword target | Formato |
|-|-|-|-|
| 1 | [Prima le correzioni on-page, poi i contenuti nuovi] | ... | pagina / articolo / scheda prodotto |
| 2 | ... | ... | ... |
| ... | ... | ... | ... |
| 8 | ... | ... | ... |

## Ipotesi dichiarate

- [Assunzioni fatte, incluse le keyword con volume stimato e non misurato]
```

## Casi particolari

- **Chiave DataForSEO mancante:** il piano si fa comunque, ma ogni volume va marcato come stima e il report lo dichiara in testa. Riporta all'utente le istruzioni stampate dallo script per attivare i dati reali.
- **Pagina irraggiungibile o resa via JavaScript:** riprova una volta; se non va, chiedi un url alternativo. Niente audit alla cieca.
- **Sito su piattaforma chiusa** (Wix, sito vetrina di terzi): alcune voci on-page non sono modificabili dall'utente. Segnala quali, e sposta il peso del piano su contenuti e scheda Google.
- **Zero contenuti oltre la homepage:** il piano a 8 settimane parte dalla costruzione delle pagine di servizio, prima ancora del blog. Scrivere articoli con una homepage sola è mettere il tetto senza i muri.
- **E-commerce con centinaia di prodotti:** non fare l'audit di tutte le schede. Prendi le 3 più importanti per l'utente (chiedi quali), trova i difetti ricorrenti e scrivi la regola da applicare in serie.
- **Keyword a volume zero:** non scartarle in automatico. Per un B2B di nicchia come OfficinaWeb, una ricerca da 20 al mese fatta dal cliente giusto vale più di mille ricerche generiche. Segnala il volume e lascia la scelta motivata nel piano.
- **Sito in più lingue:** l'audit si fa sulla lingua che porta clienti, quasi sempre l'italiano. Segnala solo se le versioni si pestano i piedi tra loro, con gli stessi title sulle stesse ricerche.
- **L'utente vuole "essere primo su Google" su una parola impossibile:** mostragli il volume e chi occupa oggi la prima pagina, poi proponi la variante più specifica dove può davvero arrivare ("dentista bambini monza" invece di "dentista"). La scelta resta sua, ma con i dati davanti.
