#!/bin/bash
# Rimozione di Team Marketing AI da ~/.claude
# Rimuove esattamente cio' che install.sh ha copiato.

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"

echo "Verranno rimossi da ~/.claude:"
echo "  - le skill di Team Marketing AI (con gli script inclusi)"
echo "  - i 6 agenti della squadra"
echo ""
read -r -p "Confermi la rimozione? (y/n) " risposta
if [ "$risposta" != "y" ] && [ "$risposta" != "Y" ]; then
    echo "Annullato. Non e' stato rimosso nulla."
    exit 0
fi

# 1. Skill (gli script vivono dentro la skill marketing, escono con lei)
n_skill=0
for skill in "$REPO_DIR"/skills/*/; do
    nome="$(basename "$skill")"
    if [ -d "$SKILLS_DIR/$nome" ]; then
        rm -rf "${SKILLS_DIR:?}/$nome"
        n_skill=$((n_skill + 1))
    fi
done
echo "Skill rimosse: $n_skill"

# 2. Agenti
n_agenti=0
for agente in "$REPO_DIR"/squadra/*.md; do
    nome="$(basename "$agente")"
    if [ -f "$AGENTS_DIR/$nome" ]; then
        rm -f "$AGENTS_DIR/$nome"
        n_agenti=$((n_agenti + 1))
    fi
done
echo "Agenti rimossi: $n_agenti"

echo ""
echo "Rimozione completata. Riavvia Claude Code per aggiornare i comandi."
