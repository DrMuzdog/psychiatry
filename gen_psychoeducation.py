#!/usr/bin/env python3
"""Generate psychoeducation.html — unified tool merging ADHD, ASD, OCD, Insomnia, PTSD, AN, AUD, BP1."""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))

def extract_js_var(text, varname):
    """Extract 'var VARNAME=[...]' from JS text, tracking bracket depth."""
    pattern = r'var ' + re.escape(varname) + r'\s*='
    m = re.search(pattern, text)
    if not m:
        raise ValueError("Could not find: var " + varname)
    start = m.start()
    # find the first [ after the =
    eq_pos = text.index('=', m.end() - 1)
    arr_start = text.index('[', eq_pos)
    depth = 0
    i = arr_start
    while i < len(text):
        c = text[i]
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0:
                end = i + 1
                return 'var ' + varname + '=' + text[arr_start:end]
        i += 1
    raise ValueError("Unmatched bracket for: " + varname)

def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()

neuro = read(os.path.join(BASE, 'neuro-psychoeducation.html'))
ocd   = read(os.path.join(BASE, 'ocd-psychoeducation.html'))
ins   = read(os.path.join(BASE, 'insomnia-psychoeducation.html'))
ptsd  = read(os.path.join(BASE, 'ptsd-psychoeducation.html'))
an    = read(os.path.join(BASE, 'an-psychoeducation.html'))
aud   = read(os.path.join(BASE, 'aud-psychoeducation.html'))
bp1   = read(os.path.join(BASE, 'bp1-psychoeducation.html'))

ADHD_JS     = extract_js_var(neuro, 'ADHD_PE_GROUPS')
ASD_JS      = extract_js_var(neuro, 'ASD_PE_GROUPS')
OCD_JS      = extract_js_var(ocd,   'OCD_PE_GROUPS')
INSOMNIA_JS = extract_js_var(ins,   'INSOMNIA_PE_GROUPS')
PTSD_JS     = extract_js_var(ptsd,  'PTSD_PE_GROUPS')
AN_JS       = extract_js_var(an,    'AN_PE_GROUPS')
AUD_JS      = extract_js_var(aud,   'AUD_PE_GROUPS')
BP1_JS      = extract_js_var(bp1,   'BP1_PE_GROUPS')

# Insomnia gets amber colour scheme (distinct from ASD teal)
# so we patch the ins-done class references in INSOMNIA_JS to keep them as-is
# (ins-done stays, we'll update CSS)

