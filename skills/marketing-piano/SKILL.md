---
name: marketing-piano
description: Trasforma i report di marketing già presenti nella directory corrente in un piano d'azione concreto a 90 giorni (PIANO-90-GIORNI.md), ordinato per impatto e sforzo. Si attiva con /marketing piano, oppure quando l'utente chiede "fammi il piano", "da dove comincio", "mettimi in ordine le cose da fare".
---

# /marketing piano

Prende tutte le azioni consigliate sparse nei report e le mette in fila: cosa fare subito, cosa nel primo mese, cosa nei due mesi dopo. Il risultato è un file solo, PIANO-90-GIORNI.md, che il titolare può stampare e seguire senza rileggere sette documenti.

## Quando si attiva

- L'utente scrive `/marketing piano`
- L'utente chiede "cosa faccio adesso", "dammi le priorità", "in che ordine sistemo le cose"
- È appena finita un'analisi e l'utente vuole passare all'azione

## Cosa legge

Cerca nella directory corrente questi report. Usa quelli che esistono, ignora quelli che mancano:

| Report | Cosa estrarre |
|---|---|
| PAGELLA-MARKETING.md | Azioni consigliate da ogni area valutata, con il voto che le motiva |
| ANALISI-COMPETITOR.md | Mosse per differenziarsi e buchi lasciati scoperti dai concorrenti |
| PIANO-SEO.md | Interventi sulle pagine, contenuti da creare, schede locali da sistemare |
| PIANO-CONTENUTI.md | Contenuti da produrre, con che frequenza e su quali temi |
| SEQUENZE-EMAIL.md | Sequenze da attivare e automazioni da montare |
| CALENDARIO-SOCIAL.md | Attività social da mettere a regime |
| CAMPAGNE-ADS.md | Campagne da lanciare e prerequisiti tecnici (pixel, pagine di destinazione) |

Se nella directory non esiste NESSUNO di questi file, fermati e rispondi: "Non trovo report da cui costruire il piano. Parti da /marketing analisi, poi torna qui." Non inventare azioni dal nulla.

## Procedura

1. Elenca i file della directory corrente e individua quali report dell'elenco esistono davvero.
2. Leggi per intero ogni report presente. Da ognuno estrai le azioni consigliate: frasi tipo "aggiungere", "rifare", "attivare", "creare", "correggere", "rispondere". Ogni azione diventa una riga: cosa fare, report di provenienza, area della Pagella collegata.
3. Togli i doppioni. Se due report suggeriscono la stessa cosa (esempio: "installa il pixel" sia in PAGELLA-MARKETING.md sia in CAMPAGNE-ADS.md), tieni una sola riga e cita entrambe le fonti.
4. Per ogni azione stima impatto (quanto può muovere clienti o fatturato) e sforzo (tempo, competenze, costo) usando le ancore della tabella qui sotto. Sono stime, non certezze: nel report va scritto.
5. Colloca ogni azione nella matrice impatto/sforzo e da lì in una delle tre fasi temporali.
6. Verifica le dipendenze: se un'azione ne richiede un'altra (la campagna richiede il pixel, la newsletter richiede la raccolta contatti), la prima va in una fase precedente.
7. Per ogni azione compila i quattro campi obbligatori: cosa fare (concreto, eseguibile), chi la fa (titolare o fornitore), tempo stimato, come capire se ha funzionato (un segnale osservabile, mai una sensazione).
8. Scrivi PIANO-90-GIORNI.md nella directory corrente seguendo la struttura qui sotto. Una sola scrittura, file completo.
9. Chiudi dicendo all'utente quante azioni ha davanti e qual è la prima della lista.

## La matrice impatto/sforzo

| | Sforzo basso | Sforzo alto |
|---|---|---|
| **Impatto alto** | Da fare subito (settimane 1-2) | Da pianificare bene (mesi 2-3) |
| **Impatto basso** | Riempitivi (mese 1, se avanza tempo) | Da scartare o rimandare oltre i 90 giorni |

Ancore per stimare in modo coerente:

