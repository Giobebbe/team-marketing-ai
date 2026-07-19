---
name: marketing-funnel
description: Mappa il percorso che porta un cliente da "non ti conosco" a "ho comprato" per una PMI italiana e trova il punto esatto dove si perdono i clienti. Si attiva con /marketing funnel <url o descrizione attivita'>, oppure quando l'utente dice "dove perdo i clienti", "ho visite ma non vendo", "il funnel non funziona", "tanti preventivi e pochi contratti". Produce la mappa del percorso con le perdite e i fix ordinati.
---

# /marketing funnel: dove si perdono i clienti

Ogni attivita' ha un percorso che il cliente attraversa: ti scopre, ti valuta, ti contatta, compra, torna. In ogni passaggio qualcuno si perde, e' normale. Il problema e' quando non sai DOVE si perdono: allora sistemi le cose a caso. Questo comando ricostruisce il percorso, stima dove si rompe e mette i fix in ordine.

## Quando si attiva

- `/marketing funnel <url>` oppure `/marketing funnel <descrizione attivita'>`
- Frasi tipo: "ho traffico ma non vendo", "mi chiedono preventivi ma non chiudono", "dove perdo i clienti".

## Procedura

1. **Ricostruisci il percorso reale.** WebFetch del sito (home + pagine di contatto/acquisto). Il percorso dipende dal tipo di attivita':

   | Tipo | Percorso tipico |
   |-|-|
   | Attivita' locale | mi cercano in zona > profilo Google o sito > telefonata o prenotazione > visita > ritorno e recensione |
   | E-commerce | mi scoprono (ads/social/ricerca) > scheda prodotto > carrello > pagamento > riacquisto |
   | Servizi B2B | mi trovano o mi presentano > sito > richiesta preventivo > trattativa > contratto > rinnovo |
   | Studio professionale | mi cercano > recensioni e sito > prenotano > prestazione > passaparola |
   | Formazione/creator | mi vedono (video/social) > contenuto gratuito > iscrizione lista > offerta > acquisto > community |

2. **Chiedi i numeri che l'utente HA.** Bastano tre: quante persone entrano nel percorso in un mese (visite, telefonate, richieste), quante arrivano in fondo (vendite, contratti), e lo scontrino medio. Se non li ha, prosegui lo stesso ma scrivi nel report che la mappa e' qualitativa: MAI inventare percentuali di conversione.

3. **Trova il punto rotto.** Per ogni passaggio guarda i segnali osservabili dal sito e dai numeri:
   - tanti visitatori e pochi contatti: si rompe SUL sito (vai di /marketing landing sulla pagina chiave)
   - tanti contatti e poche vendite: si rompe DOPO il sito (tempi di risposta, preventivo, trattativa)
   - poche visite in assoluto: non e' un problema di funnel, e' un problema di trovabilita' (/marketing seo o /marketing ads)
   - clienti che comprano una volta sola: si rompe il ritorno (/marketing email, sequenza riattivazione)

4. **Un fix per passaggio, non dieci.** Per ogni punto di perdita indica UNA mossa concreta, chi la fa, e quale numero deve muovere. Ordina per impatto/sforzo.

5. **Scrivi ANALISI-FUNNEL.md** e chiudi a terminale con: il punto piu' rotto, la prima mossa, il numero da tracciare da domani.

## Struttura del report

```markdown
# Il percorso dei tuoi clienti: [attivita']
Data: [data] | Tipo: [tipo attivita'] | Numeri forniti: [si'/no, quali]

## La mappa
[passaggio 1] > [passaggio 2] > [passaggio 3] > [passaggio 4] > [ritorno]
[per ogni passaggio: cosa c'e' oggi, citando cio' che si vede dal sito]

## Dove si rompe
| Passaggio | Segnale | Gravita' | Perche' succede |
|-|-|-|-|
[solo i passaggi con perdite anomale, con la prova: citazione dal sito o numero fornito dall'utente]

## Le mosse, in ordine
1. [passaggio]: [una mossa concreta]. La fa: [titolare/fornitore]. Deve muovere: [numero]
2. ...
3. ...

## I tre numeri da guardare ogni settimana
[entrate nel percorso, arrivi in fondo, scontrino medio: dove leggerli e ogni quanto.
Se oggi non vengono tracciati, la prima mossa in assoluto e' iniziare a contarli]

## Comandi collegati
[se il punto rotto e' una pagina: /marketing landing <url>
se e' la trovabilita': /marketing seo
se e' il ritorno dei clienti: /marketing email]
```

## Casi particolari

- **L'utente non ha nessun numero**: la mappa si fa lo stesso dal sito, ma il report deve dire chiaro che senza contare entrate e uscite ogni diagnosi e' un'ipotesi. La prima mossa diventa: traccia per due settimane.
- **Percorsi multipli** (es. negozio fisico + e-commerce): mappane uno alla volta, partendo da quello che fattura di piu'.
- **"Va tutto male"**: non e' vero mai; fatti dare i tre numeri e il punto rotto salta fuori. Se davvero mancano sia visite che vendite, il primo problema e' la trovabilita', non il funnel.
- **Il sito non esiste o e' solo social**: il percorso parte dal profilo social o Google; la mappa vale uguale, cambia solo il primo passaggio.
