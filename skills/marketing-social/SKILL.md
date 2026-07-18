---
name: marketing-social
description: Sceglie il canale social giusto per una PMI italiana e produce un calendario di 4 settimane con i testi dei post già scritti. Si attiva con /marketing social, "cosa pubblico sui social", "fammi il piano editoriale", "calendario social", "su che social devo stare", "scrivimi i post del mese".
---

# /marketing social <attività o url>

Prima decide DOVE conviene pubblicare in base al tipo di business, poi produce un calendario di 4 settimane, 3 post a settimana, con il testo pronto di ogni post. La regola di fondo: meglio un canale fatto bene che quattro fatti male.

## Quando si attiva

- L'utente digita `/marketing social` seguito dal nome dell'attività o dall'URL.
- L'utente chiede un piano editoriale, un calendario di post, su quale social puntare, o cosa pubblicare per la sua attività.

## Procedura

1. **Capisci l'attività.** Se l'argomento è un URL, leggi la home e la pagina "chi siamo". Se hai la Partita IVA, `scripts/estrai_piva.py` ricava ragione sociale e settore: se manca la chiave API lo script stampa le istruzioni e tu prosegui con quello che vedi dal sito o chiedi all'utente.
2. **Classifica il tipo di business** tra: attività locale, e-commerce, servizi B2B, studio professionale, formazione/creator.
3. **Scegli il canale** con la tabella qui sotto. Massimo due canali: uno principale e uno di supporto. Spiega in due righe perché quel canale e perché gli altri no.
4. **Guarda cosa fanno i concorrenti.** Per le attività locali lancia `scripts/competitor_locali.py` (Google Places) per vedere chi c'è in zona e quanto è attivo. Per gli altri tipi lancia `scripts/competitor_registro.py` (registro imprese) per i nomi, poi cerca i loro profili. Se manca una chiave, lo script stampa le istruzioni e tu prosegui chiedendo all'utente due o tre nomi di concorrenti.
5. **Trova gli argomenti che la gente cerca.** Lancia `scripts/volumi_ricerca.py` con 5 o 10 parole chiave del settore: gli argomenti più cercati diventano i temi dei post utili. Senza chiave, usa le domande tipiche che i clienti fanno all'attività (chiedile all'utente).
6. **Controlla la Pagella.** Se nella directory corrente esiste `PAGELLA-MARKETING.md`, leggi i voti di Messaggio e Trovabilità: se Messaggio è in rosso (sotto 5), i primi post servono a chiarire cosa fa l'attività e per chi; se Trovabilità è in rosso, spingi su Google Business Profile e sui contenuti che rispondono a ricerche reali.
7. **Scrivi il calendario**: 4 settimane, 3 post a settimana, ogni settimana 2 post utili e 1 post di fiducia. Ogni post ha il testo completo, pronto da incollare.
8. **Salva** il report come `CALENDARIO-SOCIAL.md` nella directory corrente e riassumi in tre righe il canale scelto e il piano.

### Scelta del canale per tipo di business

| Tipo | Canale principale | Canale di supporto | Perché |
| - | - | - | - |
| Attività locale | Instagram | Google Business Profile | La gente sceglie con gli occhi e cerca su Google Maps prima di entrare |
| E-commerce | Instagram | Meta Ads (vedi /marketing ads) | Il prodotto si vende con le immagini, l'organico prepara le campagne |
| Servizi B2B | LinkedIn | Nessuno | I decisori aziendali stanno lì, il resto disperde tempo |
| Studio professionale | Google Business Profile | LinkedIn se i clienti sono aziende, Instagram se privati | Chi cerca un professionista parte quasi sempre da Google |
| Formazione/creator | YouTube | Newsletter | I contenuti lunghi costruiscono fiducia e la lista email resta tua |

## Regole di scrittura

| Regola | Come si applica |
| - | - |
| Aggancio nelle prime 2 righe | La prima frase deve dare un motivo per fermarsi: una domanda vera, un numero, un errore comune. Il "vedi altro" scatta presto |
| Corpo concreto | Una sola idea per post, spiegata come la spiegheresti a voce a un cliente. Niente paroloni da agenzia |
| Chiusura con invito concreto | Ogni post chiude chiedendo una cosa sola: "prenota", "scrivici", "passa in negozio", "salva il post". Mai "link in bio" da solo |
| Mix 2 utili + 1 di fiducia | A settimana: 2 post che risolvono un problema del cliente, 1 che mostra chi siete (dietro le quinte, recensioni, casi reali) |
| Foto vere | Meglio una foto vera fatta col telefono che una immagine di repertorio patinata. La gente riconosce il finto al volo |
| Hashtag con misura | Da 3 a 5, specifici e locali. Niente muri di 30 hashtag |
| Niente numeri inventati | Mai promettere risultati in euro o clienti garantiti. I benchmark di settore si citano solo dichiarandoli come benchmark |

## Struttura del report

