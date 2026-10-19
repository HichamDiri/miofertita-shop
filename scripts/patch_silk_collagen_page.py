import re
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "korean-silk-collagen-ampoule-panama.html"
t = p.read_text(encoding="utf-8")
v = "20261019"
img = "/images/silk-collagen-ampoule"

announce = """<div class="announce" aria-hidden="true">
  <div class="announce-track">
    <span>Piel suave y luminosa ✨</span>
    <span>Envío gratis a toda Panamá</span>
    <span>Pago contra entrega</span>
    <span>K-beauty · Absorción rápida</span>
    <span>Piel suave y luminosa ✨</span>
    <span>Envío gratis a toda Panamá</span>
    <span>Pago contra entrega</span>
    <span>Ideal bajo el maquillaje</span>
  </div>
</div>"""

deal = '<div class="deal-strip">Silk Collagen · Péptidos · Envío gratis · Pago al recibir · Garantía 30 días</div>'

gallery = f"""    <section class="gallery" id="heroSection">
      <div class="gallery-stage" id="galleryTrack">
        <div class="slide">
          <img class="is-contain" src="{img}/hero-product.jpg?v={v}" alt="Korean Silk Collagen Ampoule — frasco con hilos de seda visibles" width="800" height="800" loading="eager" decoding="async" fetchpriority="high">
        </div>
        <div class="slide">
          <img class="is-contain" src="{img}/hero-texture.jpg?v={v}" alt="Textura sedosa del sérum con partículas doradas" width="800" height="800" loading="lazy" decoding="async">
        </div>
        <div class="slide">
          <img class="is-contain" src="{img}/hero-application.jpg?v={v}" alt="Aplicación del ampoule sobre piel limpia" width="800" height="800" loading="lazy" decoding="async">
        </div>
      </div>
      <div class="gallery-dots" id="galleryDots" aria-hidden="true"></div>
      <div class="gallery-thumbs">
        <button type="button" class="thumb is-active" aria-label="Producto"><img src="{img}/hero-product.jpg?v={v}" alt="" width="160" height="160" decoding="async"></button>
        <button type="button" class="thumb" aria-label="Textura"><img src="{img}/hero-texture.jpg?v={v}" alt="" width="160" height="160" loading="lazy" decoding="async"></button>
        <button type="button" class="thumb" aria-label="Aplicación"><img src="{img}/hero-application.jpg?v={v}" alt="" width="160" height="160" loading="lazy" decoding="async"></button>
      </div>
    </section>"""

