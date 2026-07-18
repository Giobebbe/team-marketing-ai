---
name: marketing-email
description: Scrive tre sequenze email complete e pronte da inviare (benvenuto, preventivo o carrello abbandonato, riattivazione clienti fermi) su misura per una PMI italiana. Si attiva con /marketing email, "scrivimi le email di benvenuto", "sequenza per il carrello abbandonato", "email per recuperare i preventivi", "come riattivo i clienti fermi", "fammi il funnel email".
---

# /marketing email <attività o url>

Prende un'attività (nome, descrizione o URL del sito) e produce tre sequenze email con testi già scritti: oggetto, corpo e PS. Tono caldo e diretto, sempre del tu, come scriverebbe il titolare a un cliente che conosce.

## Quando si attiva

- L'utente digita `/marketing email` seguito dal nome dell'attività o dall'URL.
- L'utente chiede email di benvenuto, recupero carrello, recupero preventivi, riattivazione clienti, newsletter di partenza o un "funnel email" per la sua attività.

## Procedura

1. **Capisci l'attività.** Se l'argomento è un URL, leggi la home e la pagina "chi siamo" del sito. Se l'utente fornisce una Partita IVA, lancia `scripts/estrai_piva.py` per ricavare ragione sociale e settore: se manca la chiave API lo script stampa da solo le istruzioni per ottenerla, tu prosegui con le informazioni del sito o chiedi all'utente due righe di descrizione.
2. **Classifica il tipo di business** tra: attività locale, e-commerce, servizi B2B, studio professionale, formazione/creator. Se non è chiaro, chiedi.
3. **Controlla la Pagella.** Se nella directory corrente esiste `PAGELLA-MARKETING.md`, leggi i voti di Conversione e Crescita: se Conversione è in rosso (sotto 5), nelle email spingi su prova sociale e riduzione del rischio; se Crescita è in rosso, dai più peso alla sequenza di riattivazione.
4. **Adatta le sequenze al tipo di business** usando la tabella qui sotto. Per l'attività locale e lo studio professionale la sequenza "carrello abbandonato" diventa follow-up del preventivo inviato o della prenotazione iniziata e non completata.
5. **Scrivi i testi** partendo dai modelli nella struttura del report, sostituendo i segnaposto con nomi, prodotti e dettagli veri dell'attività. Ogni email deve superare la checklist.
6. **Salva** il report come `SEQUENZE-EMAIL.md` nella directory corrente dell'utente e riassumi in tre righe cosa contiene.

### Adattamento per tipo di business

| Tipo | Benvenuto | Sequenza 2 | Riattivazione |
| - | - | - | - |
| Attività locale | Dopo iscrizione o prima visita | Follow-up preventivo o prenotazione mancata | Cliente che non passa da 3+ mesi |
| E-commerce | Dopo iscrizione alla newsletter | Carrello abbandonato classico | Cliente senza acquisti da 6+ mesi |
| Servizi B2B | Dopo primo contatto o lead magnet | Follow-up preventivo inviato | Contatto fermo da 6+ mesi, tono sobrio |
| Studio professionale | Dopo prima richiesta di informazioni | Follow-up preventivo o appuntamento saltato | Paziente o cliente senza visite da 12 mesi |
| Formazione/creator | Dopo iscrizione alla lista | Checkout del corso non completato | Iscritto che non apre da 3+ mesi |

## Regole di scrittura

| Regola | Come si applica |
| - | - |
| Un solo obiettivo per email | Una email chiede una cosa sola: rispondere, cliccare, prenotare. Mai due richieste insieme |
| Oggetto sotto le 7 parole | Concreto e curioso, niente maiuscole urlate, niente emoji a raffica |
| Sempre del tu | Mai "Gentile cliente", mai "Egregio". Si apre con "Ciao [nome]" |
| PS con leva concreta | Ogni email chiude con un PS che aggiunge un motivo reale: scadenza, link diretto, recensione |
| Mittente persona reale | Firma col nome del titolare o di chi risponde davvero, mai "info@" anonimo |
| Una sola call to action | Un solo link o bottone per email, ripetuto al massimo due volte |
| Niente stime inventate | Mai promettere risultati in euro. I benchmark di settore si citano solo dichiarandoli come benchmark |

