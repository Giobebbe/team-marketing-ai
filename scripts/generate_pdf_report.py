#!/usr/bin/env python3
"""
Generatore PDF del report marketing -- Team Marketing AI
Report cliente di fascia alta: copertina editoriale full-bleed, sommario,
pagella, analisi area per area, radar, matrice priorita', piano 90 giorni.
Impianto reportlab (come la suite di riferimento) sul nostro modello dati.

Direzione artistica "Atelier": carta avorio, inchiostro caldo, un solo accento
verde pino, display serif Cormorant + corpo DM Sans.

Richiede: reportlab (pip install reportlab)
Uso:
  python3 scripts/generate_pdf_report.py dati.json REPORT-CLIENTE.pdf
  python3 scripts/generate_pdf_report.py            # demo di esempio
"""
import sys, json, os, math
from datetime import datetime

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.colors import HexColor, Color
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.utils import ImageReader
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                    TableStyle, PageBreak, KeepTogether)
    from reportlab.graphics.shapes import Drawing, Rect, Circle, String, Line, Polygon, Wedge
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
except ImportError:
    print("Errore: serve reportlab. Installa con: pip3 install reportlab")
    sys.exit(1)

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")

# ------------------------------------------------------------------ font
SERIF, SANS, SANS_MED = "Times-Roman", "Helvetica", "Helvetica-Bold"
def _try_font(name, path):
    pdfmetrics.registerFont(TTFont(name, os.path.join(ASSETS, "fonts", path)))
try:
    _try_font("Serif", "Cormorant-VF.ttf"); SERIF = "Serif"
except Exception:
    pass
try:
    _try_font("Sans", "DMSans-Regular.ttf"); _try_font("Sans-Med", "DMSans-Medium.ttf")
    pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="Sans-Med", italic="Sans", boldItalic="Sans-Med")
    SANS, SANS_MED = "Sans", "Sans-Med"
except Exception:
    pass

# ------------------------------------------------------------------ palette
C = {
    "bone":   HexColor("#ECE7DC"),   # carta avorio calda
    "bone2":  HexColor("#E4DDCF"),   # pannello
    "ink":    HexColor("#1C1815"),   # nero caldo (espresso)
    "ink2":   HexColor("#4A423A"),   # testo scuro morbido
    "stone":  HexColor("#8B8173"),   # testo muto
    "line":   HexColor("#D6CDBC"),   # filetti
    "accent": HexColor("#2E4034"),   # verde pino (accento unico)
    "cream":  HexColor("#EFE9DD"),   # testo su fondo scuro
    "good":   HexColor("#3B5346"),   # pino
    "mid":    HexColor("#9C7A3E"),   # ocra
    "low":    HexColor("#8C4A3B"),   # oxblood
    "barbg":  HexColor("#DED6C7"),
    "barfill":HexColor("#33291F"),   # marrone inchiostro
}

def voto_color(v):
    return C["good"] if v >= 8 else (C["mid"] if v >= 5 else C["low"])
def voto_stato(v):
    return "solido" if v >= 8 else ("da rafforzare" if v >= 5 else "critico")
def hexcol(c):
    return "#%02x%02x%02x" % (int(c.red * 255), int(c.green * 255), int(c.blue * 255))
def _wrap(text, font, size, maxw):
    lines, cur = [], ""
    for w in (text or "").split():
        t = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(t, font, size) <= maxw:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

# ------------------------------------------------------------------ disegni
def gauge(v, size=120):
    d = Drawing(size, size); r = size / 2; cx = cy = r; col = voto_color(v)
    d.add(Circle(cx, cy, r - 3, fillColor=None, strokeColor=C["line"], strokeWidth=1))
    frac = max(0.0, min(1.0, v / 10.0))
    d.add(Wedge(cx, cy, r - 3, 90 - 360 * frac, 90, fillColor=col, strokeColor=None))
    d.add(Circle(cx, cy, r - 9, fillColor=C["bone"], strokeColor=None))
    d.add(String(cx, cy - 12, f"{v:.1f}", fontSize=34, fillColor=C["ink"], textAnchor="middle", fontName=SERIF))
    d.add(String(cx, cy - 26, "SU 10", fontSize=7, fillColor=C["stone"], textAnchor="middle", fontName=SANS_MED))
    d.hAlign = "LEFT"
    return d

def bar_chart(areas, scores, notes):
    row = 40; W = 500; H = row * len(areas)
    bx, bw, bh = 150, 250, 8
    d = Drawing(W, H)
    for i, (a, v, note) in enumerate(zip(areas, scores, notes)):
        y = H - (i + 1) * row + 16
        d.add(String(0, y + 4, a, fontSize=13, fillColor=C["ink"], fontName=SERIF))
        d.add(String(0, y - 9, note[:54], fontSize=8, fillColor=C["stone"], fontName=SANS))
        d.add(Rect(bx, y, bw, bh, fillColor=C["barbg"], strokeColor=None))
        d.add(Rect(bx, y, (v / 10) * bw, bh, fillColor=C["barfill"], strokeColor=None))
        d.add(Circle(bx + bw + 20, y + bh / 2, 3.5, fillColor=voto_color(v), strokeColor=None))
        d.add(String(bx + bw + 32, y - 2, f"{v:.1f}", fontSize=17, fillColor=C["ink"], fontName=SERIF))
    return d