product_info = """    <section class="product-info">
      <p class="product-subtitle">✨ Piel más suave, tersa y luminosa desde el primer día</p>
      <h1 class="product-title">Korean Silk Collagen Ampoule</h1>

      <div class="price-row">
        <span class="price-now" id="priceNow">$32</span>
        <span class="price-was" id="priceWas">$48</span>
        <span class="price-save">Ahorra 33%</span>
      </div>

      <p class="hero-lead">Descubre el secreto de una piel con apariencia más joven, hidratada y sedosa. Sérum concentrado de péptidos con hilos de seda visibles que se disuelven al aplicar. <strong>¡Pide hoy y paga al recibir!</strong></p>

      <ul class="perks">
        <li>✓ Suaviza la apariencia de líneas alrededor de la boca y los ojos</li>
        <li>✓ Despierta con una piel más suave y sedosa</li>
        <li>✓ Textura ligera, rápida absorción</li>
        <li>✓ Perfecta debajo del maquillaje</li>
      </ul>

      <p class="notice"><strong>🚚 Envío GRATIS · 💵 Pago contra entrega en Panamá</strong></p>

      <div class="buy-actions">
        <button type="button" class="btn-order js-open-order">¡Haz tu pedido ahora!</button>
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

t = re.sub(
    r'<div class="announce" aria-hidden="true">\s*<div class="announce-track">[\s\S]*?</div>\s*</div>',
    announce,
    t,
    count=1,
)
t = re.sub(r'<div class="deal-strip">.*?</div>', deal, t, count=1)
t = re.sub(
    r'<section class="gallery" id="heroSection">[\s\S]*?</section>\n\n    <section class="product-info">[\s\S]*?</section>',
    gallery + "\n\n" + product_info,
    t,
    count=1,
)

story = f"""<section class="story-flow" aria-label="Por qué Silk Collagen Ampoule">

  <section class="feature story-step">
    <div class="feature-inner">
      <div class="feature-media feature-media--square">
        <img class="story-problem-photo" src="{img}/story-problem.jpg?v={v}" alt="Mujer observando líneas de expresión en el espejo" width="800" height="800" loading="lazy" decoding="async">
      </div>
      <div class="feature-copy">
        <h2>¿Cansada de ver las mismas líneas cada mañana?</h2>
        <p>Has probado sérums que hidratan y huelen bien, pero las líneas alrededor de la boca, las patas de gallo y las arrugas entre las cejas siguen ahí.</p>
        <p><strong>Tu piel necesita más que una sensación de hidratación.</strong></p>
      </div>
    </div>
  </section>

  <section class="feature story-step is-reversed">
    <div class="feature-inner">
      <div class="feature-media feature-media--square">
        <img src="{img}/story-solution.jpg?v={v}" alt="Silk Collagen Ampoule — sérum con hilos de seda visibles" width="800" height="800" loading="lazy" decoding="async">
      </div>
      <div class="feature-copy">
        <h2>Descubre Silk Collagen Ampoule</h2>
        <p>Sérum concentrado de péptidos, pensado para esas líneas que los sérums comunes no logran suavizar.</p>
        <p>Dentro de cada frasco hay hilos de seda visibles que se disuelven en el sérum a medida que lo aplicas. Textura ligera, absorción rápida y sin sensación pegajosa.</p>
        <button type="button" class="text-link js-open-order">Quiero probarlo</button>
      </div>
    </div>
  </section>

