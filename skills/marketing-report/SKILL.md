---
name: marketing-report
description: Impacchetta i report di marketing presenti nella directory corrente in un documento unico presentabile a un cliente pagante (REPORT-CLIENTE.md). Pensato per consulenti e agenzie. Si attiva con /marketing report seguito dal nome del cliente, oppure quando l'utente chiede "preparami il report per il cliente", "documento da consegnare", "report presentabile".
---

# /marketing report [nome cliente]

Chi usa questa suite per lavorare sui clienti ha bisogno di consegnare qualcosa di leggibile, non sette file tecnici. Questa skill prende i report presenti nella directory corrente e li compila in REPORT-CLIENTE.md: un documento che un titolare di PMI legge in dieci minuti e capisce da solo.

## Quando si attiva

- L'utente scrive `/marketing report Trattoria Dal Moro` (o un altro nome cliente)
- L'utente chiede "prepara il documento per il cliente", "rendilo presentabile", "devo consegnarlo lunedì"

## Cosa legge

Tutti i report della suite presenti nella directory corrente: PAGELLA-MARKETING.md, ANALISI-COMPETITOR.md, PIANO-SEO.md, PIANO-CONTENUTI.md, SEQUENZE-EMAIL.md, CALENDARIO-SOCIAL.md, CAMPAGNE-ADS.md, più PIANO-90-GIORNI.md se esiste.

Se non ne esiste nessuno, fermati e rispondi: "Non c'è niente da impacchettare. Parti da /marketing analisi, poi torna qui."

## Procedura

1. Prendi il nome del cliente dal comando. Se manca, chiedilo prima di fare qualsiasi altra cosa, insieme al nome dell'autore da mettere in copertina (il consulente o l'agenzia).
2. Elenca i report presenti nella directory corrente e leggili per intero.
3. Scrivi la sintesi in una pagina, in linguaggio non tecnico: come sta il marketing del business oggi, i punti forti da non toccare, i problemi che costano di più, cosa succede nei prossimi 90 giorni. Un titolare che legge solo questa pagina deve avere il quadro completo.
4. Componi la pagella con i semafori: riprendi i voti da PAGELLA-MARKETING.md, calcola il Voto Finale come media semplice delle 5 aree (Messaggio, Trovabilità, Conversione, Concorrenza, Crescita) e assegna i semafori: verde da 8 a 10, giallo da 5 a 7.9, rosso sotto 5.
5. Scegli i 3 problemi più costosi tra tutti quelli emersi nei report. Criterio: quanto pesano sui clienti persi, non quanto sono facili da spiegare. Per ognuno: qual è il problema, cosa costa oggi (in clienti o occasioni perse, mai in euro inventati), come si sistema.
6. Riassumi il piano: se esiste PIANO-90-GIORNI.md, condensalo per fase. Se non esiste, costruisci una versione breve dalle azioni dei report presenti e scrivi in nota che il piano completo va generato con /marketing piano.
7. Componi l'appendice tecnica: i dettagli operativi che servono a chi implementa (parole chiave con i volumi, elenco competitor, testi delle sequenze). Qui il tecnico è ammesso, ma ogni sezione apre con una riga che dice a cosa serve.
8. Scrivi REPORT-CLIENTE.md nella directory corrente, una sola scrittura, file completo.
9. Rileggi il documento con gli occhi del cliente: ogni termine tecnico fuori dall'appendice va tradotto o tolto. Poi consegna all'utente il nome del file e due righe su cosa contiene.

## Tono: da consulente che parla chiaro

Regole fisse per tutto il documento tranne l'appendice:

| Non scrivere | Scrivi |
|---|---|
| Il funnel presenta friction nella fase di consideration | Chi visita il sito fa fatica a capire come contattarvi |
| Ottimizzare la CTR delle campagne | Far cliccare più persone tra quelle che vedono l'annuncio |
| Lead generation | Raccolta di contatti interessati |
| Il posizionamento non è distintivo | Il sito dice le stesse cose dei concorrenti |
| Implementare una strategia omnicanale | Farsi trovare in tutti i posti dove il cliente cerca |

Altre regole di tono:

- Frasi corte. Una frase, un concetto.
- Ogni numero cita la fonte (quale report, quale script, quale pagina del sito).
- Mai promettere risultati: si scrive "l'obiettivo è", non "otterrete".
- Gli anglicismi restano solo dove il termine italiano non esiste o suona artificiale (email, social, Google Ads vanno bene; "journey", "insight", "asset" no).
- Del cliente si parla con rispetto anche nei problemi: "la pagina contatti si può migliorare così", non "la pagina contatti è fatta male".

## Esempio del tono giusto

Così apre una sintesi ben scritta, per la Trattoria Dal Moro di Verona:

```markdown
La trattoria ha una reputazione che molti concorrenti si sognano: 4,7 su
Google, con recensioni entusiaste sulla cucina. Il problema è che questa
reputazione non si vede: il sito non la mostra, la scheda Google ha foto
di tre anni fa e chi cerca "trattoria verona centro" trova prima altri
tre locali. In pratica: il lavoro difficile (cucinare bene) è già fatto,
quello facile (farlo sapere) no. Il piano dei prossimi 90 giorni serve
a chiudere questa distanza.
```

Niente termini tecnici, un quadro onesto della situazione, e il lettore ha già capito dove andranno i suoi soldi e perché. Questo è il livello da tenere per tutta la parte non tecnica del documento.

## Struttura del report

```markdown
# Report Marketing: [Nome Cliente]

**Preparato per:** [Nome Cliente]
**Data:** [data]
**Preparato da:** [nome consulente o agenzia]

## La situazione in una pagina
[Sintesi non tecnica: come sta il marketing oggi, cosa funziona,
cosa costa clienti, cosa faremo nei prossimi 90 giorni. Massimo una pagina.]

## La pagella
| Area | Voto | Semaforo |
|---|---|---|
| Messaggio | X/10 | 🟢🟡🔴 |
| Trovabilità | X/10 | 🟢🟡🔴 |
| Conversione | X/10 | 🟢🟡🔴 |
| Concorrenza | X/10 | 🟢🟡🔴 |
| Crescita | X/10 | 🟢🟡🔴 |
| **Voto Finale** | **X/10** | [semaforo] |

[Due righe per area: cosa dice quel voto, in parole semplici.]

## I 3 problemi che costano di più
### 1. [Problema, detto come lo direbbe il cliente]
- Cosa succede oggi: [descrizione concreta, con l'evidenza citata]
- Cosa costa: [in clienti o occasioni perse; euro solo se presenti nei report, con fonte]
- Come si sistema: [l'intervento, chi lo fa, quanto tempo serve]

## Il piano
[Le tre fasi: settimane 1-2, mese 1, mesi 2-3. Per ogni fase le azioni
in una riga ciascuna, con chi le fa.]

## Prossimo passo
[Una sola cosa: cosa deve decidere o fare il cliente per partire.]

## Appendice tecnica
[Dettagli per chi implementa: parole chiave e volumi, elenco competitor,
dati degli script, testi completi. Ogni sezione apre con una riga
che spiega a cosa serve.]
```

## Casi particolari

- **Nome cliente mancante**: chiedi nome cliente e autore prima di generare. Mai lasciare segnaposto vuoti in un documento da consegnare.
- **Esiste solo la Pagella**: il report si fa lo stesso ma più corto; scrivi all'utente (non nel documento) quali analisi mancano per la versione completa.
- **Manca la Pagella ma ci sono altri report**: salta la tabella dei semafori, aprila con la sintesi e segnala all'utente che senza /marketing analisi il documento esce senza voti.
- **Report con date lontane tra loro**: indica in copertina il periodo dei dati ("analisi condotte tra il [data] e il [data]"). Se un report ha più di 60 giorni, suggerisci all'utente di rigenerarlo prima di consegnare.
- **Il cliente è un altro consulente o un'azienda strutturata**: l'utente può chiedere "versione tecnica"; in quel caso la sintesi resta ma l'appendice sale di dettaglio. Il default resta il titolare non tecnico.
- **Numeri in euro**: valgono solo se già presenti nei report con la loro fonte. Se l'utente chiede di aggiungere stime economiche, ogni stima entra dichiarata come ipotesi, con il ragionamento scritto accanto.
