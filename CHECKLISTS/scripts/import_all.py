"""Import ODINT checklist documents into one DB + viewer.

Final document set (3):
  1. Collection Checklist — site field inventory to capture (1–1265)
  2. OSINT Mission Set — process/SOP (Mission Objectives.txt + unique Mission MD)
  3. Country Coverage — tour geography tracker

Collection and Mission stay separate: capture fields vs how the op is run.
"""

from __future__ import annotations

import json
import re
import shutil
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "odint_checklist.db"
OUT = ROOT / "viewer.html"
SOURCES_DIR = ROOT / "sources"

COLLECTION = {
    "path": Path(r"E:\MD Library\ODINT-Collection-Checklist.md"),
    "kind": "numbered",
    "label": "Collection Checklist",
}
COUNTRIES = {
    "key": "countries",
    "name": "Country Coverage",
    "path": Path(r"E:\04 GITHUB Library\ODINT Github\README.md"),
    "description": "Cyber Recon Tour country/region tracker (geography only)",
    "kind": "checkbox_md",
}

MISSION_PRIMARY = {
    "path": Path(r"E:\TXT Library\ODINT MISSION OBJECTIVES.txt"),
    "kind": "checkbox_txt",
    "label": "Mission Objectives.txt",
}
MISSION_SECONDARY = {
    "path": Path(
        r"E:\04 GITHUB Library\ODINT Github\CYBER RECON TOUR\MISC\ODINT-README.md"
    ),
    "kind": "checkbox_md",
    "label": "ODINT-README.md",
}

ITEM_NUM_RE = re.compile(r"^(\d+)\.\s+(.+)$")
H1_RE = re.compile(r"^#\s+(.+)$")
H2_RE = re.compile(r"^##\s+(.+)$")
H3_RE = re.compile(r"^###\s+(.+)$")
CHECK_MD_RE = re.compile(r"^[-*]\s*\[([ xX])\]\s*(.+)$")
CHECK_TXT_RE = re.compile(r"^\[([ xX])\]\s*(.+)$")
# mission status line sometimes has multiple [ ] in one line
CHECK_INLINE_RE = re.compile(r"\[([ xX])\]\s*([^\[\]]+?)(?=\s*\[|$)")


def priority_for(name: str, section: str) -> str:
    blob = f"{section} {name}".lower()
    critical = [
        "password",
        "credential",
        "api key",
        "secret",
        "token",
        "gravatar",
        ".env",
        ".git",
        "backup",
        "pii",
        "national id",
        "hash",
        "wp-json",
        "private key",
        "ssh",
        "aws access",
        "database dump",
        "sql dump",
        "gps",
        "plaintext",
    ]
    high = [
        "subdomain",
        "certificate",
        "swagger",
        "openapi",
        "graphql",
        "admin",
        "email",
        "username",
        "shodan",
        "censys",
        "wayback",
        "robots",
        "sitemap",
        "wordpress",
        "arcgis",
        "critical",
    ]
    if any(k in blob for k in critical):
        return "CRITICAL"
    if any(k in blob for k in high):
        return "HIGH"
    return "STANDARD"


def parse_numbered(md: str):
    sections = []
    current = None
    subsection = None
    for line in md.splitlines():
        line = line.rstrip()
        if not line.strip():
            continue
        if line.startswith("# ") or line.startswith("**Total") or line.strip() == "---":
            continue
        m2 = H2_RE.match(line)
        if m2:
            current = {"name": m2.group(1).strip(), "items": []}
            sections.append(current)
            subsection = None
            continue
        m3 = H3_RE.match(line)
        if m3:
            subsection = m3.group(1).strip()
            continue
        mi = ITEM_NUM_RE.match(line.strip())
        if mi and current is not None:
            num = int(mi.group(1))
            body = mi.group(2).strip()
            name, detail = body, ""
            if " (" in body and body.endswith(")"):
                i = body.find(" (")
                name, detail = body[:i].strip(), body[i + 2 : -1].strip()
            current["items"].append(
                {
                    "num": num,
                    "name": name if detail else body,
                    "detail": detail,
                    "notes": subsection or "",
                    "done": False,
                }
            )
    return sections


