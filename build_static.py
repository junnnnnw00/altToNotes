#!/usr/bin/env python3
"""
Generate static files for GitHub Pages deployment.
Produces index.html, pdfview.html, files.json at repo root.
"""
import json
import re
import sys
from pathlib import Path


def _natural_key(path: Path):
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', str(path))]

ROOT = Path(__file__).parent

sys.path.insert(0, str(ROOT))
from viewer import HTML, PDFVIEW_HTML

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
groups: dict[str, list] = {}
skip_dirs = {"__pycache__", ".git", "node_modules", ".omc"}

for pdf in sorted(ROOT.glob("**/*.pdf"), key=_natural_key):
    rel = pdf.relative_to(ROOT)
    if any(p.startswith(".") or p in skip_dirs for p in rel.parts):
        continue
    rel_pdf = str(rel).replace("\\", "/")
    rel_md = str(rel.with_suffix(".md")).replace("\\", "/")
    has_notes = (ROOT / rel_md).exists()
    course = rel.parts[0] if len(rel.parts) > 1 else "."
    groups.setdefault(course, []).append({
        "stem": pdf.stem,
        "pdf": rel_pdf,
        "md": rel_md,
        "has_notes": has_notes,
    })

data = [{"course": k, "files": v} for k, v in groups.items()]
(ROOT / "files.json").write_text(
    json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
total = sum(len(g["files"]) for g in data)
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
except ImportError:
    print("⚠  cairosvg not installed — skipping icon PNGs")

print("\nDone. Commit index.html, pdfview.html, files.json to deploy.")
