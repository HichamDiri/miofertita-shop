"""Generate cubrezapatos-impermeables-panama.html from FASTIME template."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V = "20261028"
IMG = "/images/cubrezapatos"

html = (ROOT / "fastime-oil-film-wipes-panama.html").read_text(encoding="utf-8")

html = html.replace(
    "fastime-oil-film-wipes.css?v=20261027g",
    f"cubrezapatos-impermeables.css?v={V}",
)
html = html.replace(
    'data-product="fastime-wipes"',
    'data-product="cubrezapatos"',
)
html = html.replace("/images/fastime/", f"{IMG}/")
html = html.replace("?v=20261027f", f"?v={V}")
html = html.replace("?v=20261027", f"?v={V}")

html = html.replace(
    "<title>Toallitas para eliminar la película de aceite del vidrio + 3 pares de guantes GRATIS | MioFertita Panamá — Pago Contra Entrega</title>",
    "<title>Cubrezapatos impermeables reutilizables — 3 pares por $39 | MioFertita Panamá — Pago Contra Entrega</title>",
)
html = html.replace(
    'content="Elimina la película de aceite del parabrisas y recupera visión más nítida de día y de noche. Caja con 3 toallitas + guantes. Envío gratis y pago contra entrega en Panamá."',
    'content="Cubrezapatos impermeables y reutilizables para la lluvia en Panamá. Pack de 3 pares. TPE flexible, suela antideslizante. Envío gratis y pago contra entrega."',
)

announce = """<div class="announce" aria-hidden="true">
  <div class="announce-track">
    <span>Envío gratis a toda Panamá 🇵🇦</span>
    <span>Pago contra entrega</span>
    <span>Impermeables y reutilizables</span>
    <span>3 pares · $39 USD</span>
    <span>Envío gratis a toda Panamá 🇵🇦</span>
    <span>Pago contra entrega</span>
    <span>Impermeables y reutilizables</span>
    <span>3 pares · $39 USD</span>
  </div>
