import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / "universal-toilet-seat-bolts-panama.html"
t = p.read_text(encoding="utf-8")
v = "20261022"
img = f"/images/toilet-seat-bolts"

# Remove TikTok pixel block
t = re.sub(r"\s*<meta name=\"tiktok-pixel-id\".*?</script>\s*", "\n", t, count=1, flags=re.S)

head = f"""<!DOCTYPE html>
<html lang="es" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="facebook-domain-verification" content="xbcif1s989l5gi1gu3xogwfta9vg58">
  <title>Tornillos de Expansión Universales para Asiento de Inodoro | MioFertita Panamá — Pago Contra Entrega</title>
  <meta name="description" content="Repara el asiento flojo con tornillos de expansión universales. Oferta 2+2 GRATIS: 4 unidades pagando solo 2. Envío gratis y pago contra entrega en Panamá.">
  <link rel="preload" as="image" href="{img}/hero-bogo.jpg?v={v}" fetchpriority="high">
  <link rel="preload" as="style" href="/css/product.css?v=20260811a">
  <link rel="preload" as="style" href="/css/universal-toilet-seat-bolts.css?v={v}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:wght@400;500;600;700&display=swap" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:wght@400;500;600;700&display=swap"></noscript>
  <link rel="stylesheet" href="/css/product.css?v=20260811a">
  <link rel="stylesheet" href="/css/universal-toilet-seat-bolts.css?v={v}">
  <script src="/js/clarity.js?v=20260928" defer></script>
</head>
<body data-country="PA" data-lang="es" data-brand="miofertita" data-product="toilet-bolts" data-snap-pixel="off" data-abandon-checkout="on" data-abandon-idle-minutes="5" data-thankyou="/thank-you-miofertita-panama.html">
"""

t = re.sub(r"<!DOCTYPE html>.*?</head>\s*<body[^>]*>", head, t, count=1, flags=re.S)

announce = """<div class="announce" aria-hidden="true">
  <div class="announce-track">
    <span>Compra 2 y llévate 2 GRATIS — 4 unidades</span>
    <span>Envío gratis a toda Panamá</span>
    <span>Pago contra entrega</span>
    <span>Asiento firme sin cambiar todo el inodoro</span>
    <span>Compra 2 y llévate 2 GRATIS — 4 unidades</span>
    <span>Envío gratis a toda Panamá</span>
    <span>Pago contra entrega</span>
    <span>Reparación práctica para el hogar</span>
  </div>
</div>"""

t = re.sub(
    r'<div class="announce" aria-hidden="true">\s*<div class="announce-track">[\s\S]*?</div>\s*</div>',
    announce,
    t,
    count=1,
)

t = t.replace("compra<em>confio</em>", "mio<em>fertita</em>")
t = t.replace("CompraConfio", "MioFertita")
t = t.replace("contacto@compraconfio.shop", "contacto@miofertita.shop")
t = t.replace("car-solar-alarm-led", "toilet-seat-bolts")
t = t.replace("car-solar-alarm-led.css", "universal-toilet-seat-bolts.css")
t = t.replace("thank-you-compraconfio-panama", "thank-you-miofertita-panama")
t = t.replace("cc-car-alarm", "mf-toilet-bolts")
t = t.replace("car-solar-alarm-led-panama", "universal-toilet-seat-bolts-panama")

deal = '<div class="deal-strip">Compra 2 y llévate 2 GRATIS · 4 uds · Envío gratis · Pago al recibir · Garantía 30 días</div>'
t = re.sub(r'<div class="deal-strip">[^<]*</div>', deal, t, count=1)

gallery = f"""    <section class="gallery" id="heroSection">
      <div class="gallery-stage" id="galleryTrack">
        <div class="slide">
          <img src="{img}/hero-bogo.jpg?v={v}" alt="Compra 2 y llévate 2 GRATIS — 4 tornillos de expansión universales para asiento de inodoro" width="800" height="800" loading="eager" decoding="async" fetchpriority="high">
        </div>
        <div class="slide">
          <img class="is-contain" src="{img}/benefit-2.jpg?v={v}" alt="Cuatro tornillos de acero inoxidable para fijar el asiento del inodoro" width="800" height="800" loading="lazy" decoding="async">
        </div>
        <div class="slide">
          <img class="is-contain" src="{img}/benefit-3.jpg?v={v}" alt="Reparación del baño — asiento estable sin reemplazar todo el inodoro" width="800" height="800" loading="lazy" decoding="async">
        </div>
      </div>
      <div class="gallery-dots" id="galleryDots" aria-hidden="true"></div>
      <div class="gallery-thumbs">
        <button type="button" class="thumb is-active" aria-label="Oferta 2+2 gratis"><img src="{img}/hero-bogo.jpg?v={v}" alt="" width="160" height="160" decoding="async"></button>
        <button type="button" class="thumb" aria-label="Producto"><img src="{img}/benefit-2.jpg?v={v}" alt="" width="160" height="160" loading="lazy" decoding="async"></button>
        <button type="button" class="thumb" aria-label="En el baño"><img src="{img}/benefit-3.jpg?v={v}" alt="" width="160" height="160" loading="lazy" decoding="async"></button>
      </div>
    </section>"""