def parse_checkbox_md(md: str):
    """Parse markdown with ##/### sections and - [ ] items."""
    sections = []
    current = None
    subsection = None
    # Skip pure TOC-looking leading sections until we see checkboxes in a section
    for line in md.splitlines():
        raw = line.rstrip()
        s = raw.strip()
        if not s:
            continue
        m2 = H2_RE.match(s)
        if m2:
            title = m2.group(1).strip()
            # strip markdown bold/links noise lightly
            title = re.sub(r"[*_`]", "", title)
            current = {"name": title, "items": []}
            sections.append(current)
            subsection = None
            continue
        m3 = H3_RE.match(s)
        if m3:
            subsection = re.sub(r"[*_`]", "", m3.group(1).strip())
            continue
        # task list
        m = CHECK_MD_RE.match(s)
        if m and current is not None:
            done = m.group(1).lower() == "x"
            body = m.group(2).strip()
            body = re.sub(r"\*\*(.+?)\*\*", r"\1", body)
            current["items"].append(
                {
                    "num": None,
                    "name": body,
                    "detail": "",
                    "notes": subsection or "",
                    "done": done,
                }
            )
            continue
        # inline multiple checkboxes on one line (status rows)
        if current is not None and s.count("[") >= 2 and "] " in s:
            for im in CHECK_INLINE_RE.finditer(s):
                body = im.group(2).strip().strip("|").strip()
                if len(body) < 2:
                    continue
                current["items"].append(
                    {
                        "num": None,
                        "name": body,
                        "detail": "",
                        "notes": subsection or "inline",
                        "done": im.group(1).lower() == "x",
                    }
                )
    # drop empty sections
    return [sec for sec in sections if sec["items"]]


def parse_checkbox_txt(text: str):
    """Parse Mission Objectives plain-text with [ ] items and CAPS section headers."""
    sections = []
    current = {"name": "General", "items": []}
    sections.append(current)
    subsection = None

    for line in text.splitlines():
        raw = line.rstrip()
        s = raw.strip()
        if not s:
            continue

        # Section banners
        if s.startswith("####") or (s.startswith("SECTION ") and ":" in s):
            name = s.strip("#").strip()
            if name.startswith("SECTION"):
                name = name.split(":", 1)[-1].strip() if ":" in name else name
            current = {"name": name[:120], "items": []}
            sections.append(current)
            subsection = None
            continue
        if s.startswith("RULE ") and ":" in s:
            subsection = s.split(":", 1)[0].strip()
            # also treat RULE line as potential section if followed by many items
            # keep as notes via subsection
            continue
        # ALL-CAPS short headers ending with : (PRE-SCAN CHECKLIST:)
        if (
            s.endswith(":")
            and len(s) < 80
            and s.replace(" ", "").replace("-", "").replace("_", "").isalnum() is False
        ):
            # e.g. PRE-SCAN CHECKLIST:
            if s.isupper() or s.endswith("CHECKLIST:") or s.endswith("VERIFICATION:"):
                subsection = s.rstrip(":")
                continue
        if re.match(r"^[A-Z][A-Z0-9 /&().,'-]{4,}:$", s):
            subsection = s.rstrip(":")
            continue

        m = CHECK_TXT_RE.match(s)
        if m:
            done = m.group(1).lower() == "x"
            body = m.group(2).strip()
            # strip trailing arrows / notes after >>> 
            note_extra = ""
            if ">>>" in body:
                body, note_extra = body.split(">>>", 1)
                body = body.strip()
                note_extra = note_extra.strip()
            notes = subsection or ""
            if note_extra:
                notes = f"{notes} | {note_extra}" if notes else note_extra
            # path-style " /apis/  - desc"
            name, detail = body, ""
            if " - " in body:
                left, right = body.split(" - ", 1)
                if len(left) < 80:
                    name, detail = left.strip(), right.strip()
            current["items"].append(
                {
                    "num": None,
                    "name": name,
                    "detail": detail,
                    "notes": notes,
                    "done": done,
                }
            )
            continue

        # multi-checkbox status lines
        if s.count("[ ]") + s.count("[X]") + s.count("[x]") >= 2:
            for im in CHECK_INLINE_RE.finditer(s):
                body = im.group(2).strip()
                if len(body) < 2:
                    continue
                current["items"].append(
                    {
                        "num": None,
                        "name": body,
                        "detail": "",
                        "notes": subsection or "status",
                        "done": im.group(1).lower() == "x",
                    }
                )

    return [sec for sec in sections if sec["items"]]