def radar(areas, tu, comp):
    size = 210; d = Drawing(size, size)
    cx, cy, R, n = size / 2, size / 2, size / 2 - 40, len(areas)
    def pt(i, val):
        ang = math.radians(90 - i * 360 / n); rr = val / 10 * R
        return cx + rr * math.cos(ang), cy + rr * math.sin(ang)
    for ring in (2, 4, 6, 8, 10):
        pts = []
        for i in range(n):
            x, y = pt(i, ring); pts += [x, y]
        d.add(Polygon(pts, fillColor=None, strokeColor=C["line"], strokeWidth=0.6))
    for i, a in enumerate(areas):
        x, y = pt(i, 10)
        d.add(Line(cx, cy, x, y, strokeColor=C["line"], strokeWidth=0.6))
        lx, ly = pt(i, 11.6)
        anc = "middle" if abs(lx - cx) < 8 else ("start" if lx > cx else "end")
        d.add(String(lx, ly - 3, a, fontSize=7.5, fillColor=C["ink2"], textAnchor=anc, fontName=SANS))
    if comp:
        cp = []
        for i in range(n):
            x, y = pt(i, comp[i]); cp += [x, y]
        d.add(Polygon(cp, fillColor=None, strokeColor=C["stone"], strokeWidth=1.3, strokeDashArray=[3, 2]))
    tp = []
    for i in range(n):
        x, y = pt(i, tu[i]); tp += [x, y]
    d.add(Polygon(tp, fillColor=Color(0.18, 0.25, 0.20, 0.16), strokeColor=C["accent"], strokeWidth=1.8))
    d.hAlign = "LEFT"
    return d

def radar_legend(cliente, comp_nome):
    d = Drawing(230, 30)
    d.add(Rect(0, 17, 11, 11, fillColor=C["accent"], strokeColor=None))
    d.add(String(18, 20, cliente, fontSize=10, fillColor=C["ink"], fontName=SANS))
    d.add(Rect(0, 1, 11, 11, fillColor=None, strokeColor=C["stone"], strokeWidth=1.2, strokeDashArray=[2, 1.5]))
    d.add(String(18, 4, f"{comp_nome} (stima)", fontSize=10, fillColor=C["stone"], fontName=SANS))
    d.hAlign = "LEFT"
    return d