t = re.sub(r'<section class="gallery" id="heroSection">[\s\S]*?</section>', gallery, t, count=1)

hero_info = """    <section class="product-info">
      <p class="product-subtitle">🚽 ¡Dile adiós al asiento del inodoro flojo!</p>
      <h1 class="product-title">Tornillos de expansión universales para asiento de inodoro</h1>

      <div class="price-row">
        <span class="price-now" id="priceNow">$29</span>
        <span class="price-was" id="priceWas">$58</span>
        <span class="price-save" id="priceSave">2+2 GRATIS</span>
      </div>

      <p class="hero-lead">Repara tu asiento con tornillos de expansión universales y evita cambiarlo completo cuando solo necesitas reemplazar los fijadores. <strong>Oferta: compra 2 y recibe 2 GRATIS — 4 unidades pagando solo 2.</strong></p>

      <ul class="perks">
        <li>🔩 Ayuda a mantener el asiento firme</li>
        <li>🛠️ Instalación práctica</li>
        <li>💰 Ahorra en reemplazos innecesarios</li>
        <li>🎁 4 unidades · pagas solo 2</li>
      </ul>

      <p class="notice"><strong>🚚 Envío GRATIS · 💵 Pago contra entrega en Panamá</strong></p>

      <div class="buy-actions">
        <button type="button" class="btn-order js-open-order">¡Quiero mi oferta!</button>
        <p class="pay-note">Paga al recibir tu pedido · No pagas nada por adelantado</p>

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
            <strong>Pago</strong>
            <span>Al recibir</span>
          </div>
        </div>
      </div>

      <div class="collapse-group">
        <div class="collapse">
          <button type="button" class="collapse-btn">¿Cómo funciona el pago contra entrega? <i>+</i></button>
          <div class="collapse-body">No pagas nada por adelantado. Recibes tu pedido en casa y pagas en efectivo al mensajero.</div>
        </div>
        <div class="collapse">
          <button type="button" class="collapse-btn">Información de envío <i>+</i></button>
          <div class="collapse-body">Enviamos a todas las provincias de Panamá. Te contactamos por WhatsApp antes de enviar.</div>
        </div>
      </div>
    </section>"""

t = re.sub(r'<section class="product-info">[\s\S]*?</section>\s*\n\s*</div>\s*</main>', hero_info + "\n\n  </div>\n</main>", t, count=1)

story = f"""<section class="story-flow" aria-label="Por qué estos tornillos de expansión">

  <section class="feature story-step">
    <div class="feature-inner">
      <div class="feature-media feature-media--square">
        <img class="story-problem-photo" src="{img}/story-problem.jpg?v={v}" alt="Asiento de inodoro flojo que se mueve de un lado a otro" width="800" height="800" loading="lazy" decoding="async">
      </div>
      <div class="feature-copy">
        <h2>¿Tu asiento del inodoro se mueve constantemente?</h2>
        <p>Los tornillos flojos pueden hacer que el asiento se deslice de un lado a otro y resulte incómodo cada vez que lo usas.</p>
        <p><strong>¡No cambies todo el asiento sin antes revisar una solución más práctica!</strong></p>
      </div>
    </div>
  </section>

  <section class="feature story-step is-reversed">
    <div class="feature-inner">
      <div class="feature-media feature-media--square">
        <img class="story-solution-demo" src="{img}/story-solution.jpg?v={v}" alt="Tornillos de expansión universales instalados — asiento firme" width="800" height="800" loading="lazy" decoding="async">
      </div>
      <div class="feature-copy">
        <h2>¡Recupera la estabilidad de tu asiento!</h2>
        <p>Los tornillos de expansión universales están diseñados para reemplazar los fijadores desgastados y ayudar a mantener el asiento firme cuando el sistema de montaje es compatible.</p>
        <p>🔧 Una reparación práctica para tu hogar, sin reemplazar todo el asiento cuando no es necesario.</p>
        <button type="button" class="text-link js-open-order">Quiero mis 4 unidades</button>
      </div>
    </div>
  </section>

</section>"""