</div>"""
start = html.index('<div class="announce"')
end = html.index("</div>\n\n<header", start) + len("</div>")
html = html[:start] + announce + html[end:]

html = html.replace(
    "FASTIME · Elimina película de aceite · Envío gratis · Pago al recibir · Garantía 30 días",
    "Cubrezapatos · Impermeables · Envío gratis · Pago al recibir · Garantía 30 días",
)

gallery = f"""    <section class="gallery" id="heroSection">
      <div class="gallery-stage" id="galleryTrack">
        <div class="slide">
          <img src="{IMG}/lp01-hero.png?v={V}" alt="Cubrezapatos impermeables — protege tus zapatos de la lluvia en Panamá" width="1080" height="1920" fetchpriority="high" decoding="async">
        </div>
        <div class="slide">
          <img src="{IMG}/lp05-resistencia.png?v={V}" alt="Cubrezapatos resistentes al agua y reutilizables" width="1080" height="1920" loading="lazy" decoding="async">
        </div>
      </div>
      <div class="gallery-dots" id="galleryDots" aria-hidden="true"></div>
      <div class="gallery-thumbs">
        <button type="button" class="thumb is-active" aria-label="Hero"><img src="{IMG}/lp01-hero.png?v={V}" alt="" width="160" height="160" decoding="async"></button>
        <button type="button" class="thumb" aria-label="Resistencia"><img src="{IMG}/lp05-resistencia.png?v={V}" alt="" width="160" height="160" loading="lazy" decoding="async"></button>
      </div>
    </section>"""
g_start = html.index('    <section class="gallery"')
g_end = html.index("    </section>\n\n    <section class=\"product-info\"", g_start) + len("    </section>")
html = html[:g_start] + gallery + html[g_end:]

product_info = f"""    <section class="product-info">
      <p class="product-subtitle">🌧️ Lluvia en Panamá sin arruinar tus zapatos</p>
      <h1 class="product-title">Cubrezapatos impermeables reutilizables — pack de 3 pares</h1>

      <div class="price-row">
        <span class="price-now" id="priceNow">$39</span>
        <span class="price-was" id="priceWas">$49</span>
        <span class="price-save" id="priceSave">Oferta</span>
      </div>

      <ul class="perks">
        <li>💧 Impermeables — lluvia, lodo y salpicaduras</li>
        <li>👟 Se estiran sobre tus zapatos de siempre</li>
        <li>♻️ Enjuaga, seca y vuelve a usar</li>
        <li>🇵🇦 Pago contra entrega en Panamá</li>
      </ul>

      <p class="notice"><strong>🚚 Envío GRATIS · 💵 Pagas al recibir</strong></p>

      <div class="buy-actions">
        <button type="button" class="btn-order js-open-order">Quiero mis 3 pares</button>
        <p class="pay-note">Paga en efectivo cuando recibas tu pedido · Sin pagos por adelantado</p>

        <div class="guarantee-row">
          <div class="guarantee-item">
            <strong>30 días</strong>
            <span>Garantía</span>
          </div>
          <div class="guarantee-item">
            <strong>Envío</strong>
            <span>Gratis</span>
          </div>
          <div class="guarantee-item">
            <strong>COD</strong>
            <span>Panamá</span>
          </div>
        </div>
      </div>

      <div class="collapse-group">
        <div class="collapse">
          <button type="button" class="collapse-btn">¿Qué incluye el pack? <i>+</i></button>
          <div class="collapse-body">3 pares de cubrezapatos impermeables reutilizables (TPE flexible). Ideal para bolso, carro y casa.</div>
        </div>
        <div class="collapse">
          <button type="button" class="collapse-btn">¿Cómo funciona el pago contra entrega? <i>+</i></button>
          <div class="collapse-body">Confirmas tu pedido aquí, te contactamos por WhatsApp y pagas en efectivo al mensajero cuando recibas el producto.</div>
        </div>
      </div>
    </section>"""
pi_start = html.index('    <section class="product-info"')
pi_end = html.index("    </section>\n\n  </div>\n</main>", pi_start) + len("    </section>")
html = html[:pi_start] + product_info + html[pi_end:]

lp_stack = f"""<section class="lp-stack" aria-label="Detalles del producto Cubrezapatos">
  <img src="{IMG}/lp02-problema.png?v={V}" alt="La lluvia puede arruinar tus zapatos favoritos" width="1080" height="1920" loading="lazy" decoding="async">
  <img src="{IMG}/lp03-solucion.png?v={V}" alt="Protege los zapatos que sí te gustan" width="1080" height="1920" loading="lazy" decoding="async">
  <img src="{IMG}/lp04-como-usar.png?v={V}" alt="Cómo usar los cubrezapatos" width="1080" height="1920" loading="lazy" decoding="async">
  <img src="{IMG}/lp05-resistencia.png?v={V}" alt="Resistencia al agua" width="1080" height="1920" loading="lazy" decoding="async">
  <img src="{IMG}/lp06-segundos.png?v={V}" alt="Listos en segundos" width="1080" height="1920" loading="lazy" decoding="async">
  <img src="{IMG}/lp07-repartidor.png?v={V}" alt="Para repartidores y caminatas bajo la lluvia" width="1080" height="1920" loading="lazy" decoding="async">
  <img src="{IMG}/lp08-colegio.png?v={V}" alt="Ideal para colegio y trabajo" width="1080" height="1920" loading="lazy" decoding="async">
  <img src="{IMG}/lp09-usos.png?v={V}" alt="Múltiples usos diarios" width="1080" height="1920" loading="lazy" decoding="async">
  <img src="{IMG}/lp10-dudas.png?v={V}" alt="Respuestas a dudas frecuentes" width="1080" height="1920" loading="lazy" decoding="async">
  <img src="{IMG}/lp11-oferta.png?v={V}" alt="3 pares por $39 USD — pago contra entrega en Panamá" width="1080" height="1920" loading="lazy" decoding="async">