def matrix(opps):
    W, H, m = 500, 200, 22
    pw, ph = W - 2 * m, H - 2 * m
    pos = {"basso": 0.22, "medio": 0.5, "alto": 0.78}
    d = Drawing(W, H)
    d.add(Rect(m, m + ph / 2, pw / 2, ph / 2, fillColor=C["bone2"], strokeColor=None))
    d.add(Line(m, m + ph / 2, m + pw, m + ph / 2, strokeColor=C["line"], strokeWidth=0.8))
    d.add(Line(m + pw / 2, m, m + pw / 2, m + ph, strokeColor=C["line"], strokeWidth=0.8))
    for x, y, t, col in [(m + 6, m + ph - 12, "FAI SUBITO", C["accent"]),
                         (m + pw / 2 + 6, m + ph - 12, "PIANIFICA", C["stone"]),
                         (m + 6, m + ph / 2 - 14, "OPZIONALE", C["stone"]),
                         (m + pw / 2 + 6, m + ph / 2 - 14, "LASCIA STARE", C["stone"])]:
        d.add(String(x, y, t, fontSize=7.5, fillColor=col, fontName=SANS_MED))
    d.add(String(m, m - 15, "MENO SFORZO  →  PIU SFORZO", fontSize=7, fillColor=C["stone"], fontName=SANS))
    seen = {}
    for o in opps:
        imp, sf = o["impatto"], o["sforzo"]; k = seen.get((imp, sf), 0); seen[(imp, sf)] = k + 1
        jx = (k % 2) * 17 - 5; jy = -(k // 2) * 17
        x = m + pos[sf] * pw + jx; y = m + pos[imp] * ph + jy
        hot = imp == "alto" and sf == "basso"
        d.add(Circle(x, y, 9.5, fillColor=C["accent"] if hot else C["stone"], strokeColor=None))
        d.add(String(x, y - 3.5, str(o["n"]), fontSize=9, fillColor=C["cream"], textAnchor="middle", fontName=SANS_MED))
    return d

# ------------------------------------------------------------------ stili
def styles():
    s = {}
    s["standfirst"] = ParagraphStyle("sf", fontName=SERIF, fontSize=17, textColor=C["ink"], leading=23, alignment=TA_LEFT, spaceAfter=4)
    s["lead"] = ParagraphStyle("l", fontName=SANS, fontSize=11, textColor=C["ink2"], leading=17, alignment=TA_LEFT, spaceAfter=6)
    s["body"] = ParagraphStyle("b", fontName=SANS, fontSize=9.5, textColor=C["ink2"], leading=14.5, alignment=TA_LEFT, spaceAfter=4)
    s["area"] = ParagraphStyle("a", fontName=SERIF, fontSize=15, textColor=C["ink"], leading=18, alignment=TA_LEFT, spaceBefore=12, spaceAfter=3, keepWithNext=1)
    s["probt"] = ParagraphStyle("p", fontName=SERIF, fontSize=14, textColor=C["ink"], leading=17, alignment=TA_LEFT, spaceBefore=12, spaceAfter=3, keepWithNext=1)
    s["h3"] = ParagraphStyle("h3", fontName=SANS_MED, fontSize=10, textColor=C["accent"], leading=13, alignment=TA_LEFT, spaceBefore=10, spaceAfter=6, keepWithNext=1)
    s["cell"] = ParagraphStyle("c", fontName=SANS, fontSize=8.5, textColor=C["ink2"], leading=11.5, alignment=TA_LEFT)
    s["small"] = ParagraphStyle("sm", fontName=SANS, fontSize=8, textColor=C["stone"], leading=11, alignment=TA_LEFT)
    return s

def opener(num, title):
    d = Drawing(500, 44)
    d.add(String(0, 12, num, fontSize=30, fillColor=C["accent"], fontName=SERIF))
    d.add(String(46, 15, title, fontSize=20, fillColor=C["ink"], fontName=SERIF))
    d.add(Line(0, 4, 500, 4, strokeColor=C["line"], strokeWidth=0.8))
    d.hAlign = "LEFT"
    return d

# ------------------------------------------------------------------ report
def generate(data, out):
    S = styles()
    doc = SimpleDocTemplate(out, pagesize=A4, leftMargin=52, rightMargin=52, topMargin=54, bottomMargin=54,
                            title=f"Report Marketing — {data.get('cliente','')}", author="Gentes AI")
    E = []
    cliente = data.get("cliente", "Cliente")
    voto = float(data.get("voto_finale", 0))
    aree = data.get("aree", [])

    E.append(Spacer(1, 2)); E.append(PageBreak())  # pagina 1 = cover (canvas)

    # ---- I. Sommario + as-is + pagella
    E.append(opener("I", "Sommario")); E.append(Spacer(1, 12))
    E.append(Paragraph(data.get("executive_summary", ""), S["standfirst"])); E.append(Spacer(1, 10))
    asis = data.get("as_is", {})
    for k, lab in [("cosa_vende", "Cosa vende e a chi"), ("canali", "Canali attivi oggi"), ("dove_perde", "Dove si perdono i clienti")]:
        if asis.get(k):
            E.append(Paragraph(f'<font name="{SANS_MED}" color="{hexcol(C["ink"])}">{lab}.</font> {asis[k]}', S["body"]))
    E.append(Spacer(1, 16))
    if aree:
        E.append(Paragraph("LA PAGELLA", S["h3"]))
        names = [a["nome"] for a in aree]; scores = [float(a["voto"]) for a in aree]; notes = [a.get("nota", "") for a in aree]
        E.append(bar_chart(names, scores, notes))

    # ---- II. Analisi area per area
    if any(a.get("analisi") for a in aree):
        E.append(opener("II", "Analisi area per area")); E.append(Spacer(1, 6))
        for a in aree:
            an = a.get("analisi") or {}
            if not an: continue
            v = float(a["voto"])
            E.append(Paragraph(f'{a["nome"]} <font name="{SANS_MED}" size="10" color="{hexcol(voto_color(v))}">&nbsp;&nbsp;{v:.1f} / 10 · {voto_stato(v)}</font>', S["area"]))
            if an.get("funziona"): E.append(Paragraph(f'<font name="{SANS_MED}" color="{hexcol(C["ink"])}">Cosa funziona.</font> {an["funziona"]}', S["body"]))
            if an.get("manca"): E.append(Paragraph(f'<font name="{SANS_MED}" color="{hexcol(C["ink"])}">Cosa manca.</font> {an["manca"]}', S["body"]))
            for act in an.get("fare", []):
                E.append(Paragraph(f'<font color="{hexcol(C["accent"])}">&#8212;</font>&nbsp; {act}', S["body"]))

    # ---- III. Problemi
    problemi = data.get("problemi", [])
    if problemi:
        E.append(opener("III", "I problemi che costano di piu")); E.append(Spacer(1, 6))
        for i, p in enumerate(problemi, 1):
            E.append(Paragraph(f'{i}.  {p.get("titolo","")}', S["probt"]))
            for k, lab in [("oggi", "Cosa succede oggi"), ("costa", "Cosa costa"), ("sistema", "Come si sistema")]:
                if p.get(k):
                    E.append(Paragraph(f'<font name="{SANS_MED}" color="{hexcol(C["ink"])}">{lab}.</font> {p[k]}', S["body"]))

    # ---- IV. Concorrenti
    comp_p = data.get("competitor_principale"); comps = data.get("competitors", [])
    if comp_p or comps:
        E.append(opener("IV", "Voi e i concorrenti")); E.append(Spacer(1, 8))
        E.append(Paragraph("Il confronto non giudica il prodotto, ma quanto lo si fa sapere. Ecco come vi collocate "
                           "rispetto al concorrente più forte, area per area, e chi sono i concorrenti reali trovati "
                           "sui registri e su Google Places.", S["body"]))
        E.append(Spacer(1, 12))
        if comp_p and aree:
            names = [a["nome"] for a in aree]; tu = [float(a["voto"]) for a in aree]
            right = [radar_legend(cliente, comp_p.get("nome", "Concorrente")), Spacer(1, 10),
                     Paragraph(comp_p.get("lettura", ""), S["body"])]
            ct = Table([[radar(names, tu, comp_p.get("voti")), right]], colWidths=[210, 286])
            ct.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (0, 0), 0), ("LEFTPADDING", (1, 0), (1, 0), 18)]))
            E.append(ct); E.append(Spacer(1, 16))
        if comps:
            E.append(Paragraph("CONCORRENTI REALI TROVATI", S["h3"]))
            cd = [["Nome", "Dove", "Fonte", "Note"]]
            for c in comps[:5]:
                cd.append([Paragraph(c.get("nome", "—"), S["cell"]), Paragraph(c.get("dove", "—"), S["cell"]),
                           Paragraph(c.get("fonte", "—"), S["cell"]), Paragraph(c.get("note", "—"), S["cell"])])
            t = Table(cd, colWidths=[110, 90, 120, 176])
            t.setStyle(_tbl_style(head=True)); E.append(t)

    # ---- V. Priorita'
    opps = data.get("opportunita", [])
    if opps:
        E.append(opener("V", "Le priorita")); E.append(Spacer(1, 8))
        E.append(Paragraph("Ogni mossa possibile, messa dove pesa davvero: piu in alto quelle che spostano di piu, "
                           "piu a sinistra quelle che costano meno fatica. In alto a sinistra si parte; in basso a "
                           "destra non conviene mettere energia adesso.", S["body"]))
        E.append(Spacer(1, 12)); E.append(matrix(opps)); E.append(Spacer(1, 14))
        od = [["#", "Mossa", "Impatto", "Sforzo", "Ha senso qui?"]]
        for o in opps:
            od.append([str(o["n"]), Paragraph(o["mossa"], S["cell"]), o.get("impatto", "—"), o.get("sforzo", "—"),
                       Paragraph(o.get("pertinente", "—"), S["cell"])])
        t = Table(od, colWidths=[20, 210, 55, 50, 161])
        t.setStyle(_tbl_style(head=True, center0=True)); E.append(t)

    # ---- VI. Piano
    piano = data.get("piano", {})
    if piano:
        E.append(opener("VI", "Il piano a 90 giorni")); E.append(Spacer(1, 10))
        cols = [("SETTIMANE 1-2 · FRUTTI BASSI", piano.get("quick", [])),
                ("MESE 1-2 · FONDAMENTA", piano.get("medio", [])),
                ("MESE 2-3 · MOTORE", piano.get("strategico", []))]
        cells = []
        for titolo, items in cols:
            inner = [Paragraph(titolo, S["h3"])]
            for it in items:
                inner.append(Paragraph(f'<font color="{hexcol(C["accent"])}">&#8212;</font>&nbsp; {it}', S["body"]))
            cells.append(inner)
        pt = Table([cells], colWidths=[164, 164, 164])
        pt.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEABOVE", (0, 0), (-1, 0), 1.5, C["accent"]),
                                ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 14), ("TOPPADDING", (0, 0), (-1, -1), 10)]))
        E.append(pt); E.append(Spacer(1, 18))
        dec = data.get("decisione")
        if dec:
            box = Table([[Paragraph("IL PRIMO PASSO", ParagraphStyle("d1", fontName=SANS_MED, fontSize=8.5, textColor=Color(1, 1, 1, 0.55), leading=12, spaceAfter=7))],
                         [Paragraph(dec.get("titolo", ""), ParagraphStyle("d2", fontName=SERIF, fontSize=19, textColor=C["cream"], leading=22, spaceAfter=9))],
                         [Paragraph(dec.get("testo", ""), ParagraphStyle("d3", fontName=SANS, fontSize=10, textColor=Color(0.94, 0.91, 0.86, 1), leading=15))]], colWidths=[492])
            box.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), C["ink"]), ("LEFTPADDING", (0, 0), (-1, -1), 26),
                                     ("RIGHTPADDING", (0, 0), (-1, -1), 26), ("TOPPADDING", (0, 0), (0, 0), 24), ("BOTTOMPADDING", (0, -1), (-1, -1), 26)]))
            E.append(KeepTogether(box))

    # ---- VII. Metodologia (pagina pulita a sé)
    E.append(PageBreak())
    E.append(opener("VII", "Metodologia e fonti dei dati")); E.append(Spacer(1, 10))
    E.append(Paragraph("La pagella misura cinque aree del marketing, voto da 1 a 10. Il giudizio parte dai dati veri "
                       "dove esistono, non da impressioni.", S["body"])); E.append(Spacer(1, 8))
    md = [["Area", "Cosa misura"],
          ["Messaggio", "Chiarezza dell'offerta: si capisce cosa vendi, a chi, perche' voi"],
          ["Trovabilità", "Visibilità su Google e presenza locale"],
          ["Conversione", "Il percorso dal visitatore al contatto o alla vendita"],
          ["Concorrenza", "Posizionamento rispetto ai concorrenti reali"],
          ["Crescita", "Canali attivi, riacquisto, raccolta contatti"]]
    mt = Table([[Paragraph(c, S["cell"]) for c in r] for r in md], colWidths=[120, 372])
    mt.setStyle(_tbl_style(head=True)); E.append(mt); E.append(Spacer(1, 14))
    E.append(Paragraph("FONTI DEI DATI", S["h3"]))
    for f in data.get("fonti_dati", [
            "Registro imprese (openapi.com): profilo ATECO, sede, dipendenti, fatturato, concorrenti nella stessa provincia",
            "Google Places: concorrenti di zona con valutazioni e recensioni reali",
            "DataForSEO: volumi di ricerca mensili reali in Italia",
            "Lettura diretta del sito e delle pagine chiave"]):
        E.append(Paragraph(f'<font color="{hexcol(C["accent"])}">&#8212;</font>&nbsp; {f}', S["body"]))
    if data.get("nota_esempio"):
        E.append(Spacer(1, 12)); E.append(Paragraph(data["nota_esempio"], S["small"]))
    # chiusura ancorata in fondo
    E.append(Spacer(1, 150))
    close = Drawing(500, 66)
    close.add(Line(0, 58, 500, 58, strokeColor=C["line"], strokeWidth=0.8))
    close.add(String(0, 30, "Grazie.", fontSize=22, fillColor=C["ink"], fontName=SERIF))
    close.add(String(0, 8, "GENTES AI", fontSize=9, fillColor=C["accent"], fontName=SANS_MED))
    close.add(String(70, 8, "Consulenza marketing basata sui dati per le PMI italiane · gentes.ai",
                     fontSize=9, fillColor=C["stone"], fontName=SANS))
    E.append(close)

    # ---- cover + sfondi
    def cover(c, _doc):
        W, H = A4
        img = data.get("cover_image")
        if img and not os.path.exists(img):
            alt = os.path.join(ASSETS, os.path.basename(img))
            img = alt if os.path.exists(alt) else img
        if img and os.path.exists(img):
            iw, ih = ImageReader(img).getSize(); sc = max(W / iw, H / ih); dw, dh = iw * sc, ih * sc
            c.drawImage(img, (W - dw) / 2, (H - dh) / 2, width=dw, height=dh, mask="auto")
        else:
            c.setFillColor(C["ink"]); c.rect(0, 0, W, H, fill=1, stroke=0)
        # velo scuro dal basso
        for i in range(90):
            a = min(0.95, (1 - i / 90) ** 1.5 * 1.05)
            c.setFillColor(Color(0.10, 0.09, 0.08, a)); c.rect(0, i * (H * 0.62 / 90), W, H * 0.62 / 90 + 1, fill=1, stroke=0)
        c.setFillColor(Color(0.11, 0.10, 0.09, 0.5)); c.rect(0, 0, W, H, fill=1, stroke=0)
        M = 52
        c.setFillColor(Color(0.94, 0.91, 0.85, 0.88)); c.setFont(SANS_MED, 10.5)
        c.drawString(M, H - 76, "GENTES AI")
        # blocco titolo in basso
        yb = 268
        c.setStrokeColor(Color(0.94, 0.91, 0.85, 0.28)); c.setLineWidth(0.8); c.line(M, yb + 128, W - M, yb + 128)
        c.setFillColor(Color(0.82, 0.78, 0.70, 0.92)); c.setFont(SANS_MED, 9.5)
        c.drawString(M, yb + 106, "MARKETING AUDIT")
        c.setFillColor(C["cream"]); c.setFont(SERIF, 62); c.drawString(M - 2, yb + 54, cliente)
        if data.get("verdetto"):
            c.setFillColor(Color(0.91, 0.88, 0.81, 0.95)); c.setFont(SERIF, 20)
            yy = yb + 18
            for ln in _wrap(data["verdetto"], SERIF, 20, W - 2 * M - 8):
                c.drawString(M, yy, ln); yy -= 25
        if data.get("sottotitolo"):
            c.setFillColor(Color(0.78, 0.74, 0.66, 0.85)); c.setFont(SANS, 10.5)
            c.drawString(M, yb - 44, data["sottotitolo"])
        # voto grande a destra
        c.setFillColor(C["cream"]); c.setFont(SERIF, 60); c.drawRightString(W - M, yb + 54, f"{voto:.1f}")
        c.setFillColor(Color(0.80, 0.76, 0.68, 0.82)); c.setFont(SANS_MED, 8.5)
        c.drawRightString(W - M, yb + 30, "VOTO SU 10")
        # riga dati in fondo
        meta = [("PREPARATO PER", f"Leadership di {cliente}"), ("PREPARATO DA", data.get("autore", "Gentes AI")),
                ("DATA", data.get("data") or datetime.now().strftime("%d/%m/%Y"))]
        for (lab, val), cx in zip(meta, [M, M + 200, M + 370]):
            c.setFillColor(Color(0.72, 0.68, 0.60, 0.82)); c.setFont(SANS_MED, 7.5); c.drawString(cx, 92, lab)
            c.setFillColor(C["cream"]); c.setFont(SANS, 11); c.drawString(cx, 76, val)

    def body_bg(c, _doc):
        W, H = A4
        c.setFillColor(C["bone"]); c.rect(0, 0, W, H, fill=1, stroke=0)
        c.setFillColor(C["stone"]); c.setFont(SANS, 8);
        c.drawString(52, 34, f"GENTES AI  ·  {cliente.upper()}")
        c.drawRightString(W - 52, 34, f"{_doc.page:02d}");
        c.setStrokeColor(C["line"]); c.setLineWidth(0.6); c.line(52, 46, W - 52, 46)

    doc.build(E, onFirstPage=cover, onLaterPages=body_bg)
    return out