t = re.sub(
    r'<section class="story-flow" aria-label="[^"]*">[\s\S]*?</section>\s*\n\s*<section class="hl-section hl-warm" id="beneficios">',
    story + '\n\n<section class="hl-section hl-warm" id="beneficios">',
    t,
    count=1,
)

benefits_head = """    <div class="mech-head mech-head--solo">
      <h2>Una pequeña reparación que puede hacer la diferencia</h2>
      <p>Beneficios principales</p>
    </div>"""

t = re.sub(
    r'<div class="mech-head mech-head--solo">\s*<h2>Pequeña por fuera[\s\S]*?</div>',
    benefits_head,
    t,
    count=1,
)

benefit_cards = f"""      <button type="button" class="mech-card is-active">
        <img src="{img}/benefit-1.jpg?v={v}" alt="Tornillos firmes — reduce el movimiento del asiento" width="800" height="800" loading="lazy" decoding="async">
        <h3>🔩 Ayuda a mantener el asiento firme</h3>
        <p>Reduce el movimiento causado por fijadores flojos o desgastados.</p>
      </button>
      <button type="button" class="mech-card">
        <img src="{img}/benefit-2.jpg?v={v}" alt="Ahorra dinero reemplazando solo los tornillos" width="800" height="800" loading="lazy" decoding="async">
        <h3>💰 Ahorra dinero</h3>
        <p>Si tu asiento todavía está en buenas condiciones, reemplazar los tornillos puede evitar un gasto innecesario.</p>
      </button>
      <button type="button" class="mech-card">
        <img src="{img}/benefit-3.jpg?v={v}" alt="Instalación práctica en el baño" width="800" height="800" loading="lazy" decoding="async">
        <h3>🛠️ Instalación práctica</h3>
        <p>Sigue unos sencillos pasos para reemplazar los fijadores, siempre que sean compatibles con tu inodoro.</p>
      </button>
      <button type="button" class="mech-card">
        <img src="{img}/benefit-4.jpg?v={v}" alt="Ideal para reparaciones del hogar" width="800" height="800" loading="lazy" decoding="async">
        <h3>🏠 Ideal para reparaciones del hogar</h3>
        <p>Una solución útil para mantener tu baño en buenas condiciones.</p>
      </button>
      <button type="button" class="mech-card">
        <img src="{img}/benefit-5.jpg?v={v}" alt="Oferta compra 2 lleva 2 gratis — 4 unidades" width="800" height="800" loading="lazy" decoding="async">
        <h3>🎁 Oferta 2+2 GRATIS</h3>
        <p>Compra 2 unidades y recibe otras 2 GRATIS. ¡Obtén 4 unidades pagando solo 2!</p>
      </button>"""

t = re.sub(
    r'<div class="mech-track" id="reasonTrack">[\s\S]*?</div>\s*<button type="button" class="mech-arr mech-arr--r"',
    f'<div class="mech-track" id="reasonTrack">\n{benefit_cards}\n      </div>\n      <button type="button" class="mech-arr mech-arr--r"',
    t,
    count=1,
)

howto = f"""      <div class="feature-media feature-media--square">
        <img class="how-to-demo" src="{img}/how-to-demo.jpg?v={v}" alt="Cómo instalar tornillos de expansión en el asiento del inodoro" width="800" height="800" loading="lazy" decoding="async">
      </div>
      <div class="feature-copy">
        <h2>Instálalos en unos sencillos pasos</h2>
        <div class="how-to-steps">
          <article class="how-to-step">
            <h3 class="how-to-step__title"><span class="how-to-step__num">01.</span> Retira los fijadores antiguos</h3>
            <p class="how-to-step__text">Desmonta cuidadosamente los tornillos que sujetan el asiento.</p>
          </article>
          <article class="how-to-step">
            <h3 class="how-to-step__title"><span class="how-to-step__num">02.</span> Limpia los orificios</h3>
            <p class="how-to-step__text">Retira los residuos alrededor de los puntos de montaje.</p>
          </article>
          <article class="how-to-step">
            <h3 class="how-to-step__title"><span class="how-to-step__num">03.</span> Coloca los nuevos tornillos</h3>
            <p class="how-to-step__text">Introduce los anclajes compatibles y coloca los tornillos siguiendo las instrucciones del producto.</p>
          </article>
          <article class="how-to-step">
            <h3 class="how-to-step__title"><span class="how-to-step__num">04.</span> Ajusta y comprueba</h3>
            <p class="how-to-step__text">Aprieta sin excederte y verifica que el asiento quede bien sujeto.</p>
          </article>
        </div>
        <p class="how-to-note"><strong>¡Listo!</strong> Disfruta de una solución práctica para tu asiento flojo. <em>Importante: verifica la compatibilidad con tu inodoro antes de instalar.</em></p>
      </div>"""

