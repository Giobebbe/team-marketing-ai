---
name: marketing-ads
description: Progetta la prima campagna pubblicitaria a pagamento per una PMI italiana con budget piccolo (300-1.500 euro al mese): piattaforma giusta, struttura semplice, testi degli annunci pronti, budget in euro e metriche con soglie di allarme. Si attiva con /marketing ads, "voglio fare pubblicità", "quanto budget per le ads", "fammi una campagna Meta", "campagna Google Ads", "sponsorizzate".
---

# /marketing ads <url> [budget mensile]

Pensata per chi parte con un budget piccolo, tra 300 e 1.500 euro al mese. Produce una campagna sola, semplice, con i testi pronti e le regole chiare per capire in una settimana se sta funzionando o se va fermata.

## Quando si attiva

- L'utente digita `/marketing ads` seguito dall'URL del sito e, se vuole, dal budget mensile in euro.
- L'utente chiede di fare pubblicità online, sponsorizzate, campagne Meta o Google, o quanto budget serve per iniziare.

## Procedura

1. **Leggi il sito.** Dall'URL ricava cosa vende l'attività, a chi, e qual è l'azione che conta: acquisto, richiesta di preventivo, prenotazione, telefonata. Se hai la Partita IVA, `scripts/estrai_piva.py` completa il quadro: se manca la chiave API lo script stampa le istruzioni e tu prosegui col sito.
2. **Classifica il tipo di business** tra: attività locale, e-commerce, servizi B2B, studio professionale, formazione/creator.
3. **Fissa il budget.** Se l'utente non lo indica, chiedilo. Sotto i 300 euro al mese, dillo chiaro: meglio aspettare e metterli da parte, perché i dati raccolti sarebbero troppo pochi per decidere qualsiasi cosa.
4. **Scegli la piattaforma** con la tabella qui sotto. Una sola piattaforma: con questi budget dividersi su due significa non imparare niente da nessuna delle due.
5. **Controlla la domanda.** Se la piattaforma scelta è Google Search, lancia `scripts/volumi_ricerca.py` sulle parole chiave del servizio (DataForSEO): i volumi decidono se la gente cerca davvero quella cosa. Per le attività locali lancia anche `scripts/competitor_locali.py` (Google Places) per capire quanti concorrenti si contendono la stessa zona. Se una chiave manca, lo script stampa le istruzioni e tu prosegui con le parole chiave dichiarate come ipotesi da verificare nei primi 7 giorni di campagna.
6. **Controlla la Pagella.** Se nella directory corrente esiste `PAGELLA-MARKETING.md` e il voto di Conversione è in rosso (sotto 5), fermati: scrivi nel report che prima di pagare traffico va sistemata la pagina di arrivo, e indica le 2 o 3 cose minime da sistemare (telefono visibile, modulo corto, recensioni in vista).
7. **Costruisci la campagna** con la struttura fissa: 1 campagna, 2 gruppi, 3 annunci per gruppo. Scrivi i testi dei 3 annunci per la piattaforma scelta, il targeting concreto e il budget suddiviso in euro.
8. **Salva** il report come `CAMPAGNE-ADS.md` nella directory corrente e riassumi in tre righe piattaforma, budget e regola di stop.

### Scelta della piattaforma per tipo di business

| Tipo | Piattaforma | Perché |
| - | - | - |
| Attività locale | Meta (Facebook + Instagram) | Raggio geografico stretto, la gente scopre con gli occhi. Google Search se il servizio è d'urgenza (idraulico, dentista che fa male) |
| E-commerce | Meta (Facebook + Instagram) | Il prodotto si mostra, il pubblico si allarga per somiglianza |
| Servizi B2B | Google Search; LinkedIn solo sopra i 1.000 euro al mese | Su Google intercetti chi cerca già; LinkedIn costa troppo per clic per i budget minimi |
| Studio professionale | Google Search | Chi cerca "avvocato del lavoro Monza" ha già il problema: c'è solo da farsi trovare |
| Formazione/creator | Meta (Facebook + Instagram) | Il pubblico si costruisce per interesse, e il contenuto gratuito fa da esca |

