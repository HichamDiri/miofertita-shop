"""Clone CompraConfio voyage-nova-panama to MioFertita."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
CC = Path(r"C:\Users\Administrateur\Projects\compraconfio-shop")
src_html = CC / "voyage-nova-panama.html"
dst_html = ROOT / "voyage-nova-panama.html"
src_css = CC / "css" / "voyage-nova.css"
dst_css = ROOT / "css" / "voyage-nova.css"

t = src_html.read_text(encoding="utf-8")
replacements = [
    ('CompraConfio Panamá', 'MioFertita Panamá'),
    ('© 2026 CompraConfio — Panamá', '© 2026 MioFertita — Panamá'),
    ('compra<em>confio</em>', 'mio<em>fertita</em>'),
    ('contacto@compraconfio.shop', 'contacto@miofertita.shop'),
    ('data-brand="compraconfio"', 'data-brand="miofertita"'),
    ('data-fb-pixel="off" data-abandon-checkout', 'data-fb-pixel="off" data-phone-lenient="on" data-abandon-checkout'),
    ('/thank-you-compraconfio-panama.html', '/thank-you-miofertita-panama.html'),
    ('facebook-domain-verification" content="ytbsk6igo7oh4rui32ve803vp025qw"',
     'facebook-domain-verification" content="xbcif1s989l5gi1gu3xogwfta9vg58"'),
    ('cc-voyage-pa', 'mf-voyage-pa'),
    ('cc-voyage', 'mf-voyage'),
    ('<script src="/js/clarity.js?v=20261024" async></script>',
     '<script src="/js/clarity.js?v=20260928" defer></script>'),
    ('<script src="/js/config.js?v=20261023a" defer></script>',
     '<script src="/js/config.js?v=20260916b" defer></script>'),
    ('<script src="/js/main.js?v=20261025b" defer></script>',
     '<script src="/js/main.js?v=20260924a" defer></script>'),
    ('<script src="/js/abandoned-checkout.js?v=20261025b" defer></script>',
     '<script src="/js/abandoned-checkout.js?v=20260922e" defer></script>'),
]
for old, new in replacements:
    t = t.replace(old, new)

dst_html.write_text(t, encoding="utf-8")
shutil.copy2(src_css, dst_css)

images_dst = ROOT / "images"
images_dst.mkdir(parents=True, exist_ok=True)
videos_dst = ROOT / "videos"
videos_dst.mkdir(parents=True, exist_ok=True)

for p in CC.glob("images/voyage-*"):
    shutil.copy2(p, images_dst / p.name)
video = CC / "videos" / "voyage-own-room.mp4"
if video.is_file():
    shutil.copy2(video, videos_dst / video.name)

print("Wrote", dst_html)
print("CSS +", len(list(CC.glob("images/voyage-*"))), "images")