def seed(all_docs):
    try:
        if DB.exists():
            DB.unlink()
    except OSError:
        pass

    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.executescript(
        """
        DROP TABLE IF EXISTS items;
        DROP TABLE IF EXISTS sections;
        DROP TABLE IF EXISTS documents;
        CREATE TABLE documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            source_path TEXT,
            sort_order INTEGER NOT NULL DEFAULT 0
        );
        CREATE TABLE sections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            sort_order INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (document_id) REFERENCES documents(id)
        );
        CREATE TABLE items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            section_id INTEGER NOT NULL,
            item_num INTEGER,
            name TEXT NOT NULL,
            detail TEXT,
            notes TEXT,
            priority TEXT NOT NULL DEFAULT 'STANDARD',
            phase TEXT,
            sort_order INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (section_id) REFERENCES sections(id)
        );
        """
    )

    total_items = 0
    for di, doc in enumerate(all_docs, start=1):
        cur.execute(
            """INSERT INTO documents (id, key, name, description, source_path, sort_order)
               VALUES (?,?,?,?,?,?)""",
            (
                di,
                doc["key"],
                doc["name"],
                doc["description"],
                str(doc["path"]),
                di * 10,
            ),
        )
        for si, sec in enumerate(doc["sections"], start=1):
            cur.execute(
                """INSERT INTO sections (document_id, name, description, sort_order)
                   VALUES (?,?,?,?)""",
                (
                    di,
                    sec["name"],
                    f"{len(sec['items'])} items",
                    si * 10,
                ),
            )
            sec_id = cur.lastrowid
            for j, it in enumerate(sec["items"], start=1):
                pri = priority_for(it["name"], sec["name"])
                cur.execute(
                    """INSERT INTO items
                       (section_id, item_num, name, detail, notes, priority, phase, sort_order)
                       VALUES (?,?,?,?,?,?,?,?)""",
                    (
                        sec_id,
                        it.get("num"),
                        it["name"],
                        it.get("detail") or "",
                        it.get("notes") or "",
                        pri,
                        doc["key"],
                        it.get("num") or j,
                    ),
                )
                total_items += 1

    con.commit()
    n_docs = cur.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
    n_sec = cur.execute("SELECT COUNT(*) FROM sections").fetchone()[0]
    by_doc = list(
        cur.execute(
            """SELECT d.name, COUNT(i.id)
               FROM documents d
               JOIN sections s ON s.document_id = d.id
               JOIN items i ON i.section_id = s.id
               GROUP BY d.id ORDER BY d.sort_order"""
        )
    )
    by_pri = dict(cur.execute("SELECT priority, COUNT(*) FROM items GROUP BY priority"))
    con.close()
    print(f"seeded {DB}")
    print(f"  documents={n_docs} sections={n_sec} items={total_items}")
    print(f"  priority={by_pri}")
    for name, n in by_doc:
        print(f"  {n:5d}  {name}")
    return total_items


def load_data():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    documents = [
        dict(r)
        for r in con.execute(
            "SELECT id, key, name, description, source_path, sort_order FROM documents ORDER BY sort_order"
        )
    ]
    sections = [
        dict(r)
        for r in con.execute(
            "SELECT id, document_id, name, description, sort_order FROM sections ORDER BY document_id, sort_order"
        )
    ]
    items = [
        dict(r)
        for r in con.execute(
            """SELECT i.id, i.section_id, i.item_num, i.name, i.detail, i.notes,
                      i.priority, i.phase, i.sort_order, s.document_id
               FROM items i
               JOIN sections s ON s.id = i.section_id
               ORDER BY s.document_id, s.sort_order, i.sort_order, i.id"""
        )
    ]
    con.close()
    return {"documents": documents, "sections": sections, "items": items}


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ODINT Checklists</title>
<script>
  (function () {
    try {
      var t = localStorage.getItem('odint-cl-theme');
      if (t) document.documentElement.setAttribute('data-theme', t);
    } catch (e) {}
  })();