</section>"""
t = re.sub(
    r'<section class="story-flow" aria-label="[^"]*">[\s\S]*?</section>\s*\n<section class="hl-section hl-warm" id="beneficios">',
    story + '\n\n<section class="hl-section hl-warm" id="beneficios">',
    t,
    count=1,
)

benefits = f"""    <div class="mech-head mech-head--solo">
      <h2>Beneficios principales</h2>
      <p>Cuidado facial inspirado en K-beauty</p>
    </div>

    <div class="mech-wrap">
      <button type="button" class="mech-arr mech-arr--l" id="benefitPrev" aria-label="Beneficio anterior">
        <svg width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true"><path d="M12 3L6 9L12 15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>
      </button>
      <div class="mech-track" id="reasonTrack">
      <button type="button" class="mech-card is-active">
        <img src="{img}/benefit-1.jpg?v={v}" alt="Piel suave e hidratada" width="800" height="800" loading="lazy" decoding="async">
        <h3>✨ Líneas más suaves</h3>
        <p>Ayuda a suavizar la apariencia de líneas alrededor de la boca y los ojos.</p>
      </button>
      <button type="button" class="mech-card">
        <img src="{img}/benefit-2.jpg?v={v}" alt="Textura sedosa" width="800" height="800" loading="lazy" decoding="async">
        <h3>🌙 Piel sedosa</h3>
        <p>Despierta con una sensación de piel más suave desde las primeras aplicaciones.</p>
      </button>
      <button type="button" class="mech-card">
        <img src="{img}/benefit-3.jpg?v={v}" alt="Absorción rápida" width="800" height="800" loading="lazy" decoding="async">
        <h3>💧 Absorción rápida</h3>
        <p>Textura ligera, ideal para usar debajo del maquillaje.</p>
      </button>
      <button type="button" class="mech-card">
        <img src="{img}/benefit-4.jpg?v={v}" alt="Piel luminosa" width="800" height="800" loading="lazy" decoding="async">
        <h3>✨ Luminosidad</h3>
        <p>Ayuda a mantener la piel hidratada, tersa y con aspecto más luminoso.</p>
      </button>
      <button type="button" class="mech-card">
        <img src="{img}/benefit-5.jpg?v={v}" alt="Rutina diaria" width="800" height="800" loading="lazy" decoding="async">
        <h3>🌸 Sensación fresca</h3>
        <p>Deja la piel con sensación fresca, suave y revitalizada.</p>
      </button>
      <button type="button" class="mech-card">
        <img src="{img}/benefit-6.jpg?v={v}" alt="Textura uniforme" width="800" height="800" loading="lazy" decoding="async">
        <h3>🪞 Textura uniforme</h3>
        <p>Ayuda a mejorar la apariencia de la textura para un rostro más uniforme.</p>
      </button>
      </div>
      <button type="button" class="mech-arr mech-arr--r" id="benefitNext" aria-label="Beneficio siguiente">
        <svg width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true"><path d="M6 3L12 9L6 15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>
      </button>
    </div>"""
t = re.sub(
    r'<div class="mech-head mech-head--solo">[\s\S]*?</div>\s*\n\s*<div class="mech-wrap">[\s\S]*?</div>\s*\n  </div>\n</section>\s*\n<section class="section how-to-section"',
    benefits + '\n  </div>\n</section>\n\n<section class="section how-to-section"',
    t,
    count=1,
)

howto_block = f"""      <div class="feature-media feature-media--square">
        <img class="how-to-demo" src="{img}/how-to-demo.jpg?v={v}" alt="Cuatro pasos para aplicar Silk Collagen Ampoule" width="800" height="800" loading="lazy" decoding="async">
      </div>
      <div class="feature-copy">
        <h2>Cuatro pasos para una piel suave y luminosa</h2>
        <div class="how-to-steps">
          <article class="how-to-step">
            <h3 class="how-to-step__title"><span class="how-to-step__num">01.</span> Limpia tu rostro</h3>
            <p class="how-to-step__text">Lava tu cara con tu limpiador habitual y seca suavemente.</p>
          </article>
          <article class="how-to-step">
            <h3 class="how-to-step__title"><span class="how-to-step__num">02.</span> Aplica el sérum</h3>
            <p class="how-to-step__text">Distribuye una pequeña cantidad sobre la piel limpia, siguiendo las instrucciones del envase.</p>
          </article>
          <article class="how-to-step">
            <h3 class="how-to-step__title"><span class="how-to-step__num">03.</span> Extiende suavemente</h3>
            <p class="how-to-step__text">Masajea con movimientos delicados hasta distribuir el producto uniformemente.</p>
          </article>
          <article class="how-to-step">
            <h3 class="how-to-step__title"><span class="how-to-step__num">04.</span> Completa tu rutina</h3>
            <p class="how-to-step__text">Aplica tu crema hidratante. Por la mañana, termina con protector solar.</p>
          </article>
        </div>
        <p class="how-to-note"><strong>Consejo:</strong> realiza una prueba en una pequeña zona antes del primer uso.</p>
      </div>"""

ingredients = """
<section class="hl-section hl-warm" id="ingredientes">
  <div class="shell">
    <div class="mech-head mech-head--solo">
      <h2>Cuidado inspirado en la belleza coreana</h2>
    </div>
    <div class="review-grid gluta-review-grid">
      <article class="review-card"><h3 class="review-card__title">Péptidos</h3><p>Ingredientes cosméticos en fórmulas diseñadas para mejorar la apariencia de la piel.</p></article>
      <article class="review-card"><h3 class="review-card__title">Colágeno</h3><p>Ayuda a acondicionar la superficie de la piel y mantener suavidad e hidratación.</p></article>
      <article class="review-card"><h3 class="review-card__title">Extracto de seda</h3><p>Contribuye a una sensación sedosa y al acondicionamiento de la piel.</p></article>
      <article class="review-card"><h3 class="review-card__title">Ácido hialurónico</h3><p>Ayuda a retener agua para una apariencia hidratada y flexible.</p></article>
    </div>
    <p class="gluta-review-note">Confirma la lista de ingredientes en la etiqueta oficial de tu producto antes de usar.</p>
  </div>
