<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>La Red del D20 — Únete a la alianza</title>
<meta name="description" content="La alianza de servidores de rol en Discord. Compartimos jugadores, eventos y recursos sin perder autonomía. Tu servidor sigue siendo tuyo al 100%.">
<meta property="og:title" content="La Red del D20 — Alianza de servidores de rol">
<meta property="og:description" content="La alianza de servidores de rol en Discord. Compartimos jugadores, eventos y recursos sin perder autonomía. Tu servidor sigue siendo tuyo al 100%.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://hoshimorirol.github.io/la-red-del-d20/">
<meta property="og:color" content="#5865F2">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🎲%3C/text%3E%3C/svg%3E">
<style>
  :root {
    --discord: #5865F2;
    --discord-dark: #4752C4;
    --bg: #1e1f22;
    --bg-2: #2b2d31;
    --bg-3: #313338;
    --text: #f2f3f5;
    --text-2: #b5bac1;
    --text-3: #949ba4;
    --success: #57F287;
    --success-bg: rgba(87,242,135,0.08);
    --warning: #FEE75C;
    --warning-bg: rgba(254,231,92,0.08);
    --danger: #ED4245;
    --danger-bg: rgba(237,66,69,0.08);
    --info: #5865F2;
    --info-bg: rgba(88,101,242,0.08);
    --radius: 16px;
    --radius-sm: 10px;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    min-height: 100vh;
  }

  .container {
    max-width: 780px;
    margin: 0 auto;
    padding: 24px 16px 48px;
  }

  /* Hero */
  .hero {
    text-align: center;
    padding: 40px 0 32px;
    border-bottom: 1px solid var(--bg-2);
    margin-bottom: 28px;
  }

  .hero-emoji {
    font-size: 56px;
    display: inline-block;
    animation: bounce 2s ease-in-out infinite;
    margin-bottom: 12px;
  }

  @keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
  }

  .hero-title {
    font-size: 36px;
    font-weight: 800;
    letter-spacing: -0.5px;
    background: linear-gradient(135deg, var(--discord) 0%, #a5b4fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 8px;
  }

  .hero-sub {
    font-size: 17px;
    color: var(--text-2);
    font-weight: 400;
    max-width: 500px;
    margin: 0 auto;
    line-height: 1.5;
  }

  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--success-bg);
    color: var(--success);
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    margin-top: 16px;
    border: 1px solid rgba(87,242,135,0.15);
  }

  /* Tabs */
  .tabs {
    display: flex;
    gap: 6px;
    margin-bottom: 28px;
    background: var(--bg-2);
    padding: 6px;
    border-radius: var(--radius);
    overflow-x: auto;
    scrollbar-width: thin;
    scrollbar-color: var(--discord) transparent;
    -webkit-overflow-scrolling: touch;
    position: relative;
  }

  .tabs::-webkit-scrollbar {
    height: 4px;
    display: block;
  }
  .tabs::-webkit-scrollbar-track {
    background: transparent;
    border-radius: 2px;
  }
  .tabs::-webkit-scrollbar-thumb {
    background: var(--discord);
    border-radius: 2px;
    opacity: 0.5;
  }

  .tab {
    flex: 0 0 auto;
    min-width: 100px;
    max-width: 160px;
    padding: 10px 16px;
    border: none;
    border-radius: var(--radius-sm);
    background: transparent;
    color: var(--text-2);
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    white-space: nowrap;
    font-family: inherit;
    text-align: center;
    position: relative;
    overflow: hidden;
  }

  .tab::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    width: 0;
    height: 2px;
    background: var(--discord);
    transition: all 0.25s;
    transform: translateX(-50%);
    border-radius: 2px;
  }

  .tab:hover {
    color: var(--text);
    background: rgba(255,255,255,0.04);
  }
  .tab:hover::after {
    width: 40%;
  }
  .tab.active {
    background: var(--bg-3);
    color: var(--text);
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  }
  .tab.active::after {
    width: 60%;
    background: var(--discord);
  }

  .panel { display: none; animation: fadeIn 0.3s ease; }
  .panel.active { display: block; }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* Cards */
  .card {
    background: var(--bg-2);
    border: 1px solid rgba(255,255,255,0.04);
    border-radius: var(--radius);
    padding: 22px;
    margin-bottom: 18px;
  }

  .card-accent {
    border-left: 3px solid var(--discord);
  }

  .card-success { border-left: 3px solid var(--success); }
  .card-warning { border-left: 3px solid var(--warning); }

  .section-title {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    color: var(--text-3);
    margin-bottom: 14px;
    font-weight: 700;
  }

  .pitch-text {
    font-size: 16px;
    line-height: 1.7;
    color: var(--text-2);
  }

  .pitch-text strong { color: var(--text); }

  /* Features grid */
  .features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 14px;
    margin-bottom: 18px;
  }

  .feature {
    background: var(--bg-3);
    border-radius: var(--radius-sm);
    padding: 20px;
    border: 1px solid rgba(255,255,255,0.04);
    transition: all 0.25s;
    cursor: default;
  }

  .feature:hover {
    transform: translateY(-3px);
    border-color: rgba(88,101,242,0.25);
    box-shadow: 0 4px 16px rgba(0,0,0,0.2);
  }

  .feature-emoji { font-size: 32px; margin-bottom: 12px; display: block; }
  .feature-title { font-size: 15px; font-weight: 700; margin-bottom: 8px; color: var(--text); }
  .feature-desc { font-size: 13px; color: var(--text-2); line-height: 1.6; }

  /* How it works */
  .how-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 14px;
    margin-bottom: 18px;
  }

  .how-card {
    background: var(--bg-3);
    border-radius: var(--radius-sm);
    padding: 18px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.04);
  }

  .how-num {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: var(--discord);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    font-weight: 800;
    margin: 0 auto 12px;
  }

  .how-title { font-size: 14px; font-weight: 700; color: var(--text); margin-bottom: 6px; }
  .how-desc { font-size: 12px; color: var(--text-2); line-height: 1.5; }

  /* Benefits */
  .benefit-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 18px;
  }

  .benefit-card {
    background: var(--bg-3);
    border-radius: var(--radius-sm);
    padding: 18px;
    border: 1px solid rgba(255,255,255,0.04);
  }

  .benefit-card h3 {
    font-size: 14px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .benefit-card ul {
    list-style: none;
    font-size: 13px;
    color: var(--text-2);
    line-height: 1.8;
  }

  .benefit-card ul li::before {
    content: "✦";
    color: var(--discord);
    margin-right: 8px;
    font-weight: 700;
  }

  /* Checklist */
  .checklist { list-style: none; }
  .checklist li {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 10px 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    font-size: 14px;
    color: var(--text-2);
  }
  .checklist li:last-child { border-bottom: none; }
  .check-yes { color: var(--success); font-weight: 700; flex-shrink: 0; font-size: 16px; }
  .check-no { color: var(--danger); font-weight: 700; flex-shrink: 0; font-size: 16px; }

  /* FAQ */
  .faq-item {
    background: var(--bg-3);
    border-radius: var(--radius-sm);
    margin-bottom: 10px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.04);
  }

  .faq-q {
    padding: 14px 18px;
    font-size: 14px;
    font-weight: 600;
    color: var(--text);
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: background 0.2s;
  }

  .faq-q:hover { background: rgba(255,255,255,0.02); }
  .faq-q::after { content: "+"; font-size: 18px; color: var(--text-3); transition: transform 0.2s; }
  .faq-item.open .faq-q::after { transform: rotate(45deg); }

  .faq-a {
    padding: 0 18px;
    max-height: 0;
    overflow: hidden;
    transition: all 0.3s ease;
    font-size: 13px;
    color: var(--text-2);
    line-height: 1.6;
  }

  .faq-item.open .faq-a {
    padding: 0 18px 14px;
    max-height: 300px;
  }

  /* CTA */
  .cta-hero {
    background: linear-gradient(135deg, var(--discord) 0%, var(--discord-dark) 100%);
    border-radius: var(--radius);
    padding: 32px 24px;
    text-align: center;
    margin-top: 28px;
  }

  .cta-hero h2 {
    font-size: 22px;
    font-weight: 800;
    color: white;
    margin-bottom: 10px;
  }

  .cta-hero p {
    font-size: 15px;
    color: rgba(255,255,255,0.85);
    margin-bottom: 20px;
    line-height: 1.5;
  }

  .cta-btn {
    background: white;
    color: var(--discord);
    border: none;
    padding: 12px 28px;
    border-radius: var(--radius-sm);
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
    font-family: inherit;
    display: inline-block;
    text-decoration: none;
  }

  .cta-btn:hover { transform: translateY(-2px); box-shadow: 0 4px 16px rgba(0,0,0,0.3); }

  .cta-btns {
    display: flex;
    gap: 10px;
    justify-content: center;
    flex-wrap: wrap;
  }

  .cta-btn-outline {
    background: rgba(255,255,255,0.12);
    color: white;
    border: 1px solid rgba(255,255,255,0.2);
  }

  .cta-btn-outline:hover { background: rgba(255,255,255,0.2); }

  /* Lema */
  .lema {
    text-align: center;
    font-size: 15px;
    color: var(--text-3);
    font-style: italic;
    margin: 24px 0;
    padding: 18px;
    border-top: 1px solid var(--bg-2);
    border-bottom: 1px solid var(--bg-2);
  }

  /* Notice */
  .notice {
    background: var(--info-bg);
    border: 1px solid rgba(88,101,242,0.2);
    border-radius: var(--radius-sm);
    padding: 14px 18px;
    font-size: 13px;
    color: #a5b4fc;
    margin-bottom: 18px;
    line-height: 1.6;
  }

  .notice strong { color: #c7d2fe; }

  /* Tag */
  .tag {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 999px;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.04em;
    margin-right: 6px;
  }
  .tag-must { background: var(--danger-bg); color: var(--danger); }
  .tag-opt { background: rgba(255,255,255,0.06); color: var(--text-3); border: 1px solid rgba(255,255,255,0.08); }

  /* Responsive */
  @media (max-width: 600px) {
    .benefit-row { grid-template-columns: 1fr; }
    .hero-title { font-size: 28px; }
    .hero-sub { font-size: 15px; }
  }

/* === NIVELES DE ALERTA === */
.levels {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  margin-bottom: 16px;
}

.level {
  border-radius: var(--radius-sm);
  padding: 16px;
  font-size: 12px;
}

.level-verde {
  background: var(--success-bg);
  border: 1px solid rgba(87,242,135,0.15);
}
.level-verde .l-name { color: var(--success); }
.level-verde .l-items { color: #a5f5c0; }

.level-amarillo {
  background: var(--warning-bg);
  border: 1px solid rgba(254,231,92,0.15);
}
.level-amarillo .l-name { color: var(--warning); }
.level-amarillo .l-items { color: #f5eaa5; }

.level-rojo {
  background: var(--danger-bg);
  border: 1px solid rgba(237,66,69,0.15);
}
.level-rojo .l-name { color: var(--danger); }
.level-rojo .l-items { color: #f5a5a5; }

.l-name {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 8px;
}

.l-items {
  list-style: none;
  line-height: 1.8;
}

.l-action {
  font-size: 10px;
  margin-top: 10px;
  padding-top: 10px;
  border-top: 1px solid rgba(255,255,255,0.08);
  opacity: 0.8;
}

/* === FLUJO DE REPORTE === */
.flow-step {
  display: flex;
  gap: 14px;
  margin-bottom: 14px;
}

.flow-num {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--bg-3);
  border: 1px solid rgba(255,255,255,0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
  color: var(--text-3);
  flex-shrink: 0;
}

.flow-body { flex: 1; padding-top: 2px; }
.flow-title { font-size: 14px; font-weight: 700; color: var(--text); margin-bottom: 4px; }
.flow-desc { font-size: 13px; color: var(--text-2); line-height: 1.6; }

</style>
</head>
<body>

<div class="container">

  <div class="hero">
    <div class="hero-emoji">🎲</div>
    <div class="hero-title">La Red del D20</div>
    <div class="hero-sub">La alianza de servidores de rol donde tu comunidad crece sin perder su esencia</div>
    <div class="hero-badge">
      <span>🌐</span> Abierta a nuevos miembros
    </div>
  </div>

  <div class="tabs" role="tablist">
    <button class="tab active" onclick="switchTab('que')" role="tab">💡 ¿Qué es?</button>
    <button class="tab" onclick="switchTab('funciona')" role="tab">⚙️ ¿Cómo funciona?</button>
    <button class="tab" onclick="switchTab('beneficios')" role="tab">🎁 Beneficios</button>
    <button class="tab" onclick="switchTab('seguridad')" role="tab">🛡️ Seguridad</button>
    <button class="tab" onclick="switchTab('unirse')" role="tab">🚀 ¿Cómo unirse?</button>
    <button class="tab" onclick="switchTab('faq')" role="tab">❓ FAQ</button>
  </div>

  <!-- PANEL: ¿QUÉ ES? -->
  <div id="tab-que" class="panel active">
    <div class="section-title">La idea en simple</div>
    <div class="card card-accent">
      <p class="pitch-text">
        ¿Te ha pasado que tu servidor de rol nace con mucha ilusión pero se queda sin gente? ¿O que una campaña genial termina y los jugadores se dispersan? <strong>Eso pasa porque los servidores están aislados</strong>.
        <br><br>
        <strong>La Red del D20</strong> es una alianza de comunidades de rol en Discord. No somos un megaservidor que absorbe a los demás. Somos una red donde cada servidor sigue siendo independiente, pero se apoya en los demás.
        <br><br>
        Compartimos jugadores, organizamos eventos juntos, intercambiamos recursos y nos avisamos cuando algo va mal. <strong>Tu servidor sigue siendo tuyo al 100%</strong>. Solo dejas de estar solo.
      </p>
    </div>

    <div class="section-title">Los tres pilares</div>
    <div class="features">
      <div class="feature">
        <span class="feature-emoji">🤝</span>
        <div class="feature-title">Gente que fluye</div>
        <div class="feature-desc">Un directorio donde los jugadores descubren tu servidor. Cuando una mesa cierra, tus jugadores tienen dónde ir sin perderse en el vacío.</div>
      </div>
      <div class="feature">
        <span class="feature-emoji">🛡️</span>
        <div class="feature-title">Cuidarse entre todos</div>
        <div class="feature-desc">Los mods de cada servidor comparten alertas privadas sobre conductas graves. Sin listas públicas, sin linchamientos. Solo nos avisamos entre nosotros.</div>
      </div>
      <div class="feature">
        <span class="feature-emoji">📚</span>
        <div class="feature-title">Recursos compartidos</div>
        <div class="feature-desc">Plantillas para DMs, guías de moderación, bots, mapas, playlists para sesiones... ¿Tienes algo útil? Lo compartes. ¿Necesitas algo? Lo encuentras.</div>
      </div>
    </div>

    <div class="lema">— "Nadie es dueño de tu mesa, pero todos ponemos las sillas." —</div>

    <div class="section-title">Lo que NO somos</div>
    <div class="card">
      <ul class="checklist">
        <li><span class="check-no">✕</span> No gobernamos tu servidor: tu lore, reglas, moderación y estilo son completamente tuyos</li>
        <li><span class="check-no">✕</span> No cobramos cuotas, no hay pagos ni obligaciones de actividad mínima</li>
        <li><span class="check-no">✕</span> No imponemos sistema de juego: juegas D&D, Pathfinder, Vampiro o lo que quieras</li>
        <li><span class="check-no">✕</span> No decidimos qué contenido permites: ERP, lore oscuro, reglas de casa... eso va por tu cuenta</li>
        <li><span class="check-no">✕</span> No te obligamos a eventos: participas cuando quieras y puedas</li>
      </ul>
    </div>
  </div>

  <!-- PANEL: ¿CÓMO FUNCIONA? -->
  <div id="tab-funciona" class="panel">
    <div class="section-title">Así de sencillo</div>
    <div class="how-grid">
      <div class="how-card">
        <div class="how-num">1</div>
        <div class="how-title">Tu servidor entra</div>
        <div class="how-desc">Aplicas, revisamos que cumplas lo básico (reglas contra acoso, canal de reportes) y te damos la bienvenida.</div>
      </div>
      <div class="how-card">
        <div class="how-num">2</div>
        <div class="how-title">Canal de alianzas</div>
        <div class="how-desc">En tu servidor creas un canal #alianzas donde aparecen todos los miembros de la red. Tus jugadores descubren otros servidores desde ahí.</div>
      </div>
      <div class="how-card">
        <div class="how-num">3</div>
        <div class="how-title">Hub privado para mods</div>
        <div class="how-desc">Los moderadores de cada servidor tienen acceso a un servidor privado de coordinación. Ahí compartimos alertas, recursos y organizamos eventos.</div>
      </div>
      <div class="how-card">
        <div class="how-num">4</div>
        <div class="how-title">Todo fluye solo</div>
        <div class="how-desc">Eventos cruzados, jugadores que migran sanamente, recursos compartidos... la red funciona sin que tú tengas que hacer trabajo extra.</div>
      </div>
    </div>

    <div class="notice">
      <strong>Importante:</strong> La Red <strong>no es un consejo supremo</strong>. Es una mesa redonda donde cada servidor tiene voz igual. Ninguna decisión afecta lo que haces dentro de tu propio servidor.
    </div>

    <div class="section-title">Cómo nos organizamos (lo light)</div>
    <div class="card">
      <ul class="checklist">
        <li><span class="check-yes">✓</span> <strong>Mesa de Representantes:</strong> 1 rep por servidor. Votan cambios de normas y admiten nuevos miembros</li>
        <li><span class="check-yes">✓</span> <strong>Comité de Revisión:</strong> 3 mods de servidores distintos revisan casos de seguridad graves. Deciden por mayoría y se puede apelar</li>
        <li><span class="check-yes">✓</span> <strong>Admin del Hub:</strong> Quien gestiona el servidor privado técnicamente. No tiene poder de voto extra, solo mantiene las luces encendidas</li>
      </ul>
    </div>

    <div class="section-title">Rangos de servidor</div>
    <div class="features">
      <div class="feature">
        <span class="feature-emoji">🌱</span>
        <div class="feature-title">Nuevo</div>
        <div class="feature-desc">Primer mes. Evaluación en curso. Acceso básico a la red.</div>
      </div>
      <div class="feature">
        <span class="feature-emoji">🤝</span>
        <div class="feature-title">Socio</div>
        <div class="feature-desc">Cumple la carta base. Acceso completo al directorio, eventos y recursos compartidos.</div>
      </div>
      <div class="feature">
        <span class="feature-emoji">✅</span>
        <div class="feature-title">Verificado</div>
        <div class="feature-desc">3+ meses sin incidentes, moderación activa. Acceso al registro de alertas y prioridad en el directorio.</div>
      </div>
    </div>
  </div>

  <!-- PANEL: BENEFICIOS -->
  <div id="tab-beneficios" class="panel">
    <div class="section-title">¿Qué ganas tú?</div>
    <div class="benefit-row">
      <div class="benefit-card">
        <h3><span>👤</span> Si eres jugador</h3>
        <ul>
          <li>Descubres servidores de rol de confianza en un solo lugar, con estilos y universos distintos al tuyo</li>
          <li>Exploras mundos que no conocías: cyberpunk, horror cósmico, fantasía épica, steampunk, space opera...</li>
          <li>Cuando tu mesa termina, tienes dónde ir sin empezar de cero: otros universos te esperan</li>
          <li>Eventos cruzados: one-shots abiertos y torneos narrativos donde conoces gente de otras comunidades</li>
          <li>Conoces DMs con estilos distintos: desde lo narrativo puro hasta lo táctico más exigente</li>
          <li>La red te filtra servidores verificados: entras sabiendo que hay moderación activa</li>
        </ul>
      </div>
      <div class="benefit-card">
        <h3><span>⚔️</span> Si eres admin o DM</h3>
        <ul>
          <li>Más jugadores descubren tu servidor sin spam ni publicidad invasiva</li>
          <li>Cuando una campaña cierra, tus jugadores no se evaporan</li>
          <li>Alertas entre mods sobre usuarios problemáticos antes de que lleguen a ti</li>
          <li>Biblioteca de recursos compartidos: bots, mapas, plantillas de campaña</li>
          <li>Mentoría entre admins: los experimentados ayudan a los nuevos</li>
          <li>DMs invitados: directores de otros servidores pueden dirigir one-shots en el tuyo</li>
          <li>Insignia verificada que da confianza a los nuevos jugadores</li>
        </ul>
      </div>
    </div>

    <div class="section-title">Eventos que ya estamos pensando</div>
    <div class="features">
      <div class="feature">
        <span class="feature-emoji">🎃</span>
        <div class="feature-title">Eventos de Temporada</div>
        <div class="feature-desc">Halloween, Navidad, verano, San Valentín... varios servidores colaboran para montar eventos especiales. Cada uno aporta su estilo: uno el one-shot, otro el concurso de lore, otro la trivia de rol. Colaboración real entre alianzas.</div>
      </div>
      <div class="feature">
        <span class="feature-emoji">🏆</span>
        <div class="feature-title">Torneo narrativo</div>
        <div class="feature-desc">Competición amistosa de storytelling entre servidores. Jurado rotativo, mucha diversión y la oportunidad de ver cómo narran en otras comunidades.</div>
      </div>
      <div class="feature">
        <span class="feature-emoji">🌌</span>
        <div class="feature-title">Muestra de universos</div>
        <div class="feature-desc">Cada servidor presenta su mundo, su lore y su estilo en sesiones abiertas de 30 minutos. Como un festival de cine, pero de mundos de rol. Descubres dónde quieres jugar sin invertir horas.</div>
      </div>
      <div class="feature">
        <span class="feature-emoji">🎙️</span>
        <div class="feature-title">Escenarios Cruzados</div>
        <div class="feature-desc">Usamos los Escenarios (Stage Channels) de Discord para sesiones en vivo: DMs narran aventuras en directo, mesas redondas de directores, presentaciones de mundos, lecturas dramatizadas... todo dentro de Discord, sin salir de la app.</div>
      </div>
      <div class="feature">
        <span class="feature-emoji">🧙</span>
        <div class="feature-title">DMs invitados</div>
        <div class="feature-desc">Directores de otros servidores visitan el tuyo para dirigir one-shots especiales. Tus jugadores prueban un estilo nuevo sin salir de casa.</div>
      </div>
      <div class="feature">
        <span class="feature-emoji">📜</span>
        <div class="feature-title">Aventuras de Préstamo</div>
        <div class="feature-desc">DMs crean one-shots y los comparten en la biblioteca de la red. Otro DM de otro servidor puede dirigir esa aventura en su mesa, adaptándola a su mundo. Recetas listas para cocinar en cualquier cocina.</div>
      </div>
    </div>
  </div>

  
  <!-- PANEL: SEGURIDAD -->
  <div id="tab-seguridad" class="panel">
    <div class="section-title">Cómo funciona por dentro</div>
    <div class="card">
      <div class="how-grid" style="grid-template-columns: 1fr;">
        <div class="how-card" style="text-align:left; display:flex; gap:14px; align-items:flex-start;">
          <div class="how-num" style="margin:0; flex-shrink:0;">1</div>
          <div>
            <div class="how-title">Cada servidor tiene su canal #alianzas</div>
            <div class="how-desc">Es un canal público en tu servidor donde se muestra el directorio de todos los miembros de la red. Tus jugadores descubren otros servidores desde ahí. Es como una vitrina compartida.</div>
          </div>
        </div>
        <div class="how-card" style="text-align:left; display:flex; gap:14px; align-items:flex-start;">
          <div class="how-num" style="margin:0; flex-shrink:0;">2</div>
          <div>
            <div class="how-title">Los mods comparten un hub privado</div>
            <div class="how-desc">Es un servidor de Discord exclusivo para moderadores. Ahí se coordinan eventos, se comparten recursos y se gestionan las alertas de seguridad. Los jugadores normales no tienen acceso.</div>
          </div>
        </div>
        <div class="how-card" style="text-align:left; display:flex; gap:14px; align-items:flex-start;">
          <div class="how-num" style="margin:0; flex-shrink:0;">3</div>
          <div>
            <div class="how-title">Las decisiones se toman en la Mesa</div>
            <div class="how-desc">Cada servidor manda un representante a la Mesa de Representantes. Ahí se votan cambios de normas y se admiten nuevos miembros. Una persona, un voto. Nadie manda sobre nadie.</div>
          </div>
        </div>
        <div class="how-card" style="text-align:left; display:flex; gap:14px; align-items:flex-start;">
          <div class="how-num" style="margin:0; flex-shrink:0;">4</div>
          <div>
            <div class="how-title">El Comité revisa lo grave</div>
            <div class="how-desc">Si surge un caso de seguridad serio, 3 mods de servidores distintos lo revisan. Deciden por mayoría. El afectado puede apelar. Todo queda documentado con nombres y fechas.</div>
          </div>
        </div>
      </div>
    </div>

    <div class="section-title">Niveles de alerta</div>
    <div class="levels">
      <div class="level level-verde">
        <div class="l-name">🟢 Leve</div>
        <ul class="l-items">
          <li>• Spam / inmadurez</li>
          <li>• Ghosteo recurrente</li>
          <li>• Drama de mesa</li>
          <li>• Metagaming excesivo</li>
        </ul>
        <div class="l-action">Solo registro interno del servidor. Sin alerta compartida en la red</div>
      </div>
      <div class="level level-amarillo">
        <div class="l-name">🟡 Grave</div>
        <ul class="l-items">
          <li>• Acoso persistente</li>
          <li>• Evasión de bans</li>
          <li>• Manipulación emocional</li>
          <li>• Hostigamiento sexual</li>
        </ul>
        <div class="l-action">Evidencia + Comité de Revisión. Puede generar monitoreo activo entre servidores</div>
      </div>
      <div class="level level-rojo">
        <div class="l-name">🔴 Crítico</div>
        <ul class="l-items">
          <li>• Grooming</li>
          <li>• Doxxeo / amenazas</li>
          <li>• Raids coordinados</li>
          <li>• Explotación de menores</li>
        </ul>
        <div class="l-action">Alerta inmediata en el hub privado + ban preventivo recomendado en toda la red</div>
      </div>
    </div>

    <div class="section-title">Flujo de un reporte de seguridad</div>
    <div class="card">
      <div class="flow-step">
        <div class="flow-num">1</div>
        <div class="flow-body">
          <div class="flow-title">Un mod de tu servidor detecta el problema</div>
          <div class="flow-desc">Recopila evidencia: capturas de pantalla, logs, contexto. Clasifica el nivel que cree correspondiente (leve, grave o crítico).</div>
        </div>
      </div>
      <div class="flow-step">
        <div class="flow-num">2</div>
        <div class="flow-body">
          <div class="flow-title">Reporta en el canal privado del hub</div>
          <div class="flow-desc">Solo mods tienen acceso. Incluye: ID de Discord, alias, evidencia y nivel propuesto. Si es leve, se archiva. Si es grave o crítico, va al Comité.</div>
        </div>
      </div>
      <div class="flow-step">
        <div class="flow-num">3</div>
        <div class="flow-body">
          <div class="flow-title">El Comité revisa (plazo: 72 horas)</div>
          <div class="flow-desc">3 mods de servidores distintos miran la evidencia. El reportado puede dar su versión. Deciden por mayoría: archivar, monitorear o alertar a la red.</div>
        </div>
      </div>
      <div class="flow-step">
        <div class="flow-num">4</div>
        <div class="flow-body">
          <div class="flow-title">Decisión documentada y transparente</div>
          <div class="flow-desc">Todo queda registrado: quién decidió qué, cuándo y por qué. Las alertas críticas se comparten en el hub privado para que todos los mods estén informados.</div>
        </div>
      </div>
      <div class="flow-step">
        <div class="flow-num">5</div>
        <div class="flow-body">
          <div class="flow-title">Se puede apelar (30 días)</div>
          <div class="flow-desc">Cualquier decisión se puede llevar a la Mesa completa de representantes. Necesitas aportar evidencia nueva. Sin drama, con procedimiento.</div>
        </div>
      </div>
    </div>

    <div class="notice">
      <strong>Privacidad garantizada:</strong> Solo se almacenan IDs de Discord y aliases públicos. Nunca nombres reales, edades, fotos ni redes personales. El acceso al hub privado está restringido estrictamente a mods autorizados de servidores miembro.
    </div>

    <div class="section-title">Lo que la red NO hace</div>
    <div class="card">
      <ul class="checklist">
        <li><span class="check-no">✕</span> No publicamos listas de usuarios baneados en canales públicos</li>
        <li><span class="check-no">✕</span> No juzgamos opiniones, gustos o estilos de rol</li>
        <li><span class="check-no">✕</span> No intervenimos en los bans internos de tu servidor (eso es 100% tuyo)</li>
        <li><span class="check-no">✕</span> No compartimos datos personales de nadie</li>
        <li><span class="check-no">✕</span> No actuamos sin evidencia: capturas, logs, contexto. Sin pruebas, no hay caso</li>
      </ul>
    </div>

    <div class="section-title">Lo que la red SÍ hace</div>
    <div class="card card-success">
      <ul class="checklist">
        <li><span class="check-yes">✓</span> Se avisa entre mods cuando un usuario con conducta crítica aparece en otro servidor</li>
        <li><span class="check-yes">✓</span> Se documenta todo con responsables nombrados y fechas</li>
        <li><span class="check-yes">✓</span> Se puede apelar cualquier decisión ante la Mesa completa</li>
        <li><span class="check-yes">✓</span> Se protege la privacidad de todos los involucrados</li>
        <li><span class="check-yes">✓</span> Se castigan conductas verificables, no opiniones ni gustos</li>
      </ul>
    </div>
  </div>


  <!-- PANEL: CÓMO UNIRSE -->
  <div id="tab-unirse" class="panel">
    <div class="section-title">Requisitos mínimos (lo básico)</div>
    <div class="card">
      <div style="margin-bottom:14px; font-weight:700; font-size:14px;">
        🔒 Compromisos obligatorios
      </div>
      <ul class="checklist">
        <li><span class="tag tag-must">obligatorio</span> Tener un canal de reportes activo con mods que respondan en menos de 48 horas</li>
        <li><span class="tag tag-must">obligatorio</span> Reglas claras contra acoso, grooming y discriminación grave</li>
        <li><span class="tag tag-must">obligatorio</span> Compartir alertas nivel crítico en las primeras 24 horas de confirmarlas</li>
        <li><span class="tag tag-must">obligatorio</span> No publicar datos personales de usuarios en canales públicos</li>
        <li><span class="tag tag-must">obligatorio</span> Crear un canal #alianzas en tu servidor donde se muestren los miembros de la red</li>
      </ul>
      <div style="margin-top:14px; padding-top:14px; border-top:1px solid rgba(255,255,255,0.04); font-weight:700; font-size:14px;">
        ✅ Lo que decides tú
      </div>
      <ul class="checklist">
        <li><span class="tag tag-opt">libre</span> Tu estilo narrativo, sistema de juego, lore, reglas de casa, ERP sí o no</li>
        <li><span class="tag tag-opt">libre</span> Participar en eventos: recomendado, nunca obligatorio</li>
        <li><span class="tag tag-opt">libre</span> Compartir recursos: si tienes algo útil, genial. Si no, no pasa nada</li>
        <li><span class="tag tag-opt">libre</span> Aceptar jugadores de otros servidores: tú decides quién entra a tu mesa</li>
      </ul>
    </div>

    <div class="section-title">Proceso de entrada</div>
    <div class="card">
      <div class="how-grid" style="grid-template-columns: 1fr;">
        <div class="how-card" style="text-align:left; display:flex; gap:14px; align-items:flex-start;">
          <div class="how-num" style="margin:0; flex-shrink:0;">1</div>
          <div>
            <div class="how-title">Rellenas el formulario</div>
            <div class="how-desc">Nos cuentas de tu servidor: sistema de juego, tamaño, reglas básicas, link de invitación.</div>
          </div>
        </div>
        <div class="how-card" style="text-align:left; display:flex; gap:14px; align-items:flex-start;">
          <div class="how-num" style="margin:0; flex-shrink:0;">2</div>
          <div>
            <div class="how-title">Revisamos tu servidor</div>
            <div class="how-desc">Un par de mods de la red entran a echar un vistazo. No buscamos perfección, solo que cumplas lo básico.</div>
          </div>
        </div>
        <div class="how-card" style="text-align:left; display:flex; gap:14px; align-items:flex-start;">
          <div class="how-num" style="margin:0; flex-shrink:0;">3</div>
          <div>
            <div class="how-title">Período de prueba (30 días)</div>
            <div class="how-desc">Entras como "Nuevo". Participas en la red, ves cómo funciona, y nosotros vemos cómo funciona la química.</div>
          </div>
        </div>
        <div class="how-card" style="text-align:left; display:flex; gap:14px; align-items:flex-start;">
          <div class="how-num" style="margin:0; flex-shrink:0;">4</div>
          <div>
            <div class="how-title">¡Bienvenido oficial!</div>
            <div class="how-desc">Si todo va bien, pasas a "Socio" con acceso completo. Si no encaja, te lo decimos con honestidad y sin drama.</div>
          </div>
        </div>
      </div>
    </div>

    <div class="notice">
      <strong>Salir de la red:</strong> Puedes irte cuando quieras, sin preguntas ni reproches. Tus datos en el registro se anonimizan en 30 días, excepto alertas críticas activas que afectan a la seguridad de la red.
    </div>
  </div>

  <!-- PANEL: FAQ -->
  <div id="tab-faq" class="panel">
    <div class="section-title">Preguntas frecuentes</div>

    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">¿Mi servidor deja de ser independiente?</div>
      <div class="faq-a">Para nada. Tú sigues siendo el dueño de tu servidor, con tus reglas, tu lore, tu moderación y tu gente. La Red no interviene en nada de eso. Solo conectamos servidores para que se apoyen entre sí.</div>
    </div>

    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">¿Tengo que pagar algo?</div>
      <div class="faq-a">Nada. Ni cuotas, ni suscripciones, ni porcentajes. Todo se gestiona con herramientas gratuitas (Discord, Notion, Google Forms). Si algún día hacemos un sorteo conjunto, buscamos patrocinios o lo pagamos entre los admins que quieran.</div>
    </div>

    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">¿Qué pasa si no quiero participar en eventos?</div>
      <div class="faq-a">No pasa nada. La participación en eventos es 100% voluntaria. Puedes estar en la red, disfrutar del directorio y las alertas, sin organizar ni un solo evento cruzado. Cuando quieras y puedas, te sumas.</div>
    </div>

    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">¿Mi servidor es muy pequeño? ¿Puedo entrar igual?</div>
      <div class="faq-a">Claro. No hay mínimo de miembros. Lo que valoramos es que tengas reglas claras, moderación activa y ganas de formar parte de algo más grande. Hemos tenido servidores de 20 personas que aportan más que otros de 500.</div>
    </div>

    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">¿Qué sistemas de juego permiten?</div>
      <div class="faq-a">Todos. D&D 5e, Pathfinder, Vampiro, Call of Cthulhu, sistemas caseros, narrativos libres... La Red no impone sistema. De hecho, cuanto más variado, mejor para todos.</div>
    </div>

    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">¿Qué es el canal #alianzas?</div>
      <div class="faq-a">Es un canal que creas en tu servidor donde publicamos una lista actualizada de todos los miembros de La Red del D20. Tus jugadores pueden descubrir otros servidores desde ahí, y los jugadores de otros servidores pueden descubrir el tuyo. Es como un directorio viviente dentro de tu propia comunidad.</div>
    </div>

    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">¿Y el servidor privado de mods? ¿Qué se hace ahí?</div>
      <div class="faq-a">Es un servidor de Discord exclusivo para moderadores de los servidores miembro. Ahí compartimos alertas de seguridad (de forma privada y con evidencia), coordinamos eventos, compartimos recursos y resolvemos dudas. Los jugadores normales no tienen acceso ahí.</div>
    </div>

    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">¿Puedo echar a alguien de mi servidor sin que la Red se meta?</div>
      <div class="faq-a">Por supuesto. Tú decides quién entra y quién sale de tu servidor. La Red solo se entera si el caso es de seguridad crítica (grooming, doxxeo, amenazas) y solo para alertar a otros mods. Un ban por drama de mesa o inmadurez es 100% tu decisión.</div>
    </div>

    <div class="faq-item">
      <div class="faq-q" onclick="toggleFaq(this)">¿Qué pasa si me quiero ir?</div>
      <div class="faq-a">Nadie te retiene. Puedes salir cuando quieras. Borramos tus datos del registro en 30 días (excepto alertas críticas activas que protegen a otros). No hay preguntas incómodas ni drama.</div>
    </div>
  </div>



</div>

<script>
function switchTab(id) {
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + id).classList.add('active');
  const tabs = ['que','funciona','beneficios','seguridad','unirse','faq'];
  const idx = tabs.indexOf(id);
  document.querySelectorAll('.tab')[idx].classList.add('active');
}

function toggleFaq(el) {
  const item = el.parentElement;
  const wasOpen = item.classList.contains('open');
  document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
  if (!wasOpen) item.classList.add('open');
}
</script>

</body>
</html>