</script>
<style>
  :root {
    color-scheme: light;
    --bg:#fff; --bg-alt:#fafafa; --text:#1a1a1a; --text-muted:#666;
    --border:#e5e5e5; --border-strong:#d0d0d0; --accent:#1a1a1a; --code-bg:#f4f4f4;
    --risk-critical-bg:#c62828; --risk-critical-fg:#fff;
    --risk-high-bg:#e65100; --risk-high-fg:#fff;
    --risk-medium-bg:#f9a825; --risk-medium-fg:#1a1a1a;
    --risk-low-bg:#2e7d32; --risk-low-fg:#fff;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      color-scheme: dark;
      --bg:#131313; --bg-alt:#1a1a1a; --text:#ededed; --text-muted:#9a9a9a;
      --border:#2b2b2b; --border-strong:#3a3a3a; --accent:#ededed; --code-bg:#1f1f1f;
      --risk-critical-bg:#ef5350; --risk-critical-fg:#131313;
      --risk-high-bg:#ff9800; --risk-high-fg:#131313;
      --risk-medium-bg:#fdd835; --risk-medium-fg:#131313;
      --risk-low-bg:#66bb6a; --risk-low-fg:#131313;
    }
  }
  :root[data-theme="dark"] {
    color-scheme: dark;
    --bg:#131313; --bg-alt:#1a1a1a; --text:#ededed; --text-muted:#9a9a9a;
    --border:#2b2b2b; --border-strong:#3a3a3a; --accent:#ededed; --code-bg:#1f1f1f;
    --risk-critical-bg:#ef5350; --risk-critical-fg:#131313;
    --risk-high-bg:#ff9800; --risk-high-fg:#131313;
    --risk-medium-bg:#fdd835; --risk-medium-fg:#131313;
    --risk-low-bg:#66bb6a; --risk-low-fg:#131313;
  }
  * { box-sizing: border-box; }
  body { margin:0; background:var(--bg); color:var(--text); font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; font-size:15px; line-height:1.55; }
  .layout { display:grid; grid-template-columns:300px 1fr; max-width:1500px; margin:0 auto; min-height:100vh; }
  .sidebar { position:sticky; top:0; align-self:start; height:100vh; overflow-y:auto; background:var(--bg-alt); border-right:1px solid var(--border); padding:22px 16px; font-size:13px; }
  .brand { font-size:17px; font-weight:700; margin:0 0 2px; }
  .brand-sub { color:var(--text-muted); font-size:12px; margin:0 0 14px; }
  .sidebar h5 { font-size:11px; font-weight:600; text-transform:uppercase; letter-spacing:1px; color:var(--text-muted); margin:16px 0 8px; }
  .sidebar h5:first-of-type { margin-top:0; }
  .facet { display:flex; align-items:center; gap:7px; padding:2px 0; cursor:pointer; }
  .facet input { margin:0; accent-color:var(--accent); }
  .facet .count { margin-left:auto; color:var(--text-muted); font-variant-numeric:tabular-nums; font-size:12px; }
  .swatch { width:9px; height:9px; border-radius:2px; display:inline-block; margin-right:5px; }
  .swatch.critical{background:var(--risk-critical-bg)} .swatch.high{background:var(--risk-high-bg)}
  .swatch.standard{background:var(--risk-medium-bg)} .swatch.low{background:var(--risk-low-bg)}
  .sidebar-actions { display:flex; flex-wrap:wrap; gap:7px; margin-top:18px; padding-top:14px; border-top:1px solid var(--border); }
  .main { padding:36px 44px; }
  h1 { font-size:28px; font-weight:700; margin:0 0 6px; letter-spacing:-.4px; }
  .lede { color:var(--text-muted); margin:0 0 18px; }
  .stats { display:flex; border:1px solid var(--border); border-radius:4px; overflow:hidden; margin-bottom:18px; flex-wrap:wrap; }
  .stat { flex:1; min-width:110px; padding:12px 14px; background:var(--bg-alt); border-right:1px solid var(--border); }
  .stat:last-child { border-right:none; }
  .stat strong { display:block; font-size:20px; font-variant-numeric:tabular-nums; }
  .stat span { font-size:10px; font-weight:600; text-transform:uppercase; letter-spacing:1px; color:var(--text-muted); }
  .searchbar { position:relative; margin-bottom:10px; }
  .searchbar svg { position:absolute; left:12px; top:50%; transform:translateY(-50%); color:var(--text-muted); }
  input[type=search] { width:100%; padding:10px 12px 10px 36px; font:inherit; font-size:14px; color:var(--text); background:var(--bg); border:1px solid var(--border-strong); border-radius:4px; }
  input[type=search]:focus { outline:none; border-color:var(--accent); }
  button { font:inherit; font-size:12px; font-weight:600; padding:7px 11px; color:var(--text); background:var(--bg); border:1px solid var(--border-strong); border-radius:3px; cursor:pointer; }
  button:hover { background:var(--code-bg); }
  .resultbar { font-size:13px; color:var(--text-muted); margin-bottom:14px; }
  .doc-block { margin-bottom:40px; }
  .doc-block > h2 { font-size:20px; margin:0 0 4px; }
  .doc-desc { font-size:13px; color:var(--text-muted); margin:0 0 16px; }
  .section-block { margin-bottom:22px; }
  .section-block h3 { font-size:15px; margin:0 0 4px; padding-bottom:6px; border-bottom:1px solid var(--border); }
  .section-desc { font-size:12px; color:var(--text-muted); margin:0 0 10px; }
  .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(290px,1fr)); gap:9px; }
  .card { background:var(--bg-alt); border:1px solid var(--border); border-radius:4px; padding:11px 12px; }
  .card-head { display:flex; gap:7px; align-items:flex-start; }
  .card-num { color:var(--text-muted); font-size:11px; font-variant-numeric:tabular-nums; min-width:2em; }
  .card-title { font-size:13px; font-weight:600; flex:1; word-break:break-word; }
  .badge { flex-shrink:0; padding:2px 6px; font-size:9px; font-weight:600; text-transform:uppercase; letter-spacing:.5px; border-radius:3px; }
  .badge.critical{background:var(--risk-critical-bg);color:var(--risk-critical-fg)}
  .badge.high{background:var(--risk-high-bg);color:var(--risk-high-fg)}
  .badge.standard{background:var(--risk-medium-bg);color:var(--risk-medium-fg)}
  .badge.low{background:var(--risk-low-bg);color:var(--risk-low-fg)}
  .card-detail { font-size:12px; margin:5px 0 0; }
  .card-notes { font-size:11px; margin:5px 0 0; color:var(--text-muted); border-left:3px solid var(--border-strong); padding-left:8px; }
  .empty { padding:36px; text-align:center; color:var(--text-muted); border:1px dashed var(--border-strong); border-radius:4px; }
  footer { margin-top:36px; padding-top:14px; border-top:1px solid var(--border); font-size:12px; color:var(--text-muted); }
  @media (max-width:960px) {
    .layout { grid-template-columns:1fr; }
    .sidebar { position:static; height:auto; border-right:none; border-bottom:1px solid var(--border); }
    .main { padding:24px 16px; }
  }
