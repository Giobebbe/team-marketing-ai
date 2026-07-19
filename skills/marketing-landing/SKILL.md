---
name: marketing-landing
description: Ottimizza UNA pagina specifica del sito di una PMI italiana perche' trasformi piu' visitatori in contatti o vendite. Si attiva con /marketing landing <url della pagina>, oppure quando l'utente dice "sistemami questa pagina", "questa pagina non converte", "migliora la mia landing", "perche' nessuno compila il modulo". Lavora su una pagina sola, con riscritture pronte da incollare.
---

# /marketing landing: sistema QUESTA pagina

Il comando chirurgico. Non giudica tutto il sito, prende una pagina sola, quella che deve portare contatti o vendite, e la sistema pezzo per pezzo. Il risultato non e' una lista di consigli: sono testi riscritti pronti da incollare, con il prima e il dopo affiancati.

## Quando si attiva

- `/marketing landing <url della pagina>`
- Frasi tipo: "questa pagina non converte", "sistemami la pagina del preventivo", "la gente arriva ma non compila il modulo".

Se l'utente passa la homepage generica, chiedi qual e' l'azione che quella pagina deve produrre (telefonata, modulo compilato, acquisto, prenotazione). Senza un'azione dichiarata non si puo' giudicare niente.

## Procedura

1. **Leggi la pagina.** WebFetch dell'url. Annota nell'ordine in cui un visitatore le incontra: titolo, sottotitolo, prima chiamata all'azione, prove di fiducia, modulo o pulsante finale. Cita SEMPRE il testo reale trovato: ogni giudizio senza citazione non vale.

2. **Dichiara l'azione della pagina.** Una sola. Se la pagina ne chiede tre (chiama, scrivi, scarica la brochure), quello e' gia' il primo problema da segnalare.

3. **Passa la checklist dei 7 punti**, dall'alto verso il basso:

   | # | Punto | Domanda a cui rispondere |
   |-|-|-|
   | 1 | Primo schermo | In 5 secondi si capisce cosa offri, per chi, e cosa fare adesso? |
   | 2 | Titolo | Parla del problema del cliente o parla dell'azienda? |
   | 3 | Chiamata all'azione | Il pulsante dice cosa succede dopo ("Ricevi il preventivo in 24 ore") o e' generico ("Invia")? |
   | 4 | Prova di fiducia | C'e' almeno una prova concreta (recensioni con nome, numeri, foto vere) VICINO al punto di conversione? |
   | 5 | Attrito del modulo | Quanti campi? Ognuno oltre nome, contatto e richiesta deve guadagnarsi il posto |
   | 6 | Obiezioni | Le 2-3 paure tipiche del cliente ("quanto costa", "quanto ci mette", "e se non va bene") hanno una risposta in pagina? |
   | 7 | Mobile | Dal telefono il pulsante e' raggiungibile senza zoomare, il numero si chiama con un tocco? |

4. **Riscrivi i 3 testi piu' deboli.** Titolo, chiamata all'azione e il terzo peggiore a tua scelta. Regole: parole del cliente, beneficio concreto, zero slogan. Se un'informazione necessaria non esiste sul sito (es. i tempi di consegna), NON inventarla: segna il testo con [DA COMPLETARE: dato mancante] e dillo.

5. **Scrivi ANALISI-LANDING.md** e chiudi a terminale con: azione della pagina, i 3 problemi piu' gravi, la riscrittura del titolo.

## Struttura del report

```markdown
# Landing: [url]
Data: [data] | Azione della pagina: [una sola azione]

## Verdetto in una riga
[la pagina oggi lavora per o contro la conversione, e perche']

## Checklist dei 7 punti
| Punto | Stato | Cosa c'e' oggi (citazione) | Cosa fare |
|-|-|-|-|
[verde / giallo / rosso per ognuno dei 7, con il testo reale citato]

## Riscritture pronte da incollare
### Titolo
Prima: "[testo attuale]"
Dopo: "[riscrittura]"
Perche' funziona: [una riga]

### Chiamata all'azione
Prima: "[testo attuale]"
Dopo: "[riscrittura]"
Perche' funziona: [una riga]

### [Terzo testo scelto]
Prima: "[testo attuale]"
Dopo: "[riscrittura]"
Perche' funziona: [una riga]

## L'ordine dei lavori
1. [il fix col miglior rapporto impatto/sforzo]
2. [secondo]
3. [terzo]

## Come capire se ha funzionato
[la misura concreta da guardare: richieste a settimana, telefonate, ordini.
Prima annota il numero di OGGI, senza baseline nessun test dice niente]
```

## Casi particolari

- **Pagina dietro login o carrello**: analizza fino a dove arrivi e segnala che i passi successivi vanno controllati a mano dall'utente.
- **Pagina lentissima o irraggiungibile**: fermati e dillo subito, la velocita' viene prima di qualsiasi testo.
- **E-commerce**: la "landing" e' la scheda prodotto; i 7 punti valgono uguali, la prova di fiducia diventa recensioni del prodotto e le obiezioni diventano spedizioni e resi.
- **Attivita' locale senza modulo**: l'azione e' la telefonata o la prenotazione; il numero cliccabile e gli orari in vista contano piu' di qualsiasi titolo.
- **L'utente chiede la pagella completa**: questa skill fa una pagina sola; per tutto il sito indirizzalo a /marketing analisi.