t = re.sub(
    r'<div class="feature-inner how-to-inner">[\s\S]*?</div>\s*</div>\s*</section>\s*\n\s*<section class="hl-section hl-warm" id="resenas">',
    f'<div class="feature-inner how-to-inner">\n{howto}\n    </div>\n  </div>\n</section>\n\n<section class="hl-section hl-warm" id="resenas">',
    t,
    count=1,
)

reviews = """    <div class="mech-head mech-head--solo">
      <h2>Una solución práctica para el día a día</h2>
      <p>¿Buscas una manera sencilla de reparar un asiento flojo sin cambiarlo completo?</p>
    </div>

    <div class="review-grid gluta-review-grid">
      <article class="review-card">
        <div class="stars">★★★★★</div>
        <p><strong>“Dejó de moverse el asiento”</strong><br>“Tenía el asiento flojo hace meses. Reemplacé los tornillos y ahora queda firme. Muy práctico y económico.”</p>
        <cite>— Roberto M.</cite>
      </article>
      <article class="review-card">
        <div class="stars">★★★★★</div>
        <p><strong>“Instalación sencilla”</strong><br>“Lo instalé yo mismo en pocos minutos. Verifiqué que fueran compatibles con mi inodoro y listo.”</p>
        <cite>— Carmen L.</cite>
      </article>
      <article class="review-card">
        <div class="stars">★★★★★</div>
        <p><strong>“Buena oferta 2+2”</strong><br>“Pedí la promoción de 4 unidades. Guardé repuestos por si vuelve a pasar en otro baño de la casa.”</p>
        <cite>— Luis A.</cite>
      </article>
    </div>

    <p class="gluta-review-note">Los resultados dependen del tipo de inodoro y del estado del asiento. Verifica compatibilidad antes de instalar.</p>"""

t = re.sub(
    r'<div class="mech-head mech-head--solo">\s*<h2>Experiencias de quienes[\s\S]*?<p class="gluta-review-note">[^<]*</p>',
    reviews,
    t,
    count=1,
)

# Remove review lightbox section and photo reviews if still present
t = re.sub(r'<div class="review-lightbox"[\s\S]*?</div>\s*\n\s*<footer', '<footer', t, count=1)

faq = """    <div class="faq collapse-group">
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Sirven para cualquier inodoro? <i>+</i></button>
        <div class="collapse-body">Están diseñados para sistemas de montaje compatibles. Comprueba las medidas y el tipo de fijación antes de realizar tu pedido.</div>
      </div>
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Tengo que cambiar todo el asiento? <i>+</i></button>
        <div class="collapse-body">No necesariamente. Si el asiento está en buenas condiciones y el problema está en los fijadores, reemplazarlos puede ser suficiente.</div>
      </div>
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Son fáciles de instalar? <i>+</i></button>
        <div class="collapse-body">La instalación puede ser sencilla si el sistema es compatible. Sigue las instrucciones incluidas con el producto.</div>
      </div>
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Qué herramientas necesito? <i>+</i></button>
        <div class="collapse-body">Depende del tipo de fijación. Algunos modelos requieren un destornillador u otra herramienta básica.</div>
      </div>
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Qué incluye la oferta? <i>+</i></button>
        <div class="collapse-body">¡Recibes <strong>4 unidades pagando solo 2</strong>! Compras 2 unidades y obtienes otras 2 GRATIS.</div>
      </div>
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Puedo pagar al recibir? <i>+</i></button>
        <div class="collapse-body">Sí, en Panamá con pago contra entrega. Te confirmamos por WhatsApp antes de enviar.</div>
      </div>
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Cuánto tarda la entrega? <i>+</i></button>
        <div class="collapse-body">El tiempo de entrega depende de tu ubicación. Nuestro equipo te confirmará los detalles de envío al gestionar tu pedido.</div>
      </div>
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Qué hago si los tornillos no son compatibles? <i>+</i></button>
        <div class="collapse-body">Verifica las dimensiones y el sistema de montaje antes de comprar. Si el asiento, las bisagras o los orificios están dañados, es posible que necesites reemplazar otras piezas.</div>
      </div>
    </div>"""

