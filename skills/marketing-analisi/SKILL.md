---
name: marketing-analisi
description: Analisi marketing completa del sito di una PMI italiana, con Pagella Marketing a 5 aree, concorrenti reali presi da registro imprese o Google Places e piano d'azione concreto. Si attiva con /marketing analisi <url>, oppure quando l'utente dice "analizza il mio sito", "fammi la pagella marketing", "come sta messo il mio marketing", "valuta il sito di un cliente". La variante /marketing analisi rapida <url> fa una valutazione veloce solo a terminale, senza agenti e senza file.
---

# /marketing analisi

Il comando di punta della suite. Prende l'url di un sito, capisce che business c'è dietro, va a cercare i concorrenti veri (non quelli immaginati), fa lavorare la squadra di sei agenti in parallelo e consegna una Pagella Marketing con voti, semaforo e le mosse da fare subito.

## Quando si attiva

- `/marketing analisi <url>`: analisi completa con squadra di agenti e report su file.
- `/marketing analisi rapida <url>`: valutazione veloce, solo a terminale.
- Frasi tipo: "analizza il marketing di questo sito", "pagella marketing", "quanto è messo bene questo sito per vendere".

Se manca l'url, chiedilo e fermati lì. Non partire con un'analisi generica.

## Procedura

1. **Leggi il sito.** WebFetch della homepage, poi di 3-5 pagine chiave se esistono: chi siamo, prodotti o servizi, prezzi o listino, contatti, blog. Annota cosa vendono, a chi, con quali parole, e quali inviti all'azione ci sono (telefono, form, carrello, prenotazione).

2. **Rileva il tipo di business.** Scegli uno tra: attività locale, e-commerce, servizi B2B, studio professionale, formazione/creator. Segnali utili:

   | Tipo | Segnali sul sito |
   |-|-|
   | Attività locale | Indirizzo in evidenza, orari, mappa, "vieni a trovarci", prenotazione |
   | E-commerce | Carrello, schede prodotto con prezzo, spedizioni, resi |
   | Servizi B2B | "Richiedi un preventivo", casi studio, pagine per settore, listino assente |
   | Studio professionale | Albo, ordine, "il team", prestazioni, prenota una visita o consulenza |
   | Formazione/creator | Corsi, community, newsletter, link ai social, "iscriviti" |

   Tutti i giudizi delle fasi successive vanno adattati al tipo: a Trattoria Dal Moro di Verona non serve un funnel B2B, serve che chi cerca "trattoria verona centro" la trovi e prenoti.

3. **Dati reali PRIMA del giudizio.** Mai giudicare la concorrenza a memoria. In ordine:
   - `python3 scripts/estrai_piva.py <url>` per tirare fuori la P.IVA dal sito (di solito nel footer o nella privacy policy).
   - Con la P.IVA: `python3 scripts/competitor_registro.py` per il profilo dal registro imprese (ATECO, sede, dipendenti, fatturato depositato) e i concorrenti con stesso ATECO nella stessa provincia.
   - Se il tipo è attività locale: `python3 scripts/competitor_locali.py` per i concorrenti di zona su Google Places, con rating e numero recensioni.
   - Se uno script stampa che manca la chiave API, segui le istruzioni che stampa ma NON bloccarti: prosegui col fallback WebSearch (cerca "categoria + città" e prendi i primi concorrenti veri che emergono), dichiarando nel report che la lista viene dal web e non dal registro.

4. **Lancia la squadra in parallelo.** Sei agenti (installati in `~/.claude/agents`), tutti nello stesso blocco, ognuno col suo mandato. Passa a ciascuno: sintesi del sito, tipo di business, lista dei concorrenti reali trovati al passo 3.

   | Agente | Mandato | Voto assegnato |
   |-|-|-|
   | stratega-marketing | Chiarezza dell'offerta e leve di crescita | Messaggio, Crescita |
   | specialista-seo | Visibilità su Google e presenza locale | Trovabilità |
   | esperto-conversioni | Percorso dal visitatore al contatto o alla vendita | Conversione |
   | analista-competitor | Confronto con i concorrenti reali del passo 3 | Concorrenza |
   | copywriter-pmi | Riscritture concrete di titoli e testi deboli | Nessuno (contributo qualitativo) |
   | media-buyer | Dove avrebbe senso spendere in pubblicità, e se ha senso ora | Nessuno (contributo qualitativo) |

   Ogni voto va da 1 a 10, una cifra decimale ammessa, e deve essere motivato con esempi presi dal sito, non con frasi generiche.

5. **Sintesi e pagella.** Raccogli i voti, calcola il Voto Finale come media semplice delle 5 aree, assegna il semaforo per area (verde 8-10, giallo 5-7.9, rosso sotto 5) e scrivi `PAGELLA-MARKETING.md` nella directory corrente dell'utente, seguendo il template qui sotto. Le riscritture del copywriter e le note del media-buyer entrano nel dettaglio delle aree pertinenti.

6. **Chiudi a terminale.** Voto finale, semaforo delle 5 aree in una riga, le 3 mosse della settimana, e il nome del file salvato.

## Variante rapida

