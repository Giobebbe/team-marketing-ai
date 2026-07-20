---
name: marketing-report
description: Impacchetta i report di marketing della directory corrente in un report visivo da consegnare a un cliente pagante (REPORT-CLIENTE.html) con grafici veri - scorecard as-is, radar cliente vs concorrenti, matrice impatto/sforzo - autoconsistente, zero dipendenze, si apre nel browser e si stampa in PDF. Pensato per consulenti e agenzie. Si attiva con /marketing report seguito dal nome del cliente, oppure "preparami il report per il cliente", "documento da consegnare", "report presentabile", "report con i grafici".
---

# /marketing report [nome cliente]

Il deliverable che fa scena. Prende i report tecnici della directory corrente e li trasforma in un **report visivo HTML** che un titolare di PMI legge in dieci minuti e capisce da solo: grafici che mostrano com'è messo oggi, come sta rispetto ai concorrenti, e cosa conviene fare (e cosa no). Un solo file, `REPORT-CLIENTE.html`, che si apre nel browser e si stampa in PDF con un clic.

## Quando si attiva

- `/marketing report Trattoria Dal Moro` (o un altro nome cliente)
- "prepara il documento per il cliente", "rendilo presentabile", "report con i grafici", "devo consegnarlo lunedì"

## Cosa legge

Tutti i report della suite presenti nella directory corrente: `PAGELLA-MARKETING.md` (obbligatorio per i grafici), `MAPPA-OPPORTUNITA.md`, `ANALISI-COMPETITOR.md`, `PIANO-SEO.md`, `PIANO-CONTENUTI.md`, `SEQUENZE-EMAIL.md`, `CALENDARIO-SOCIAL.md`, `CAMPAGNE-ADS.md`, `PIANO-90-GIORNI.md`.

Se non c'è nessun report, fermati: "Non c'è niente da impacchettare. Parti da `/marketing analisi`, poi torna qui." Se manca solo la Pagella, il report si fa ma senza grafici: avvisa l'utente e procedi in versione testo.

## Procedura