</section>
"""

t = re.sub(
    r'<div class="feature-inner how-to-inner">[\s\S]*?</div>\s*\n  </div>\n</section>\s*\n<section class="hl-section hl-warm" id="resenas">',
    '<div class="feature-inner how-to-inner">\n' + howto_block + '\n    </div>\n  </div>\n</section>\n' + ingredients + '\n<section class="hl-section hl-warm" id="resenas">',
    t,
    count=1,
)

reviews = """    <div class="mech-head mech-head--solo">
      <h2>Tu piel merece un cuidado especial ✨</h2>
    </div>

    <div class="review-grid gluta-review-grid">
      <article class="review-card">
        <div class="stars">★★★★★</div>
        <h3 class="review-card__title">“Textura ligera y sedosa”</h3>
        <p>Se absorbe rápido y no deja la piel pegajosa. La uso por la mañana antes del maquillaje y se siente muy cómoda.</p>
        <cite>— Laura M.</cite>
      </article>
      <article class="review-card">
        <div class="stars">★★★★★</div>
        <h3 class="review-card__title">“Me gusta la sensación al despertar”</h3>
        <p>Llevo unas semanas usándolo en mi rutina nocturna y la piel se siente más suave e hidratada.</p>
        <cite>— Carmen S.</cite>
      </article>
      <article class="review-card">
        <div class="stars">★★★★★</div>
        <h3 class="review-card__title">“Los hilos de seda son curiosos”</h3>
        <p>Al aplicarlo se disuelven y dejan una sensación muy agradable. Fácil de incorporar a la rutina diaria.</p>
        <cite>— Patricia R.</cite>
      </article>
    </div>

    <p class="gluta-review-note">Los resultados varían según cada persona y el uso continuado.</p>
    <p class="notice notice--center"><strong>🚚 Envío GRATIS · 💵 Pago contra entrega</strong></p>
    <div class="section-cta">
      <button type="button" class="btn-order js-open-order">¡Haz tu pedido ahora!</button>
    </div>"""
t = re.sub(
    r'<div class="mech-head mech-head--solo">\s*<h2>Experiencias[\s\S]*?<div class="section-cta">[\s\S]*?</div>',
    reviews,
    t,
    count=1,
)

faq = """    <h2 class="section-title">❓ Preguntas frecuentes</h2>
    <div class="faq collapse-group">
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Para qué sirve Silk Collagen Ampoule? <i>+</i></button>
        <div class="collapse-body">Es un sérum cosmético diseñado para hidratar la piel, mejorar su suavidad y favorecer una apariencia más luminosa.</div>
      </div>
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Ayuda a suavizar las líneas de expresión? <i>+</i></button>
        <div class="collapse-body">Puede ayudar a que algunas líneas finas relacionadas con la sequedad sean menos visibles gracias a la hidratación. Los resultados varían según cada persona.</div>
      </div>
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Puedo notar resultados desde el primer día? <i>+</i></button>
        <div class="collapse-body">La sensación de suavidad e hidratación puede notarse desde las primeras aplicaciones. Los cambios en la apariencia dependen del uso continuado.</div>
      </div>
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Deja la piel pegajosa? <i>+</i></button>
        <div class="collapse-body">Su textura es ligera y de rápida absorción. La experiencia puede variar según la cantidad aplicada y tu tipo de piel.</div>
      </div>
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Puedo usarlo debajo del maquillaje? <i>+</i></button>
        <div class="collapse-body">Sí. Deja que el sérum se absorba por completo antes de aplicar el maquillaje.</div>
      </div>
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Es adecuado para todo tipo de piel? <i>+</i></button>
        <div class="collapse-body">Revisa los ingredientes y realiza una prueba en una pequeña zona antes del uso regular.</div>
      </div>
      <div class="collapse">
        <button type="button" class="collapse-btn">¿Cómo realizo mi pedido? <i>+</i></button>
        <div class="collapse-body">Completa el formulario con tus datos y dirección. Pagas en efectivo al recibir, según cobertura en tu zona.</div>
      </div>
    </div>"""
t = re.sub(
    r'<h2 class="section-title">❓ Preguntas frecuentes</h2>[\s\S]*?</div>\s*\n  </div>\n</section>\s*\n<div class="review-lightbox"',
    faq + '\n  </div>\n</section>\n\n<footer',
    t,
    count=1,
)
if '<div class="review-lightbox"' in t:
    t = re.sub(r'<div class="review-lightbox"[\s\S]*?</div>\s*\n\n<footer', '<footer', t, count=1)

bundles = """        <div class="bundles">
          <label class="bundle bundle-option is-selected">
            <input type="radio" name="bundleOption" value="mf-silk-collagen-pa-1" data-product-id="mf-silk-collagen-pa-1" data-product-name="Korean Silk Collagen Ampoule - 1 unidad" data-price="32" data-old-price="48" data-save="33" data-label="1 ampoule" checked>
            <div class="bundle-card">
              <div class="bundle-head">
                <span class="bundle-pick"><span class="radio"></span>1 ampoule (40 mL)</span>
                <span class="bundle-cost"><strong>$32</strong><del>$48</del></span>
              </div>
            </div>
          </label>
          <label class="bundle bundle-option">
            <input type="radio" name="bundleOption" value="mf-silk-collagen-pa-2" data-product-id="mf-silk-collagen-pa-2" data-product-name="Korean Silk Collagen Ampoule - 2 unidades" data-price="54" data-old-price="96" data-save="44" data-label="2 ampoules">
            <div class="bundle-card">
              <span class="bundle-flag">Más popular</span>
              <div class="bundle-head">
                <span class="bundle-pick"><span class="radio"></span>2 ampoules</span>
                <span class="bundle-cost"><strong>$54</strong><del>$96</del></span>
              </div>
            </div>
          </label>
          <label class="bundle bundle-option">
            <input type="radio" name="bundleOption" value="mf-silk-collagen-pa-3" data-product-id="mf-silk-collagen-pa-3" data-product-name="Korean Silk Collagen Ampoule - 3 unidades" data-price="72" data-old-price="144" data-save="50" data-label="3 ampoules">
            <div class="bundle-card">
              <span class="bundle-flag">Mejor valor</span>
              <div class="bundle-head">
                <span class="bundle-pick"><span class="radio"></span>3 ampoules</span>
                <span class="bundle-cost"><strong>$72</strong><del>$144</del></span>
              </div>
            </div>
          </label>
        </div>"""
t = re.sub(r'<div class="bundles">[\s\S]*?</div>\s*\n        <div class="form-head">', bundles + '\n        <div class="form-head">', t, count=1)
t = re.sub(
    r'<input type="hidden" name="source" value="[^"]*">',
    '<input type="hidden" name="source" value="korean-silk-collagen-ampoule-panama">',
    t,
    count=1,
)
t = t.replace('Luz LED alarma solar para auto', 'Korean Silk Collagen Ampoule')
t = t.replace('id="orderTotal" value="39"', 'id="orderTotal" value="32"')
t = t.replace('<strong id="stickyPrice">$39</strong>', '<strong id="stickyPrice">$32</strong>')
t = t.replace('<span id="stickyLabel">2 unidades (1+1)</span>', '<span id="stickyLabel">1 ampoule</span>')
t = t.replace('<strong id="sumSubtotal">$39</strong>', '<strong id="sumSubtotal">$32</strong>')
t = t.replace('<strong id="sumTotal">$39</strong>', '<strong id="sumTotal">$32</strong>')

t = re.sub(
    r"\n  var lightbox = document.getElementById\('reviewLightbox'\);[\s\S]*?lightboxNext\.addEventListener\('click', function \(\) \{ showLightboxPhoto\(lightboxIndex \+ 1\); \}\);\n  \}\n",
    "\n",
    t,
    count=1,
)

p.write_text(t, encoding="utf-8")
print("patched ok", p.stat().st_size)