| Giudizio | Impatto | Sforzo |
|---|---|---|
| Basso | Migliora un dettaglio, il cliente medio non se ne accorge | Meno di mezza giornata, lo fa il titolare da solo |
| Medio | Tocca un punto del percorso di acquisto | Da uno a tre giorni, oppure serve un fornitore per una parte |
| Alto | Tocca il motivo per cui la gente compra, o il canale principale da cui arrivano i clienti | Più di una settimana, oppure serve un fornitore per tutto |

Esempio: per la Trattoria Dal Moro di Verona "rispondere alle recensioni Google ferme da sei mesi" è impatto alto e sforzo basso, quindi va nelle settimane 1-2. "Rifare il sito da zero" è impatto alto ma sforzo alto, quindi va nei mesi 2-3, con un fornitore.

## Le tre fasi

| Fase | Cosa ci va | Regola |
|---|---|---|
| Settimane 1-2 | Alto impatto, basso sforzo | Massimo 5 azioni, tutte chiudibili in due settimane |
| Mese 1 | Impatto medio-alto, sforzo medio, più i riempitivi | Le fondamenta: quello che serve alle fasi successive |
| Mesi 2-3 | Alto impatto, alto sforzo | Progetti veri, quasi sempre con un fornitore |

## Struttura del report

```markdown
# Piano marketing a 90 giorni
Business: [nome] | Data: [data] | Costruito da: [elenco dei report letti]

## Come leggere questo piano
[2-3 righe: le stime di impatto e sforzo sono ipotesi di lavoro, dichiarate,
non promesse. Ogni azione cita il report da cui viene.]

## La mappa delle priorità
| Azione | Impatto | Sforzo | Fase | Fonte |
|---|---|---|---|---|
| [azione] | Alto | Basso | Settimane 1-2 | PAGELLA-MARKETING.md |

## Settimane 1-2: partenza veloce
### 1. [Azione]
- Cosa fare: [passi concreti, eseguibili da domani]
- Chi: [titolare / fornitore, e perché]
- Tempo stimato: [ore o giorni]
- Ha funzionato se: [segnale osservabile entro una data]
- Fonte: [report di provenienza]

## Mese 1: le fondamenta
[stesse schede, stessa struttura]

## Mesi 2-3: i progetti grossi
[stesse schede, stessa struttura]

## Azioni scartate e perché
- [azione]: [motivo in una riga]

## Il primo controllo
[Quando rifare il punto: a fine mese 1, guardando i segnali "ha funzionato se"
delle azioni chiuse. Cosa fare se un segnale non si è mosso.]
```

## Cosa non fa questa skill

- Non rifà le analisi: se un report è debole o vecchio, il piano lo eredita. Meglio rigenerare prima il report che rattoppare dopo il piano.
- Non inventa azioni: ogni riga del piano risale a un report. Se il piano sembra corto, mancano analisi, non fantasia.
- Non promette risultati: i campi "ha funzionato se" sono segnali da controllare a una data precisa, non garanzie.
- Non decide al posto del titolare: dove due strade sono possibili, il piano presenta la scelta e il criterio per decidere.

## Casi particolari

- **Esiste solo la Pagella**: costruisci il piano dalle sue azioni e scrivi nel report che il piano si baserà su una fonte sola; suggerisci quali altre analisi lanciare per completarlo.
- **Numeri in euro**: mai inventarli. Se un report cita un costo, riportalo con la fonte. Se un'azione richiede una spesa non nota, l'azione diventa "chiedere un preventivo a due fornitori", non una cifra tirata a indovinare.
- **Business stagionale**: per Oro del Salento, e-commerce di olio con il picco a Natale, le fasi vanno ancorate alla stagione: la preparazione del picco batte l'ordine standard della matrice. Scrivi nel report perché hai spostato le azioni.
- **Più di 25 azioni estratte**: taglia. Tieni le 20 con il miglior rapporto impatto/sforzo e metti le altre nella sezione "Azioni scartate e perché", una riga ciascuna.
- **Titolare senza tempo** (se dichiarato dall'utente): sposta il più possibile su "fornitore" e segnala esplicitamente le azioni non delegabili, tipo rispondere di persona alle recensioni.
- **Report in contraddizione tra loro** (uno dice "punta sui social", l'altro "i social non portano niente"): non scegliere in silenzio. Segnala il conflitto nel report e proponi la via con l'ipotesi meno rischiosa.
