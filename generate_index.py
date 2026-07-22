#!/usr/bin/env python3
"""Rebuild index.html from briefs/*.html, newest first."""

import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BRIEFS = ROOT / "briefs"

entries = []
for f in sorted(BRIEFS.glob("*.html"), reverse=True):
    m = re.match(r"^(\d{4}-\d{2}-\d{2})\.html$", f.name)
    if not m:
        continue
    date = datetime.strptime(m.group(1), "%Y-%m-%d")
    entries.append((m.group(1), date.strftime("%A · %B %-d, %Y")))

items = "\n".join(
    f'      <li><a href="briefs/{slug}.html"><h2>{label}</h2>'
    f'<span class="slug">{slug}</span></a></li>'
    for slug, label in entries
)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Morning Brief</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    background: #FCFCFB;
    color: #2E2C27;
    font-family: -apple-system, "Segoe UI", sans-serif;
    line-height: 1.5;
  }}
  main {{ max-width: 720px; margin: 0 auto; padding: 72px 28px 96px; }}
  header h1 {{
    font-family: Georgia, serif;
    font-weight: 600;
    font-size: 40px;
    letter-spacing: -0.01em;
  }}
  header p {{ color: #6B6A63; margin-top: 10px; font-size: 15px; }}
  hr {{ border: 0; border-top: 1px solid #E4E3DC; margin: 40px 0; }}
  ul {{ list-style: none; }}
  li a {{
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 16px;
    padding: 20px 4px;
    text-decoration: none;
    border-bottom: 1px solid #E4E3DC;
  }}
  li a:hover h2 {{ color: #C6613F; }}
  li h2 {{
    color: #2E2C27;
    font-family: Georgia, serif;
    font-weight: 600;
    font-size: 22px;
    transition: color 120ms ease;
  }}
  li .slug {{
    color: #B4B3A8;
    font-size: 13px;
    font-variant-numeric: tabular-nums;
    white-space: nowrap;
  }}
  .empty {{ color: #6B6A63; padding: 20px 4px; }}
  @media (max-width: 640px) {{
    main {{ padding: 48px 20px 64px; }}
    header h1 {{ font-size: 30px; }}
  }}
</style>
</head>
<body>
<main>
  <header>
    <h1>Morning Brief</h1>
    <p>A calm look at each day — published weekday mornings.</p>
  </header>
  <hr>
  {'<ul>' + chr(10) + items + chr(10) + '    </ul>' if entries else '<p class="empty">No briefs yet.</p>'}
</main>
</body>
</html>
"""

(ROOT / "index.html").write_text(html)
print(f"index.html written with {len(entries)} brief(s)")