def _tbl_style(head=False, center0=False):
    cmd = [("FONTNAME", (0, 0), (-1, -1), SANS), ("FONTSIZE", (0, 0), (-1, -1), 8.5),
           ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), 0.5, C["line"]),
           ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6), ("LEFTPADDING", (0, 0), (-1, -1), 8)]
    if head:
        cmd += [("FONTNAME", (0, 0), (-1, 0), SANS_MED), ("TEXTCOLOR", (0, 0), (-1, 0), C["accent"]),
                ("FONTSIZE", (0, 0), (-1, 0), 8), ("LINEBELOW", (0, 0), (-1, 0), 1, C["ink"]), ("BOTTOMPADDING", (0, 0), (-1, 0), 8)]
    if center0:
        cmd += [("ALIGN", (0, 0), (0, -1), "CENTER")]
    return TableStyle(cmd)

# ------------------------------------------------------------------ demo
DEMO = {
    "cliente": "Caffè Aurelio", "autore": "Gentes AI", "data": "20/07/2026",
    "sottotitolo": "Torrefazione artigianale · e-commerce DTC · Bologna",
    "verdetto": "Il prodotto è forte. La macchina che lo vende, no.",
    "voto_finale": 5.5,
    "cover_image": os.path.join(ASSETS, "cover-hero.jpg"),
    "executive_summary": "Aurelio tosta un caffè che i clienti amano: 4,8 stelle su 320 recensioni. Ma chi non "
        "vi conosce non vi trova, e chi compra una volta sparisce. Due aree tirano giù tutto il resto, "
        "Trovabilità e Crescita, e sono anche quelle col miglior rapporto tra risultato e fatica: si "
        "muovono in settimane. Il piano parte da lì.",
    "as_is": {
        "cosa_vende": "Caffè specialty tostato a Bologna, venduto online in grani e macinato, più abbonamento.",
        "canali": "Passaparola e clienti storici; scheda Google curata a metà; social presenti ma fermi.",
        "dove_perde": "Chi cerca “caffè specialty online” non vi trova, e i carrelli abbandonati non vengono recuperati."},
    "aree": [
        {"nome": "Messaggio", "voto": 7.0, "nota": "Chiaro cosa vendi, meno perché proprio voi",
         "analisi": {"funziona": "La home dice subito cosa siete: 'Torrefazione artigianale dal 1987'. Il tono è caldo, le foto del laboratorio danno fiducia. Chi arriva capisce in cinque secondi che vendete caffè vostro, non rivenduto.",
                     "manca": "Non dite perché scegliere voi e non un'altra torrefazione. La frase in home è 'Il piacere del caffè italiano', che starebbe bene sul sito di chiunque. Manca la promessa concreta: freschezza, origine, il fatto che tostate a Bologna e spedite in 48 ore.",
                     "fare": ["Riscrivere l'H1 da 'Il piacere del caffè italiano' a qualcosa di specifico: 'Caffè specialty tostato a mano a Bologna. A casa tua entro 48 ore dalla tostatura.'",
                              "Aggiungere sotto l'H1 tre prove: 'Tostato fresco ogni settimana · Chicchi tracciati per origine · 4,8/5 su 320 recensioni'.",
                              "Mettere la data di tostatura sulla confezione e dirlo sul sito: è la vostra arma contro il caffè del supermercato."]}},
        {"nome": "Trovabilità", "voto": 4.5, "nota": "Invisibili sulle ricerche che contano",
         "analisi": {"funziona": "La scheda Google esiste ed è verificata, con l'indirizzo del laboratorio e qualche foto. Sul nome 'Caffè Aurelio' comparite primi.",
                     "manca": "Nessuno vi cerca per nome: vi cercano per bisogno. Su 'caffè specialty online' (1.900 ricerche al mese in Italia) e 'caffè in abbonamento' non comparite in prima pagina. Non avete pagine costruite su queste ricerche.",
                     "fare": ["Creare due pagine pensate per due ricerche precise: una su 'caffè specialty online', una su 'caffè in abbonamento'.",
                              "Sistemare i titoli delle schede prodotto: da 'Miscela Aurelio 250g' a 'Miscela Aurelio 250g · caffè specialty in grani, tostato fresco'.",
                              "Rimettere in moto la scheda Google: categoria 'Torrefazione', un post a settimana, richiesta recensione dopo ogni consegna."]}},
        {"nome": "Conversione", "voto": 5.5, "nota": "Il sito vende, ma perde per strada",
         "analisi": {"funziona": "Lo shop funziona, il carrello è chiaro, si paga anche con PayPal. Le schede prodotto hanno belle foto.",
                     "manca": "Il carrello si abbandona e non lo recuperate: circa il 68% se ne va senza comprare e non riceve nessuna email. Le schede non spiegano cosa stai comprando (origine, tostatura, note): chi non è esperto non sa scegliere e chiude.",
                     "fare": ["Attivare due email automatiche: recupero carrello dopo un'ora, post-acquisto su come preparare il caffè.",
                              "Completare le schede: origine, grado di tostatura, tre note di gusto, metodo consigliato.",
                              "Dire la soglia di spedizione gratuita in alto nel sito: 'Spedizione gratis sopra i 30 euro'."]}},
        {"nome": "Concorrenza", "voto": 6.5, "nota": "Ben posizionati, poco dichiarato",
         "analisi": {"funziona": "Avete qualcosa che i concorrenti non hanno: laboratorio visitabile, storia dal 1987, recensioni migliori della media (4,8 contro 4,6 di Torrefazione Sole). Chi vi prova, torna.",
                     "manca": "Non lo dite da nessuna parte. Il sito non nomina mai un confronto, non c'è una pagina che spieghi perché voi e non il caffè del supermercato. State vincendo sul prodotto e pareggiando sulla comunicazione.",
                     "fare": ["Aprire una pagina 'Perché Aurelio' con tre differenze concrete e verificabili.",
                              "Mostrare le recensioni vere in home, con nome e data, non un generico '4,8 stelle'.",
                              "Raccontare la tostatura come processo: una foto-storia batte dieci righe di 'qualità artigianale'."]}},
        {"nome": "Crescita", "voto": 4.0, "nota": "Tutto poggia sul primo acquisto",
         "analisi": {"funziona": "Il prodotto crea affezione: chi compra il vostro caffè difficilmente torna a quello del supermercato. La materia prima per crescere c'è.",
                     "manca": "Non avete un modo per far tornare chi ha già comprato. Niente abbonamento in evidenza, niente email a chi non ordina da due mesi, niente programma referral. Ogni vendita è un colpo singolo.",
                     "fare": ["Mettere l'abbonamento (ogni 2 o 4 settimane, con sconto) come offerta in evidenza.",
                              "Email a chi non ordina da 60 giorni con un motivo per tornare.",
                              "Programma 'porta un amico': sconto a chi invita e a chi è invitato."]}}],
    "problemi": [
        {"titolo": "I carrelli pieni se ne vanno e non tornano",
         "oggi": "Circa due carrelli su tre vengono abbandonati prima del pagamento, e nessuno riceve un'email che lo inviti a tornare. Sono persone che avevano già scelto il prodotto e messo mano al portafoglio.",
         "costa": "Ogni giorno perdete ordini già a un passo dalla chiusura. Non è traffico da comprare: è gente che vi ha già trovato e voleva comprare.",
         "sistema": "Due email automatiche: recupero carrello dopo un'ora e post-acquisto. Si imposta una volta, lavora da sola. È la mossa numero uno del piano."},
        {"titolo": "Chi cerca caffè specialty non vi trova",
         "oggi": "Su 'caffè specialty online' e 'caffè in abbonamento', dove ogni mese cercano migliaia di persone in Italia, non comparite in prima pagina. Non avete pagine costruite su queste ricerche.",
         "costa": "Il concorrente Nero Nobile intercetta quella domanda e la porta a casa. Voi restate a dipendere dal passaparola, che non scala.",
         "sistema": "Due pagine pensate per due ricerche precise, titoli prodotto sistemati, scheda Google riattivata. Risultati in 6-8 settimane."},
        {"titolo": "Vincete sul prodotto, pareggiate sulla comunicazione",
         "oggi": "Avete recensioni migliori dei concorrenti (4,8 contro 4,6) e un laboratorio visitabile, ma il sito non lo dice: nessuna pagina spiega perché scegliere voi, e le recensioni non si vedono in home.",
         "costa": "Il vantaggio vero che avete conquistato tostando bene resta invisibile. Chi confronta due torrefazioni sceglie quella che glielo racconta meglio.",
         "sistema": "Pagina 'Perché Aurelio' con tre differenze concrete, recensioni vere in home, la tostatura raccontata per immagini."}],
    "competitor_principale": {"nome": "Nero Nobile", "voti": [6.0, 7.5, 6.5, 6.0, 6.5],
        "lettura": "Non tosta meglio di voi. Ma si fa trovare (7,5 contro 4,5) e ha un motivo di riacquisto: "
                   "l'abbonamento in home. Vince dove siete scoperti, non dove siete deboli davvero. Il divario è "
                   "tutto su cose che si costruiscono, non su reputazione o prodotto: terreno recuperabile in un trimestre."},
    "competitors": [
        {"nome": "Nero Nobile", "dove": "Milano", "fonte": "Registro imprese", "note": "Abbonamento in evidenza, blog attivo"},
        {"nome": "Torrefazione Sole", "dove": "Bologna", "fonte": "Google Places", "note": "4,6/5, 210 recensioni, ritiro in sede"},
        {"nome": "Caffè del Borgo", "dove": "Modena", "fonte": "Google Places", "note": "Forte su Instagram, poco e-commerce"}],
    "opportunita": [
        {"n": 1, "mossa": "Home riscritta sul beneficio (freschezza, tostato a Bologna)", "impatto": "alto", "sforzo": "basso", "pertinente": "Sì, la home non lo dice"},
        {"n": 2, "mossa": "Email carrello abbandonato + post-acquisto", "impatto": "alto", "sforzo": "basso", "pertinente": "Sì, oggi nessun recupero"},
        {"n": 3, "mossa": "Recensioni sistematiche post-consegna", "impatto": "medio", "sforzo": "basso", "pertinente": "Sì, reputazione non sfruttata"},
        {"n": 4, "mossa": "Schede prodotto: origine, tostatura, metodo", "impatto": "alto", "sforzo": "medio", "pertinente": "Sì"},
        {"n": 5, "mossa": "SEO: pagine per le ricerche ad alto volume", "impatto": "alto", "sforzo": "medio", "pertinente": "Sì, 1.900 ricerche/mese"},
        {"n": 6, "mossa": "Abbonamento come offerta in evidenza", "impatto": "alto", "sforzo": "medio", "pertinente": "Sì, leva di riacquisto"},
        {"n": 7, "mossa": "Campagna Meta di retargeting", "impatto": "medio", "sforzo": "medio", "pertinente": "Sì, dopo le fondamenta"},
        {"n": 8, "mossa": "Restyling completo del sito", "impatto": "basso", "sforzo": "alto", "pertinente": "No, non ora"}],
    "piano": {
        "quick": ["Home riscritta sul beneficio", "Email carrello + post-acquisto", "Richiesta recensioni automatica"],
        "medio": ["Schede prodotto complete", "Pagine SEO sulle ricerche chiave", "Abbonamento in evidenza"],
        "strategico": ["Retargeting Meta", "Misurazione e iterazione", "Secondo giro di contenuti"]},
    "decisione": {"titolo": "Una cosa sola per partire",
        "testo": "Dare l'ok ai frutti bassi delle prime due settimane: home riscritta sul beneficio, email di "
                 "recupero carrello e post-acquisto, richiesta recensioni automatica. Zero rifacimenti, solo cose "
                 "che si accendono in giorni. Obiettivo: intercettare i carrelli persi e far tornare chi ha già comprato."},
    "nota_esempio": "Documento di esempio a scopo dimostrativo. Caffè Aurelio è un'azienda ipotetica; i dati e i "
        "grafici sono illustrativi e internamente coerenti, non riferiti a una realtà esistente."}

def main():
    if len(sys.argv) < 2:
        print("Report di esempio generato:", generate(DEMO, "REPORT-CLIENTE-esempio.pdf")); return
    with open(sys.argv[1], encoding="utf-8") as f:
        data = json.load(f)
    generate(data, sys.argv[2] if len(sys.argv) > 2 else "REPORT-CLIENTE.pdf")
    print("Report generato.")

if __name__ == "__main__":
    main()