## Checklist prima di partire

| Controllo | Perché |
| - | - |
| La pagina di arrivo dice in 5 secondi cosa offri e cosa fare | Pagare clic verso una pagina confusa è buttare soldi |
| Telefono, modulo o carrello funzionano da telefono | La maggior parte dei clic arriva da smartphone |
| Il pixel o il tag di conversione è installato | Senza misurare i contatti, tra 30 giorni non saprai cosa ha funzionato |
| Un solo obiettivo di campagna | Contatti O acquisti O telefonate: mai due obiettivi insieme con questi budget |
| Nessuna promessa di risultato nei testi | Mai stime di fatturato o guadagno negli annunci: oltre che scorretto, viola le regole delle piattaforme |

## Struttura del report

```markdown
# Campagna Ads: [Nome attività]

Tipo di business: [tipo]. Budget: [X] euro al mese. Data: [data].
Piattaforma scelta: [piattaforma]. Perché: [2 righe]. Perché NON le altre: [2 righe].
Azione che conta (conversione): [preventivo / acquisto / telefonata / prenotazione].

## Struttura della campagna
1 campagna: [obiettivo, es. contatti].
Gruppo A: [pubblico o parole chiave principali]
Gruppo B: [pubblico o parole chiave alternative, per confronto]
3 annunci per gruppo, gli stessi testi in entrambi: dopo 7 giorni si tiene quello che porta contatti al costo più basso.

## Targeting concreto
Gruppo A: [zona geografica precisa in km o comuni; età; interessi O parole chiave con tipo di corrispondenza]
Gruppo B: [la variante da confrontare: altra zona, altro interesse, altre parole chiave]
Esclusioni: [chi NON deve vedere gli annunci: già clienti, zone non servite, ricerche fuori tema come "gratis" o "lavora con noi"]

## Budget suddiviso in euro
| Budget mensile | Al giorno | Gruppo A | Gruppo B |
| - | - | - | - |
| 300 euro | 10 euro | 5 euro | 5 euro |
| 600 euro | 20 euro | 10 euro | 10 euro |
| 900 euro | 30 euro | 15 euro | 15 euro |
| 1.500 euro | 50 euro | 25 euro | 25 euro |
[Riga evidenziata sul budget reale dell'utente.]
Dopo i primi 14 giorni: sposta il budget sul gruppo che porta contatti a costo più basso, in proporzione 70 e 30.

## I 3 annunci (testi pronti)
Formato Meta: testo principale di 3 o 4 righe, titolo sotto le 6 parole, invito all'azione coerente con la conversione.
Formato Google: 3 titoli da massimo 30 caratteri, 2 descrizioni da massimo 90 caratteri, la parola cercata dentro il primo titolo.

### Annuncio 1: il problema
[Testo pronto nel formato della piattaforma scelta, centrato sul problema del cliente e su come l'attività lo risolve.]

### Annuncio 2: la prova
[Testo pronto centrato su recensioni, anni di attività e numeri veri e verificabili dell'attività, mai inventati.]

### Annuncio 3: l'offerta
[Testo pronto centrato su un'offerta concreta con scadenza, o su cosa rende diversa l'attività dai concorrenti.]

## Metriche della prima settimana
| Metrica | Cosa dice | Soglia di allarme (benchmark di settore, da verificare sui tuoi dati) |
| - | - | - |
| CPM | Quanto costa farsi vedere da 1.000 persone | Sopra i [15] euro su Meta: pubblico troppo stretto o creatività debole |
| CTR | Su 100 persone che vedono, quante cliccano | Sotto lo [0,8]% su Meta o il [2]% su Google Search: l'annuncio non aggancia |
| Costo per contatto | Quanto paghi ogni richiesta reale | Sopra [soglia coerente col valore di un cliente, dichiarata dall'utente]: si interviene |

## La prima settimana, giorno per giorno
Giorno 1: controlla che gli annunci siano approvati e che il tracciamento registri le visite.
Giorni 2 e 3: guarda solo che il budget esca in modo uniforme, non toccare niente.
Giorno 4: primo sguardo a CPM e CTR, ancora nessuna decisione.
Giorno 7: primo bilancio vero con la tabella qui sopra e la regola di stop.

## Regola di stop
Dopo 7 giorni pieni: se un annuncio ha speso più di [2 volte il costo per contatto accettabile] senza portare nemmeno un contatto, si spegne quell'annuncio.
Dopo 14 giorni: se l'intera campagna ha speso metà del budget mensile senza contatti, si mette in pausa tutto e si riparte dalla pagina di arrivo, non da altri annunci.
Mai giudicare prima di 7 giorni: i primi giorni le piattaforme stanno ancora imparando.

## Glossario minimo
| Termine | In parole povere |
| - | - |
| CPM | quanto paghi per far vedere l'annuncio a 1.000 persone |
| CTR | su 100 persone che vedono l'annuncio, quante ci cliccano |
| Conversione | l'azione che conta per te: preventivo, acquisto, telefonata |
| Pixel o tag | il pezzetto di codice sul sito che conta le conversioni |

## Dopo i primi 30 giorni
[Cosa fare col vincitore: spostare il budget, scrivere 2 varianti del miglior annuncio, allargare il pubblico con giudizio, un passo alla volta.]
```

