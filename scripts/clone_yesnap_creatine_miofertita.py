"""Clone CompraConfio yesnap-creatine-women-panama to MioFertita."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

CC = Path(r"C:\Users\Administrateur\Projects\compraconfio-shop")
ROOT = Path(__file__).resolve().parents[1]
V = "20261029a"

src_html = CC / "yesnap-creatine-women-panama.html"
dst_html = ROOT / "yesnap-creatine-women-panama.html"
src_css = CC / "css" / "yesnap-creatine-women.css"
dst_css = ROOT / "css" / "yesnap-creatine-women.css"
src_img = CC / "images" / "yesnap-creatine-women"
dst_img = ROOT / "images" / "yesnap-creatine-women"

html = src_html.read_text(encoding="utf-8")

# Remove TikTok pixel block from <head>
html = re.sub(
    r"\s*<meta name=\"tiktok-pixel-id\".*?<link rel=\"stylesheet\" href=\"/css/yesnap-creatine-women.css[^\"]+\">",
    '\n  <link rel="stylesheet" href="/css/yesnap-creatine-women.css?v=PLACEHOLDER">',
    html,
    count=1,
    flags=re.S,
)
html = html.replace("?v=PLACEHOLDER", f"?v={V}")
html = re.sub(
    r"\s*<script>\s*function bootTikTokPixel\(\).*?</script>\s*",
    '\n  <script src="/js/clarity.js?v=20260928" defer></script>\n',
    html,
    count=1,
    flags=re.S,
)

replacements = [
    ('content="ytbsk6igo7oh4rui32ve803vp025qw"', 'content="xbcif1s989l5gi1gu3xogwfta9vg58"'),
    ("| CompraConfio Panamá", "| MioFertita Panamá"),
    ("compra<em>confio</em>", "mio<em>fertita</em>"),
    ("contacto@compraconfio.shop", "contacto@miofertita.shop"),
    ("© 2026 CompraConfio — Panamá", "© 2026 MioFertita — Panamá"),
    (
        'data-brand="compraconfio" data-product="creatine-pa" data-snap-pixel="off" data-fb-pixel="off" data-tiktok-pixel-id="DA46KJ3C77U8UMTFN63G" data-thankyou="/thank-you-compraconfio-panama.html"',
        'data-brand="miofertita" data-product="creatine-pa" data-fb-pixel-id="1825937068441998" data-fb-thankyou-event="Lead" data-snap-pixel="off" data-abandon-checkout="on" data-abandon-idle-minutes="5" data-thankyou="/thank-you-miofertita-panama.html"',
    ),
    ("/thank-you-compraconfio-panama.html", "/thank-you-miofertita-panama.html"),
    ("cc-creatine-pa", "mf-creatine-pa"),
    ("?v=20261025k", f"?v={V}"),
    ("?v=20261025g", f"?v={V}"),
    ("?v=20261025a", f"?v={V}"),
    ("yesnap-creatine-women.css?v=20261025k", f"yesnap-creatine-women.css?v={V}"),
    ("/js/clarity.js?v=20261024", "/js/clarity.js?v=20260928"),
    ("/js/config.js?v=20261021a", "/js/config.js?v=20261027"),
    ("/js/main.js?v=20261025b", "/js/main.js?v=20261028"),
]

for old, new in replacements:
    html = html.replace(old, new)

if "abandoned-checkout.js" not in html:
    html = html.replace(
        '<script src="/js/main.js?v=20261028" defer></script>',
        '<script src="/js/main.js?v=20261028" defer></script>\n'
        f'<script src="/js/abandoned-checkout.js?v=20261027" defer></script>',
    )

dst_html.write_text(html, encoding="utf-8")

shutil.copy2(src_css, dst_css)
if src_img.is_dir():
    if dst_img.exists():
        shutil.rmtree(dst_img)
    shutil.copytree(src_img, dst_img)

print("Wrote", dst_html)
print("CSS + images copied")
