---
name: marketing-opportunita
description: Costruisce la mappa di TUTTO quello che si può fare per il marketing di una PMI italiana, partendo dalla Pagella. Ogni mossa con impatto, sforzo e se ha senso per quel business (MAPPA-OPPORTUNITA.md). Si attiva con /marketing opportunita, oppure quando l'utente chiede "cosa posso fare", "tutte le cose che si possono migliorare", "dammi il quadro completo delle opportunità", "cosa conviene fare e cosa no".
---

# /marketing opportunita

La Pagella dice come sta messo il business. Questa skill dice **tutto quello che si potrebbe fare per migliorarlo**: il menu completo, non ancora la scelta. È il documento che fa dire al titolare "ah, non sapevo si potessero fare tutte queste cose". La scelta di cosa fare prima arriva dopo, col piano.

Serve una cosa sola per non confondersi:
- **Questa mappa = l'ampiezza.** Ogni mossa possibile, con quanto rende e quanto costa in fatica. Non è ordinata per priorità: è un catalogo.
- **Il piano (`/marketing piano`) = la profondità.** Poche mosse scelte, messe in fila nel tempo, con chi le fa.

## Quando si attiva

- `/marketing opportunita`
- "fammi vedere tutto quello che si può fare", "quali sono le opportunità", "cosa conviene e cosa no"

## Cosa legge

`PAGELLA-MARKETING.md` nella directory corrente: da lì prende tipo di business, i voti delle 5 aree, i concorrenti trovati e le note della squadra. Se la Pagella non c'è, fermati e rispondi: "Prima mi serve la fotografia del business. Lancia `/marketing analisi <url>`, poi torno qui."

## Procedura

1. Leggi la Pagella per intero. Segna il tipo di business e quali aree sono rosse o gialle: lì stanno le opportunità che pesano di più.
2. Per ogni fronte del marketing, elenca le mosse concrete possibili per **questo** business. I fronti da coprire: Messaggio e offerta, Trovabilità (SEO e scheda Google), Conversione (sito e pagine), Contenuti, Email, Social, Pubblicità a pagamento, Crescita e riacquisto.
3. Per ogni mossa assegna tre etichette:
   - **Impatto**: alto / medio / basso (quanto sposta i clienti o le vendite, non quanto è vistosa).
   - **Sforzo**: alto / medio / basso (tempo e mani che servono, fatte da un titolare o da un fornitore locale, non da un reparto marketing).
   - **Pertinenza**: sì / no, con una riga di perché. Una mossa può essere ottima in generale e inutile per questo business: dillo. A una trattoria le sequenze email per carrelli abbandonati non servono; a un e-commerce sì.
4. Metti in cima le mosse a **impatto alto e sforzo basso** (i frutti bassi), in fondo quelle a impatto basso e sforzo alto (da lasciar stare per ora).
5. Chiudi con la riga onesta: le 2-3 cose che, per questo business, è meglio **non** fare adesso, e perché. Un consulente bravo si vede da cosa toglie, non solo da cosa aggiunge.
6. Scrivi `MAPPA-OPPORTUNITA.md` nella directory corrente, una sola scrittura, file completo.

## Regole di sostanza

- Ogni mossa è eseguibile: cosa si fa, dove, e quale area della Pagella migliora. Niente buoni propositi ("migliorare la brand awareness").
- MAI cifre in euro inventate. L'impatto si dice a parole ("più richieste di preventivo", "più prenotazioni nel weekend"). Se il titolare ha dato i suoi numeri, usali e cita che sono suoi.
- Adatta tutto al tipo di business: le mosse di una trattoria non sono quelle di un e-commerce o di uno studio legale.
- Italiano concreto, da bar. Frasi corte. Niente gergo da agenzia.
- Non inventare opportunità per fare numero: se un fronte non ha senso per quel business, la riga è "niente di utile qui, ecco perché".

## Struttura del file

```markdown
# Mappa delle opportunità

**Sito:** www.esempio.it
**Tipo di business:** attività locale
**Basata su:** PAGELLA-MARKETING.md del [data]

## In due righe
Tutto quello che si può fare per questo business, dal frutto più basso al più
faticoso. Non è ancora il piano: è il quadro completo, per scegliere con la testa.

## Le mosse, dalla più conveniente alla meno

| Mossa | Fronte | Area che migliora | Impatto | Sforzo | Ha senso qui? |
|---|---|---|---|---|---|
| Rimettere a posto la scheda Google (foto, orari, servizi) | Trovabilità | Trovabilità | Alto | Basso | Sì: la maggior parte cerca "categoria + città" e la scheda è ferma |
| Un invito all'azione chiaro sopra la piega della home | Conversione | Conversione | Alto | Basso | Sì: oggi il telefono è nel footer |
| Chiedere una recensione dopo ogni servizio | Crescita | Crescita | Medio | Basso | Sì: reputazione forte non sfruttata |
| Piano editoriale social di un mese | Social | Messaggio, Crescita | Medio | Medio | Sì, ma dopo le prime due |
| Campagna Meta a raggio stretto | Pubblicità | Trovabilità | Medio | Medio | Sì, quando la scheda Google è a posto |
| Sequenze email per carrelli abbandonati | Email | Conversione | Alto | Medio | No: non è un e-commerce, non c'è carrello |
| ... | ... | ... | ... | ... | ... |

## Cosa NON fare adesso (e perché)

1. [Mossa da rimandare o evitare per questo business, con il motivo in una riga]
2. ...

## Il frutto più basso
La cosa da fare per prima, se se ne facesse una sola: [una mossa a impatto alto e
sforzo basso, con perché parte da lì].
```

## Casi particolari

- **Manca la Pagella:** non tirare a indovinare le opportunità. Rimanda a `/marketing analisi`.
- **Business appena nato, quasi vuoto:** le opportunità diventano "costruire le fondamenta" (messaggio chiaro, scheda Google, una pagina che converte) prima delle mosse di crescita. Dillo nella mappa.
- **L'utente vuole solo i frutti bassi:** filtra la tabella su impatto alto + sforzo basso e consegnala così, dicendo che il resto è nel file completo.