1. **Nome cliente e autore.** Prendi il nome del cliente dal comando. Se manca, chiedilo insieme al nome da mettere in copertina (il consulente o l'agenzia). Mai segnaposto vuoti in un documento da consegnare.
2. **Leggi i dati.** Apri i report presenti. Dalla Pagella estrai: tipo di business, la fotografia as-is, i 5 voti (Messaggio, Trovabilità, Conversione, Concorrenza, Crescita), il Voto Finale, i concorrenti trovati e la tabella "Confronto col concorrente principale (stima)". Dalla Mappa delle opportunità estrai le mosse con impatto/sforzo/pertinenza.
3. **Scrivi la sintesi in una pagina**, in linguaggio non tecnico: com'è messo il marketing oggi, cosa non toccare, cosa costa clienti, cosa succede nei 90 giorni. Chi legge solo questa pagina deve avere il quadro.
4. **Prepara i dati dei grafici** (vedi sotto: scorecard, radar, matrice). Calcola le coordinate SVG dai voti veri. Se un input manca (es. niente stima concorrente), salta quel grafico e dillo in una riga, non inventare numeri.
5. **Genera `REPORT-CLIENTE.html`** con lo scheletro qui sotto: una sola scrittura, file completo, autoconsistente (nessun CDN, nessuna libreria, CSS e SVG inline). Il file deve aprirsi anche offline con doppio clic.
6. **Apri il file**: `open REPORT-CLIENTE.html` (su mac). Se `open` non c'è, stampa il path e di' all'utente di aprirlo nel browser e usare Stampa > Salva come PDF per la versione da consegnare.
7. **Consegna** all'utente il nome del file e due righe su cosa contiene.

## I tre grafici (SVG inline, calcolati dai numeri veri)

Palette già validata (colorblind-safe, chiara in light e dark). Definiscila come variabili CSS in cima al file e usa i ruoli, mai l'hex grezzo nel corpo.

| Ruolo | Light | Dark |
|---|---|---|
| Superficie | `#fcfcfb` | `#1a1a19` |
| Testo primario | `#0b0b0b` | `#ffffff` |
| Testo secondario | `#52514e` | `#c3c2b7` |
| Serie "Tu" (blu) | `#2a78d6` | `#3987e5` |
| Serie "Concorrente" (arancio) | `#eb6834` | `#d95926` |
| Verde (semaforo) | `#008300` | `#008300` |
| Giallo (semaforo) | `#eda100` | `#c98500` |
| Rosso (semaforo) | `#e34948` | `#e66767` |

Regole comuni: titoli **allineati a sinistra** (mai centrati), marchi sottili, ogni serie con etichetta diretta (identità mai affidata al solo colore), griglia in secondo piano. Il semaforo porta sempre il voto scritto accanto, non solo il colore.

### 1. Scorecard as-is (barre orizzontali)
Cinque barre, una per area, sotto un indicatore grande del Voto Finale.
- Larghezza barra = `voto / 10 * larghezza_max`.
- Colore barra = semaforo: verde se voto ≥ 8, giallo se 5-7.9, rosso se < 5.
- A destra di ogni barra il voto in cifra. A sinistra il nome dell'area.
È il colpo d'occhio sulla situazione attuale.

### 2. Radar cliente vs concorrente (pentagono a 5 assi)
Due poligoni sovrapposti sulle 5 aree: "Tu" (blu) e "[Concorrente]" (arancio), con legenda.
- 5 assi, angolo asse `i` = `-90° + i*72°` (i da 0 a 4), ordine aree: Messaggio, Trovabilità, Conversione, Concorrenza, Crescita.
- Vertice per un voto `v` (0-10): raggio `r = v/10 * R`; `x = cx + r*cos(angolo)`, `y = cy + r*sin(angolo)` (angoli in radianti).
- Riempimento poligono a ~18% opacità, bordo pieno 2px. Etichetta dell'area alla punta di ogni asse.
- I voti del concorrente vengono dalla tabella stima della Pagella: metti una nota "(stima)" nella legenda. Se la stima manca, disegna solo "Tu" e scrivi che il confronto non è disponibile.

### 3. Matrice impatto/sforzo (2×2)
Le mosse della Mappa delle opportunità come punti in quattro quadranti.
- Asse X = sforzo (sinistra basso → destra alto). Asse Y = impatto (basso in basso → alto in alto).
- Mappa le etichette: basso→0.2, medio→0.5, alto→0.8 della dimensione; per l'impatto in SVG ricorda che y cresce verso il basso, quindi impatto alto = y piccolo.
- Quadranti con sfondo tenue e nome: alto-basso = **Fai subito**, alto-alto = **Pianifica**, basso-basso = **Opzionale**, basso-alto = **Lascia stare**.
- **Etichette in legenda numerata sotto il grafico, non accanto ai punti** (le posizioni possibili sono poche e i punti si accavallano quasi sempre): ogni punto porta solo il suo numero, la lista `1. nome mossa · 2. ...` sta sotto. Se più mosse cadono nello stesso quadrante, spargile con un piccolo scostamento (jitter di qualche pixel) così non si coprono. È il "cosa migliorare e cosa no", visivo.

## Scheletro del file (adattalo, non copiarlo alla lettera)

```html
<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Report Marketing — [Nome Cliente]</title>
<style>
  :root { color-scheme: light dark; }
  .viz-root {
    --surface-1:#fcfcfb; --text-primary:#0b0b0b; --text-secondary:#52514e;
    --tu:#2a78d6; --comp:#eb6834; --verde:#008300; --giallo:#eda100; --rosso:#e34948;
  }
  @media (prefers-color-scheme: dark) {
    :root:where(:not([data-theme="light"])) .viz-root {
      --surface-1:#1a1a19; --text-primary:#fff; --text-secondary:#c3c2b7;
      --tu:#3987e5; --comp:#d95926; --giallo:#c98500; --rosso:#e66767;
    }
  }
  :root[data-theme="dark"] .viz-root {
    --surface-1:#1a1a19; --text-primary:#fff; --text-secondary:#c3c2b7;
    --tu:#3987e5; --comp:#d95926; --giallo:#c98500; --rosso:#e66767;
  }
  body{margin:0;background:var(--surface-1);color:var(--text-primary);
    font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;}
  .viz-root{max-width:860px;margin:0 auto;padding:40px 24px;}
  h1,h2,h3{text-align:left;line-height:1.2;}
  h1{font-size:2rem;margin:0 0 .2em;} h2{font-size:1.4rem;margin:2em 0 .6em;}
  .meta{color:var(--text-secondary);margin-bottom:2em;}
  .card{border:1px solid color-mix(in srgb,var(--text-secondary) 22%,transparent);
    border-radius:12px;padding:20px 22px;margin:16px 0;}
  svg{max-width:100%;height:auto;display:block;}
  table{border-collapse:collapse;width:100%;} td,th{text-align:left;padding:6px 10px;
    border-bottom:1px solid color-mix(in srgb,var(--text-secondary) 18%,transparent);}
  @media print{ .viz-root{max-width:none;} .card{break-inside:avoid;} }
</style>
</head>
<body>
<main class="viz-root">
  <h1>Report Marketing: [Nome Cliente]</h1>
  <p class="meta">Preparato da [autore] · [data] · [tipo di business]</p>

  <section><!-- La situazione in una pagina (testo non tecnico) --></section>

  <h2>Com'è messo oggi</h2>
  <div class="card"><!-- SVG scorecard: 5 barre + Voto Finale --></div>

  <h2>Tu e i tuoi concorrenti</h2>
  <div class="card"><!-- SVG radar 5 assi, 2 poligoni + legenda --></div>

  <h2>Cosa conviene fare (e cosa no)</h2>
  <div class="card"><!-- SVG matrice impatto/sforzo 2x2 --></div>
  <!-- sotto, la tabella delle mosse dalla Mappa delle opportunità -->

  <h2>I 3 problemi che costano di più</h2>
  <!-- per ognuno: cosa succede oggi, cosa costa (in clienti, mai euro inventati), come si sistema -->

  <h2>Il piano</h2>
  <!-- tre fasi dal PIANO-90-GIORNI.md, azioni in una riga con chi le fa -->

  <h2>Prossimo passo</h2>
  <!-- una sola cosa che il cliente deve decidere o fare per partire -->
</main>
</body>
</html>
```

## Tono: da consulente che parla chiaro

Regole fisse per tutto il testo (non per la tabella tecnica delle mosse):

| Non scrivere | Scrivi |
|---|---|
| Il funnel presenta friction nella fase di consideration | Chi visita il sito fa fatica a capire come contattarvi |
| Ottimizzare la CTR delle campagne | Far cliccare più persone tra quelle che vedono l'annuncio |
| Lead generation | Raccolta di contatti interessati |
| Il posizionamento non è distintivo | Il sito dice le stesse cose dei concorrenti |

- Frasi corte. Una frase, un concetto. Ogni numero cita la fonte (quale report, quale pagina, quale script).
- Mai promettere risultati: "l'obiettivo è", non "otterrete". Mai cifre in euro inventate: valgono solo se già nei report con la loro fonte.
- Del cliente si parla con rispetto anche nei problemi: "la pagina contatti si può migliorare così", non "è fatta male".
- Anglicismi solo dove l'italiano non esiste (email, social, Google Ads sì; "journey", "insight", "asset" no).

## Esempio del tono giusto (la sintesi in una pagina)

```
La trattoria ha una reputazione che molti concorrenti si sognano: 4,7 su
Google, con recensioni entusiaste sulla cucina. Il problema è che questa
reputazione non si vede: il sito non la mostra, la scheda Google ha foto
di tre anni fa e chi cerca "trattoria verona centro" trova prima altri
tre locali. In pratica: il lavoro difficile (cucinare bene) è già fatto,
quello facile (farlo sapere) no. Il piano dei prossimi 90 giorni serve
a chiudere questa distanza.
```

## Casi particolari

- **Manca la Pagella:** niente grafici. Fai il report in versione testo (sintesi + problemi + piano) e avvisa l'utente che con `/marketing analisi` esce con scorecard e radar.
- **Manca la stima concorrente:** disegna solo il poligono "Tu" e scrivi che il confronto non è disponibile finché non giri `/marketing competitor`.
- **Manca la Mappa delle opportunità:** salta la matrice impatto/sforzo, tieni gli altri due grafici, e suggerisci `/marketing opportunita`.
- **Nome cliente mancante:** chiedi nome cliente e autore prima di generare.
- **Report con date lontane:** indica in copertina il periodo dei dati. Se un report ha più di 60 giorni, suggerisci di rigenerarlo prima di consegnare.
- **Numeri in euro:** solo se già nei report con la fonte. Ogni stima chiesta dall'utente entra dichiarata come ipotesi, col ragionamento accanto.