html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>Psychoeducation — Dr Benjamin Murrie</title>
<style>
:root{
  --bg:#f0f2f5;--surface:#fff;--border:#e2e6ed;--text:#1a1d23;--muted:#6b7280;--navy:#0f172a;
  --adhd:#1a56db;--adhd-bg:#e8f0fe;--adhd-dark:#1e3a5f;
  --asd:#0d9488;--asd-bg:#ccfbf1;--asd-dark:#134e4a;
  --ocd:#7c3aed;--ocd-bg:#ede9fe;--ocd-dark:#4c1d95;--ocd-mid:#6d28d9;
  --ins:#b45309;--ins-bg:#fef3c7;--ins-dark:#78350f;--ins-mid:#92400e;
  --ptsd:#be123c;--ptsd-bg:#ffe4e6;--ptsd-dark:#881337;--ptsd-mid:#9f1239;
  --an:#9d174d;--an-bg:#fdf2f8;--an-dark:#831843;--an-mid:#be185d;
  --aud:#15803d;--aud-bg:#dcfce7;--aud-dark:#14532d;--aud-mid:#166534;
  --bp1:#a21caf;--bp1-bg:#fdf4ff;--bp1-dark:#701a75;--bp1-mid:#c026d3;
  --sans:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif
}
*{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
body{font-family:var(--sans);background:var(--bg);color:var(--text);font-size:15px;min-height:100vh}
.topbar{background:var(--navy);padding:10px 14px;border-bottom:3px solid var(--adhd);display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.topbar-title{font-size:13px;font-weight:800;color:#93c5fd;letter-spacing:.05em;text-transform:uppercase;white-space:nowrap;flex-shrink:0}
.ti{background:#1e293b;border:1px solid #334155;color:#f1f5f9;padding:5px 9px;border-radius:7px;font:inherit;font-size:13px;min-width:0}
.ti::placeholder{color:#64748b}
.ti:focus{outline:1px solid var(--adhd);background:#243349}
.content{max-width:1000px;margin:0 auto;padding:14px 12px 40px}
.section-label{font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.07em;color:var(--muted);margin-bottom:7px;margin-top:16px}
.disorder-row{display:flex;gap:7px;flex-wrap:wrap}
.dis-btn{padding:9px 22px;border-radius:999px;border:2px solid var(--border);background:#fff;font:700 13px var(--sans);cursor:pointer;transition:all .12s;color:#475569}
.dis-btn:hover{border-color:#94a3b8;background:#f8fafc}
.dis-btn.active-adhd{background:var(--adhd-dark);border-color:var(--adhd-dark);color:#fff}
.dis-btn.active-asd{background:var(--asd-dark);border-color:var(--asd-dark);color:#fff}
.dis-btn.active-ocd{background:var(--ocd-dark);border-color:var(--ocd-dark);color:#fff}
.dis-btn.active-ins{background:var(--ins-dark);border-color:var(--ins-dark);color:#fff}
.dis-btn.active-ptsd{background:var(--ptsd-dark);border-color:var(--ptsd-dark);color:#fff}
.dis-btn.active-an{background:var(--an-dark);border-color:var(--an-dark);color:#fff}
.dis-btn.active-aud{background:var(--aud-dark);border-color:var(--aud-dark);color:#fff}
.dis-btn.active-bp1{background:var(--bp1-dark);border-color:var(--bp1-dark);color:#fff}
.condition-block{margin-bottom:14px;border-radius:10px;overflow:hidden;border:1px solid var(--border)}
.condition-header{padding:10px 14px;font:700 12px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:#fff;display:flex;align-items:center;gap:10px}
.condition-header.adhd-h{background:var(--adhd-dark)}
.condition-header.asd-h{background:var(--asd-dark)}
.condition-header.ocd-h{background:var(--ocd-dark)}
.condition-header.ins-h{background:var(--ins-dark)}
.condition-header.ptsd-h{background:var(--ptsd-dark)}
.condition-header.an-h{background:var(--an-dark)}
.condition-header.aud-h{background:var(--aud-dark)}
.condition-header.bp1-h{background:var(--bp1-dark)}
.cond-sel-btns{margin-left:auto;display:flex;gap:5px;flex-shrink:0}
.cond-sel-btn{background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.35);color:#fff;font:600 11px var(--sans);padding:3px 10px;border-radius:5px;cursor:pointer;transition:background .1s}
.cond-sel-btn:hover{background:rgba(255,255,255,.3)}
.topic-list{background:#fff}
.pe-group-label{font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);padding:10px 14px 5px;background:#f8fafc;border-top:1px solid #f0f2f5}
.pe-section{border-top:1px solid #f4f5f8}
.pe-section:first-child{border-top:none}
.pe-header{display:flex;align-items:center;gap:9px;padding:9px 14px;cursor:pointer;user-select:none;-webkit-user-select:none}
.pe-header:hover{background:#f9fafb}
.pe-tick-btn{font-size:1rem;color:var(--muted);flex-shrink:0;min-width:20px;text-align:center;line-height:1;padding:2px;border-radius:4px;transition:color .1s}
.pe-title{font-weight:600;font-size:13px;color:var(--text);flex:1;line-height:1.35}
.pe-arrow{font-size:9px;color:var(--muted);flex-shrink:0;transition:transform .15s;margin-left:auto}
.pe-section.pe-open .pe-arrow{transform:rotate(90deg)}
.pe-body{display:none;padding:8px 14px 14px 43px;font-size:12.5px;line-height:1.65;color:#374151;border-top:1px solid #f4f5f8}
.pe-section.pe-open .pe-body{display:block}
.pe-body p{margin:0 0 7px}
.pe-body p:last-child{margin:0}
.pe-body ul{margin:4px 0 8px 16px}
.pe-body li{margin-bottom:4px}
.pe-body table{width:100%;border-collapse:collapse;font-size:11.5px;margin:6px 0 10px}
.pe-body th{background:#f1f5f9;padding:5px 8px;text-align:left;border:1px solid var(--border);font-size:11px}
.pe-body td{padding:4px 8px;border:1px solid var(--border);vertical-align:top}
.pe-body a{color:var(--asd)}
.pe-section.adhd-done{background:#eff6ff}
.pe-section.adhd-done .pe-tick-btn{color:var(--adhd)}
.pe-section.asd-done{background:#f0fdf4}
.pe-section.asd-done .pe-tick-btn{color:var(--asd)}
.pe-section.ocd-done{background:#f5f3ff}
.pe-section.ocd-done .pe-tick-btn{color:var(--ocd)}
.pe-section.ins-done{background:#fffbeb}
.pe-section.ins-done .pe-tick-btn{color:var(--ins)}
.pe-section.ptsd-done{background:#fff1f2}
.pe-section.ptsd-done .pe-tick-btn{color:var(--ptsd)}
.pe-section.an-done{background:#fdf2f8}
.pe-section.an-done .pe-tick-btn{color:var(--an)}
.pe-section.aud-done{background:#f0fdf4}
.pe-section.aud-done .pe-tick-btn{color:var(--aud)}
.pe-section.bp1-done{background:#fdf4ff}
.pe-section.bp1-done .pe-tick-btn{color:var(--bp1)}
.pe-section.pe-optional{opacity:.88}
.export-row{background:#fff;border:1px solid var(--border);border-radius:10px;padding:11px 14px;margin-bottom:14px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.export-row .ex-label{font:700 12px var(--sans);color:var(--muted);flex-shrink:0;white-space:nowrap}
.abtn{padding:7px 14px;border-radius:8px;border:1.5px solid var(--border);background:#fff;color:var(--text);font:600 12px var(--sans);cursor:pointer;transition:background .1s,border-color .1s}
.abtn:hover{background:#f3f4f6;border-color:#94a3b8}
.abtn.copied{background:#dcfce7;border-color:#86efac;color:#166534}
.preview-wrap{background:#fff;border:1px solid var(--border);border-radius:10px;overflow:hidden}
.preview-head{background:#f8fafc;border-bottom:1px solid var(--border);padding:9px 14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.preview-head-title{font:700 11px var(--sans);text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
.preview-body{padding:22px 26px;font-family:Arial,sans-serif;font-size:10pt;line-height:1.55;color:#111;min-height:100px}
.preview-body .empty-msg{color:var(--muted);font-style:italic;text-align:center;padding:36px 20px;font-size:11pt}
/* Handout preview styles */
.ho-header{margin-bottom:16px;padding-bottom:12px;border-bottom:2px solid #e5e7eb}
.ho-pt{font-size:17pt;font-weight:800;color:#0f172a;margin-bottom:2px}
.ho-meta{font-size:9pt;color:#6b7280;margin-bottom:12px}
.ho-notice{font-size:9.5pt;background:#f0f9ff;border-left:3px solid #0e7490;padding:9px 12px;line-height:1.5;color:#0c4a6e;margin-bottom:0}
.ho-condition-title{font-size:15pt;font-weight:800;padding:8px 12px;border-radius:6px;margin:20px 0 10px;color:#fff}
.ho-condition-title.adhd-t{background:var(--adhd-dark)}
.ho-condition-title.asd-t{background:var(--asd-dark)}
.ho-condition-title.ocd-t{background:var(--ocd-dark)}
.ho-condition-title.ins-t{background:var(--ins-dark)}
.ho-condition-title.ptsd-t{background:var(--ptsd-dark)}
.ho-condition-title.an-t{background:var(--an-dark)}
.ho-condition-title.aud-t{background:var(--aud-dark)}
.ho-condition-title.bp1-t{background:var(--bp1-dark)}
.ho-group-label{font-size:9pt;font-weight:800;text-transform:uppercase;letter-spacing:.07em;margin:12px 0 6px;padding-bottom:3px;border-bottom-width:2px;border-bottom-style:solid}
/* ADHD group label colours */
.ho-group-label.adhd-g-general{color:var(--adhd-dark);border-bottom-color:var(--adhd-dark)}
.ho-group-label.adhd-g-med{color:#0e7490;border-bottom-color:#0e7490}
.ho-group-label.adhd-g-nonpharm{color:#7c3aed;border-bottom-color:#7c3aed}
.ho-group-label.adhd-g-products{color:#065f46;border-bottom-color:#065f46}
/* ASD group label colours */
.ho-group-label.asd-g{color:var(--asd-dark);border-bottom-color:var(--asd-dark)}
/* OCD group label colours */
.ho-group-label.ocd-g-core{color:var(--ocd-dark);border-bottom-color:var(--ocd-dark)}
.ho-group-label.ocd-g-treatment{color:#1e3a5f;border-bottom-color:#1e3a5f}
.ho-group-label.ocd-g-strategies{color:#0e7490;border-bottom-color:#0e7490}
.ho-group-label.ocd-g-resources{color:#065f46;border-bottom-color:#065f46}
/* Insomnia group label colours */
.ho-group-label.ins-g-core{color:var(--ins-dark);border-bottom-color:var(--ins-dark)}
.ho-group-label.ins-g-treatment{color:#1e3a5f;border-bottom-color:#1e3a5f}
.ho-group-label.ins-g-strategies{color:#0e7490;border-bottom-color:#0e7490}
.ho-group-label.ins-g-resources{color:#065f46;border-bottom-color:#065f46}
/* PTSD group label colours */
.ho-group-label.ptsd-g-core{color:var(--ptsd-dark);border-bottom-color:var(--ptsd-dark)}
.ho-group-label.ptsd-g-treatment{color:#1e3a5f;border-bottom-color:#1e3a5f}
.ho-group-label.ptsd-g-strategies{color:#0e7490;border-bottom-color:#0e7490}
.ho-group-label.ptsd-g-resources{color:#065f46;border-bottom-color:#065f46}
/* AN group label colours */
.ho-group-label.an-g-core{color:var(--an-dark);border-bottom-color:var(--an-dark)}
.ho-group-label.an-g-treatment{color:#1e3a5f;border-bottom-color:#1e3a5f}
.ho-group-label.an-g-recovery{color:#0e7490;border-bottom-color:#0e7490}
.ho-group-label.an-g-resources{color:#065f46;border-bottom-color:#065f46}
/* AUD group label colours */
.ho-group-label.aud-g-core{color:var(--aud-dark);border-bottom-color:var(--aud-dark)}
.ho-group-label.aud-g-treatment{color:#1e3a5f;border-bottom-color:#1e3a5f}
.ho-group-label.aud-g-medications{color:#6d28d9;border-bottom-color:#6d28d9}
.ho-group-label.aud-g-recovery{color:#0e7490;border-bottom-color:#0e7490}
/* BP1 group label colours */
.ho-group-label.bp1-g-core{color:var(--bp1-dark);border-bottom-color:var(--bp1-dark)}
.ho-group-label.bp1-g-treatment{color:#1e3a5f;border-bottom-color:#1e3a5f}
.ho-group-label.bp1-g-medications{color:#4c1d95;border-bottom-color:#4c1d95}
.ho-group-label.bp1-g-living{color:#0e7490;border-bottom-color:#0e7490}
.ho-topic{margin-bottom:20px;padding:11px 14px;border:1px solid #e5e7eb;border-radius:7px;background:#fafbff}
.ho-topic-title{font-weight:700;font-size:11pt;color:#0f172a;margin:0 0 6px;padding-bottom:5px;border-bottom:1px solid #e5e7eb}
.ho-topic-body{font-size:10pt;line-height:1.65;color:#374151}
.ho-topic-body p{margin:0 0 6px}
.ho-topic-body p:last-child{margin:0}
.ho-topic-body ul{margin:3px 0 7px 16px}
.ho-topic-body li{margin-bottom:3px}
.ho-topic-body table{width:100%;border-collapse:collapse;font-size:9.5pt;margin:5px 0 8px}
.ho-topic-body th{background:#f1f5f9;padding:4px 7px;text-align:left;border:1px solid #d1d5db;font-size:9pt}
.ho-topic-body td{padding:3px 7px;border:1px solid #d1d5db;vertical-align:top}
.ho-topic-body a{color:#0d9488}
.ho-footer{margin-top:24px;padding-top:12px;border-top:1px solid #e5e7eb;font-size:8.5pt;color:#9ca3af;font-style:italic}
</style>
</head>
<body>

<div class="topbar">
  <span class="topbar-title">Psychoeducation</span>
  <input class="ti" id="ptName" placeholder="Patient name..." style="flex:1;min-width:130px;max-width:210px" oninput="refresh()">
  <input class="ti" id="ptDate" type="date" style="flex:0 0 128px" oninput="refresh()">
  <input class="ti" id="drName" placeholder="Clinician name..." style="flex:1;min-width:130px;max-width:200px" oninput="refresh()">
</div>

<div class="content">

  <div class="section-label" style="margin-top:12px">Select condition — tap to switch</div>
  <div class="disorder-row">
    <button class="dis-btn" id="dis-adhd" onclick="toggleCondition('adhd')">ADHD</button>
    <button class="dis-btn" id="dis-asd" onclick="toggleCondition('asd')">ASD</button>
    <button class="dis-btn" id="dis-ocd" onclick="toggleCondition('ocd')">OCD</button>
    <button class="dis-btn" id="dis-ins" onclick="toggleCondition('ins')">Insomnia</button>
    <button class="dis-btn" id="dis-ptsd" onclick="toggleCondition('ptsd')">PTSD</button>
    <button class="dis-btn" id="dis-an" onclick="toggleCondition('an')">Anorexia Nervosa</button>
    <button class="dis-btn" id="dis-aud" onclick="toggleCondition('aud')">Alcohol Use Disorder</button>
    <button class="dis-btn" id="dis-bp1" onclick="toggleCondition('bp1')">Bipolar 1</button>
  </div>

  <div id="block-adhd" class="condition-block" style="display:none;margin-top:14px">
    <div class="condition-header adhd-h">
      ADHD — Topics
      <div class="cond-sel-btns">
        <button class="cond-sel-btn" onclick="selectAll('adhd')">Select all</button>
        <button class="cond-sel-btn" onclick="clearAll('adhd')">Clear all</button>
      </div>
    </div>
    <div class="topic-list" id="adhd-topic-list"></div>
  </div>

  <div id="block-asd" class="condition-block" style="display:none">
    <div class="condition-header asd-h">
      ASD — Topics
      <div class="cond-sel-btns">
        <button class="cond-sel-btn" onclick="selectAll('asd')">Select all</button>
        <button class="cond-sel-btn" onclick="clearAll('asd')">Clear all</button>
      </div>
    </div>
    <div class="topic-list" id="asd-topic-list"></div>
  </div>

  <div id="block-ocd" class="condition-block" style="display:none">
    <div class="condition-header ocd-h">
      OCD — Topics
      <div class="cond-sel-btns">
        <button class="cond-sel-btn" onclick="selectAll('ocd')">Select all</button>
        <button class="cond-sel-btn" onclick="clearAll('ocd')">Clear all</button>
      </div>
    </div>
    <div class="topic-list" id="ocd-topic-list"></div>
  </div>

  <div id="block-ins" class="condition-block" style="display:none">
    <div class="condition-header ins-h">
      Insomnia — Topics
      <div class="cond-sel-btns">
        <button class="cond-sel-btn" onclick="selectAll('ins')">Select all</button>
        <button class="cond-sel-btn" onclick="clearAll('ins')">Clear all</button>
      </div>
    </div>
    <div class="topic-list" id="ins-topic-list"></div>
  </div>

  <div id="block-ptsd" class="condition-block" style="display:none">
    <div class="condition-header ptsd-h">
      PTSD — Topics
      <div class="cond-sel-btns">
        <button class="cond-sel-btn" onclick="selectAll('ptsd')">Select all</button>
        <button class="cond-sel-btn" onclick="clearAll('ptsd')">Clear all</button>
      </div>
    </div>
    <div class="topic-list" id="ptsd-topic-list"></div>
  </div>

  <div id="block-an" class="condition-block" style="display:none">
    <div class="condition-header an-h">
      Anorexia Nervosa — Topics
      <div class="cond-sel-btns">
        <button class="cond-sel-btn" onclick="selectAll('an')">Select all</button>
        <button class="cond-sel-btn" onclick="clearAll('an')">Clear all</button>
      </div>
    </div>
    <div class="topic-list" id="an-topic-list"></div>
  </div>

  <div id="block-aud" class="condition-block" style="display:none">
    <div class="condition-header aud-h">
      Alcohol Use Disorder — Topics
      <div class="cond-sel-btns">
        <button class="cond-sel-btn" onclick="selectAll('aud')">Select all</button>
        <button class="cond-sel-btn" onclick="clearAll('aud')">Clear all</button>
      </div>
    </div>
    <div class="topic-list" id="aud-topic-list"></div>
  </div>

  <div id="block-bp1" class="condition-block" style="display:none">
    <div class="condition-header bp1-h">
      Bipolar 1 Disorder — Topics
      <div class="cond-sel-btns">
        <button class="cond-sel-btn" onclick="selectAll('bp1')">Select all</button>
        <button class="cond-sel-btn" onclick="clearAll('bp1')">Clear all</button>
      </div>
    </div>
    <div class="topic-list" id="bp1-topic-list"></div>
  </div>

  <div class="export-row">
    <span class="ex-label">Export</span>
    <button class="abtn" id="btn-docx" onclick="dlDocx()">Download .docx</button>
    <button class="abtn" id="btn-plain" onclick="copyPlain(this)">Copy plain text</button>
    <button class="abtn" id="btn-fmt" onclick="copyFormatted(this)">Copy formatted</button>
  </div>

  <div class="preview-wrap">
    <div class="preview-head">
      <span class="preview-head-title">Handout Preview</span>
      <button class="abtn" onclick="refresh()" style="padding:4px 11px;font-size:11px">Refresh</button>
    </div>
    <div class="preview-body" id="preview">
      <div class="empty-msg">Select a condition and tick topics above to generate the handout.</div>
    </div>
  </div>

</div>

<script>
""" + ADHD_JS + "\n\n" + ASD_JS + "\n\n" + OCD_JS + "\n\n" + INSOMNIA_JS + "\n\n" + PTSD_JS + "\n\n" + AN_JS + "\n\n" + AUD_JS + "\n\n" + BP1_JS + r"""

var adhdSel={}, asdSel={}, ocdSel={}, insSel={}, ptsdSel={}, anSel={}, audSel={}, bp1Sel={};

var CONDITIONS={
  adhd:{groups:ADHD_PE_GROUPS, sel:adhdSel, done:'adhd-done', listId:'adhd-topic-list', blockId:'block-adhd', btnId:'dis-adhd', cls:'active-adhd'},
  asd: {groups:ASD_PE_GROUPS,  sel:asdSel,  done:'asd-done',  listId:'asd-topic-list',  blockId:'block-asd',  btnId:'dis-asd',  cls:'active-asd'},
  ocd: {groups:OCD_PE_GROUPS,  sel:ocdSel,  done:'ocd-done',  listId:'ocd-topic-list',  blockId:'block-ocd',  btnId:'dis-ocd',  cls:'active-ocd'},
  ins: {groups:INSOMNIA_PE_GROUPS,sel:insSel,done:'ins-done', listId:'ins-topic-list',  blockId:'block-ins',  btnId:'dis-ins',  cls:'active-ins'},
  ptsd:{groups:PTSD_PE_GROUPS, sel:ptsdSel, done:'ptsd-done', listId:'ptsd-topic-list', blockId:'block-ptsd', btnId:'dis-ptsd', cls:'active-ptsd'},
  an:  {groups:AN_PE_GROUPS,   sel:anSel,   done:'an-done',   listId:'an-topic-list',   blockId:'block-an',   btnId:'dis-an',   cls:'active-an'},
  aud: {groups:AUD_PE_GROUPS,  sel:audSel,  done:'aud-done',  listId:'aud-topic-list',  blockId:'block-aud',  btnId:'dis-aud',  cls:'active-aud'},
  bp1: {groups:BP1_PE_GROUPS,  sel:bp1Sel,  done:'bp1-done',  listId:'bp1-topic-list',  blockId:'block-bp1',  btnId:'dis-bp1',  cls:'active-bp1'}
};

var SHOW={adhd:false,asd:false,ocd:false,ins:false,ptsd:false,an:false,aud:false,bp1:false};
var activeCond=null;

function $(id){return document.getElementById(id);}
function f(id){var el=$(id);return el?el.value.trim():'';}
function esc(s){if(!s)return '';return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}

function toggleCondition(cond){
  Object.keys(CONDITIONS).forEach(function(k){
    SHOW[k]=(k===cond);
    var ck=CONDITIONS[k];
    $(ck.btnId).className='dis-btn'+(SHOW[k]?' '+ck.cls:'');
    $(ck.blockId).style.display=SHOW[k]?'':'none';
  });
  activeCond=cond;
  refresh();
}

function renderTopics(){
  Object.keys(CONDITIONS).forEach(function(cond){
    var c=CONDITIONS[cond];
    renderTopicList(c.listId, c.groups, c.sel, cond, c.done);
  });
}

function renderTopicList(containerId, groups, sel, condKey, doneClass){
  var el=$(containerId); if(!el) return;
  var html='';
  groups.forEach(function(g){
    if(g.label) html+='<div class="pe-group-label">'+(g.optional?'<span style="font-size:9px;opacity:.6;font-weight:600;margin-right:4px">OPTIONAL</span>':'')+esc(g.label)+'</div>';
    g.items.forEach(function(item){
      var done=!!sel[item.id];
      html+='<div class="pe-section'+(done?' '+doneClass:'')+(g.optional?' pe-optional':'')+'" data-id="'+item.id+'" data-cond="'+condKey+'">';
      html+='<div class="pe-header">';
      html+='<span class="pe-tick-btn">'+(done?'&#9745;':'&#9744;')+'</span>';
      html+='<span class="pe-title">'+esc(item.title)+'</span>';
      html+='<span class="pe-arrow">&#9658;</span>';
      html+='</div>';
      html+='<div class="pe-body">'+item.body+'</div>';
      html+='</div>';
    });
  });
  el.innerHTML=html;
  el.onclick=function(e){
    var sec=e.target.closest('[data-id]'); if(!sec) return;
    var id=sec.getAttribute('data-id'), cn=sec.getAttribute('data-cond');
    var isTick=e.target.classList.contains('pe-tick-btn');
    if(isTick){
      e.stopPropagation();
      var c=CONDITIONS[cn];
      c.sel[id]=!c.sel[id];
      sec.classList.toggle(c.done,!!c.sel[id]);
      sec.querySelector('.pe-tick-btn').innerHTML=c.sel[id]?'&#9745;':'&#9744;';
      refresh();
    } else {
      var hdr=e.target.closest('.pe-header'); if(hdr) sec.classList.toggle('pe-open');
    }
  };
}

function selectAll(cond){
  var c=CONDITIONS[cond];
  c.groups.forEach(function(g){g.items.forEach(function(item){c.sel[item.id]=true;});});
  renderTopics(); refresh();
}
function clearAll(cond){
  var c=CONDITIONS[cond];
  Object.keys(c.sel).forEach(function(k){c.sel[k]=false;});
  renderTopics(); refresh();
}

var ADHD_GROUP_COLORS={'null':'adhd-g-general','Medication Information':'adhd-g-med','Non-pharmacological Strategies':'adhd-g-nonpharm','Products and Resources':'adhd-g-products'};
var ASD_GROUP_COLORS={'null':'asd-g','Products and Resources':'asd-g','Additional Topics':'asd-g'};
var OCD_GROUP_COLORS={'null':'ocd-g-core','Treatment':'ocd-g-treatment','Strategies and Self-Help':'ocd-g-strategies','Products and Resources':'ocd-g-resources'};
var INS_GROUP_COLORS={'null':'ins-g-core','Treatment':'ins-g-treatment','Practical Strategies':'ins-g-strategies','Products and Resources':'ins-g-resources'};
var PTSD_GROUP_COLORS={'null':'ptsd-g-core','Treatment':'ptsd-g-treatment','Strategies':'ptsd-g-strategies','Products and Resources':'ptsd-g-resources'};
var AN_GROUP_COLORS={'null':'an-g-core','Treatment':'an-g-treatment','Recovery and Psychology':'an-g-recovery','Products and Resources':'an-g-resources'};
var AUD_GROUP_COLORS={'null':'aud-g-core','Treatment':'aud-g-treatment','Medications':'aud-g-medications','Recovery and Support':'aud-g-recovery'};
var BP1_GROUP_COLORS={'null':'bp1-g-core','Treatment':'bp1-g-treatment','Medications':'bp1-g-medications','Living Well with Bipolar 1':'bp1-g-living'};

var CONDITION_META={
  adhd:{titleCls:'adhd-t',label:'Attention Deficit Hyperactivity Disorder (ADHD)',groupColors:ADHD_GROUP_COLORS,defaultGroupCls:'adhd-g-general'},
  asd: {titleCls:'asd-t', label:'Autism Spectrum Disorder (ASD)', groupColors:ASD_GROUP_COLORS, defaultGroupCls:'asd-g'},
  ocd: {titleCls:'ocd-t', label:'Obsessive-Compulsive Disorder (OCD)', groupColors:OCD_GROUP_COLORS, defaultGroupCls:'ocd-g-core'},
  ins: {titleCls:'ins-t', label:'Insomnia', groupColors:INS_GROUP_COLORS, defaultGroupCls:'ins-g-core'},
  ptsd:{titleCls:'ptsd-t',label:'Post-Traumatic Stress Disorder (PTSD)', groupColors:PTSD_GROUP_COLORS,defaultGroupCls:'ptsd-g-core'},
  an:  {titleCls:'an-t',  label:'Anorexia Nervosa', groupColors:AN_GROUP_COLORS, defaultGroupCls:'an-g-core'},
  aud: {titleCls:'aud-t', label:'Alcohol Use Disorder', groupColors:AUD_GROUP_COLORS, defaultGroupCls:'aud-g-core'},
  bp1: {titleCls:'bp1-t', label:'Bipolar 1 Disorder', groupColors:BP1_GROUP_COLORS, defaultGroupCls:'bp1-g-core'}
};

function buildHandout(){
  var name=f('ptName')||'Patient';
  var dr=f('drName')||'Your clinician';
  var dv=f('ptDate'),ds=dv?new Date(dv+'T12:00:00').toLocaleDateString('en-AU',{day:'numeric',month:'long',year:'numeric'}):'';

  var hasAny=false;
  ['adhd','asd','ocd','ins','ptsd','an','aud','bp1'].forEach(function(cond){
    if(!SHOW[cond]) return;
    var c=CONDITIONS[cond];
    c.groups.forEach(function(g){g.items.forEach(function(item){if(c.sel[item.id])hasAny=true;});});
  });
  if(!hasAny) return null;

  var h='';
  h+='<div class="ho-header">';
  h+='<div class="ho-pt">Psychoeducation Handout</div>';
  h+='<div class="ho-meta">Patient: <strong>'+esc(name)+'</strong>';
  if(ds) h+=' &nbsp;|&nbsp; '+esc(ds);
  h+=' &nbsp;|&nbsp; Clinician: <strong>'+esc(dr)+'</strong></div>';
  h+='</div>';

  ['adhd','asd','ocd','ins','ptsd','an','aud','bp1'].forEach(function(cond){
    if(!SHOW[cond]) return;
    var c=CONDITIONS[cond];
    var meta=CONDITION_META[cond];
    var selItems=getSelectedItems(c.groups,c.sel);
    if(!selItems.length) return;
    h+='<div class="ho-condition-title '+meta.titleCls+'">'+meta.label+'</div>';
    h+=buildConditionContent(selItems,c.groups,meta.groupColors,meta.defaultGroupCls);
  });

  h+='<div class="ho-footer">This handout was prepared specifically for '+esc(name)+(ds?' following a psychiatric appointment on '+esc(ds):'')+'. It is not a substitute for clinical advice.</div>';
  return h;
}

function getSelectedItems(groups,sel){
  var result=[];
  groups.forEach(function(g){
    g.items.forEach(function(item){
      if(sel[item.id]) result.push({group:g.label,item:item});
    });
  });
  return result;
}

function buildConditionContent(selectedItems,groups,groupColors,defaultCls){
  var groupMap={},groupOrder=[];
  groups.forEach(function(g){
    var gKey=g.label||'null';
    g.items.forEach(function(item){
      var found=selectedItems.find(function(s){return s.item.id===item.id;});
      if(found){
        if(!groupMap[gKey]){groupMap[gKey]=[];groupOrder.push({key:gKey,label:g.label});}
        groupMap[gKey].push(item);
      }
    });
  });
  var h='';
  groupOrder.forEach(function(gInfo){
    var gKey=gInfo.key, gLabel=gInfo.label;
    if(gLabel){
      var cls=groupColors[gLabel]||defaultCls;
      h+='<div class="ho-group-label '+cls+'">'+esc(gLabel)+'</div>';
    }
    groupMap[gKey].forEach(function(item){
      h+='<div class="ho-topic">';
      h+='<div class="ho-topic-title">'+esc(item.title)+'</div>';
      h+='<div class="ho-topic-body">'+item.body+'</div>';
      h+='</div>';
    });
  });
  return h;
}

function refresh(){
  var html=buildHandout();
  var pv=$('preview');
  if(!html){pv.innerHTML='<div class="empty-msg">Select a condition and tick topics above to generate the handout.</div>';return;}
  pv.innerHTML=html;
}

/* Add inline styles to table cells in item body HTML so they work in Word and off-DOM contexts */
function styleBody(s){
  return s
    .replace(/<table/g,'<table style="border-collapse:collapse;width:100%;font-size:9pt;margin:5px 0 9px"')
    .replace(/<th>/g,'<th style="padding:4px 7px;border:1px solid #ccc;background:#f0f0f0;font-weight:bold;text-align:left">')
    .replace(/<th /g,'<th style="padding:4px 7px;border:1px solid #ccc;background:#f0f0f0;font-weight:bold;text-align:left" ')
    .replace(/<td>/g,'<td style="padding:3px 7px;border:1px solid #ccc;vertical-align:top">')
    .replace(/<td /g,'<td style="padding:3px 7px;border:1px solid #ccc;vertical-align:top" ');
}

/* Build Word-compatible HTML directly — no div backgrounds, table-per-topic for reliable spacing */
function buildDocxHtml(){
  var name=f('ptName')||'Patient';
  var dr=f('drName')||'Your clinician';
  var dv=f('ptDate'),ds=dv?new Date(dv+'T12:00:00').toLocaleDateString('en-AU',{day:'numeric',month:'long',year:'numeric'}):'';
  var bgMap={adhd:'#1e3a5f',asd:'#134e4a',ocd:'#4c1d95',ins:'#78350f',ptsd:'#881337',an:'#831843',aud:'#14532d',bp1:'#701a75'};
  var hasAny=false;
  ['adhd','asd','ocd','ins','ptsd','an','aud','bp1'].forEach(function(cond){
    if(!SHOW[cond]) return;
    var c=CONDITIONS[cond];
    c.groups.forEach(function(g){g.items.forEach(function(item){if(c.sel[item.id])hasAny=true;});});
  });
  if(!hasAny) return null;
  var h='';
  h+='<p style="font-size:17pt;font-weight:bold;color:#0f172a;margin:0 0 3pt">Psychoeducation Handout</p>';
  h+='<p style="font-size:9pt;color:#555;margin:0 0 14pt">Patient: <b>'+esc(name)+'</b>';
  if(ds) h+=' &nbsp;|&nbsp; '+esc(ds);
  h+=' &nbsp;|&nbsp; Clinician: <b>'+esc(dr)+'</b></p>';
  ['adhd','asd','ocd','ins','ptsd','an','aud','bp1'].forEach(function(cond){
    if(!SHOW[cond]) return;
    var c=CONDITIONS[cond],meta=CONDITION_META[cond];
    var selItems=getSelectedItems(c.groups,c.sel);
    if(!selItems.length) return;
    var bg=bgMap[cond]||'#1e3a5f';
    h+='<p style="font-size:14pt;font-weight:bold;color:#fff;background:'+bg+';padding:7pt 10pt;margin:18pt 0 10pt">'+esc(meta.label)+'</p>';
    var curGroup=null;
    c.groups.forEach(function(g){
      g.items.forEach(function(item){
        if(!c.sel[item.id]) return;
        if(g.label&&g.label!==curGroup){
          curGroup=g.label;
          h+='<p style="font-size:8pt;font-weight:bold;text-transform:uppercase;letter-spacing:.06em;margin:12pt 0 5pt">'+esc(g.label)+'</p>';
        }
        h+='<table width="100%" cellspacing="0" cellpadding="0" style="border:1pt solid #d1d5db;border-collapse:collapse;margin-bottom:14pt">';
        h+='<tr><td style="padding:9pt 11pt;font-family:Arial,sans-serif;font-size:10pt;line-height:1.55;color:#222">';
        h+='<p style="font-weight:bold;font-size:11pt;color:#0f172a;margin:0 0 6pt;padding-bottom:5pt;border-bottom:1pt solid #e0e0e0">'+esc(item.title)+'</p>';
        h+=styleBody(item.body);
        h+='</td></tr></table>';
      });
    });
  });
  h+='<p style="margin-top:18pt;padding-top:9pt;border-top:1pt solid #e5e7eb;font-size:8pt;color:#9ca3af;font-style:italic">This handout was prepared specifically for '+esc(name)+(ds?' following a psychiatric appointment on '+esc(ds):'')+'. It is not a substitute for clinical advice.</p>';
  return '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns="http://www.w3.org/TR/REC-html40">'+
    '<head><meta charset="UTF-8"><style>@page{margin:2cm 2.5cm;}body{font-family:Arial,sans-serif;font-size:10pt;line-height:1.5;color:#111;}p{margin:0 0 4pt;}ul{margin:3pt 0 6pt 14pt;}li{margin-bottom:3pt;}</style></head><body>'+h+'</body></html>';
}

function dlDocx(){
  var docx=buildDocxHtml(); if(!docx){alert('No topics selected — please tick some topics first.');return;}
  var name=(f('ptName')||'Patient').replace(/[^a-zA-Z0-9]/g,'_');
  var blob=new Blob(['﻿'+docx],{type:'application/msword;charset=utf-8'});
  var url=URL.createObjectURL(blob),a=document.createElement('a');
  a.href=url;a.download='Psychoeducation_Handout_'+name+'.doc';
  document.body.appendChild(a);a.click();document.body.removeChild(a);
  setTimeout(function(){URL.revokeObjectURL(url);},2000);
  flash($('btn-docx'),'Downloaded!');
}

/* Build plain text from data — not from DOM innerText which collapses whitespace */
function buildPlainText(){
  var name=f('ptName')||'Patient';
  var dr=f('drName')||'Your clinician';
  var dv=f('ptDate'),ds=dv?new Date(dv+'T12:00:00').toLocaleDateString('en-AU',{day:'numeric',month:'long',year:'numeric'}):'';
  var lines=['PSYCHOEDUCATION HANDOUT','Patient: '+name+(ds?' | '+ds:'')+(dr?' | Clinician: '+dr:'')];
  var hasAny=false;
  ['adhd','asd','ocd','ins','ptsd','an','aud','bp1'].forEach(function(cond){
    if(!SHOW[cond]) return;
    var c=CONDITIONS[cond],meta=CONDITION_META[cond];
    var selItems=getSelectedItems(c.groups,c.sel);
    if(!selItems.length) return;
    hasAny=true;
    lines.push('','═══════════════════════════════════',meta.label.toUpperCase(),'═══════════════════════════════════');
    var curGroup=null;
    c.groups.forEach(function(g){
      g.items.forEach(function(item){
        if(!c.sel[item.id]) return;
        if(g.label&&g.label!==curGroup){curGroup=g.label;lines.push('','— '+g.label.toUpperCase()+' —');}
        lines.push('','■ '+item.title);
        var tmp=document.createElement('div');
        tmp.innerHTML=item.body;
        lines.push((tmp.innerText||tmp.textContent).trim().replace(/\n{3,}/g,'\n\n'));
      });
    });
  });
  if(!hasAny) return null;
  lines.push('','──────────────────────────────────────','This handout was prepared for '+name+(ds?' on '+ds:'')+'.');
  return lines.join('\n');
}

function copyPlain(btn){
  var txt=buildPlainText();
  if(!txt){alert('No topics selected — please tick some topics first.');return;}
  navigator.clipboard.writeText(txt).then(function(){flash(btn,'Copied!');}).catch(function(){alert('Copy failed — try Download .doc instead.');});
}

/* Build inline-styled HTML for paste into clinical software */
function buildPasteHtml(){
  var name=f('ptName')||'Patient';
  var dr=f('drName')||'Your clinician';
  var dv=f('ptDate'),ds=dv?new Date(dv+'T12:00:00').toLocaleDateString('en-AU',{day:'numeric',month:'long',year:'numeric'}):'';
  var bgMap={adhd:'#1e3a5f',asd:'#134e4a',ocd:'#4c1d95',ins:'#78350f',ptsd:'#881337',an:'#831843',aud:'#14532d',bp1:'#701a75'};
  var hasAny=false;
  ['adhd','asd','ocd','ins','ptsd','an','aud','bp1'].forEach(function(cond){
    if(!SHOW[cond]) return;
    var c=CONDITIONS[cond];
    c.groups.forEach(function(g){g.items.forEach(function(item){if(c.sel[item.id])hasAny=true;});});
  });
  if(!hasAny) return null;
  var h='<div style="font-family:Arial,sans-serif;font-size:10pt;line-height:1.55;color:#111;max-width:780px">';
  h+='<p style="font-size:16pt;font-weight:bold;margin:0 0 4px">Psychoeducation Handout</p>';
  h+='<p style="font-size:9pt;color:#555;margin:0 0 14px">Patient: <b>'+esc(name)+'</b>';
  if(ds) h+=' &nbsp;|&nbsp; '+esc(ds);
  h+=' &nbsp;|&nbsp; Clinician: <b>'+esc(dr)+'</b></p>';
  ['adhd','asd','ocd','ins','ptsd','an','aud','bp1'].forEach(function(cond){
    if(!SHOW[cond]) return;
    var c=CONDITIONS[cond],meta=CONDITION_META[cond];
    var selItems=getSelectedItems(c.groups,c.sel);
    if(!selItems.length) return;
    var bg=bgMap[cond]||'#1e3a5f';
    h+='<p style="font-size:13pt;font-weight:bold;color:#fff;background:'+bg+';padding:5px 9px;margin:16px 0 8px">'+esc(meta.label)+'</p>';
    var curGroup=null;
    c.groups.forEach(function(g){
      g.items.forEach(function(item){
        if(!c.sel[item.id]) return;
        if(g.label&&g.label!==curGroup){
          curGroup=g.label;
          h+='<p style="font-size:8pt;font-weight:bold;text-transform:uppercase;margin:10px 0 4px;color:#444">'+esc(g.label)+'</p>';
        }
        h+='<div style="margin:0 0 14px;border:1px solid #ddd;padding:8px 11px">';
        h+='<p style="font-weight:bold;font-size:11pt;margin:0 0 6px;padding-bottom:5px;border-bottom:1px solid #e5e7eb">'+esc(item.title)+'</p>';
        h+='<div style="font-size:10pt;line-height:1.6">'+styleBody(item.body)+'</div>';
        h+='</div>';
      });
    });
  });
  h+='</div>';
  return h;
}

/* Uses execCommand copy on live DOM element — works on file:// and HTTPS, pastes rich text into any app */
function copyFormatted(btn){
  var content=buildPasteHtml();
  if(!content){alert('No topics selected — please tick some topics first.');return;}
  var el=document.createElement('div');
  el.style.cssText='position:fixed;left:-9999px;top:0;width:780px;background:#fff;overflow:hidden';
  el.innerHTML=content;
  document.body.appendChild(el);
  var range=document.createRange();
  range.selectNodeContents(el);
  var sel=window.getSelection();
  sel.removeAllRanges();
  sel.addRange(range);
  var ok=false;
  try{ok=document.execCommand('copy');}catch(ex){}
  sel.removeAllRanges();
  document.body.removeChild(el);
  if(ok){flash(btn,'Copied!');}
  else if(window.ClipboardItem){
    var blob=new Blob([content],{type:'text/html'});
    navigator.clipboard.write([new ClipboardItem({'text/html':blob})]).then(function(){flash(btn,'Copied!');}).catch(function(){copyPlain(btn);});
  } else {copyPlain(btn);}
}
function flash(btn,msg){
  if(!btn)return;
  var orig=btn.textContent;btn.textContent=msg;btn.classList.add('copied');
  setTimeout(function(){btn.textContent=orig;btn.classList.remove('copied');},2000);
}

document.addEventListener('DOMContentLoaded',function(){
  var td=new Date().toISOString().slice(0,10);
  var dtEl=$('ptDate'); if(dtEl&&!dtEl.value) dtEl.value=td;
  renderTopics();
  toggleCondition('adhd');
  refresh();
});
</script>
</body>
</html>"""

out = os.path.join(BASE, 'psychoeducation.html')
with open(out, 'w', encoding='utf-8') as fh:
    fh.write(html)
print("Written:", out, "(%d bytes)" % len(html))
