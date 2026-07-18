---
name: marketing-contenuti
description: Piano editoriale di 30 giorni per una PMI italiana, con 3 pilastri derivati da ciò che il cliente compra, il canale principale giusto per il tipo di business, 12 idee concrete e il riciclo di ogni contenuto su 2 canali secondari. Si attiva con /marketing contenuti <url o descrizione attività>, oppure quando l'utente dice "piano editoriale", "cosa pubblico questo mese", "idee di contenuto", "calendario contenuti", "non so cosa postare".
---

# /marketing contenuti

Costruisce un piano editoriale di 30 giorni che parte da una domanda sola: cosa compra il cliente, e cosa deve credere per comprarlo? Da lì escono i pilastri, il canale giusto e 12 idee pronte da produrre. Non un elenco di "post motivazionali del lunedì": idee legate a quello che l'azienda vende.

## Quando si attiva

- `/marketing contenuti <url>`: legge il sito e ne deriva il piano.
- `/marketing contenuti <descrizione attività>`: funziona anche senza sito ("studio dentistico a Monza, 2 poltrone, pazienti soprattutto famiglie").
- Frasi tipo: "cosa pubblico questo mese", "fammi il piano editoriale", "idee per i contenuti di un cliente".
- Funziona anche per il mese successivo: si rilancia con le stesse informazioni più una riga su cosa ha funzionato nel mese appena chiuso.

## Procedura

1. **Capisci cosa comprano i clienti.** Se c'è un url, WebFetch della homepage e delle pagine prodotto o servizio. Se c'è solo la descrizione, lavora su quella e chiedi al massimo UNA domanda di chiarimento (il prodotto di punta, o il cliente tipo). L'output di questo passo: il prodotto o servizio principale, chi lo compra, e le 3 cose che il cliente deve credere prima di comprare (che ne vale il prezzo, che può fidarsi, che fa per lui).

2. **Rileva il tipo di business** (attività locale, e-commerce, servizi B2B, studio professionale, formazione/creator) e assegna il canale principale con la tabella della checklist. Il canale principale è UNO: una PMI che pubblica ovunque pubblica male ovunque.

3. **Deriva i 3 pilastri.** Ogni pilastro nasce da ciò che il cliente compra e da cosa gli impedisce di comprare, non da ciò che l'azienda ha voglia di raccontare. Schema che funziona quasi sempre:
   - **Pilastro prodotto:** il prodotto o servizio visto da vicino, come si usa, come si sceglie. Per Oro del Salento: come riconoscere un olio buono, cosa dice l'etichetta, come conservarlo.
   - **Pilastro fiducia:** dietro le quinte, il metodo, i clienti serviti (fittizi o con permesso), le domande frequenti con risposte oneste. Per lo Studio dentistico Bianchi: cosa succede alla prima visita, quanto dura, cosa si paga.
   - **Pilastro decisione:** i contenuti che sciolgono l'ultima obiezione e portano al contatto. Confronti onesti, "per chi NON fa per te", prezzi spiegati.

4. **Genera le 12 idee** (3 a settimana per 4 settimane, ripartite sui 3 pilastri). Ognuna con: titolo, aggancio (la prima frase o la prima immagine, quella che decide se il cliente si ferma) e formato adatto al canale principale. Idee producibili da un titolare senza troupe: telefono, buona luce, 20 minuti.

5. **Pianifica il riciclo.** Ogni contenuto va riadattato su 2 canali secondari, cambiando forma e non sostanza: il video della trattoria diventa 3 foto con didascalia su Facebook e una storia con sondaggio su Instagram. Il riciclo si pianifica adesso, nel piano, non "poi si vedrà".

6. **Scrivi `PIANO-CONTENUTI.md`** nella directory corrente dell'utente col template qui sotto. A terminale: i 3 pilastri in una riga ciascuno, il canale principale con la motivazione, e il nome del file.

Regola d'oro dei numeri: MAI promettere risultati in euro o stime di fatturato dai contenuti. Se l'utente non ha fornito i suoi numeri, gli obiettivi si scrivono a parole ("più richieste dal modulo contatti", "più gente che cita i video in negozio") e le ipotesi si dichiarano nel report.

## Checklist di valutazione

Canale principale per tipo di business:

| Tipo | Canale principale | Perché | Secondari tipici |
|-|-|-|-|
| Attività locale | Instagram + scheda Google | Il cliente decide guardando foto e recensioni di zona | Facebook, WhatsApp Business |
| E-commerce | Instagram o TikTok | Il prodotto si vende mostrandolo in uso | Email, Pinterest |
| Servizi B2B | LinkedIn | Il decisore è lì, e compra da chi dimostra competenza | Newsletter, YouTube |
| Studio professionale | Scheda Google + sito | Il paziente cerca su Google e verifica la reputazione | Instagram, Facebook |
| Formazione/creator | YouTube | Il contenuto lungo costruisce la fiducia che vende un corso | Newsletter, Instagram |

Controllo qualità delle 12 idee, prima di consegnare:

| Controllo | Domanda |
|-|-|
| Legame con l'acquisto | Questa idea avvicina qualcuno a comprare, o è solo simpatica? |
| Aggancio concreto | La prima frase ferma il cliente tipo, o è un'introduzione generica? |
| Producibilità | Il titolare la realizza in mezz'ora con un telefono? |
| Equilibrio | I 3 pilastri sono coperti tutti, nessuna settimana monotematica? |
| Riciclo definito | Per ogni idea sono indicati i 2 canali secondari e come adattarla? |
| Invito all'azione | Almeno le idee del pilastro decisione dicono cosa fare dopo (prenota, scrivi, passa in negozio)? |
| Voce coerente | Le 12 idee sembrano scritte dalla stessa azienda, con lo stesso tono? |

Se un'idea non passa uno di questi controlli, si sostituisce prima di consegnare: il piano esce con 12 idee buone, non con 12 caselle riempite.

## Struttura del report

```markdown
# Piano Contenuti: 30 giorni

**Attività:** Trattoria Dal Moro, Verona
**Data:** 18 luglio 2026
**Tipo di business:** attività locale
**Cosa compra il cliente:** una cena di cucina veronese, prenotata per lo più nel weekend

## I 3 pilastri

1. **[Nome pilastro prodotto]**: [cosa copre e perché al cliente interessa]
2. **[Nome pilastro fiducia]**: [cosa copre]
3. **[Nome pilastro decisione]**: [cosa copre]

## Il canale principale

**[Canale]**, perché [motivazione legata al tipo di business e al cliente].
Canali secondari per il riciclo: [canale A] e [canale B].

## Le 12 idee

### Settimana 1
| # | Pilastro | Titolo | Aggancio | Formato | Riciclo |
|-|-|-|-|-|-|
| 1 | Prodotto | ... | "..." | reel 30s | [canale A: come], [canale B: come] |
| 2 | Fiducia | ... | "..." | carosello 5 slide | ... |
| 3 | Decisione | ... | "..." | post con foto | ... |

### Settimana 2
[stessa tabella]

### Settimana 3
[stessa tabella]

### Settimana 4
[stessa tabella]

## Ritmo di produzione

- [Quando produrre: esempio, tutto in una sessione da 2 ore a settimana]
- [Chi fa cosa, se c'è più di una persona]
- [Il giorno fisso di pubblicazione per ogni canale]

## Il primo contenuto da produrre oggi

[L'idea numero 1, scelta perché è la più semplice da fare subito: il piano parte davvero solo se il primo pezzo esce entro 48 ore]

## Come capire se funziona (senza inventare numeri)

- [Segnali osservabili: richieste dal modulo, messaggi, prenotazioni che citano i contenuti]
- [Confronto a parole col mese precedente: più o meno richieste, più o meno gente]
- [Cosa chiedere a ogni cliente nuovo: "come ci hai trovati?"]

## Ipotesi dichiarate

- [Assunzioni fatte su cliente tipo, stagionalità, capacità di produzione]
```

## Casi particolari

- **Né url né descrizione utilizzabile:** chiedi cosa vende e a chi. Senza queste due risposte il piano non parte: i pilastri derivano da lì.
- **Sito irraggiungibile:** proponi di procedere da descrizione, dichiarando nel report che il piano non ha potuto leggere il sito.
- **L'azienda vende cose molto diverse** (OfficinaWeb che fa siti e campagne): un piano solo, sul servizio che porta più margine o che l'utente vuole spingere. Chiedi quale; se non risponde, scegli il più in evidenza sul sito e dichiaralo.
- **Il titolare non vuole metterci la faccia:** capita spesso. Sposta i formati su prodotto, mani al lavoro, prima e dopo, testo su immagine. Niente idee che richiedono di parlare in camera.
- **Settori con regole pubblicitarie** (sanitario, legale, finanziario): per lo Studio dentistico Bianchi niente promesse di risultato clinico e prudenza con i casi dei pazienti. Segnala nel report che i contenuti vanno verificati rispetto alle regole deontologiche dell'ordine.
- **Zero tempo per produrre:** se l'utente dice che ha meno di 2 ore a settimana, riduci a 8 idee (2 a settimana) e dichiara il taglio nel report. Un piano rispettato batte un piano ambizioso abbandonato alla seconda settimana.
- **Attività fortemente stagionale:** ancora il piano alla stagione in corso (il gelataio a novembre parla di torte e buoni regalo, non di coni). L'ipotesi stagionale va scritta nelle ipotesi dichiarate.
- **Profili social già aperti ma fermi da mesi:** meglio riattivare il canale principale con le prime 3 idee che aprirne uno nuovo da zero. I follower esistenti, pochi o tanti, sono il primo pubblico di prova.
- **L'utente vuole pubblicare tutti i giorni:** sconsiglialo e scrivilo nel report: 3 contenuti a settimana fatti bene battono 7 fatti di fretta. Se insiste, il piano resta di 12 idee e i giorni extra si coprono col riciclo.