</style>
</head>
<body>
<div class="layout">
  <aside class="sidebar">
    <p class="brand">ODINT Checklists</p>
    <p class="brand-sub">Collection · Mission · Countries</p>
    <h5>Document</h5>
    <div id="f-doc"></div>
    <h5>Priority</h5>
    <div id="f-priority"></div>
    <div class="sidebar-actions">
      <button type="button" id="reset">Reset filters</button>
      <button type="button" id="csv">Export CSV</button>
      <button type="button" id="theme">Theme</button>
    </div>
  </aside>
  <main class="main">
    <h1>ODINT Checklists</h1>
    <p class="lede">Three lists: Collection Checklist (what to capture on a site), OSINT Mission Set (how to run the op), Country Coverage (tour geography).</p>
    <div class="stats">
      <div class="stat"><strong id="s-total">0</strong><span>Items</span></div>
      <div class="stat"><strong id="s-docs">0</strong><span>Documents</span></div>
      <div class="stat"><strong id="s-crit">0</strong><span>Critical</span></div>
      <div class="stat"><strong id="s-high">0</strong><span>High</span></div>
    </div>
    <div class="searchbar">
      <svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6">
        <circle cx="7" cy="7" r="4.5"/><path d="M10.5 10.5 L14 14" stroke-linecap="round"/>
      </svg>
      <input type="search" id="q" placeholder="Search all checklists…" autocomplete="off">
    </div>
    <div class="resultbar"><span id="count"></span></div>
    <div id="list"></div>
    <footer id="foot"></footer>
  </main>
