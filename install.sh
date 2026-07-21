#!/bin/bash
# Installazione di Team Marketing AI in ~/.claude
set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"

echo "Installazione di Team Marketing AI..."
echo ""

mkdir -p "$SKILLS_DIR" "$AGENTS_DIR"

# 1. Skill
n_skill=0
for skill in "$REPO_DIR"/skills/*/; do
    nome="$(basename "$skill")"
    rm -rf "${SKILLS_DIR:?}/$nome"
    cp -R "$skill" "$SKILLS_DIR/$nome"
    n_skill=$((n_skill + 1))
done
echo "Skill installate: $n_skill"

# 2. Agenti della squadra
n_agenti=0
for agente in "$REPO_DIR"/squadra/*.md; do
    cp "$agente" "$AGENTS_DIR/"
    n_agenti=$((n_agenti + 1))
done
echo "Agenti installati: $n_agenti"

# 3. Script Python
mkdir -p "$SKILLS_DIR/marketing/scripts"
n_script=0
for script in "$REPO_DIR"/scripts/*.py; do
    cp "$script" "$SKILLS_DIR/marketing/scripts/"
    chmod +x "$SKILLS_DIR/marketing/scripts/$(basename "$script")"
    n_script=$((n_script + 1))
done
echo "Script installati: $n_script"

# 4. Asset del report PDF (font + immagine di copertina)
if [ -d "$REPO_DIR/assets" ]; then
    rm -rf "$SKILLS_DIR/marketing/assets"
    cp -R "$REPO_DIR/assets" "$SKILLS_DIR/marketing/assets"
    echo "Asset del report installati."
fi

# 5. Controllo python3 e reportlab
if ! command -v python3 >/dev/null 2>&1; then
    echo ""
    echo "Attenzione: python3 non trovato sul sistema."
    echo "Gli script dei dati reali (registro imprese, Places, volumi) non funzioneranno finche' non lo installi."
elif ! python3 -c "import reportlab" >/dev/null 2>&1; then
    echo ""
    echo "Nota: 'reportlab' non installato: serve solo per il report PDF (/marketing report)."
    echo "Installalo con: pip3 install reportlab"
fi

echo ""
echo "Installazione completata: $n_skill skill, $n_agenti agenti, $n_script script."
echo ""
echo "Comando principale:"
echo "  /marketing <url>       Flusso autonomo: as-is, opportunita, proposta, piano e report PDF"
echo ""
echo "Comandi singoli:"
echo "  /marketing analisi     Pagella Marketing completa (6 agenti in parallelo)"
echo "  /marketing competitor  Concorrenti veri da registro imprese e Google Places"
echo "  /marketing seo         Analisi SEO con volumi di ricerca reali"
echo "  /marketing contenuti   Piano editoriale"
echo "  /marketing email       Sequenze email"
echo "  /marketing social      Calendario social di un mese"
echo "  /marketing ads         Struttura campagne a pagamento"
echo "  /marketing opportunita La mappa di tutto il possibile (impatto/sforzo)"
echo "  /marketing piano       Piano operativo di 90 giorni"
echo "  /marketing report      Report PDF professionale da consegnare al cliente"
echo ""
echo "Riavvia Claude Code per caricare i comandi."
