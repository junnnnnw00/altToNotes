#!/usr/bin/env python3
"""
Generate static files for GitHub Pages deployment.
Produces index.html, pdfview.html, files.json at repo root.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent

sys.path.insert(0, str(ROOT))
from viewer import HTML, PDFVIEW_HTML
from notes_index import build_file_groups

# ── Patch main viewer HTML for static serving ─────────────────────────────────
index_html = HTML
index_html = index_html.replace(
    "fetch('/api/files')",
    "fetch('files.json')"
)
index_html = index_html.replace(
    "'/pdfview?path=' + encodeURIComponent(f.pdf)",
    "'pdfview.html?path=' + encodeURIComponent(f.pdf)"
)
index_html = index_html.replace(
    "'/file?path=' + encodeURIComponent(f.md) + '&raw=1'",
    "f.md"
)

(ROOT / "index.html").write_text(index_html, encoding="utf-8")
print("✓ index.html")

# ── Patch pdfview HTML ────────────────────────────────────────────────────────
pdfview_html = PDFVIEW_HTML
pdfview_html = pdfview_html.replace(
    "'/file?path=' + encodeURIComponent(pdfPath)",
    "pdfPath"
)

(ROOT / "pdfview.html").write_text(pdfview_html, encoding="utf-8")
print("✓ pdfview.html")

# ── Generate files.json ───────────────────────────────────────────────────────
data = build_file_groups(ROOT)
(ROOT / "files.json").write_text(
    json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
total = sum(len(group["files"]) for group in data)
print(f"✓ files.json  ({len(data)} courses, {total} files)")

# ── PWA static assets ─────────────────────────────────────────────────────────
for fname in ("manifest.json", "sw.js", "icon.svg", "favicon.svg"):
    if (ROOT / fname).exists():
        print(f"✓ {fname}")
    else:
        print(f"⚠  {fname} not found — skipping")

try:
    import cairosvg
    cairosvg.svg2png(
        url=str(ROOT / "icon.svg"),
        write_to=str(ROOT / "icon-512.png"),
        output_width=512,
        output_height=512,
    )
    cairosvg.svg2png(
        url=str(ROOT / "icon.svg"),
        write_to=str(ROOT / "icon-192.png"),
        output_width=192,
        output_height=192,
    )
    print("✓ icon-512.png, icon-192.png  (via cairosvg)")
except (ImportError, OSError) as exc:
    print(f"⚠  icon PNG generation skipped: {exc}")

print("\nDone. Commit index.html, pdfview.html, files.json to deploy.")
