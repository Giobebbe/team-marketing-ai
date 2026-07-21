# Team Marketing AI

Una squadra di marketing completa dentro Claude Code, in italiano, pensata per le PMI italiane. **Incolli il link di un'azienda e la squadra parte da sola**: sei specialisti analizzano il sito in parallelo, studiano i concorrenti veri, ti mostrano com'è messa oggi, ti propongono cosa fare e ti consegnano un report PDF pronto per il cliente.

![Panoramica di Team Marketing AI](assets/panoramica.png)

Dietro ogni comando non c'è un prompt che improvvisa: c'è un metodo ripetibile. Sotto trovi i metodi spiegati uno per uno, così sai esattamente cosa fa la suite e perché ti puoi fidare del risultato.

## Indice

- [Perché è diverso](#perché-è-diverso)
- [I metodi dietro la suite](#i-metodi-dietro-la-suite) (i framework)
- [Come lavora, in un colpo d'occhio](#come-lavora-in-un-colpo-docchio)
- [Installazione](#installazione)
- [I comandi, uno per uno](#i-comandi-uno-per-uno)
- [La squadra](#la-squadra)
- [Per chi è](#per-chi-è)
- [Le chiavi (opzionali)](#le-chiavi-opzionali)
- [Quanto costa](#quanto-costa)
- [Struttura del progetto](#struttura-del-progetto)
- [Disinstallazione](#disinstallazione)
- [Licenza](#licenza)

## Perché è diverso

La maggior parte degli strumenti "AI per il marketing" tira a indovinare: chiedi un'analisi dei concorrenti e ti risponde con nomi plausibili inventati sul momento. Questa suite no. Ogni giudizio parte da dati verificabili, con un metodo dichiarato, e ogni raccomandazione dice cosa fare, non solo cosa non va.

Tre cose la distinguono:

1. **Dati veri prima delle opinioni.** Concorrenti dal registro imprese e da Google Places, volumi di ricerca reali. Non "aziende simili secondo l'AI".
2. **Metodi espliciti, non magia.** La valutazione, l'analisi dei concorrenti, la scelta delle priorità: ognuno è un procedimento ripetibile che trovi scritto qui sotto. Stesso metodo, stesso tipo di risultato, ogni volta.
3. **Un deliverable da consegnare.** Un report PDF editoriale con pagella, radar del confronto coi concorrenti e piano a 90 giorni. Pronto da mettere sul tavolo di un cliente.

## I metodi dietro la suite

Questa è la parte che conta. Sei metodi, ognuno articolato in passi, che la suite applica ogni volta allo stesso modo.

### Metodo 1 · La scala dei dati veri

Il modo in cui la suite si procura i fatti prima di dare un giudizio. Si sale gradino per gradino: si usa il dato più affidabile disponibile, e solo quando manca si scende al successivo, dichiarandolo sempre nel report.

1. **Partita IVA dal sito.** Le aziende italiane devono esporla per legge, quindi c'è quasi sempre (footer o privacy policy). È la chiave che apre tutto il resto.
2. **Registro imprese** (via openapi.com). Con la P.IVA: profilo ATECO, sede legale, dipendenti, fatturato depositato. Poi i concorrenti con lo stesso codice ATECO nella stessa provincia. Aziende registrate che fanno la stessa cosa nello stesso territorio, non "aziende simili".
3. **Google Places** per le attività locali. Chi compare davvero quando un cliente cerca "idraulico Verona", con recensioni e valutazioni reali.
4. **DataForSEO** per i volumi di ricerca. Quante persone cercano davvero una parola chiave in Italia ogni mese, non una stima a occhio.
5. **Ricerca web, dichiarata.** Se una chiave API manca, la suite non si blocca: ripiega sulla ricerca web e **scrive nel report che quel dato è una stima**, non una misura. L'onestà della fonte è parte del metodo.

### Metodo 2 · La Pagella Marketing

Il modello di valutazione, unico per tutta la suite. Fotografa la salute del marketing di un'azienda su cinque aree, con un voto e un semaforo per ognuna.

| Area | Domanda a cui risponde | Vale 8+ quando | È sotto il 5 quando |
|---|---|---|---|
| **Messaggio** | Si capisce in 5 secondi cosa vendi e a chi? | Offerta chiara sopra la piega, cliente tipo evidente | Slogan vaghi, si intuisce il settore ma non l'offerta |
| **Trovabilità** | Chi ti cerca ti trova? | Contenuti sulle ricerche giuste, scheda Google curata | Invisibile sulle ricerche di categoria, scheda ferma o assente |
| **Conversione** | Chi ti trova diventa cliente? | Un invito all'azione chiaro per pagina, contatto in un click | Nessun invito, form chilometrici, telefono introvabile |
| **Concorrenza** | Perché scegliere te e non gli altri? | Differenza concreta rispetto ai concorrenti reali | Sito fotocopia, nessun motivo per preferirti |
| **Crescita** | Hai un sistema per crescere o vai a episodi? | Più canali attivi, riacquisto o passaparola coltivati | Un canale solo, nessun modo di ricontattare chi è già passato |

**Come si legge il voto:**

- Scala da 1 a 10, una cifra decimale. Ogni voto è **motivato con esempi presi dal sito**, mai con frasi generiche.
- Semaforo: 🟢 verde 8-10, 🟡 giallo 5-7.9, 🔴 rosso sotto 5.
- **Voto Finale = media semplice** delle cinque aree. Semplice apposta: nessun peso nascosto, chiunque può rifare il conto e vedere da dove esce il numero.
- Ogni area la valuta l'agente specializzato su quel fronte (vedi [La squadra](#la-squadra)).

### Metodo 3 · Analisi dei concorrenti in 5 passi

Chiunque può chiedere a un'AI "chi sono i miei concorrenti" e ricevere nomi inventati. Qui il procedimento è un altro.

1. **Inquadra l'attività.** Tipo di business, città o provincia, cosa vende esattamente. Da qui dipende tutto il resto.
2. **Scegli la fonte giusta.** Attività locale con vetrina → Google Places (stessa categoria, stessa zona). Azienda italiana → registro imprese (stesso ATECO, stessa provincia). Azienda estera o P.IVA introvabile → ricerca web dichiarata.
3. **Guardali in faccia.** Dalla lista si scelgono i 3-5 più vicini per attività e dimensione e si aprono i loro siti: come si presentano, prezzi visibili sì o no, recensioni mostrate, punti di forza dichiarati.
4. **Dove vinci, dove perdi.** Confronto punto per punto, sempre con la prova: cosa c'è sul tuo sito che loro non hanno, e viceversa.
5. **Le mosse per staccarti.** Azioni ordinate per impatto e sforzo, pensate contro *questi* concorrenti, non contro la concorrenza in astratto.

### Metodo 4 · Il flusso autonomo in 3 fasi

Cosa succede quando incolli un link senza sottocomando. La squadra non si ferma a un singolo report: percorre tutte e tre le fasi mostrandoti il lavoro mentre succede.

1. **Fase A · Fotografia as-is.** I 6 agenti partono in parallelo, con il tabellone in diretta: li vedi lavorare e vedi entrare i voti uno a uno. Esce la Pagella Marketing (Metodo 2), coi concorrenti veri (Metodo 1).
2. **Fase B · Tutto il possibile, poi la proposta.** La squadra elenca ogni mossa fattibile (Metodo 5), poi ti propone il **sottoinsieme giusto per quel business** e aspetta il tuo ok. Un idraulico di quartiere non si sente proporre le email dei carrelli abbandonati.
3. **Fase C · Piano e report.** Su conferma produce il piano a 90 giorni e il report PDF da consegnare (Metodo 6).

Alla fine hai in mano: la fotografia di com'è messa l'azienda, la mappa di tutto il possibile, il piano d'azione e il documento per il cliente.

### Metodo 5 · La mappa delle opportunità (impatto × sforzo × pertinenza)

Il catalogo di **tutto quello che si potrebbe fare**, prima di scegliere cosa fare davvero. Ogni mossa possibile riceve tre etichette:

- **Impatto**: alto / medio / basso (quanto sposta i clienti o le vendite, non quanto è vistosa).
- **Sforzo**: alto / medio / basso (tempo e mani che servono a un titolare, non a un reparto marketing).
- **Pertinenza**: ha senso per *questo* business, sì o no, con il perché. Una mossa può essere ottima in generale e inutile qui: la mappa lo dice.

In cima finiscono i frutti bassi (impatto alto, sforzo basso), in fondo quello che conviene lasciar stare per ora. Un consulente bravo si vede anche da cosa toglie.

### Metodo 6 · La matrice impatto/sforzo e il report

Le opportunità del Metodo 5 diventano priorità visive in una matrice 2×2, che finisce nel report PDF insieme al resto:

- **Fai subito** (impatto alto, sforzo basso) · **Pianifica** (impatto alto, sforzo alto)
- **Opzionale** (impatto basso, sforzo basso) · **Lascia stare per ora** (impatto basso, sforzo alto)

Il report finale (`REPORT-CLIENTE.pdf`) è un documento editoriale multipagina: copertina, pagella a barre, analisi area per area con le evidenze citate, **radar del confronto coi concorrenti**, questa matrice, piano a 90 giorni, e la pagina di metodologia e fonti. Impaginato sempre allo stesso modo: tu compili i dati, lo script fa la grafica.

## Come lavora, in un colpo d'occhio

```
   un link
      │
      ▼
┌─────────────────┐   Metodo 1: P.IVA → registro imprese → Places → DataForSEO
│  dati veri      │   (web dichiarato se manca una chiave)
└────────┬────────┘
         ▼
┌─────────────────┐   Metodo 2 + 4/Fase A: 6 agenti in parallelo, tabellone in diretta
│  la squadra     │   → PAGELLA-MARKETING.md
└────────┬────────┘
         ▼
┌─────────────────┐   Metodo 5 + 4/Fase B: ogni mossa possibile, poi la proposta su misura
│  opportunità    │   → MAPPA-OPPORTUNITA.md  →  "procedo con questi?"
└────────┬────────┘
         ▼ (su conferma)
┌─────────────────┐   Metodo 6 + 4/Fase C: priorità, piano, documento per il cliente
│  piano + report │   → PIANO-90-GIORNI.md  +  REPORT-CLIENTE.pdf
└─────────────────┘
```

## Installazione

```bash
git clone https://github.com/Giobebbe/team-marketing-ai.git
cd team-marketing-ai
bash install.sh
```

Poi riavvia Claude Code. I comandi `/marketing` saranno disponibili in qualsiasi progetto.

Per il solo report PDF serve una libreria: `pip3 install -r requirements.txt` (reportlab). Tutto il resto gira con Python 3 puro, zero dipendenze.

## I comandi, uno per uno

Il flusso autonomo (`/marketing www.azienda.it`) percorre da solo i tre metodi in fila. Se preferisci lavorare a pezzi, ogni fase è anche un comando a sé.

| Comando | Cosa fa | Metodo | File prodotto |
|---|---|---|---|
| `/marketing <url>` | Flusso autonomo completo: as-is, proposta, piano, report | 1→6 | tutti i file sotto |
| `/marketing analisi` | La Pagella Marketing completa: 6 agenti in parallelo su 5 aree | 1, 2 | `PAGELLA-MARKETING.md` |
| `/marketing competitor` | Concorrenti veri da registro imprese e Google Places | 1, 3 | `ANALISI-COMPETITOR.md` |
| `/marketing seo` | Analisi SEO: parole chiave, volumi reali, priorità | 1 | `PIANO-SEO.md` |
| `/marketing contenuti` | Piano editoriale calibrato sul pubblico dell'azienda | 2 | `PIANO-CONTENUTI.md` |
| `/marketing email` | Sequenze email pronte: benvenuto, nurturing, recupero | 2 | `SEQUENZE-EMAIL.md` |
| `/marketing social` | Calendario social di un mese con post già scritti | 2 | `CALENDARIO-SOCIAL.md` |
| `/marketing ads` | Struttura campagne: pubblici, budget, testi degli annunci | 2 | `CAMPAGNE-ADS.md` |
| `/marketing landing` | Sistema una singola pagina: checklist 7 punti e riscritture | 2 | `ANALISI-LANDING.md` |
| `/marketing funnel` | Mappa il percorso del cliente e trova dove si perde | 2 | `ANALISI-FUNNEL.md` |
| `/marketing opportunita` | La mappa di tutto il possibile, con impatto e sforzo | 5 | `MAPPA-OPPORTUNITA.md` |
| `/marketing piano` | Piano operativo di 90 giorni, in ordine di priorità | 6 | `PIANO-90-GIORNI.md` |
| `/marketing report` | Report PDF professionale da consegnare al cliente | 6 | `REPORT-CLIENTE.pdf` |

## La squadra

Sei agenti specializzati, ognuno con il proprio file in `squadra/`. Nella Pagella ognuno vota l'area di sua competenza, così ogni voto ha dietro uno specialista, non un giudizio unico e generico.

| Agente | Di cosa risponde | Vota |
|---|---|---|
| **stratega-marketing** | Chiarezza dell'offerta e leve di crescita; coordina e scrive il piano | Messaggio, Crescita |
| **specialista-seo** | Visibilità su Google e presenza locale | Trovabilità |
| **esperto-conversioni** | Percorso dal visitatore al contatto o alla vendita | Conversione |
| **analista-competitor** | Registro imprese, Places, confronto coi concorrenti reali | Concorrenza |
| **copywriter-pmi** | Riscritture concrete di titoli e testi deboli | contributo qualitativo |
| **media-buyer** | Dove ha senso spendere in pubblicità, e se ha senso ora | contributo qualitativo |

## Per chi è

- **Titolari di PMI** che vogliono capire dove perde colpi il loro marketing senza pagare un audit da migliaia di euro.
- **Consulenti e agenzie** che vogliono produrre analisi e report per i clienti in una frazione del tempo. `/marketing report` nasce per questo: il documento da consegnare esce già impaginato.
- **Chi parte da zero** e vuole un piano di 90 giorni concreto invece di una lista di buone intenzioni.

## Le chiavi (opzionali)

La suite funziona anche senza chiavi API: in quel caso la scala dei dati veri (Metodo 1) scende all'ultimo gradino e usa la ricerca web, dichiarandolo nel report. Con le chiavi arrivano i dati misurati.

| Variabile | Dove ottenerla | Costo |
|---|---|---|
| `OPENAPI_TOKEN` | console.openapi.com | Fascia gratuita: 100 ricerche al giorno |
| `GOOGLE_PLACES_API_KEY` | Google Cloud Console | Fascia gratuita mensile inclusa |
| `DATAFORSEO_LOGIN` e `DATAFORSEO_PASSWORD` | dataforseo.com | A consumo, pochi centesimi a richiesta |

Per configurarle:

```bash
cp .env.example .env
# apri .env e incolla le tue chiavi
```

Nota su openapi.com: l'attivazione della Company API richiede una verifica d'identità con un documento (il registro imprese è un dato regolamentato, la richiedono a tutti). Si fa una volta sola dalla console: Company API, Activate, carichi il documento, aspetti l'approvazione e generi il token. Nel frattempo la suite funziona comunque col fallback web.

## Quanto costa

Ogni script ha un tetto rigido di 1 o 2 chiamate API per esecuzione e stampa il costo stimato a fine run. Con le fasce gratuite dei tre servizi, un uso normale (qualche analisi a settimana) costa zero. Non ci sono chiamate nascoste né loop che consumano credito.

## Struttura del progetto

```
team-marketing-ai/
├── skills/          # le skill di Claude Code (una per comando)
├── squadra/         # i 6 agenti specializzati
├── scripts/         # script Python (dati reali in stdlib; generatore PDF con reportlab)
├── assets/          # font (Cormorant, DM Sans) e immagine di copertina per il report PDF
├── requirements.txt # reportlab (serve solo per il report PDF)
├── install.sh       # installazione
├── uninstall.sh     # rimozione pulita
└── .env.example     # modello per le chiavi API
```

Gli script dei dati reali (registro, Places, volumi) sono Python 3 puro, zero dipendenze. Il solo report PDF (`/marketing report`) usa **reportlab**: `pip3 install reportlab` (o `pip3 install -r requirements.txt`).

## Disinstallazione

```bash
bash uninstall.sh
```

Rimuove esattamente quello che `install.sh` ha copiato in `~/.claude`, senza toccare altro.

## Licenza

MIT. Vedi il file `LICENSE`.