</div>
<script>
const DATA = __DATA_JSON__;
const DOC = {}; const SEC = {};
DATA.documents.forEach(d => { DOC[d.id] = d; });
DATA.sections.forEach(s => { SEC[s.id] = s; });
const PRI_ORDER = ['CRITICAL','HIGH','STANDARD','LOW'];
const $ = id => document.getElementById(id);
const esc = t => String(t == null ? '' : t).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

function facet(container, values, labelOf, countOf) {
  container.innerHTML = values.map(v => `
    <label class="facet">
      <input type="checkbox" value="${String(v).replace(/"/g,'&quot;')}">
      <span>${labelOf(v)}</span>
      <span class="count">${countOf(v)}</span>
    </label>`).join('');
  container.querySelectorAll('input').forEach(el => el.addEventListener('change', render));
}
function checked(container) {
  return [...container.querySelectorAll('input:checked')].map(el => el.value);
}

facet($('f-doc'), DATA.documents.map(d => d.id),
  v => DOC[v].name,
  v => DATA.items.filter(i => i.document_id === v).length);

facet($('f-priority'), PRI_ORDER,
  v => `<span class="swatch ${v.toLowerCase()}"></span>${v.charAt(0)+v.slice(1).toLowerCase()}`,
  v => DATA.items.filter(i => i.priority === v).length);

function filtered() {
  const q = $('q').value.trim().toLowerCase();
  const docs = checked($('f-doc'));
  const pris = checked($('f-priority'));
  return DATA.items.filter(i => {
    const blob = ((i.item_num||'')+' '+i.name+' '+(i.detail||'')+' '+(i.notes||'')+' '+(SEC[i.section_id]?.name||'')+' '+(DOC[i.document_id]?.name||'')).toLowerCase();
    return (!q || blob.includes(q))
      && (!docs.length || docs.includes(String(i.document_id)))
      && (!pris.length || pris.includes(i.priority));
  });
}

function render() {
  const rows = filtered();
  const list = $('list');
  $('count').textContent = rows.length === DATA.items.length
    ? `${rows.length} items`
    : `${rows.length} of ${DATA.items.length} items`;

  if (!rows.length) {
    list.innerHTML = '<p class="empty">No items match these filters.</p>';
    return;
  }

  const byDoc = new Map();
  rows.forEach(i => {
    if (!byDoc.has(i.document_id)) byDoc.set(i.document_id, new Map());
    const bySec = byDoc.get(i.document_id);
    if (!bySec.has(i.section_id)) bySec.set(i.section_id, []);
    bySec.get(i.section_id).push(i);
  });
  const docOrder = DATA.documents.map(d => d.id).filter(id => byDoc.has(id));

  list.innerHTML = docOrder.map(did => {
    const doc = DOC[did];
    const bySec = byDoc.get(did);
    const secOrder = DATA.sections.filter(s => s.document_id === did && bySec.has(s.id)).map(s => s.id);
    const sectionsHtml = secOrder.map(sid => {
      const sec = SEC[sid];
      const cards = bySec.get(sid).map(i => `
        <article class="card">
          <div class="card-head">
            <span class="card-num">${i.item_num != null ? esc(i.item_num)+'.' : ''}</span>
            <span class="card-title">${esc(i.name)}</span>
            <span class="badge ${i.priority.toLowerCase()}">${esc(i.priority)}</span>
          </div>
          ${i.detail ? `<p class="card-detail">${esc(i.detail)}</p>` : ''}
          ${i.notes ? `<p class="card-notes">${esc(i.notes)}</p>` : ''}
        </article>`).join('');
      return `<section class="section-block">
        <h3>${esc(sec.name)}</h3>
        <p class="section-desc">${esc(sec.description||'')}</p>
        <div class="grid">${cards}</div>
      </section>`;
    }).join('');
    return `<div class="doc-block">
      <h2>${esc(doc.name)}</h2>
      <p class="doc-desc">${esc(doc.description||'')}</p>
      ${sectionsHtml}
    </div>`;
  }).join('');
}