```markdown
# Calendario Social: [Nome attività]

Tipo di business: [tipo]. Data: [data].

## Il canale giusto per te
Canale principale: [canale]. Canale di supporto: [canale o "nessuno"].
Perché: [2 righe]. Perché NON gli altri: [2 righe].
Cosa fanno i concorrenti: [3 righe da quanto emerso dagli script o dai profili guardati].

## Come usare questo calendario
Pubblica nei giorni indicati, orari suggeriti: [orari sensati per il settore].
Ogni post qui sotto è pronto: sostituisci i campi tra parentesi quadre e aggiungi una foto vera.

## Settimana 1
### Post 1 (lunedì), utile
Tema: [la domanda più cercata o più frequente dei clienti]
Testo:
[Aggancio in 2 righe: domanda o errore comune.]
[Corpo: la risposta pratica, 4 o 6 righe, come la diresti a voce.]
[Chiusura: invito concreto, una sola azione.]
[3 o 5 hashtag]

### Post 2 (mercoledì), utile
Tema: [secondo argomento cercato]
Testo: [testo completo con la stessa struttura: aggancio, corpo, invito, hashtag]

### Post 3 (venerdì), di fiducia
Tema: dietro le quinte
Testo: [una scena vera di lavoro raccontata in prima persona, chiusa con un invito leggero]

## Settimana 2
### Post 4 (lunedì), utile
Tema: [terzo argomento cercato]
Testo: [testo completo: aggancio, corpo, invito, hashtag]

### Post 5 (mercoledì), utile
Tema: [quarto argomento cercato]
Testo: [testo completo: aggancio, corpo, invito, hashtag]

### Post 6 (venerdì), di fiducia
Tema: una recensione vera commentata
Testo: [riporta la recensione parola per parola, racconta il retroscena di quel lavoro, chiudi con un invito leggero]

## Settimana 3
### Post 7 (lunedì), utile
Tema: [quinto argomento cercato]
Testo: [testo completo: aggancio, corpo, invito, hashtag]

### Post 8 (mercoledì), utile
Tema: [sesto argomento cercato]
Testo: [testo completo: aggancio, corpo, invito, hashtag]

### Post 9 (venerdì), di fiducia
Tema: un caso reale dall'inizio alla fine
Testo: [com'è arrivato il cliente, che problema aveva, cosa avete fatto, com'è finita: senza numeri inventati]

## Settimana 4
### Post 10 (lunedì), utile
Tema: [settimo argomento cercato]
Testo: [testo completo: aggancio, corpo, invito, hashtag]

### Post 11 (mercoledì), utile
Tema: [ottavo argomento cercato]
Testo: [testo completo: aggancio, corpo, invito, hashtag]

### Post 12 (venerdì), di fiducia
Tema: le persone dietro l'attività
Testo: [presenta chi lavora lì, con nome e ruolo detto in modo umano, chiudi invitando a passare o scrivere]

## Dopo le 4 settimane
Guarda quali post hanno portato messaggi, prenotazioni o domande (non solo like).
Rifai il mese ripetendo i temi che hanno funzionato. Se un formato non ha portato niente per 4 settimane, cambialo.
```

Nel report generato ogni segnaposto va sostituito con testo vero e ogni post delle settimane 2, 3 e 4 va scritto per intero come quelli della settimana 1: il calendario consegnato contiene 12 testi completi, mai "da completare".

## Casi particolari

- **L'attività è già su un canale "sbagliato".** Non dire di buttare via il lavoro fatto: proponi di mantenere il canale attuale al minimo e spostare le energie sul canale giusto, con una frase tipo "continua a pubblicare lì una volta a settimana, il grosso va qui".
- **Attività locale senza Google Business Profile.** Prima voce del report: aprire e completare la scheda (foto, orari, categoria, telefono). Per la Trattoria Dal Moro di Verona vale più una scheda Google curata con 50 recensioni che un anno di post.
- **Nessuna foto disponibile.** Aggiungi al report una lista della spesa fotografica: 10 foto da fare col telefono in una giornata (locale, persone al lavoro, prodotto, dettagli). I post si scrivono comunque.
- **B2B che vuole stare su Instagram.** Spiega senza giri che i clienti aziendali non scelgono un fornitore da un reel: per OfficinaWeb di Bologna il post giusto è un caso cliente su LinkedIn, con problema, lavoro fatto e risultato verificabile.
- **E-commerce con pochi prodotti.** Ruota gli angoli invece dei prodotti: come si usa, chi lo produce, come si sceglie, errori da evitare. Oro del Salento può parlare di olio per un anno senza ripetersi: abbinamenti, conservazione, etichette, raccolta.
- **L'utente vuole più di 3 post a settimana.** Sconsiglialo se parte da zero: meglio 3 post costanti per 3 mesi che 7 per due settimane e poi il silenzio. Se insiste, aggiungi post utili, mai riempitivi.
- **Formazione/creator senza canale YouTube avviato.** Il calendario diventa: 1 video a settimana al posto dei 2 post utili, più 1 email alla lista come post di fiducia. La struttura del report resta identica.
