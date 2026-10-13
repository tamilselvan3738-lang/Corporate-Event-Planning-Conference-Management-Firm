import os

def generate_about():
    with open('navbar.html', 'r', encoding='utf-8') as f:
        nav_text = f.read()

    style_pos = nav_text.find('</style>')
    if style_pos == -1:
        raise Exception("Could not find </style> in navbar.html")

    nav_head_up_to_style = nav_text[:style_pos]

    split_tag = '<!-- FOOTER -->'
    footer_pos = nav_text.find(split_tag)
    if footer_pos == -1:
        raise Exception("Could not find <!-- FOOTER --> in navbar.html")

    nav_mid = nav_text[style_pos:footer_pos]

    body_close_pos = nav_text.rfind('</body>')
    if body_close_pos == -1:
        raise Exception("Could not find </body> in navbar.html")

    footer_full = nav_text[footer_pos:body_close_pos]
    closing_part = nav_text[body_close_pos:]

    # CSS for the new about.html layout
    new_abt_css = """
    /* =====================================================================
       REDESIGNED ABOUT ARCHITECTURE: HERITAGE, ETHOS & ENTERPRISE CITADEL
       Supports Light Mode, Dark Mode (body.dark), and RTL (body.rtl)
       ===================================================================== */
    :root {
      --abt-primary: #1e3a8a;
      --abt-primary-dark: #0f172a;
      --abt-accent: #d97706;
      --abt-accent-light: #fbbf24;
      --abt-accent-glow: rgba(217, 119, 6, 0.16);
      --abt-amber: #b45309;
      --abt-emerald: #059669;
      --abt-emerald-glow: rgba(5, 150, 105, 0.16);
      --abt-indigo: #4338ca;
      --abt-indigo-glow: rgba(67, 56, 202, 0.16);
      --abt-bg: #f8fafc;
      --abt-surface: #ffffff;
      --abt-surface-muted: #f1f5f9;
      --abt-card-border: #e2e8f0;
      --abt-text-main: #0f172a;
      --abt-text-muted: #64748b;
      --abt-text-light: #94a3b8;
      --abt-gold-gradient: linear-gradient(135deg, #b45309 0%, #d97706 50%, #f59e0b 100%);
      --abt-blue-gradient: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      --abt-shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --abt-shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.07), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
      --abt-shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      --abt-shadow-glow: 0 0 25px rgba(217, 119, 6, 0.22);
    }

    body.dark {
      --abt-bg: #070b14;
      --abt-surface: #0f172a;
      --abt-surface-muted: #131d33;
      --abt-card-border: #1e293b;
      --abt-text-main: #f8fafc;
      --abt-text-muted: #94a3b8;
      --abt-text-light: #64748b;
      --abt-blue-gradient: linear-gradient(135deg, #070b14 0%, #172554 100%);
    }

    /* RTL Support */
    body.rtl .abt-section-head { text-align: right; }
    body.rtl .abt-badge i { margin-left: 0.5rem; margin-right: 0; }
    body.rtl .abt-btn i { margin-right: 0.5rem; margin-left: 0; }

    /* Base Container */
    .abt-page-wrap {
      background-color: var(--abt-bg);
      color: var(--abt-text-main);
      font-family: 'Inter', system-ui, sans-serif;
      overflow-x: hidden;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    .abt-container {
      max-width: 1320px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }

    /* SECTION HEADER STYLING */
    .abt-section-head {
      margin-bottom: 3.5rem;
      position: relative;
    }

    .abt-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.45rem 1.1rem;
      border-radius: 9999px;
      background: var(--abt-accent-glow);
      color: var(--abt-accent);
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 1rem;
      border: 1px solid rgba(217, 119, 6, 0.3);
    }

    .abt-title {
      font-size: 2.5rem;
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.025em;
      color: var(--abt-text-main);
      margin-bottom: 1rem;
    }

    .abt-title-gradient {
      background: var(--abt-gold-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .abt-subtitle {
      font-size: 1.1rem;
      color: var(--abt-text-muted);
      max-width: 760px;
      line-height: 1.65;
    }

    /* BUTTONS */
    .abt-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.6rem;
      padding: 0.8rem 1.6rem;
      border-radius: 0.6rem;
      font-weight: 600;
      font-size: 0.95rem;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      border: 1px solid transparent;
    }

    .abt-btn-primary {
      background: var(--abt-gold-gradient);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(217, 119, 6, 0.35);
    }

    .abt-btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(217, 119, 6, 0.45);
      color: #ffffff;
    }

    .abt-btn-outline {
      background: transparent;
      color: var(--abt-text-main);
      border-color: var(--abt-card-border);
    }

    .abt-btn-outline:hover {
      border-color: var(--abt-accent);
      color: var(--abt-accent);
      background: var(--abt-accent-glow);
    }

    /* =====================================================================
       FRAMER MOTION SPECIFIC CLASSES & KEYFRAMES (1 PER SECTION)
       ===================================================================== */

    /* 1. Company Heritage: .framer-epoch-chronicle */
    .framer-epoch-chronicle {
      opacity: 0;
      transform: translateY(35px) scale(0.98);
      transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1),
                  transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .framer-epoch-chronicle.framer-in-view {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    /* 2. Mission & Vision: .framer-polarity-gyro */
    .framer-polarity-gyro {
      opacity: 0;
      transform: scale(0.95) rotateY(4deg);
      transition: opacity 0.75s cubic-bezier(0.34, 1.56, 0.64, 1),
                  transform 0.75s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .framer-polarity-gyro.framer-in-view {
      opacity: 1;
      transform: scale(1) rotateY(0deg);
    }

    /* 3. Philosophy: .framer-triad-pedestal */
    .framer-triad-pedestal {
      opacity: 0;
      transform: translateY(40px);
      transition: opacity 0.85s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                  transform 0.85s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    .framer-triad-pedestal.framer-in-view {
      opacity: 1;
      transform: translateY(0);
    }

    /* 4. Leadership Team: .framer-council-quad */
    .framer-council-quad {
      opacity: 0;
      transform: translateY(30px) scale(0.97);
      transition: opacity 0.8s cubic-bezier(0.19, 1, 0.22, 1),
                  transform 0.8s cubic-bezier(0.19, 1, 0.22, 1);
    }
    .framer-council-quad.framer-in-view {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    /* 5. Specialists: .framer-division-matrix */
    .framer-division-matrix {
      opacity: 0;
      transform: translateX(-35px) scale(0.98);
      transition: opacity 0.8s cubic-bezier(0.22, 1, 0.36, 1),
                  transform 0.8s cubic-bezier(0.22, 1, 0.36, 1);
    }
    .framer-division-matrix.framer-in-view {
      opacity: 1;
      transform: translateX(0) scale(1);
    }

    /* 6. Client Portfolio: .framer-marquee-portfolio */
    .framer-marquee-portfolio {
      opacity: 0;
      transform: translateY(35px);
      filter: blur(3px);
      transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1),
                  transform 0.8s cubic-bezier(0.16, 1, 0.3, 1),
                  filter 0.8s ease;
    }
    .framer-marquee-portfolio.framer-in-view {
      opacity: 1;
      transform: translateY(0);
      filter: blur(0px);
    }

    /* 7. Safety & Advantage: .framer-citadel-moat */
    .framer-citadel-moat {
      opacity: 0;
      transform: scale(0.94) translateY(30px);
      transition: opacity 0.7s cubic-bezier(0.33, 1, 0.68, 1),
                  transform 0.7s cubic-bezier(0.33, 1, 0.68, 1);
    }
    .framer-citadel-moat.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    /* =====================================================================
       SECTION 1: COMPANY HERITAGE - EPOCH RIBBON & DUAL CHRONICLE
       ===================================================================== */
    .abt-section-heritage {
      padding: 6rem 0;
      position: relative;
    }

    .abt-heritage-stats-ribbon {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.5rem;
      background: var(--abt-surface);
      border: 1px solid var(--abt-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem 2rem;
      box-shadow: var(--abt-shadow-sm);
      margin-bottom: 3rem;
    }

    .abt-hstat-item {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .abt-hstat-icon {
      width: 2.75rem;
      height: 2.75rem;
      border-radius: 0.75rem;
      background: var(--abt-accent-glow);
      color: var(--abt-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
    }

    .abt-hstat-val {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--abt-text-main);
      line-height: 1.2;
    }

    .abt-hstat-lbl {
      font-size: 0.78rem;
      color: var(--abt-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .abt-heritage-chronicle-grid {
      display: grid;
      grid-template-columns: 1.1fr 1.2fr;
      gap: 2.5rem;
      align-items: center;
    }

    .abt-monolith-visual-card {
      background: var(--abt-surface);
      border: 1px solid var(--abt-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--abt-shadow-md);
      position: relative;
    }

    .abt-monolith-img-wrap {
      height: 440px;
      position: relative;
      overflow: hidden;
    }

    .abt-monolith-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s ease;
    }

    .abt-monolith-visual-card:hover .abt-monolith-img-wrap img {
      transform: scale(1.04);
    }

    .abt-wax-seal {
      position: absolute;
      top: 1.5rem;
      left: 1.5rem;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(8px);
      padding: 0.5rem 1.2rem;
      border-radius: 9999px;
      color: #fbbf24;
      font-size: 0.85rem;
      font-weight: 800;
      border: 1px solid rgba(251, 191, 36, 0.3);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    /* Right Epoch Ribbon Stack */
    .abt-epoch-ribbon-stack {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    .abt-epoch-card {
      background: var(--abt-surface);
      border: 1px solid var(--abt-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem 1.75rem;
      box-shadow: var(--abt-shadow-sm);
      transition: all 0.25s ease;
      cursor: pointer;
      position: relative;
    }

    .abt-epoch-card:hover,
    .abt-epoch-card.active {
      border-color: var(--abt-accent);
      box-shadow: var(--abt-shadow-md);
      transform: translateX(4px);
    }

    body.rtl .abt-epoch-card:hover,
    body.rtl .abt-epoch-card.active {
      transform: translateX(-4px);
    }

    .abt-epoch-card.active::before {
      content: '';
      position: absolute;
      top: 0;
      bottom: 0;
      left: 0;
      width: 4px;
      background: var(--abt-accent);
      border-radius: 1.25rem 0 0 1.25rem;
    }

    body.rtl .abt-epoch-card.active::before {
      left: auto;
      right: 0;
      border-radius: 0 1.25rem 1.25rem 0;
    }

    .abt-epoch-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.35rem;
    }

    .abt-epoch-dates {
      font-size: 0.78rem;
      font-weight: 800;
      color: var(--abt-accent);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .abt-epoch-era {
      font-size: 0.75rem;
      color: var(--abt-text-muted);
      font-weight: 600;
    }

    .abt-epoch-title {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--abt-text-main);
      margin-bottom: 0.35rem;
    }

    .abt-epoch-desc {
      font-size: 0.88rem;
      color: var(--abt-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 2: MISSION & VISION - DUAL-POLARITY HORIZON DECK
       ===================================================================== */
    .abt-section-mission-vision {
      padding: 6rem 0;
      background: var(--abt-surface-muted);
      border-top: 1px solid var(--abt-card-border);
      border-bottom: 1px solid var(--abt-card-border);
    }

    .abt-polarity-deck-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.5rem;
    }

    .abt-polarity-card {
      background: var(--abt-surface);
      border: 1px solid var(--abt-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--abt-shadow-md);
      display: flex;
      flex-direction: column;
    }

    .abt-polarity-img-box {
      height: 240px;
      position: relative;
      overflow: hidden;
    }

    .abt-polarity-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .abt-vision-hud-box {
      height: 240px;
      position: relative;
      background: radial-gradient(circle at center, #172554 0%, #070b14 100%);
      border-bottom: 1px solid var(--abt-card-border);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }

    .abt-hud-radar-ring {
      position: absolute;
      width: 190px;
      height: 190px;
      border-radius: 50%;
      border: 2px dashed rgba(217, 119, 6, 0.4);
      animation: abtSpinSlow 25s linear infinite;
    }

    @keyframes abtSpinSlow {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    .abt-hud-icon {
      width: 4rem;
      height: 4rem;
      border-radius: 1rem;
      background: var(--abt-accent-glow);
      color: var(--abt-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.85rem;
      z-index: 2;
      box-shadow: 0 0 25px rgba(217, 119, 6, 0.35);
      border: 1px solid rgba(217, 119, 6, 0.3);
    }

    .abt-hud-telemetry-tag {
      margin-top: 0.85rem;
      font-size: 0.75rem;
      font-weight: 800;
      letter-spacing: 0.12em;
      color: var(--abt-accent-light);
      z-index: 2;
    }

    .abt-polarity-badge {
      position: absolute;
      top: 1.25rem;
      left: 1.25rem;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(8px);
      padding: 0.4rem 1rem;
      border-radius: 9999px;
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #fbbf24;
      border: 1px solid rgba(251, 191, 36, 0.3);
    }

    .abt-polarity-body {
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      flex: 1;
    }

    .abt-polarity-title {
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--abt-text-main);
      margin-bottom: 1rem;
    }

    .abt-polarity-desc {
      font-size: 0.95rem;
      color: var(--abt-text-muted);
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }

    .abt-polarity-bullets {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      margin-top: auto;
    }

    .abt-pbullet-row {
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      font-size: 0.88rem;
      color: var(--abt-text-main);
    }

    .abt-pbullet-row i {
      color: var(--abt-accent);
      margin-top: 0.2rem;
    }

    /* =====================================================================
       SECTION 3: PHILOSOPHY - TRIAD PRINCIPLES PEDESTAL
       ===================================================================== */
    .abt-section-philosophy {
      padding: 6rem 0;
      position: relative;
    }

    .abt-philosophy-hero-frame {
      background: var(--abt-surface);
      border: 1px solid var(--abt-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--abt-shadow-md);
      margin-bottom: 3.5rem;
    }

    .abt-philosophy-img-box {
      height: 320px;
      position: relative;
      overflow: hidden;
    }

    .abt-philosophy-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .abt-philosophy-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, transparent 20%, rgba(15, 23, 42, 0.88) 100%);
      display: flex;
      align-items: flex-end;
      padding: 2rem 2.5rem;
      color: #ffffff;
    }

    .abt-philosophy-manifesto {
      font-size: 1.35rem;
      font-weight: 700;
      line-height: 1.45;
      max-width: 860px;
    }

    .abt-triad-pedestals-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 2rem;
    }

    .abt-pedestal-card {
      background: var(--abt-surface);
      border: 1px solid var(--abt-card-border);
      border-radius: 1.25rem;
      padding: 2.25rem;
      box-shadow: var(--abt-shadow-sm);
      display: flex;
      flex-direction: column;
      transition: all 0.3s ease;
      position: relative;
    }

    .abt-pedestal-card:hover {
      transform: translateY(-6px);
      box-shadow: var(--abt-shadow-md);
      border-color: var(--abt-accent);
    }

    .abt-pedestal-num {
      width: 3rem;
      height: 3rem;
      border-radius: 0.85rem;
      background: var(--abt-accent-glow);
      color: var(--abt-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.25rem;
      font-weight: 800;
      margin-bottom: 1.5rem;
    }

    .abt-pedestal-title {
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--abt-text-main);
      margin-bottom: 0.75rem;
    }

    .abt-pedestal-desc {
      font-size: 0.92rem;
      color: var(--abt-text-muted);
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }

    .abt-pedestal-points {
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      margin-top: auto;
      font-size: 0.82rem;
      color: var(--abt-text-main);
    }

    .abt-pedestal-points i {
      color: var(--abt-emerald);
      margin-right: 0.4rem;
    }

    body.rtl .abt-pedestal-points i {
      margin-right: 0;
      margin-left: 0.4rem;
    }

    /* =====================================================================
       SECTION 4: LEADERSHIP TEAM - EXECUTIVE COUNCIL QUAD-MOSAIC
       ===================================================================== */
    .abt-section-leadership {
      padding: 6rem 0;
      background: var(--abt-surface-muted);
      border-top: 1px solid var(--abt-card-border);
      border-bottom: 1px solid var(--abt-card-border);
    }

    .abt-council-mosaic-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.75rem;
    }

    .abt-leader-card {
      background: var(--abt-surface);
      border: 1px solid var(--abt-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--abt-shadow-sm);
      transition: all 0.3s ease;
      display: flex;
      flex-direction: column;
    }

    .abt-leader-card:hover {
      transform: translateY(-6px);
      box-shadow: var(--abt-shadow-md);
      border-color: var(--abt-accent);
    }

    .abt-leader-img-box {
      height: 280px;
      position: relative;
      overflow: hidden;
    }

    .abt-leader-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s ease;
    }

    .abt-leader-card:hover .abt-leader-img-box img {
      transform: scale(1.05);
    }

    .abt-leader-body {
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      flex: 1;
    }

    .abt-leader-role {
      font-size: 0.78rem;
      font-weight: 800;
      color: var(--abt-accent);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.35rem;
    }

    .abt-leader-name {
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--abt-text-main);
      margin-bottom: 0.75rem;
    }

    .abt-leader-bio {
      font-size: 0.85rem;
      color: var(--abt-text-muted);
      line-height: 1.55;
      margin-bottom: 1.25rem;
    }

    .abt-leader-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: auto;
      padding-top: 1rem;
      border-top: 1px dashed var(--abt-card-border);
    }

    .abt-leader-credential {
      font-size: 0.75rem;
      color: var(--abt-text-light);
      font-weight: 600;
    }

    .abt-leader-btn {
      color: var(--abt-accent);
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }

    /* =====================================================================
       SECTION 5: SPECIALISTS - DIVISION COMMAND MATRIX
       ===================================================================== */
    .abt-section-specialists {
      padding: 6rem 0;
      position: relative;
    }

    .abt-division-matrix-grid {
      display: grid;
      grid-template-columns: 1fr 1.2fr;
      gap: 2.5rem;
      align-items: center;
    }

    .abt-specialists-visual-card {
      background: var(--abt-surface);
      border: 1px solid var(--abt-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--abt-shadow-md);
    }

    .abt-spec-img-box {
      height: 400px;
      position: relative;
      overflow: hidden;
    }

    .abt-spec-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .abt-spec-badge-floating {
      position: absolute;
      bottom: 1.5rem;
      left: 1.5rem;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(8px);
      padding: 0.6rem 1.25rem;
      border-radius: 9999px;
      color: #ffffff;
      font-size: 0.82rem;
      font-weight: 700;
      border: 1px solid rgba(255, 255, 255, 0.2);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .abt-divisions-stack {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    .abt-division-card {
      background: var(--abt-surface);
      border: 1px solid var(--abt-card-border);
      border-radius: 1.25rem;
      padding: 1.75rem;
      box-shadow: var(--abt-shadow-sm);
      transition: all 0.25s ease;
      cursor: pointer;
    }

    .abt-division-card:hover,
    .abt-division-card.active {
      border-color: var(--abt-accent);
      box-shadow: var(--abt-shadow-md);
      transform: translateX(4px);
    }

    body.rtl .abt-division-card:hover,
    body.rtl .abt-division-card.active {
      transform: translateX(-4px);
    }

    .abt-div-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.5rem;
    }

    .abt-div-tag {
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--abt-accent);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .abt-div-title {
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--abt-text-main);
      margin-bottom: 0.5rem;
    }

    .abt-div-desc {
      font-size: 0.88rem;
      color: var(--abt-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 6: CLIENT PORTFOLIO - MARQUEE SUMMITS & SECTOR ROSTER
       ===================================================================== */
    .abt-section-portfolio {
      padding: 6rem 0;
      background: var(--abt-surface-muted);
      border-top: 1px solid var(--abt-card-border);
      border-bottom: 1px solid var(--abt-card-border);
    }

    .abt-portfolio-marquee-grid {
      display: grid;
      grid-template-columns: 1.1fr 1fr;
      gap: 2.5rem;
      align-items: start;
    }

    .abt-portfolio-hero-card {
      background: var(--abt-surface);
      border: 1px solid var(--abt-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--abt-shadow-md);
    }

    .abt-port-img-box {
      height: 320px;
      position: relative;
      overflow: hidden;
    }

    .abt-port-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .abt-port-body {
      padding: 2rem;
    }

    .abt-port-quote {
      font-size: 1.15rem;
      font-style: italic;
      color: var(--abt-text-main);
      line-height: 1.5;
      margin-bottom: 1rem;
    }

    .abt-port-author {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--abt-accent);
    }

    .abt-sectors-deck {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.5rem;
    }

    .abt-sector-card {
      background: var(--abt-surface);
      border: 1px solid var(--abt-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      box-shadow: var(--abt-shadow-sm);
      transition: all 0.25s ease;
    }

    .abt-sector-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--abt-shadow-md);
      border-color: var(--abt-accent);
    }

    .abt-sec-icon {
      width: 2.5rem;
      height: 2.5rem;
      border-radius: 0.6rem;
      background: var(--abt-accent-glow);
      color: var(--abt-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      margin-bottom: 1rem;
    }

    .abt-sec-title {
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--abt-text-main);
      margin-bottom: 0.5rem;
    }

    .abt-sec-clients {
      font-size: 0.82rem;
      color: var(--abt-text-muted);
      line-height: 1.45;
    }

    /* =====================================================================
       SECTION 7: SAFETY & ADVANTAGE - INSTITUTIONAL CITADEL & MOAT
       ===================================================================== */
    .abt-section-safety {
      padding: 6rem 0;
      position: relative;
    }

    .abt-citadel-split-grid {
      display: grid;
      grid-template-columns: 420px 1fr;
      gap: 2.5rem;
      align-items: start;
    }

    .abt-citadel-visual-card {
      background: var(--abt-surface);
      border: 1px solid var(--abt-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--abt-shadow-md);
    }

    .abt-citadel-img-box {
      height: 260px;
      position: relative;
      overflow: hidden;
    }

    .abt-citadel-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .abt-citadel-body {
      padding: 2rem;
    }

    .abt-citadel-title {
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--abt-text-main);
      margin-bottom: 0.75rem;
    }

    .abt-citadel-desc {
      font-size: 0.88rem;
      color: var(--abt-text-muted);
      line-height: 1.55;
      margin-bottom: 1.5rem;
    }

    .abt-citadel-cert-list {
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      font-size: 0.82rem;
      color: var(--abt-text-main);
    }

    .abt-citadel-cert-list i {
      color: var(--abt-emerald);
      margin-right: 0.5rem;
    }

    body.rtl .abt-citadel-cert-list i {
      margin-right: 0;
      margin-left: 0.5rem;
    }

    /* Right 4-Pillar Moat Grid */
    .abt-moat-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.5rem;
    }

    .abt-moat-card {
      background: var(--abt-surface);
      border: 1px solid var(--abt-card-border);
      border-radius: 1.25rem;
      padding: 1.75rem;
      box-shadow: var(--abt-shadow-sm);
      transition: all 0.25s ease;
    }

    .abt-moat-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--abt-shadow-md);
      border-color: var(--abt-accent);
    }

    .abt-moat-icon {
      width: 2.75rem;
      height: 2.75rem;
      border-radius: 0.75rem;
      background: var(--abt-accent-glow);
      color: var(--abt-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
      margin-bottom: 1rem;
    }

    .abt-moat-title {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--abt-text-main);
      margin-bottom: 0.5rem;
    }

    .abt-moat-desc {
      font-size: 0.85rem;
      color: var(--abt-text-muted);
      line-height: 1.55;
    }

    /* Interactive Dossier Modal */
    .abt-modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(6px);
      z-index: 9999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }

    .abt-modal-card {
      background: var(--abt-surface);
      border: 1px solid var(--abt-card-border);
      border-radius: 1.5rem;
      max-width: 540px;
      width: 100%;
      padding: 2.5rem;
      box-shadow: var(--abt-shadow-lg);
      position: relative;
    }

    .abt-modal-close {
      position: absolute;
      top: 1.25rem;
      right: 1.25rem;
      background: transparent;
      border: none;
      color: var(--abt-text-muted);
      font-size: 1.25rem;
      cursor: pointer;
    }

    body.rtl .abt-modal-close {
      right: auto;
      left: 1.25rem;
    }

    /* Responsive Queries */
    @media (max-width: 1100px) {
      .abt-heritage-stats-ribbon { grid-template-columns: repeat(2, 1fr); }
      .abt-heritage-chronicle-grid { grid-template-columns: 1fr; }
      .abt-polarity-deck-grid { grid-template-columns: 1fr; }
      .abt-triad-pedestals-grid { grid-template-columns: 1fr; }
      .abt-council-mosaic-grid { grid-template-columns: repeat(2, 1fr); }
      .abt-division-matrix-grid { grid-template-columns: 1fr; }
      .abt-portfolio-marquee-grid { grid-template-columns: 1fr; }
      .abt-citadel-split-grid { grid-template-columns: 1fr; }
    }

    @media (max-width: 768px) {
      .abt-heritage-stats-ribbon { grid-template-columns: 1fr; }
      .abt-council-mosaic-grid { grid-template-columns: 1fr; }
      .abt-sectors-deck { grid-template-columns: 1fr; }
      .abt-moat-grid { grid-template-columns: 1fr; }
      .abt-title { font-size: 2rem; }
      .abt-monolith-img-wrap { height: 300px; }
    }
"""

    # HTML for the redesigned about page
    new_abt_content = """
  <!-- MAIN ABOUT CONTENT WRAPPER -->
  <main class="abt-page-wrap">

    <!-- =====================================================================
         SECTION 1: COMPANY HERITAGE (EPOCH RIBBON & DUAL CHRONICLE)
         ===================================================================== -->
    <section id="company-heritage" class="abt-section-heritage">
      <div class="abt-container">
        <!-- Section Header -->
        <div class="abt-section-head framer-epoch-chronicle">
          <div class="abt-badge"><i class="fas fa-crown"></i> Institutional Legacy</div>
          <h2 class="abt-title">Company Heritage & <span class="abt-title-gradient">Archival Provenance</span></h2>
          <p class="abt-subtitle">Founded in 2012, Apex has evolved from an elite diplomatic protocol advisory into the world's foremost corporate conference architecture firm.</p>
        </div>

        <!-- Heritage Metric Ribbon -->
        <div class="abt-heritage-stats-ribbon framer-epoch-chronicle">
          <div class="abt-hstat-item">
            <div class="abt-hstat-icon"><i class="fas fa-hourglass-start"></i></div>
            <div>
              <div class="abt-hstat-val">Est. 2012</div>
              <div class="abt-hstat-lbl">14 Years of Leadership</div>
            </div>
          </div>
          <div class="abt-hstat-item">
            <div class="abt-hstat-icon"><i class="fas fa-earth-americas"></i></div>
            <div>
              <div class="abt-hstat-val">42 Nations</div>
              <div class="abt-hstat-lbl">Global Host Capitals</div>
            </div>
          </div>
          <div class="abt-hstat-item">
            <div class="abt-hstat-icon"><i class="fas fa-users-viewfinder"></i></div>
            <div>
              <div class="abt-hstat-val">1,850+</div>
              <div class="abt-hstat-lbl">Summits Orchestrated</div>
            </div>
          </div>
          <div class="abt-hstat-item">
            <div class="abt-hstat-icon"><i class="fas fa-shield-heart"></i></div>
            <div>
              <div class="abt-hstat-val">99.8%</div>
              <div class="abt-hstat-lbl">Zero-Incident Record</div>
            </div>
          </div>
        </div>

        <!-- Asymmetric Dual-Chronicle Layout -->
        <div class="abt-heritage-chronicle-grid">
          <!-- Monolith Visual Card -->
          <div class="abt-monolith-visual-card framer-epoch-chronicle">
            <div class="abt-monolith-img-wrap">
              <img src="images/about_heritage.jpg" alt="Apex Corporate Event Heritage & Founders Assembly">
              <div class="abt-wax-seal">
                <i class="fas fa-certificate"></i> Apex Group Charter • Est. 2012
              </div>
            </div>
          </div>

          <!-- 4-Epoch Evolutionary Ribbon -->
          <div class="abt-epoch-ribbon-stack">
            <!-- Epoch 1 -->
            <div class="abt-epoch-card active framer-epoch-chronicle" onclick="selectEpoch(this, 'Foundation')">
              <div class="abt-epoch-top">
                <span class="abt-epoch-dates">2012 – 2015</span>
                <span class="abt-epoch-era">Epoch I • Genesis</span>
              </div>
              <h4 class="abt-epoch-title">Diplomatic Protocol & Bilateral Summits</h4>
              <p class="abt-epoch-desc">Launched in Zurich and London as an elite protocol advisory, stewarding high-security ministerial roundtables and bilateral economic summits.</p>
            </div>

            <!-- Epoch 2 -->
            <div class="abt-epoch-card framer-epoch-chronicle" onclick="selectEpoch(this, 'Expansion')">
              <div class="abt-epoch-top">
                <span class="abt-epoch-dates">2016 – 2019</span>
                <span class="abt-epoch-era">Epoch II • Transatlantic Scale</span>
              </div>
              <h4 class="abt-epoch-title">Enterprise Plenary Modernization</h4>
              <p class="abt-epoch-desc">Established headquarters in New York and Singapore, executing flagship Fortune 100 technology keynotes and multi-track partner expos.</p>
            </div>

            <!-- Epoch 3 -->
            <div class="abt-epoch-card framer-epoch-chronicle" onclick="selectEpoch(this, 'Broadcast')">
              <div class="abt-epoch-top">
                <span class="abt-epoch-dates">2020 – 2023</span>
                <span class="abt-epoch-era">Epoch III • Dual-Hemisphere</span>
              </div>
              <h4 class="abt-epoch-title">Hybrid Broadcast & Spatial Engineering</h4>
              <p class="abt-epoch-desc">Pioneered sub-50ms synchronized cloud broadcasting, linking physically dispersed audiences across 5 continents during global transitions.</p>
            </div>

            <!-- Epoch 4 -->
            <div class="abt-epoch-card framer-epoch-chronicle" onclick="selectEpoch(this, 'Regenerative')">
              <div class="abt-epoch-top">
                <span class="abt-epoch-dates">2024 – 2026+</span>
                <span class="abt-epoch-era">Epoch IV • Autonomous Stagecraft</span>
              </div>
              <h4 class="abt-epoch-title">Generative AI Canvasses & Net-Zero Summits</h4>
              <p class="abt-epoch-desc">Setting the global standard for certified ISO-20121 carbon-neutral summits powered by real-time generative staging and spatial audio.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 2: MISSION & VISION (DUAL-POLARITY HORIZON DECK)
         ===================================================================== -->
    <section id="mission-vision" class="abt-section-mission-vision">
      <div class="abt-container">
        <!-- Section Header -->
        <div class="abt-section-head framer-polarity-gyro">
          <div class="abt-badge"><i class="fas fa-compass"></i> Guiding Horizons</div>
          <h2 class="abt-title">The Operational Mission & <span class="abt-title-gradient">2035 Vision</span></h2>
          <p class="abt-subtitle">Our mission anchors day-to-day production precision, while our vision engineers the regenerative, multi-dimensional conference architectures of tomorrow.</p>
        </div>

        <div class="abt-polarity-deck-grid">
          <!-- Left Horizon: Mission -->
          <div class="abt-polarity-card framer-polarity-gyro">
            <div class="abt-polarity-img-box">
              <img src="images/about_mission.jpg" alt="Apex Operational Mission Production Command">
              <div class="abt-polarity-badge"><i class="fas fa-bullseye"></i> Operational Mission</div>
            </div>
            <div class="abt-polarity-body">
              <h3 class="abt-polarity-title">The Operational Mission Engine</h3>
              <p class="abt-polarity-desc">To architect zero-defect corporate summits where every technological, spatial, and human touchpoint reinforces the executive narrative and delivers verifiable corporate resonance.</p>
              <div class="abt-polarity-bullets">
                <div class="abt-pbullet-row"><i class="fas fa-circle-check"></i> <strong>Rigorous Protocol:</strong> Flawless dignitary movement and military-grade run-of-show timing.</div>
                <div class="abt-pbullet-row"><i class="fas fa-circle-check"></i> <strong>Institutional Redundancy:</strong> N+2 hardware backups across all mission-critical feeds.</div>
                <div class="abt-pbullet-row"><i class="fas fa-circle-check"></i> <strong>Financial Transparency:</strong> 100% open-book Capex/Opex ledger governance.</div>
              </div>
            </div>
          </div>

          <!-- Right Horizon: Vision -->
          <div class="abt-polarity-card framer-polarity-gyro">
            <div class="abt-vision-hud-box">
              <div class="abt-hud-radar-ring"></div>
              <div class="abt-hud-icon"><i class="fas fa-meteor"></i></div>
              <div class="abt-polarity-badge"><i class="fas fa-eye"></i> Future Horizon 2035</div>
              <div class="abt-hud-telemetry-tag">QUANTUM SPATIAL ARCHITECTURE</div>
            </div>
            <div class="abt-polarity-body">
              <h3 class="abt-polarity-title">The Future Vision Paradigm</h3>
              <p class="abt-polarity-desc">To redefine human assembly by synthesizing sustainable spatial architecture, bio-resonant acoustics, and real-time generative media into net-zero carbon summits.</p>
              <div class="abt-polarity-bullets">
                <div class="abt-pbullet-row"><i class="fas fa-circle-check"></i> <strong>Carbon-Neutral Plenaries:</strong> Verified Scope 1-3 net-zero emission standard across all events.</div>
                <div class="abt-pbullet-row"><i class="fas fa-circle-check"></i> <strong>Generative Canvasses:</strong> Real-time 3D Unreal Engine environments replacing static presentations.</div>
                <div class="abt-pbullet-row"><i class="fas fa-circle-check"></i> <strong>Biometric Comfort:</strong> Micro-climate zoned auditoriums maximizing executive alertness.</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 3: PHILOSOPHY (TRIAD PRINCIPLES PEDESTAL)
         ===================================================================== -->
    <section id="philosophy" class="abt-section-philosophy">
      <div class="abt-container">
        <!-- Section Header -->
        <div class="abt-section-head framer-triad-pedestal">
          <div class="abt-badge"><i class="fas fa-brain"></i> Core Methodology</div>
          <h2 class="abt-title">Production Philosophy & <span class="abt-title-gradient">Sensory Triad</span></h2>
          <p class="abt-subtitle">Our three foundational pillars transform traditional corporate conferences from passive presentations into catalytic business milestones.</p>
        </div>

        <!-- Philosophy Hero Frame -->
        <div class="abt-philosophy-hero-frame framer-triad-pedestal">
          <div class="abt-philosophy-img-box">
            <img src="images/about_philosophy.jpg" alt="Apex Production Philosophy & Spatial Resonance">
            <div class="abt-philosophy-overlay">
              <div class="abt-philosophy-manifesto">
                "Events are not passive calendar dates. They are hyper-calibrated spatial ecosystems engineered to align corporate vision, accelerate deal flow, and shift industry trajectories."
              </div>
            </div>
          </div>
        </div>

        <!-- The 3-Pedestal Spatial Geometry Triad -->
        <div class="abt-triad-pedestals-grid">
          <!-- Pillar 1 -->
          <div class="abt-pedestal-card framer-triad-pedestal">
            <div class="abt-pedestal-num">01</div>
            <h4 class="abt-pedestal-title">Sensory Architecture</h4>
            <p class="abt-pedestal-desc">We sculpt physical space through balanced color temperatures, spatial line-array acoustics, and ergonomic flow lines to eliminate executive conference fatigue.</p>
            <div class="abt-pedestal-points">
              <div><i class="fas fa-check"></i> STC 58 Acoustic Isolation</div>
              <div><i class="fas fa-check"></i> Circadian Rhythm Stage Lighting</div>
              <div><i class="fas fa-check"></i> Sightline Optimization Geometry</div>
            </div>
          </div>

          <!-- Pillar 2 -->
          <div class="abt-pedestal-card framer-triad-pedestal">
            <div class="abt-pedestal-num">02</div>
            <h4 class="abt-pedestal-title">Frictionless Protocol</h4>
            <p class="abt-pedestal-desc">From discreet dignitary motorcades to touchless RFID registration badges, logistical complexity dissolves into an effortless, white-glove delegate experience.</p>
            <div class="abt-pedestal-points">
              <div><i class="fas fa-check"></i> Triple-Ring Security Clearances</div>
              <div><i class="fas fa-check"></i> Dedicated Green Room Concierges</div>
              <div><i class="fas fa-check"></i> 0-Second Delay Ingress Scanning</div>
            </div>
          </div>

          <!-- Pillar 3 -->
          <div class="abt-pedestal-card framer-triad-pedestal">
            <div class="abt-pedestal-num">03</div>
            <h4 class="abt-pedestal-title">Measurable Resonance</h4>
            <p class="abt-pedestal-desc">We calibrate return on objective (ROO) with empirical metrics—tracking post-keynote recall, pipeline acceleration, and audited ESG carbon diversion.</p>
            <div class="abt-pedestal-points">
              <div><i class="fas fa-check"></i> Post-Summit C-Suite Recall Audits</div>
              <div><i class="fas fa-check"></i> Verified Scope 1-3 Carbon Accounting</div>
              <div><i class="fas fa-check"></i> Media & Stakeholder Sentiment Tracking</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 4: LEADERSHIP TEAM (EXECUTIVE COUNCIL QUAD-MOSAIC)
         ===================================================================== -->
    <section id="leadership-team" class="abt-section-leadership">
      <div class="abt-container">
        <!-- Section Header -->
        <div class="abt-section-head framer-council-quad">
          <div class="abt-badge"><i class="fas fa-users-gear"></i> Executive Council</div>
          <h2 class="abt-title">Executive Leadership & <span class="abt-title-gradient">Council of Architects</span></h2>
          <p class="abt-subtitle">Meet the visionary strategists, acousticians, and operational commanders directing our global conference production operations.</p>
        </div>

        <div class="abt-council-mosaic-grid">
          <!-- Leader 1 -->
          <div class="abt-leader-card framer-council-quad">
            <div class="abt-leader-img-box">
              <img src="images/leader_julian.jpg" alt="Julian Vance - Chief Executive Officer">
            </div>
            <div class="abt-leader-body">
              <span class="abt-leader-role">Founder & CEO</span>
              <h4 class="abt-leader-name">Julian Vance</h4>
              <p class="abt-leader-bio">Former G8 Summit protocol lead with 24 years directing world economic plenaries and sovereign state functions.</p>
              <div class="abt-leader-footer">
                <span class="abt-leader-credential"><i class="fas fa-shield"></i> Protocol Master</span>
                <span class="abt-leader-btn" onclick="openBioModal('Julian Vance', 'Founder & Chief Executive Officer', 'Julian Vance established Apex in 2012 following a distinguished decade advising heads of state on multilateral summit coordination. Under his stewardship, Apex has managed over 1,850 international conferences without a single security breach or broadcast interruption.')">
                  Bio <i class="fas fa-arrow-right"></i>
                </span>
              </div>
            </div>
          </div>

          <!-- Leader 2 -->
          <div class="abt-leader-card framer-council-quad">
            <div class="abt-leader-img-box">
              <img src="images/leader_sophia.jpg" alt="Dr. Sophia Sterling - Chief Strategy Officer">
            </div>
            <div class="abt-leader-body">
              <span class="abt-leader-role">Chief Strategy Officer</span>
              <h4 class="abt-leader-name">Dr. Sophia Sterling</h4>
              <p class="abt-leader-bio">Ph.D. in Architectural Acoustics from MIT; pioneer of cognitive neurodesign in keynote plenary atmospheres.</p>
              <div class="abt-leader-footer">
                <span class="abt-leader-credential"><i class="fas fa-wave-square"></i> Acoustic Fellow</span>
                <span class="abt-leader-btn" onclick="openBioModal('Dr. Sophia Sterling', 'Chief Strategy Officer', 'Dr. Sophia Sterling leads spatial architecture at Apex, engineering venues where acoustics, illumination, and circulation maximize neurological engagement and audience retention.')">
                  Bio <i class="fas fa-arrow-right"></i>
                </span>
              </div>
            </div>
          </div>

          <!-- Leader 3 -->
          <div class="abt-leader-card framer-council-quad">
            <div class="abt-leader-img-box">
              <img src="images/leader_marcus.jpg" alt="Marcus Chen - VP of Global Operations">
            </div>
            <div class="abt-leader-body">
              <span class="abt-leader-role">VP Global Operations</span>
              <h4 class="abt-leader-name">Marcus Chen</h4>
              <p class="abt-leader-bio">Emmy Award-winning broadcast producer; manages our worldwide N+2 redundant hardware rigs and satellite uplinks.</p>
              <div class="abt-leader-footer">
                <span class="abt-leader-credential"><i class="fas fa-satellite"></i> Broadcast Master</span>
                <span class="abt-leader-btn" onclick="openBioModal('Marcus Chen', 'VP of Global Operations & Broadcast', 'Marcus Chen commands Apex on-site engineering crews across Europe, North America, and the Asia-Pacific. He holds 12 patents in low-latency IP broadcast signal routing.')">
                  Bio <i class="fas fa-arrow-right"></i>
                </span>
              </div>
            </div>
          </div>

          <!-- Leader 4 -->
          <div class="abt-leader-card framer-council-quad">
            <div class="abt-leader-img-box">
              <img src="images/leader_amara.jpg" alt="Amara Patel - Head of ESG Production">
            </div>
            <div class="abt-leader-body">
              <span class="abt-leader-role">Head of ESG & Safety</span>
              <h4 class="abt-leader-name">Amara Patel</h4>
              <p class="abt-leader-bio">Lead auditor for ISO-20121 sustainable events; author of the Corporate Net-Zero Event Blueprint.</p>
              <div class="abt-leader-footer">
                <span class="abt-leader-credential"><i class="fas fa-leaf"></i> ISO-20121 Auditor</span>
                <span class="abt-leader-btn" onclick="openBioModal('Amara Patel', 'Head of Sustainable Production & ESG', 'Amara Patel oversees Apex zero-waste and carbon-neutral initiatives, ensuring all partner events achieve auditable ESG compliance with zero single-use plastics.')">
                  Bio <i class="fas fa-arrow-right"></i>
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 5: SPECIALISTS (DIVISION COMMAND MATRIX)
         ===================================================================== -->
    <section id="specialists" class="abt-section-specialists">
      <div class="abt-container">
        <!-- Section Header -->
        <div class="abt-section-head framer-division-matrix">
          <div class="abt-badge"><i class="fas fa-people-group"></i> Operations Fleet</div>
          <h2 class="abt-title">Specialist Corps & <span class="abt-title-gradient">Command Divisions</span></h2>
          <p class="abt-subtitle">Over 280 dedicated in-house technical directors, spatial acousticians, and bilingual protocol marshals deployed across our global hubs.</p>
        </div>

        <div class="abt-division-matrix-grid">
          <!-- Visual Card -->
          <div class="abt-specialists-visual-card framer-division-matrix">
            <div class="abt-spec-img-box">
              <img src="images/about_specialists.jpg" alt="Specialist Operations Control Center">
              <div class="abt-spec-badge-floating">
                <i class="fas fa-headset text-warning"></i> 24/7 Global Dispatch Active
              </div>
            </div>
          </div>

          <!-- Divisions Stack -->
          <div class="abt-divisions-stack">
            <!-- Division 1 -->
            <div class="abt-division-card active framer-division-matrix" onclick="selectDivision(this, 'AV')">
              <div class="abt-div-head">
                <span class="abt-div-tag">Division Alpha</span>
                <span style="font-size: 0.8rem; font-weight: 700; color: var(--abt-text-muted);"><i class="fas fa-users"></i> 110 Engineers</span>
              </div>
              <h4 class="abt-div-title">AV, Rigging & Spatial Acoustic Engineering</h4>
              <p class="abt-div-desc">Certified Dante Level 3 audio engineers, Disguise media server operators, and certified structural riggers managing stagecraft loads up to 45,000 lbs.</p>
            </div>

            <!-- Division 2 -->
            <div class="abt-division-card framer-division-matrix" onclick="selectDivision(this, 'Protocol')">
              <div class="abt-div-head">
                <span class="abt-div-tag">Division Bravo</span>
                <span style="font-size: 0.8rem; font-weight: 700; color: var(--abt-text-muted);"><i class="fas fa-users"></i> 85 Officers</span>
              </div>
              <h4 class="abt-div-title">Diplomatic Protocol & Executive Protection Detachment</h4>
              <p class="abt-div-desc">Bilingual marshals and executive security coordinators trained in head-of-state motorcade movements, secret service liaisons, and private green room security.</p>
            </div>

            <!-- Division 3 -->
            <div class="abt-division-card framer-division-matrix" onclick="selectDivision(this, 'Broadcast')">
              <div class="abt-div-head">
                <span class="abt-div-tag">Division Charlie</span>
                <span style="font-size: 0.8rem; font-weight: 700; color: var(--abt-text-muted);"><i class="fas fa-users"></i> 65 Specialists</span>
              </div>
              <h4 class="abt-div-title">Hybrid Satellite & Real-Time Cloud Ingest</h4>
              <p class="abt-div-desc">Broadcasting engineers operating bonded satellite trucks and dual SRT pipelines delivering sub-45ms latency across 18 simultaneous translation languages.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 6: CLIENT PORTFOLIO (MARQUEE SUMMITS & SECTOR ROSTER)
         ===================================================================== -->
    <section id="client-portfolio" class="abt-section-portfolio">
      <div class="abt-container">
        <!-- Section Header -->
        <div class="abt-section-head framer-marquee-portfolio">
          <div class="abt-badge"><i class="fas fa-briefcase"></i> Enterprise Roster</div>
          <h2 class="abt-title">Client Portfolio & <span class="abt-title-gradient">Marquee Summits</span></h2>
          <p class="abt-subtitle">Trusted by Fortune 500 corporations, sovereign wealth forums, and breakthrough global technology enterprises worldwide.</p>
        </div>

        <div class="abt-portfolio-marquee-grid">
          <!-- Left Hero Card -->
          <div class="abt-portfolio-hero-card framer-marquee-portfolio">
            <div class="abt-port-img-box">
              <img src="images/about_portfolio.jpg" alt="Marquee Corporate Summit Assembly">
            </div>
            <div class="abt-port-body">
              <p class="abt-port-quote">"Apex does not merely execute logistics—they elevated our global developer conference into a historic market catalyst with precision that left our board breathless."</p>
              <div class="abt-port-author">— Chief Executive Officer, Fortune 50 Enterprise Cloud Platform</div>
            </div>
          </div>

          <!-- Right Sectors Grid -->
          <div class="abt-sectors-deck">
            <!-- Sector 1 -->
            <div class="abt-sector-card framer-marquee-portfolio">
              <div class="abt-sec-icon"><i class="fas fa-cloud"></i></div>
              <h4 class="abt-sec-title">Enterprise Cloud & AI</h4>
              <div class="abt-sec-clients">Apex Cloud Technologies, Quantum BioVentures, Synapse AI Flagship Summit</div>
            </div>

            <!-- Sector 2 -->
            <div class="abt-sector-card framer-marquee-portfolio">
              <div class="abt-sec-icon"><i class="fas fa-chart-line"></i></div>
              <h4 class="abt-sec-title">FinTech & Capital</h4>
              <div class="abt-sec-clients">Horizon FinTech Global, Swiss-Atlantic Capital, Sovereign Wealth Annual Forum</div>
            </div>

            <!-- Sector 3 -->
            <div class="abt-sector-card framer-marquee-portfolio">
              <div class="abt-sec-icon"><i class="fas fa-dna"></i></div>
              <h4 class="abt-sec-title">Life Sciences & Pharma</h4>
              <div class="abt-sec-clients">Aura BioGenomics, Global Healthcare Vanguard, NextGen Oncology Assembly</div>
            </div>

            <!-- Sector 4 -->
            <div class="abt-sector-card framer-marquee-portfolio">
              <div class="abt-sec-icon"><i class="fas fa-car"></i></div>
              <h4 class="abt-sec-title">Mobility & Aerospace</h4>
              <div class="abt-sec-clients">Vanguard Aerospace, Electra Hypercars, Global Autonomous Summit</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 7: SAFETY & ADVANTAGE (INSTITUTIONAL CITADEL & MOAT)
         ===================================================================== -->
    <section id="safety-advantage" class="abt-section-safety">
      <div class="abt-container">
        <!-- Section Header -->
        <div class="abt-section-head framer-citadel-moat">
          <div class="abt-badge"><i class="fas fa-shield-halved"></i> Institutional Trust</div>
          <h2 class="abt-title">Safety Standards & <span class="abt-title-gradient">Our Competitive Moat</span></h2>
          <p class="abt-subtitle">Our uncompromising commitment to structural safety, data encryption, financial escrow, and sustainability sets us fundamentally apart.</p>
        </div>

        <div class="abt-citadel-split-grid">
          <!-- Left Citadel Card -->
          <div class="abt-citadel-visual-card framer-citadel-moat">
            <div class="abt-citadel-img-box">
              <img src="images/about_safety.jpg" alt="Quality and Safety Citadel Framework">
            </div>
            <div class="abt-citadel-body">
              <h4 class="abt-citadel-title">The Quality Assurance Citadel</h4>
              <p class="abt-citadel-desc">Every event blueprint undergoes a rigorous 42-point safety audit before ground is broken or staging trussing is raised.</p>
              <div class="abt-citadel-cert-list">
                <div><i class="fas fa-circle-check"></i> ISO-20121 Sustainable Event Certified</div>
                <div><i class="fas fa-circle-check"></i> ISO-9001 Quality Management Certified</div>
                <div><i class="fas fa-circle-check"></i> $50M Comprehensive Umbrella Policy</div>
                <div><i class="fas fa-circle-check"></i> NEBOSH Certified On-Site Safety Leads</div>
              </div>
            </div>
          </div>

          <!-- Right 4-Pillar Moat Grid -->
          <div class="abt-moat-grid">
            <div class="abt-moat-card framer-citadel-moat">
              <div class="abt-moat-icon"><i class="fas fa-server"></i></div>
              <h4 class="abt-moat-title">N+2 Hardware Redundancy</h4>
              <p class="abt-moat-desc">Zero single points of failure. Every power feed, video switcher, and microphone has hot-swap automated backups.</p>
            </div>
            <div class="abt-moat-card framer-citadel-moat">
              <div class="abt-moat-icon"><i class="fas fa-scale-balanced"></i></div>
              <h4 class="abt-moat-title">Open-Book Fiscal Governance</h4>
              <p class="abt-moat-desc">100% transparent itemized invoicing. All negotiated volume rebates from venue and hotel partners are credited back to clients.</p>
            </div>
            <div class="abt-moat-card framer-citadel-moat">
              <div class="abt-moat-icon"><i class="fas fa-bolt"></i></div>
              <h4 class="abt-moat-title">Rapid Rapid-Deployment</h4>
              <p class="abt-moat-desc">Full turn-key stadium staging and broadcast control centers deployed anywhere in the world within 21 business days.</p>
            </div>
            <div class="abt-moat-card framer-citadel-moat">
              <div class="abt-moat-icon"><i class="fas fa-leaf"></i></div>
              <h4 class="abt-moat-title">Carbon-Neutral Guarantee</h4>
              <p class="abt-moat-desc">Audited Scope 1-3 carbon tracking with verified offsets and 100% diversion of leftover banquet meals to local food rescues.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Interactive Executive Bio Modal -->
  <div id="abtBioModal" class="abt-modal-overlay">
    <div class="abt-modal-card">
      <button class="abt-modal-close" onclick="closeAbtModal()">&times;</button>
      <div style="width: 3.5rem; height: 3.5rem; border-radius: 0.85rem; background: var(--abt-accent-glow); color: var(--abt-accent); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; margin-bottom: 1.25rem;">
        <i class="fas fa-id-badge"></i>
      </div>
      <h3 id="abtModalName" style="font-size: 1.4rem; font-weight: 800; color: var(--abt-text-main); margin-bottom: 0.25rem;">Executive Bio</h3>
      <div id="abtModalRole" style="font-size: 0.85rem; font-weight: 700; color: var(--abt-accent); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">Role</div>
      <p id="abtModalDesc" style="font-size: 0.95rem; color: var(--abt-text-muted); line-height: 1.6; margin-bottom: 1.5rem;">Dossier description</p>
      <button class="abt-btn abt-btn-primary" style="width: 100%;" onclick="closeAbtModal()">Close Executive Dossier</button>
    </div>
  </div>
"""

    # Page Interactive Scripts
    new_abt_scripts = """
  <!-- =====================================================================
       INTERACTIVE ABOUT PAGE CONTROLLER SCRIPT
       ===================================================================== -->
  <script>
    // 1. Intersection Observer for Unique Framer Motion Animations
    document.addEventListener('DOMContentLoaded', function() {
      var framerElements = document.querySelectorAll(
        '.framer-epoch-chronicle, ' +
        '.framer-polarity-gyro, ' +
        '.framer-triad-pedestal, ' +
        '.framer-council-quad, ' +
        '.framer-division-matrix, ' +
        '.framer-marquee-portfolio, ' +
        '.framer-citadel-moat'
      );

      var observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('framer-in-view');
          }
        });
      }, {
        threshold: 0.12,
        rootMargin: '0px 0px -40px 0px'
      });

      framerElements.forEach(function(el) {
        observer.observe(el);
      });
    });

    // 2. Epoch Timeline Selector
    function selectEpoch(card, era) {
      var cards = document.querySelectorAll('.abt-epoch-card');
      cards.forEach(function(c) { c.classList.remove('active'); });
      card.classList.add('active');
    }

    // 3. Division Selector
    function selectDivision(card, divName) {
      var cards = document.querySelectorAll('.abt-division-card');
      cards.forEach(function(c) { c.classList.remove('active'); });
      card.classList.add('active');
    }

    // 4. Executive Bio Modal
    function openBioModal(name, role, desc) {
      var modal = document.getElementById('abtBioModal');
      var nameEl = document.getElementById('abtModalName');
      var roleEl = document.getElementById('abtModalRole');
      var descEl = document.getElementById('abtModalDesc');

      if (nameEl) nameEl.textContent = name;
      if (roleEl) roleEl.textContent = role;
      if (descEl) descEl.textContent = desc;
      if (modal) modal.style.display = 'flex';
    }

    function closeAbtModal() {
      var modal = document.getElementById('abtBioModal');
      if (modal) modal.style.display = 'none';
    }
  </script>
"""

    # Assemble complete document
    final_html = (
        nav_head_up_to_style
        + new_abt_css
        + "\n  </style>"
        + nav_mid[len("</style>"):]
        + new_abt_content
        + footer_full
        + new_abt_scripts
        + closing_part
    )

    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print("Successfully built redesigned about.html! Total length:", len(final_html))

if __name__ == '__main__':
    generate_about()