`/marketing analisi rapida <url>`: solo WebFetch della homepage, nessun agente, nessuno script, nessun file. Stampi a terminale, in massimo 25 righe: tipo di business, pagella STIMATA (dichiarata come tale, riga per area con voto e semaforo), le 2-3 cose più urgenti. Serve per farsi un'idea in un minuto, non sostituisce l'analisi completa.

## Checklist di valutazione

Cosa guarda ogni area, e come si distribuiscono i voti:

| Area | Domanda chiave | Da 8 in su | Sotto il 5 |
|-|-|-|-|
| Messaggio | Si capisce in 5 secondi cosa vendi e a chi? | Offerta chiara sopra la piega, cliente tipo evidente | Slogan vaghi, si capisce il settore ma non l'offerta |
| Trovabilità | Chi ti cerca su Google ti trova? | Title e contenuti sulle ricerche giuste, presenza locale curata | Invisibile sulle ricerche di categoria, scheda Google assente o abbandonata |
| Conversione | Il visitatore sa cosa fare dopo? | Un invito all'azione chiaro per pagina, contatto raggiungibile in un click | Nessun invito, form chilometrici, telefono introvabile |
| Concorrenza | Perché scegliere te e non gli altri? | Differenza concreta e dichiarata rispetto ai concorrenti reali | Sito fotocopia dei concorrenti, nessun motivo per preferirti |
| Crescita | Da dove arrivano clienti nuovi e ricorrenti? | Più canali attivi, riacquisto o passaparola coltivati | Un canale solo, nessun modo di ricontattare chi è già passato |

Semaforo: verde 8-10, giallo 5-7.9, rosso sotto 5. Voto Finale = media semplice delle 5 aree.

Regola d'oro dei numeri: MAI inventare stime di fatturato o di impatto in euro. Se l'utente non ha fornito i suoi numeri, le conseguenze si descrivono a parole ("più richieste di preventivo", "più prenotazioni nel weekend") e le ipotesi si dichiarano nel report.

## Struttura del report

```markdown
# Pagella Marketing

**Sito:** www.esempio.it
**Data:** 18 luglio 2026
**Tipo di business:** attività locale

## La pagella

| Area | Voto | Semaforo | In una riga |
|-|-|-|-|
| Messaggio | 7.5 | 🟡 | Si capisce cosa fai, meno per chi |
| Trovabilità | 4.0 | 🔴 | Scheda Google ferma da due anni |
| Conversione | 6.0 | 🟡 | Il telefono c'è ma è nascosto nel footer |
| Concorrenza | 5.5 | 🟡 | Stessi argomenti dei tre concorrenti di zona |
| Crescita | 5.0 | 🟡 | Tutto poggia sul passaparola spontaneo |

**Voto Finale: 5.6** (media semplice delle 5 aree)

## Le 3 mosse di questa settimana

1. [Azione concreta, fattibile in poche ore, con l'area che migliora]
2. [Seconda azione]
3. [Terza azione]

## Il piano del mese

- Settimana 1: ...
- Settimana 2: ...
- Settimana 3: ...
- Settimana 4: ...

## Dettaglio per area

### Messaggio (7.5)
Cosa funziona: ...
Cosa manca: ...
Cosa fare: ... [qui entrano le riscritture proposte dal copywriter-pmi]

### Trovabilità (4.0)
...

### Conversione (6.0)
...

### Concorrenza (5.5)
Confronto puntuale con i concorrenti reali della tabella sotto: cosa fanno meglio loro, cosa fai meglio tu.

### Crescita (5.0)
... [qui entrano le note del media-buyer: dove spendere, o perché non spendere ancora]

## I concorrenti reali trovati

| Nome | Dove | Fonte | Note |
|-|-|-|-|
| ... | ... | Registro imprese / Google Places / WebSearch | ... |

## Ipotesi dichiarate

- [Ogni assunzione fatta in assenza di numeri forniti dall'utente, scritta a parole]
```

## Casi particolari

- **Sito irraggiungibile o tutto in JavaScript:** riprova una volta, poi chiedi all'utente un url alternativo o una descrizione dell'attività. Mai valutare un sito che non hai letto.
- **P.IVA non trovata:** capita con i siti su piattaforme tipo Wix o con footer minimali. Salta il registro imprese e passa direttamente a competitor_locali.py (se attività locale) o al fallback WebSearch, dichiarandolo nel report.
- **Chiavi API mancanti:** lo script stampa le istruzioni per ottenerle. Riportale all'utente a fine analisi, ma completa comunque la pagella col fallback: un'analisi con concorrenti presi dal web vale più di nessuna analisi.
- **Un agente fallisce o torna vuoto:** rilancia solo quello, con lo stesso contesto. Se fallisce di nuovo, compila tu la sua area segnandola come "valutata senza agente dedicato".
- **Sito multi-attività** (esempio: OfficinaWeb di Bologna che fa sia siti sia campagne pubblicitarie): chiedi all'utente su quale linea concentrare la pagella. Se non risponde, valuta quella più in evidenza in homepage e dichiaralo.
- **Sito appena nato, quasi vuoto:** la pagella si fa lo stesso, ma il piano del mese diventa un piano di costruzione (prima le fondamenta: messaggio e scheda Google, poi il resto).
- **L'utente fornisce i suoi numeri** (fatturato, margini, valore del cliente medio): usali per dare priorità alle mosse, citandoli come "numeri forniti dall'utente". Senza numeri, niente cifre in euro nel report.