t = re.sub(
    r'<div class="faq collapse-group">[\s\S]*?</div>\s*</div>\s*</section>\s*\n\s*<footer',
    faq + '\n  </div>\n</section>\n\n<footer',
    t,
    count=1,
)

bundles = """        <div class="bundles">
          <label class="bundle bundle-option is-selected">
            <input type="radio" name="bundleOption" value="mf-toilet-bolts-pa-4" data-product-id="mf-toilet-bolts-pa-4" data-product-name="Tornillos expansión asiento inodoro - 4 uds (2+2 GRATIS)" data-price="29" data-old-price="58" data-save="50" data-label="4 uds (2+2)" checked>
            <div class="bundle-card">
              <span class="bundle-flag">Oferta especial</span>
              <div class="bundle-head">
                <span class="bundle-pick"><span class="radio"></span>Compra 2 y llévate 2 GRATIS</span>
                <span class="bundle-cost"><strong>$29</strong><del>$58</del></span>
              </div>
              <div class="bundle-units">
                <span class="unit-chip"><span class="dot alarm"></span>4 unidades · pagas solo 2</span>
              </div>
            </div>
          </label>
          <label class="bundle bundle-option">
            <input type="radio" name="bundleOption" value="mf-toilet-bolts-pa-8" data-product-id="mf-toilet-bolts-pa-8" data-product-name="Tornillos expansión asiento inodoro - 8 uds (4+4)" data-price="49" data-old-price="116" data-save="58" data-label="8 uds (4+4)">
            <div class="bundle-card">
              <span class="bundle-flag">Mejor valor</span>
              <div class="bundle-head">
                <span class="bundle-pick"><span class="radio"></span>8 unidades (4+4)</span>
                <span class="bundle-cost"><strong>$49</strong><del>$116</del></span>
              </div>
              <div class="bundle-units">
                <span class="unit-chip"><span class="dot alarm"></span>Repuestos para varios baños</span>
              </div>
            </div>
          </label>
        </div>"""

t = re.sub(r'<div class="bundles">[\s\S]*?</div>\s*<div class="form-head"><span class="block-label">2\. Tus datos', bundles + '\n        <div class="form-head"><span class="block-label">2. Tus datos', t, count=1)

t = t.replace('<strong id="stickyPrice">$39</strong>', '<strong id="stickyPrice">$29</strong>')
t = t.replace('<span id="stickyLabel">2 unidades (1+1)</span>', '<span id="stickyLabel">4 uds (2+2)</span>')
t = t.replace('id="orderTotal" value="39"', 'id="orderTotal" value="29"')
t = t.replace('<strong id="sumSubtotal">$39</strong>', '<strong id="sumSubtotal">$29</strong>')
t = t.replace('<strong id="sumTotal">$39</strong>', '<strong id="sumTotal">$29</strong>')
t = t.replace('<strong>Luz LED alarma solar para auto</strong>', '<strong>Tornillos de expansión para asiento</strong>')
t = t.replace('<span>30 días Garantía · Pago al recibir</span>', '<span>4 uds · Envío gratis · Pago al recibir</span>')
t = t.replace('data-cost="5"', 'data-cost="2"')
t = t.replace('<span class="ship-cost">$5</span>', '<span class="ship-cost">$2</span>')

order_img = f'<img src="{img}/hero-bogo.jpg?v={v}" alt="" width="72" height="72"'
t = re.sub(r'<img src="/images/toilet-seat-bolts/hero-product[^"]*" alt="" width="72', order_img, t)
t = re.sub(r'<img src="/images/car-solar-alarm-led/hero-product[^"]*" alt="" width="72', order_img, t)

# Remove lightbox init from script if present - keep simple
t = t.replace("/js/config.js?v=20261021a", "/js/config.js?v=20260916b")
t = t.replace("/js/abandoned-checkout.js?v=20261021a", "/js/abandoned-checkout.js?v=20260922e")
t = t.replace("/js/main.js?v=20260918b", "/js/main.js?v=20260924a")

p.write_text(t, encoding="utf-8")
print("Wrote", p)