$('q').addEventListener('input', render);
$('reset').addEventListener('click', () => {
  $('q').value = '';
  document.querySelectorAll('.sidebar input[type=checkbox]').forEach(el => { el.checked = false; });
  render();
});
$('csv').addEventListener('click', () => {
  const cell = v => `"${String(v==null?'':v).replace(/"/g,'""')}"`;
  const lines = [['Document','Section','Num','Name','Detail','Notes','Priority'].join(',')];
  filtered().forEach(i => lines.push([
    DOC[i.document_id].name, SEC[i.section_id].name, i.item_num, i.name, i.detail, i.notes, i.priority
  ].map(cell).join(',')));
  const url = URL.createObjectURL(new Blob([lines.join('\n')], {type:'text/csv;charset=utf-8'}));
  const a = document.createElement('a'); a.href=url; a.download='odint-all-checklists.csv'; a.click();
  URL.revokeObjectURL(url);
});
$('theme').addEventListener('click', () => {
  const saved = document.documentElement.getAttribute('data-theme');
  const current = saved || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  try { localStorage.setItem('odint-cl-theme', next); } catch (e) {}
});

$('s-total').textContent = DATA.items.length;
$('s-docs').textContent = DATA.documents.length;
$('s-crit').textContent = DATA.items.filter(i => i.priority === 'CRITICAL').length;
$('s-high').textContent = DATA.items.filter(i => i.priority === 'HIGH').length;
$('foot').textContent = `odint_checklist.db — ${DATA.items.length} items from ${DATA.documents.length} documents, ${DATA.sections.length} sections.`;
render();
</script>
</body>
</html>
"""


def build_viewer():
    data = load_data()
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    OUT.write_text(TEMPLATE.replace("__DATA_JSON__", payload), encoding="utf-8")
    print(f"wrote {OUT} ({len(data['items'])} items)")


def _parse_kind(kind: str, text: str):
    if kind == "numbered":
        return parse_numbered(text)
    if kind == "checkbox_txt":
        return parse_checkbox_txt(text)
    return parse_checkbox_md(text)


def _norm_name(name: str) -> str:
    n = name.strip().lower()
    n = re.sub(r"[`*_]+", "", n)
    n = re.sub(r"\s+", " ", n)
    return n


def merge_mission_process(primary_secs: list, secondary_secs: list) -> list:
    """Mission Objectives.txt + unique Mission MD only (process/SOP, not collection)."""
    seen: set[str] = set()
    merged: list[dict] = []

    def add_section(name: str) -> dict:
        for s in merged:
            if _norm_name(s["name"]) == _norm_name(name):
                return s
        sec = {"name": name, "items": []}
        merged.append(sec)
        return sec

    def add_items(sections: list, *, tag: str = "") -> int:
        added = 0
        for sec in sections:
            target = add_section(sec["name"] or "General")
            for it in sec["items"]:
                key = _norm_name(it["name"])
                if not key or key in seen:
                    continue
                seen.add(key)
                notes = (it.get("notes") or "").strip()
                if tag:
                    notes = f"{notes} | {tag}".strip(" |") if notes else tag
                target["items"].append({**it, "notes": notes})
                added += 1
        return added

    n1 = add_items(primary_secs, tag="mission SOP")
    n2 = add_items(secondary_secs, tag="from Mission MD")
    merged = [s for s in merged if s["items"]]
    print(
        f"  mission process merge: sop={n1}, md_unique={n2}, "
        f"total={n1 + n2}, sections={len(merged)}"
    )
    return merged


def _load_one(path: Path, kind: str, key: str, name: str, description: str) -> dict | None:
    if not path.exists():
        print(f"MISSING {path}")
        return None
    dest = SOURCES_DIR / f"{key}_{path.name}"
    shutil.copy2(path, dest)
    text = path.read_text(encoding="utf-8", errors="ignore")
    sections = _parse_kind(kind, text)
    n = sum(len(s["items"]) for s in sections)
    print(f"parsed {name}: {len(sections)} sections, {n} items  ← {path}")
    return {
        "key": key,
        "name": name,
        "description": description,
        "path": path,
        "sections": sections,
    }


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    SOURCES_DIR.mkdir(exist_ok=True)

    all_docs = []

    # 1) Collection Checklist — what to capture on a site (standalone)
    if COLLECTION["path"].exists():
        shutil.copy2(
            COLLECTION["path"],
            SOURCES_DIR / f"collection_{COLLECTION['path'].name}",
        )
        shutil.copy2(COLLECTION["path"], ROOT / COLLECTION["path"].name)
        collection_secs = _parse_kind(
            COLLECTION["kind"],
            COLLECTION["path"].read_text(encoding="utf-8", errors="ignore"),
        )
        n_coll = sum(len(s["items"]) for s in collection_secs)
        print(
            f"parsed {COLLECTION['label']}: {len(collection_secs)} sections, {n_coll} items"
        )
        all_docs.append(
            {
                "key": "collection",
                "name": "Collection Checklist",
                "description": (
                    f"What to collect during a site inspection — all {n_coll} "
                    "numbered capture fields. Required on every target."
                ),
                "path": COLLECTION["path"],
                "sections": collection_secs,
            }
        )
    else:
        print(f"MISSING {COLLECTION['path']}")

    # 2) OSINT Mission Set — process/SOP only (Mission txt + unique MD)
    primary: list = []
    secondary: list = []
    if MISSION_PRIMARY["path"].exists():
        shutil.copy2(
            MISSION_PRIMARY["path"],
            SOURCES_DIR / f"mission_{MISSION_PRIMARY['path'].name}",
        )
        shutil.copy2(MISSION_PRIMARY["path"], ROOT / MISSION_PRIMARY["path"].name)
        primary = _parse_kind(
            MISSION_PRIMARY["kind"],
            MISSION_PRIMARY["path"].read_text(encoding="utf-8", errors="ignore"),
        )
        print(
            f"parsed {MISSION_PRIMARY['label']}: "
            f"{len(primary)} sections, {sum(len(s['items']) for s in primary)} items"
        )
    else:
        print(f"MISSING {MISSION_PRIMARY['path']}")

    if MISSION_SECONDARY["path"].exists():
        shutil.copy2(
            MISSION_SECONDARY["path"],
            SOURCES_DIR / f"mission-md_{MISSION_SECONDARY['path'].name}",
        )
        secondary = _parse_kind(
            MISSION_SECONDARY["kind"],
            MISSION_SECONDARY["path"].read_text(encoding="utf-8", errors="ignore"),
        )
        print(
            f"parsed {MISSION_SECONDARY['label']}: "
            f"{len(secondary)} sections, {sum(len(s['items']) for s in secondary)} items"
        )
    else:
        print(f"MISSING {MISSION_SECONDARY['path']}")

    if primary or secondary:
        merged_secs = merge_mission_process(primary, secondary)
        n = sum(len(s["items"]) for s in merged_secs)
        print(f"OSINT Mission Set (process): {len(merged_secs)} sections, {n} items")
        all_docs.append(
            {
                "key": "osint-mission",
                "name": "OSINT Mission Set",
                "description": (
                    "How to run the OSINT op — Mission Objectives.txt plus unique "
                    f"items from ODINT-README.md ({n} process items, deduped). "
                    "Does not replace the Collection Checklist."
                ),
                "path": MISSION_PRIMARY["path"],
                "sections": merged_secs,
            }
        )

    # 3) Country coverage
    countries = _load_one(
        COUNTRIES["path"],
        COUNTRIES["kind"],
        "countries",
        "Country Coverage",
        COUNTRIES["description"],
    )
    if countries:
        all_docs.append(countries)

    if not all_docs:
        raise SystemExit("no documents parsed")
    seed(all_docs)
    build_viewer()


if __name__ == "__main__":
    main()