## Struttura del report

```markdown
# Sequenze Email: [Nome attività]

Tipo di business: [tipo]. Data: [data].
Tre sequenze pronte: copia i testi nel tuo strumento di invio (Mailchimp, Brevo, MailerLite) e sostituisci i campi tra parentesi quadre.

## Sequenza 1: Benvenuto (5 email in 14 giorni)
Parte quando qualcuno si iscrive o lascia il contatto per la prima volta.

### Email 1, giorno 0
**Oggetto:** Benvenuto, si parte da qui
Ciao [nome], grazie per esserti iscritto. Ti scrivo io, [titolare] di [attività].
Nei prossimi giorni ti racconto chi siamo e come possiamo esserti utili, senza riempirti la casella.
Se hai già una domanda, rispondi pure a questa email: la leggo io di persona.
**PS:** intanto ti lascio [risorsa utile: guida, listino, menù]: [link].

### Email 2, giorno 2
**Oggetto:** Perché facciamo questo lavoro
Ciao [nome], due righe su di noi. [Attività] nasce nel [anno] perché [motivo vero e concreto].
Da allora [fatto verificabile: numero clienti serviti, anni di attività, specialità].
Ti racconto questo perché quando scegli [categoria], conta sapere chi c'è dall'altra parte.
**PS:** qui trovi le recensioni di chi ci ha già provato: [link].

### Email 3, giorno 5
**Oggetto:** La cosa che ci chiedono tutti
Ciao [nome], se c'è una cosa per cui i clienti tornano da noi è [prodotto o servizio di punta].
In pratica: [beneficio concreto in una frase, senza paroloni].
Se ti interessa, la trovi qui: [link diretto].
**PS:** se preferisci parlarne a voce, chiamaci al [telefono]: rispondiamo noi, non un centralino.

### Email 4, giorno 9
**Oggetto:** Cosa dicono i clienti come te
Ciao [nome], invece di dirti quanto siamo bravi, ti riporto due frasi vere:
"[recensione reale 1]" e "[recensione reale 2]".
Le trovi insieme alle altre qui: [link recensioni].
**PS:** se sei già stato da noi, una tua recensione ci aiuta più di qualsiasi pubblicità.

### Email 5, giorno 14
**Oggetto:** Un piccolo pensiero per iniziare
Ciao [nome], per chi è appena arrivato abbiamo [offerta di benvenuto concreta: sconto, omaggio, prima consulenza].
Vale fino a [data precisa], poi torna tutto come prima.
Per usarla: [istruzione semplice in una riga].
**PS:** scade davvero il [data]. Non la prolunghiamo, altrimenti non varrebbe niente.

## Sequenza 2: [Carrello abbandonato / Preventivo senza risposta] (3 email in 5 giorni)
Parte quando qualcuno lascia il carrello a metà, oppure riceve un preventivo o inizia una prenotazione e poi sparisce.

### Email 1, entro 24 ore
**Oggetto:** Ti sei fermato a un passo
Ciao [nome], ho visto che [hai lasciato il carrello a metà / non mi hai ancora risposto sul preventivo].
Capita, la vita è piena di cose. Ti ho tenuto tutto da parte: [link o riepilogo].
Se qualcosa non ti torna, rispondi a questa email e lo sistemiamo.
**PS:** [leva concreta: la disponibilità è limitata, il preventivo vale 30 giorni, i posti della settimana si riempiono].

### Email 2, giorno 2
**Oggetto:** Hai qualche dubbio? Chiedimi pure
Ciao [nome], di solito chi si ferma ha un dubbio su [obiezione tipica: prezzo, tempi, spedizione, garanzia].
Ti rispondo subito: [risposta onesta all'obiezione in due righe].
Se il dubbio è un altro, scrivimelo: rispondo io.
**PS:** qui trovi [garanzia, resi, condizioni] spiegati in parole semplici: [link].

### Email 3, giorno 5
**Oggetto:** Ultimo promemoria, poi basta
Ciao [nome], questa è l'ultima email su questo, promesso.
[Il carrello / Il preventivo] resta valido fino a [data], poi lo lascio andare.
Se vuoi chiuderla qui, nessun problema: cancellati con un clic e non se ne parla più.
**PS:** se il momento è sbagliato ma l'interesse c'è, rispondi "più avanti" e ti ricontatto io tra un mese.

## Sequenza 3: Riattivazione clienti fermi (3 email)
Parte per chi non compra, non prenota o non apre da [soglia per tipo di business].

### Email 1
**Oggetto:** Ci sei ancora?
Ciao [nome], è un po' che non ci sentiamo e volevo capire se va tutto bene.
Se non ti interessa più ricevere queste email, dimmelo pure: [link cancellazione].
Se invece è solo un periodo pieno, tranquillo: questa è solo per dirti che ci siamo.
**PS:** se c'è stato qualcosa che non ti è piaciuto, rispondi e dimmelo: mi serve saperlo.

### Email 2, una settimana dopo
**Oggetto:** Cosa è cambiato da quando manchi
Ciao [nome], dall'ultima volta che ci siamo visti abbiamo [novità concreta: nuovo servizio, nuovo prodotto, nuovi orari].
Te lo dico perché [collegamento con quello che aveva comprato o chiesto].
Dai un'occhiata qui: [link].
**PS:** [dettaglio pratico: parcheggio, spedizione più veloce, nuova sede].

### Email 3, due settimane dopo
**Oggetto:** Un motivo per tornare
Ciao [nome], ultima email di questa serie. Per chi torna abbiamo [offerta di ritorno concreta].
Vale fino a [data], solo per chi era già cliente.
Per usarla: [istruzione semplice].
**PS:** se non ti fai vivo, tolgo il tuo indirizzo dalle prossime campagne: niente rancore, solo rispetto per la tua casella.

## Note di invio
[Consigli pratici: orari di invio, strumento consigliato, come impostare le automazioni, consenso e cancellazione a norma.]
```