## Casi particolari

- **Budget sotto i 300 euro.** Scrivi comunque il report ma con l'avviso in testa: con meno di 10 euro al giorno i dati arrivano lenti, servirà più pazienza prima di giudicare (30 giorni, non 7).
- **B2B con budget sotto i 1.000 euro che chiede LinkedIn.** Spiega il motivo del no: il costo per clic su LinkedIn mangia il budget in pochi giorni. Per OfficinaWeb di Bologna con 600 euro al mese la strada è Google Search sulle ricerche dei servizi che vende.
- **E-commerce senza foto decenti dei prodotti.** Le foto vengono prima degli annunci: Oro del Salento con tre belle foto della latta e dell'uliveto batte qualsiasi testo scritto bene appoggiato su una foto buia.
- **Servizio d'urgenza locale.** Anche se il tipo è "attività locale", vince Google Search: chi ha il dente che fa male alle 22 cerca su Google, non scorre Instagram. Per lo Studio dentistico Bianchi di Monza: campagna Search su "dentista urgenza Monza" e ricerche simili, con estensione di chiamata.
- **Nessun modo di tracciare le conversioni.** Fermati su questo punto prima dei testi: senza pixel o tag, il report include come prima azione l'installazione del tracciamento, anche nella versione minima (numero di telefono dedicato, modulo con pagina di ringraziamento).
- **Attività stagionale.** Se il grosso dei clienti arriva in certi mesi (gelateria, agriturismo, commercialista sotto scadenze), concentra il budget nei 2 o 3 mesi giusti invece di spalmarlo sull'anno, e scrivilo esplicitamente nel report.
- **L'utente ha già campagne attive.** Non buttare il lavoro fatto: chiedi uno screenshot dei risultati (spesa, contatti, costo per contatto) e confronta la struttura esistente con quella proposta. Il report indica cosa tenere e cosa spegnere, con il motivo accanto a ogni voce.
- **Più sedi o più servizi.** Con questi budget si parte da UNA sede o UN servizio: quello con più margine o più richiesta. Il report lo dichiara e mette gli altri in coda, da attivare solo quando il primo gira in attivo.
- **L'utente chiede "quanto guadagnerò?".** La risposta onesta va scritta nel report: nessuno può saperlo prima. Quello che il report promette è un altro numero: entro 14 giorni saprai quanto ti costa un contatto vero, e con quello deciderai tu se il conto torna.
- **Regola d'oro dei numeri.** Nel report mai stime di fatturato o di guadagno in euro. Le soglie di CPM e CTR vanno sempre presentate come benchmark di settore da confrontare con i dati veri della campagna, mai come promesse.