</section>"""
ls_start = html.index('<section class="lp-stack"')
ls_end = html.index("</section>\n\n<div class=\"lp-cta-wrap\"", ls_start) + len("</section>")
html = html[:ls_start] + lp_stack + html[ls_end:]

html = html.replace('class="faq-fastime"', 'class="faq-lp"')

faq = """    <div class="collapse-group">
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Sirven para cualquier zapato? <i>+</i></button>
        <div class="collapse-body">El material TPE es flexible y se adapta a la mayoría de zapatillas y calzado casual. Elige la talla según la guía del empaque.</div>
      </div>
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Cuánto tarda el envío? <i>+</i></button>
        <div class="collapse-body">Enviamos a todo Panamá. Te confirmamos por WhatsApp el tiempo estimado según tu provincia y distrito.</div>
      </div>
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Puedo pedir más de un pack? <i>+</i></button>
        <div class="collapse-body">Sí. En el checkout puedes elegir 3, 6 o 9 pares con mejor precio por par.</div>
      </div>
    </div>"""
fq_start = html.index('<section class="faq-lp"')
fq_body = html.index('<div class="collapse-group">', fq_start)
fq_end = html.index("</div>\n  </div>\n</section>", fq_body) + len("</div>")
html = html[:fq_body] + faq + html[fq_end:]

html = html.replace(
    '<span id="stickyLabel">1 caja de toallitas + 3 pares de guantes GRATIS</span>',
    '<span id="stickyLabel">3 pares impermeables reutilizables</span>',
)

order_product = f"""      <div class="order-product">
        <img src="{IMG}/lp01-hero.png?v={V}" alt="" width="72" height="72" style="width:72px;height:72px;object-fit:cover;border-radius:8px;background:#fff" loading="lazy" decoding="async">
        <div>
          <strong>Cubrezapatos impermeables reutilizables — 3 pares</strong>
          <span>Pack de 3 · Envío gratis · Pago al recibir</span>
        </div>
      </div>"""
op_start = html.index('      <div class="order-product">')
op_end = html.index("      </div>\n      <form id=\"orderForm\"", op_start) + len("      </div>")
html = html[:op_start] + order_product + html[op_end:]

html = html.replace(
    'value="fastime-oil-film-wipes-panama"',
    'value="cubrezapatos-impermeables-panama"',
)

bundles = """        <div class="bundles">
          <label class="bundle bundle-option is-selected">
            <input type="radio" name="bundleOption" value="mf-cubrezapatos-pa-1" data-product-id="mf-cubrezapatos-pa-1" data-product-name="3 pares cubrezapatos impermeables reutilizables" data-price="39" data-old-price="49" data-save="20" data-label="3 pares impermeables reutilizables" checked>
            <div class="bundle-card">
              <span class="bundle-flag">Más pedido</span>
              <div class="bundle-head">
                <span class="bundle-pick"><span class="radio"></span>3 pares cubrezapatos impermeables</span>
                <span class="bundle-cost"><strong>$39</strong><del>$49</del></span>
              </div>
            </div>
          </label>
          <label class="bundle bundle-option">
            <input type="radio" name="bundleOption" value="mf-cubrezapatos-pa-2" data-product-id="mf-cubrezapatos-pa-2" data-product-name="6 pares cubrezapatos impermeables reutilizables" data-price="49" data-old-price="78" data-save="37" data-label="6 pares impermeables reutilizables">
            <div class="bundle-card">
              <span class="bundle-flag">Súper oferta</span>
              <div class="bundle-head">
                <span class="bundle-pick"><span class="radio"></span>6 pares cubrezapatos impermeables</span>
                <span class="bundle-cost"><strong>$49</strong><del>$78</del></span>
              </div>
            </div>
          </label>
          <label class="bundle bundle-option">
            <input type="radio" name="bundleOption" value="mf-cubrezapatos-pa-3" data-product-id="mf-cubrezapatos-pa-3" data-product-name="9 pares cubrezapatos impermeables reutilizables" data-price="59" data-old-price="117" data-save="50" data-label="9 pares impermeables reutilizables">
            <div class="bundle-card">
              <span class="bundle-flag">Mejor valor</span>
              <div class="bundle-head">
                <span class="bundle-pick"><span class="radio"></span>9 pares cubrezapatos impermeables</span>
                <span class="bundle-cost"><strong>$59</strong><del>$117</del></span>
              </div>
            </div>
          </label>
        </div>"""
b_start = html.index('        <div class="bundles">')
b_end = html.index("        </div>\n        <div class=\"form-head\">", b_start) + len("        </div>")
html = html[:b_start] + bundles + html[b_end:]

out = ROOT / "cubrezapatos-impermeables-panama.html"
out.write_text(html, encoding="utf-8")
print("Wrote", out)