## Casi particolari

- **Nessuna lista contatti.** Se l'attività non raccoglie email, prima del report suggerisci un modo semplice per iniziare (modulo sul sito, QR in cassa, richiesta al momento del preventivo) e scrivi comunque le sequenze: serviranno appena arrivano i primi contatti.
- **Attività locale o studio professionale.** La sequenza 2 diventa follow-up del preventivo o della prenotazione mancata: mai parlare di "carrello" a una trattoria o a un dentista. Esempio: per lo Studio dentistico Bianchi di Monza la Email 1 diventa "Il preventivo per la tua otturazione è pronto, hai dubbi?".
- **B2B.** Tono più sobrio ma sempre del tu, mai burocratese. Il PS punta su casi concreti e referenze, non su sconti.
- **E-commerce con tanti prodotti.** Le email citano il prodotto specifico lasciato nel carrello, mai un generico "i tuoi articoli". Esempio: Oro del Salento scrive "la tua latta di olio da 5 litri ti aspetta", non "il tuo ordine".
- **Consenso.** Ricorda sempre nel report che le sequenze partono solo verso contatti che hanno dato il consenso e che ogni email deve avere il link di cancellazione. Niente liste comprate, mai.
- **L'utente vuole una sola sequenza.** Scrivi solo quella richiesta ma salva comunque il file `SEQUENZE-EMAIL.md` con le altre due sezioni segnate come "da attivare quando vuoi".
