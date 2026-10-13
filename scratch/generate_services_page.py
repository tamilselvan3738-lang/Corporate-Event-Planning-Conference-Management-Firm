import os

def generate_services():
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

    # CSS for the new services.html layout
    new_srv_css = """
    /* =====================================================================
       REDESIGNED SERVICES ARCHITECTURE: ENTERPRISE CAPABILITY SUITE
       Supports Light Mode, Dark Mode (body.dark), and RTL (body.rtl)
       ===================================================================== */
    :root {
      --srv-primary: #1e3a8a;
      --srv-primary-dark: #0f172a;
      --srv-accent: #d97706;
      --srv-accent-light: #fbbf24;
      --srv-accent-glow: rgba(217, 119, 6, 0.16);
      --srv-teal: #0d9488;
      --srv-teal-glow: rgba(13, 148, 136, 0.16);
      --srv-emerald: #059669;
      --srv-emerald-glow: rgba(5, 150, 105, 0.16);
      --srv-indigo: #4338ca;
      --srv-indigo-glow: rgba(67, 56, 202, 0.16);
      --srv-bg: #f8fafc;
      --srv-surface: #ffffff;
      --srv-surface-muted: #f1f5f9;
      --srv-card-border: #e2e8f0;
      --srv-text-main: #0f172a;
      --srv-text-muted: #64748b;
      --srv-text-light: #94a3b8;
      --srv-gold-gradient: linear-gradient(135deg, #b45309 0%, #d97706 50%, #f59e0b 100%);
      --srv-blue-gradient: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      --srv-teal-gradient: linear-gradient(135deg, #0f766e 0%, #0d9488 100%);
      --srv-shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --srv-shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.07), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
      --srv-shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      --srv-shadow-glow: 0 0 25px rgba(217, 119, 6, 0.22);
    }

    body.dark {
      --srv-bg: #070b14;
      --srv-surface: #0f172a;
      --srv-surface-muted: #131d33;
      --srv-card-border: #1e293b;
      --srv-text-main: #f8fafc;
      --srv-text-muted: #94a3b8;
      --srv-text-light: #64748b;
      --srv-blue-gradient: linear-gradient(135deg, #070b14 0%, #172554 100%);
    }

    /* RTL Support */
    body.rtl .srv-section-head { text-align: right; }
    body.rtl .srv-badge i { margin-left: 0.5rem; margin-right: 0; }
    body.rtl .srv-btn i { margin-right: 0.5rem; margin-left: 0; }

    /* Base Container */
    .srv-page-wrap {
      background-color: var(--srv-bg);
      color: var(--srv-text-main);
      font-family: 'Inter', system-ui, sans-serif;
      overflow-x: hidden;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    .srv-container {
      max-width: 1320px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }

    /* SECTION HEADER STYLING */
    .srv-section-head {
      margin-bottom: 3.5rem;
      position: relative;
    }

    .srv-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.45rem 1.1rem;
      border-radius: 9999px;
      background: var(--srv-accent-glow);
      color: var(--srv-accent);
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 1rem;
      border: 1px solid rgba(217, 119, 6, 0.3);
    }

    .srv-title {
      font-size: 2.5rem;
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.025em;
      color: var(--srv-text-main);
      margin-bottom: 1rem;
    }

    .srv-title-gradient {
      background: var(--srv-gold-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .srv-subtitle {
      font-size: 1.1rem;
      color: var(--srv-text-muted);
      max-width: 760px;
      line-height: 1.65;
    }

    /* BUTTONS */
    .srv-btn {
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

    .srv-btn-primary {
      background: var(--srv-gold-gradient);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(217, 119, 6, 0.35);
    }

    .srv-btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(217, 119, 6, 0.45);
      color: #ffffff;
    }

    .srv-btn-outline {
      background: transparent;
      color: var(--srv-text-main);
      border-color: var(--srv-card-border);
    }

    .srv-btn-outline:hover {
      border-color: var(--srv-accent);
      color: var(--srv-accent);
      background: var(--srv-accent-glow);
    }

    /* =====================================================================
       FRAMER MOTION SPECIFIC CLASSES & KEYFRAMES (1 PER SECTION)
       ===================================================================== */

    /* 1. Corporate Event Management: .framer-boardroom-elevation */
    .framer-boardroom-elevation {
      opacity: 0;
      transform: translateY(35px) perspective(1000px) rotateX(3deg);
      transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1),
                  transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .framer-boardroom-elevation.framer-in-view {
      opacity: 1;
      transform: translateY(0) perspective(1000px) rotateX(0deg);
    }

    /* 2. Conference Management: .framer-plenary-amphitheater */
    .framer-plenary-amphitheater {
      opacity: 0;
      transform: scale(0.96) translateY(30px);
      transition: opacity 0.75s cubic-bezier(0.22, 1, 0.36, 1),
                  transform 0.75s cubic-bezier(0.22, 1, 0.36, 1);
    }
    .framer-plenary-amphitheater.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    /* 3. Venue Sourcing: .framer-spatial-cadence */
    .framer-spatial-cadence {
      opacity: 0;
      transform: translateX(-35px) scale(0.98);
      transition: opacity 0.8s cubic-bezier(0.19, 1, 0.22, 1),
                  transform 0.8s cubic-bezier(0.19, 1, 0.22, 1);
    }
    .framer-spatial-cadence.framer-in-view {
      opacity: 1;
      transform: translateX(0) scale(1);
    }

    /* 4. Audio-Visual Production: .framer-broadcast-matrix */
    .framer-broadcast-matrix {
      opacity: 0;
      transform: translateY(35px) scale(0.97);
      transition: opacity 0.85s cubic-bezier(0.34, 1.56, 0.64, 1),
                  transform 0.85s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .framer-broadcast-matrix.framer-in-view {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    /* 5. Event Design & Branding: .framer-sculptural-prism */
    .framer-sculptural-prism {
      opacity: 0;
      transform: rotate(-1.5deg) scale(0.96);
      transition: opacity 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                  transform 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    .framer-sculptural-prism.framer-in-view {
      opacity: 1;
      transform: rotate(0deg) scale(1);
    }

    /* 6. Catering & Hospitality: .framer-gastronomic-concierge */
    .framer-gastronomic-concierge {
      opacity: 0;
      transform: translateY(40px);
      filter: blur(3px);
      transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1),
                  transform 0.8s cubic-bezier(0.16, 1, 0.3, 1),
                  filter 0.8s ease;
    }
    .framer-gastronomic-concierge.framer-in-view {
      opacity: 1;
      transform: translateY(0);
      filter: blur(0px);
    }

    /* 7. Delegate Logistics: .framer-concourse-dispatch */
    .framer-concourse-dispatch {
      opacity: 0;
      transform: translateY(30px) scale(0.98);
      transition: opacity 0.7s cubic-bezier(0.33, 1, 0.68, 1),
                  transform 0.7s cubic-bezier(0.33, 1, 0.68, 1);
    }
    .framer-concourse-dispatch.framer-in-view {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    /* =====================================================================
       SECTION 1: CORPORATE EVENT MANAGEMENT - BOARDROOM COMMAND VIEWPORT
       ===================================================================== */
    .srv-section-corporate {
      padding: 6rem 0;
      position: relative;
    }

    .srv-metric-banner-5 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.5rem;
      background: var(--srv-surface);
      border: 1px solid var(--srv-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem 2rem;
      box-shadow: var(--srv-shadow-sm);
      margin-bottom: 3rem;
    }

    .srv-mitem {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .srv-micon {
      width: 2.75rem;
      height: 2.75rem;
      border-radius: 0.75rem;
      background: var(--srv-accent-glow);
      color: var(--srv-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
    }

    .srv-mval {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--srv-text-main);
      line-height: 1.2;
    }

    .srv-mlbl {
      font-size: 0.78rem;
      color: var(--srv-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .srv-boardroom-grid {
      display: grid;
      grid-template-columns: 1.15fr 1.25fr;
      gap: 2.5rem;
      align-items: center;
    }

    .srv-boardroom-visual-card {
      background: var(--srv-surface);
      border: 1px solid var(--srv-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--srv-shadow-md);
      position: relative;
    }

    .srv-bimg-wrap {
      height: 480px;
      position: relative;
      overflow: hidden;
    }

    .srv-bimg-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s ease;
    }

    .srv-boardroom-visual-card:hover .srv-bimg-wrap img {
      transform: scale(1.04);
    }

    .srv-boardroom-floating-tag {
      position: absolute;
      top: 1.25rem;
      left: 1.25rem;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(8px);
      padding: 0.45rem 1rem;
      border-radius: 9999px;
      color: #fbbf24;
      font-size: 0.8rem;
      font-weight: 700;
      border: 1px solid rgba(251, 191, 36, 0.3);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    /* 5-Quadrant Tiered Array */
    .srv-quadrant-stack {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    .srv-quadrant-card {
      background: var(--srv-surface);
      border: 1px solid var(--srv-card-border);
      border-radius: 1.25rem;
      padding: 1.4rem 1.75rem;
      box-shadow: var(--srv-shadow-sm);
      transition: all 0.25s ease;
      cursor: pointer;
    }

    .srv-quadrant-card:hover,
    .srv-quadrant-card.active {
      border-color: var(--srv-accent);
      box-shadow: var(--srv-shadow-md);
      transform: translateX(4px);
    }

    body.rtl .srv-quadrant-card:hover,
    body.rtl .srv-quadrant-card.active {
      transform: translateX(-4px);
    }

    .srv-qtop {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.35rem;
    }

    .srv-qbadge {
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--srv-accent);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .srv-qscope {
      font-size: 0.75rem;
      color: var(--srv-text-muted);
      font-weight: 600;
    }

    .srv-qtitle {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--srv-text-main);
      margin-bottom: 0.35rem;
    }

    .srv-qdesc {
      font-size: 0.88rem;
      color: var(--srv-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 2: CONFERENCE MANAGEMENT - PLENARY AMPHITHEATER & 5-PILLARS
       ===================================================================== */
    .srv-section-conference {
      padding: 6rem 0;
      background: var(--srv-surface-muted);
      border-top: 1px solid var(--srv-card-border);
      border-bottom: 1px solid var(--srv-card-border);
    }

    .srv-amphitheater-showcase {
      background: var(--srv-surface);
      border: 1px solid var(--srv-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--srv-shadow-md);
      margin-bottom: 3rem;
    }

    .srv-amp-img-box {
      height: 440px;
      position: relative;
      overflow: hidden;
    }

    .srv-amp-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .srv-amp-overlay-ribbon {
      position: absolute;
      bottom: 1.5rem;
      left: 1.5rem;
      right: 1.5rem;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(10px);
      padding: 1.25rem 2rem;
      border-radius: 1rem;
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.2);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .srv-amp-stat-group {
      display: flex;
      align-items: center;
      gap: 2rem;
    }

    .srv-amp-stat-item {
      display: flex;
      flex-direction: column;
    }

    .srv-amp-sval {
      font-size: 1.2rem;
      font-weight: 800;
      color: #fbbf24;
    }

    .srv-amp-slbl {
      font-size: 0.75rem;
      color: #cbd5e1;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* 5-Pillar Horizontal Conference Architecture Deck */
    .srv-conf-pillars-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 1.5rem;
    }

    .srv-cpillar-card {
      background: var(--srv-surface);
      border: 1px solid var(--srv-card-border);
      border-radius: 1.25rem;
      padding: 1.75rem;
      box-shadow: var(--srv-shadow-sm);
      display: flex;
      flex-direction: column;
      transition: all 0.25s ease;
    }

    .srv-cpillar-card:hover {
      transform: translateY(-5px);
      box-shadow: var(--srv-shadow-md);
      border-color: var(--srv-accent);
    }

    .srv-cpillar-icon {
      width: 2.75rem;
      height: 2.75rem;
      border-radius: 0.75rem;
      background: var(--srv-accent-glow);
      color: var(--srv-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
      margin-bottom: 1.25rem;
    }

    .srv-cpillar-title {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--srv-text-main);
      margin-bottom: 0.5rem;
    }

    .srv-cpillar-desc {
      font-size: 0.85rem;
      color: var(--srv-text-muted);
      line-height: 1.55;
    }

    /* =====================================================================
       SECTION 3: VENUE SOURCING - SPATIAL GEOMETRY & 5-DIMENSION VAULT
       ===================================================================== */
    .srv-section-venue {
      padding: 6rem 0;
      position: relative;
    }

    .srv-venue-split-grid {
      display: grid;
      grid-template-columns: 1.1fr 1fr;
      gap: 2.5rem;
      align-items: center;
    }

    .srv-venue-visual-frame {
      background: var(--srv-surface);
      border: 1px solid var(--srv-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--srv-shadow-md);
    }

    .srv-vimg-wrap {
      height: 460px;
      position: relative;
      overflow: hidden;
    }

    .srv-vimg-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .srv-vblueprint-overlay {
      position: absolute;
      top: 1.25rem;
      left: 1.25rem;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(8px);
      padding: 0.5rem 1.2rem;
      border-radius: 9999px;
      color: #38bdf8;
      font-size: 0.8rem;
      font-weight: 700;
      border: 1px solid rgba(56, 189, 248, 0.3);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .srv-venue-category-stack {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    .srv-vcat-card {
      background: var(--srv-surface);
      border: 1px solid var(--srv-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem 1.75rem;
      box-shadow: var(--srv-shadow-sm);
      transition: all 0.25s ease;
      cursor: pointer;
    }

    .srv-vcat-card:hover,
    .srv-vcat-card.active {
      border-color: var(--srv-teal);
      box-shadow: var(--srv-shadow-md);
      transform: translateX(4px);
    }

    body.rtl .srv-vcat-card:hover,
    body.rtl .srv-vcat-card.active {
      transform: translateX(-4px);
    }

    .srv-vcat-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.35rem;
    }

    .srv-vcat-tag {
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--srv-teal);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .srv-vcat-title {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--srv-text-main);
      margin-bottom: 0.35rem;
    }

    .srv-vcat-desc {
      font-size: 0.88rem;
      color: var(--srv-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 4: AUDIO-VISUAL PRODUCTION - BROADCAST SYNTHESIS CONSOLE
       ===================================================================== */
    .srv-section-av {
      padding: 6rem 0;
      background: var(--srv-surface-muted);
      border-top: 1px solid var(--srv-card-border);
      border-bottom: 1px solid var(--srv-card-border);
    }

    .srv-av-console-grid {
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 2.5rem;
      align-items: start;
    }

    .srv-av-monitor-card {
      background: var(--srv-surface);
      border: 1px solid var(--srv-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--srv-shadow-md);
    }

    .srv-av-screen-box {
      height: 380px;
      position: relative;
      overflow: hidden;
    }

    .srv-av-screen-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .srv-av-tally-bar {
      position: absolute;
      top: 1.25rem;
      right: 1.25rem;
      background: rgba(15, 23, 42, 0.9);
      padding: 0.4rem 0.9rem;
      border-radius: 9999px;
      color: #ef4444;
      font-size: 0.78rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      border: 1px solid rgba(239, 68, 68, 0.4);
    }

    .srv-av-layer-deck {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    .srv-layer-card {
      background: var(--srv-surface);
      border: 1px solid var(--srv-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem 1.75rem;
      box-shadow: var(--srv-shadow-sm);
      transition: all 0.25s ease;
    }

    .srv-layer-card:hover {
      border-color: var(--srv-accent);
      transform: translateX(4px);
    }

    body.rtl .srv-layer-card:hover {
      transform: translateX(-4px);
    }

    .srv-layer-title {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--srv-text-main);
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .srv-layer-title i {
      color: var(--srv-accent);
    }

    .srv-layer-desc {
      font-size: 0.88rem;
      color: var(--srv-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 5: EVENT DESIGN & BRANDING - SCULPTURAL PRISM ATELIER
       ===================================================================== */
    .srv-section-design {
      padding: 6rem 0;
      position: relative;
    }

    .srv-design-grid {
      display: grid;
      grid-template-columns: 1.1fr 1.1fr;
      gap: 2.5rem;
      align-items: center;
    }

    .srv-design-visual-card {
      background: var(--srv-surface);
      border: 1px solid var(--srv-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--srv-shadow-md);
    }

    .srv-dimg-wrap {
      height: 460px;
      position: relative;
      overflow: hidden;
    }

    .srv-dimg-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .srv-design-pillars-stack {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    .srv-dpillar-card {
      background: var(--srv-surface);
      border: 1px solid var(--srv-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem 1.75rem;
      box-shadow: var(--srv-shadow-sm);
      transition: all 0.25s ease;
    }

    .srv-dpillar-card:hover {
      border-color: var(--srv-accent);
      transform: translateX(4px);
    }

    body.rtl .srv-dpillar-card:hover {
      transform: translateX(-4px);
    }

    .srv-dpillar-title {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--srv-text-main);
      margin-bottom: 0.35rem;
    }

    .srv-dpillar-desc {
      font-size: 0.88rem;
      color: var(--srv-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 6: CATERING & HOSPITALITY - GASTRONOMIC CONCIERGE ATELIER
       ===================================================================== */
    .srv-section-hospitality {
      padding: 6rem 0;
      background: var(--srv-surface-muted);
      border-top: 1px solid var(--srv-card-border);
      border-bottom: 1px solid var(--srv-card-border);
    }

    .srv-hospitality-3col-grid {
      display: grid;
      grid-template-columns: 1fr 1.2fr 1fr;
      gap: 2rem;
      align-items: center;
    }

    .srv-hosp-side-card {
      background: var(--srv-surface);
      border: 1px solid var(--srv-card-border);
      border-radius: 1.5rem;
      padding: 2rem;
      box-shadow: var(--srv-shadow-sm);
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    .srv-hosp-center-card {
      background: var(--srv-surface);
      border: 2px solid var(--srv-accent);
      border-radius: 2rem;
      overflow: hidden;
      box-shadow: 0 0 35px rgba(217, 119, 6, 0.25);
      position: relative;
    }

    .srv-himg-wrap {
      height: 440px;
      position: relative;
      overflow: hidden;
    }

    .srv-himg-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .srv-hitem-box h4 {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--srv-text-main);
      margin-bottom: 0.35rem;
    }

    .srv-hitem-box p {
      font-size: 0.88rem;
      color: var(--srv-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 7: DELEGATE LOGISTICS - CONCOURSE & OPERATIONS COMMAND
       ===================================================================== */
    .srv-section-logistics {
      padding: 6rem 0;
      position: relative;
    }

    .srv-logistics-split-grid {
      display: grid;
      grid-template-columns: 1.15fr 1.2fr;
      gap: 2.5rem;
      align-items: center;
    }

    .srv-logistics-visual-card {
      background: var(--srv-surface);
      border: 1px solid var(--srv-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--srv-shadow-md);
      position: relative;
    }

    .srv-limg-wrap {
      height: 480px;
      position: relative;
      overflow: hidden;
    }

    .srv-limg-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .srv-logistics-wings-stack {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    .srv-lwing-card {
      background: var(--srv-surface);
      border: 1px solid var(--srv-card-border);
      border-radius: 1.25rem;
      padding: 1.75rem;
      box-shadow: var(--srv-shadow-sm);
    }

    .srv-lwing-title {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--srv-text-main);
      margin-bottom: 1rem;
      padding-bottom: 0.75rem;
      border-bottom: 1px solid var(--srv-card-border);
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .srv-lwing-title i {
      color: var(--srv-accent);
    }

    .srv-lwing-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .srv-lrow {
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      font-size: 0.88rem;
      color: var(--srv-text-main);
    }

    .srv-lrow i {
      color: var(--srv-emerald);
      margin-top: 0.2rem;
    }

    /* Interactive Service Quote Modal */
    .srv-modal-overlay {
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

    .srv-modal-card {
      background: var(--srv-surface);
      border: 1px solid var(--srv-card-border);
      border-radius: 1.5rem;
      max-width: 540px;
      width: 100%;
      padding: 2.5rem;
      box-shadow: var(--srv-shadow-lg);
      position: relative;
      text-align: center;
    }

    .srv-modal-close {
      position: absolute;
      top: 1.25rem;
      right: 1.25rem;
      background: transparent;
      border: none;
      color: var(--srv-text-muted);
      font-size: 1.25rem;
      cursor: pointer;
    }

    body.rtl .srv-modal-close {
      right: auto;
      left: 1.25rem;
    }

    /* Responsive Queries */
    @media (max-width: 1100px) {
      .srv-metric-banner-5 { grid-template-columns: repeat(2, 1fr); }
      .srv-boardroom-grid { grid-template-columns: 1fr; }
      .srv-conf-pillars-grid { grid-template-columns: repeat(2, 1fr); }
      .srv-venue-split-grid { grid-template-columns: 1fr; }
      .srv-av-console-grid { grid-template-columns: 1fr; }
      .srv-design-grid { grid-template-columns: 1fr; }
      .srv-hospitality-3col-grid { grid-template-columns: 1fr; }
      .srv-logistics-split-grid { grid-template-columns: 1fr; }
    }

    @media (max-width: 768px) {
      .srv-metric-banner-5 { grid-template-columns: 1fr; }
      .srv-conf-pillars-grid { grid-template-columns: 1fr; }
      .srv-title { font-size: 2rem; }
      .srv-bimg-wrap { height: 320px; }
      .srv-amp-img-box { height: 280px; }
      .srv-vimg-wrap { height: 300px; }
      .srv-av-screen-box { height: 260px; }
      .srv-dimg-wrap { height: 300px; }
      .srv-himg-wrap { height: 300px; }
      .srv-limg-wrap { height: 300px; }
    }
"""

    # HTML for the redesigned services page
    new_srv_content = """
  <!-- MAIN SERVICES CONTENT WRAPPER -->
  <main class="srv-page-wrap">

    <!-- =====================================================================
         SECTION 1: CORPORATE EVENT MANAGEMENT (BOARDROOM COMMAND VIEWPORT)
         ===================================================================== -->
    <section id="corporate-events" class="srv-section-corporate">
      <div class="srv-container">
        <!-- Section Header -->
        <div class="srv-section-head framer-boardroom-elevation">
          <div class="srv-badge"><i class="fas fa-briefcase"></i> Enterprise Command</div>
          <h2 class="srv-title">Corporate Event Management & <span class="srv-title-gradient">Executive Assemblies</span></h2>
          <p class="srv-subtitle">From high-stakes board meetings and Annual General Meetings to milestone corporate jubilees and executive retreats, we deliver frictionless governance, confidentiality, and flawless execution.</p>
        </div>

        <!-- Capability Status Bar -->
        <div class="srv-metric-banner-5 framer-boardroom-elevation">
          <div class="srv-mitem">
            <div class="srv-micon"><i class="fas fa-handshake"></i></div>
            <div>
              <div class="srv-mval">1,200+</div>
              <div class="srv-mlbl">Corporate Gatherings</div>
            </div>
          </div>
          <div class="srv-mitem">
            <div class="srv-micon"><i class="fas fa-shield-halved"></i></div>
            <div>
              <div class="srv-mval">100% NDA</div>
              <div class="srv-mlbl">C-Suite Confidentiality</div>
            </div>
          </div>
          <div class="srv-mitem">
            <div class="srv-micon"><i class="fas fa-clock"></i></div>
            <div>
              <div class="srv-mval">99.8%</div>
              <div class="srv-mlbl">On-Schedule Run-of-Show</div>
            </div>
          </div>
          <div class="srv-mitem">
            <div class="srv-micon"><i class="fas fa-award"></i></div>
            <div>
              <div class="srv-mval">Fortune 100</div>
              <div class="srv-mlbl">Trusted By Industry Leaders</div>
            </div>
          </div>
        </div>

        <!-- Asymmetric Boardroom Command Viewport -->
        <div class="srv-boardroom-grid">
          <!-- Left Visual Frame -->
          <div class="srv-boardroom-visual-card framer-boardroom-elevation">
            <div class="srv-bimg-wrap">
              <img src="images/service_corporate_management.jpg" alt="Executive Corporate Board Meeting & Strategy Summit">
              <div class="srv-boardroom-floating-tag">
                <i class="fas fa-certificate"></i> Apex Executive Boardroom Command
              </div>
            </div>
          </div>

          <!-- Right 5-Quadrant Tiered Array -->
          <div class="srv-quadrant-stack">
            <!-- 1. Business Meetings -->
            <div class="srv-quadrant-card active framer-boardroom-elevation" onclick="highlightService(this, 'Business Meetings')">
              <div class="srv-qtop">
                <span class="srv-qbadge">Tier I • Executive Strategy</span>
                <span class="srv-qscope">Board of Directors & C-Suite</span>
              </div>
              <h4 class="srv-qtitle">Strategic Business Meetings</h4>
              <p class="srv-qdesc">SCIF-grade acoustic isolation, encrypted wireless audio feeds, confidential digital document distribution, and executive teleprompters for decisive board alignments.</p>
            </div>

            <!-- 2. Annual General Meetings -->
            <div class="srv-quadrant-card framer-boardroom-elevation" onclick="highlightService(this, 'Annual General Meetings')">
              <div class="srv-qtop">
                <span class="srv-qbadge">Tier II • Investor Governance</span>
                <span class="srv-qscope">Regulatory & Shareholder Compliant</span>
              </div>
              <h4 class="srv-qtitle">Annual General Meetings (AGM)</h4>
              <p class="srv-qdesc">Secure hybrid shareholder proxy voting, real-time audited ballot tabulation, certified video archival, and multi-channel Q&A moderation ensuring regulatory compliance.</p>
            </div>

            <!-- 3. Corporate Celebrations -->
            <div class="srv-quadrant-card framer-boardroom-elevation" onclick="highlightService(this, 'Corporate Celebrations')">
              <div class="srv-qtop">
                <span class="srv-qbadge">Tier III • Milestone Galas</span>
                <span class="srv-qscope">Jubilees & Award Evenings</span>
              </div>
              <h4 class="srv-qtitle">Corporate Celebrations & Jubilees</h4>
              <p class="srv-qdesc">High-production milestone celebrations, executive awards ceremonies, bespoke theatrical staging, and unforgettable culinary experiences honoring company achievements.</p>
            </div>

            <!-- 4. Executive Retreats -->
            <div class="srv-quadrant-card framer-boardroom-elevation" onclick="highlightService(this, 'Executive Retreats')">
              <div class="srv-qtop">
                <span class="srv-qbadge">Tier IV • Secluded Sanctuaries</span>
                <span class="srv-qscope">Private Mountain & Coastal Havens</span>
              </div>
              <h4 class="srv-qtitle">Executive Strategic Retreats</h4>
              <p class="srv-qdesc">Discreet sanctuary buyouts for top leadership councils, blending focused strategic workshops with private aviation, sommelier dinners, and biometric wellness.</p>
            </div>

            <!-- 5. Employee Engagement Events -->
            <div class="srv-quadrant-card framer-boardroom-elevation" onclick="highlightService(this, 'Employee Engagement Events')">
              <div class="srv-qtop">
                <span class="srv-qbadge">Tier V • Culture & Unity</span>
                <span class="srv-qscope">Townhalls & Team Synergy</span>
              </div>
              <h4 class="srv-qtitle">Employee Engagement Events</h4>
              <p class="srv-qdesc">Dynamic multi-hub company townhalls, interactive experiential activations, live gamification, and cultural celebrations designed to galvanize workforce morale.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 2: CONFERENCE MANAGEMENT (PLENARY AMPHITHEATER & 5-PILLARS)
         ===================================================================== -->
    <section id="conference-management" class="srv-section-conference">
      <div class="srv-container">
        <!-- Section Header -->
        <div class="srv-section-head framer-plenary-amphitheater">
          <div class="srv-badge"><i class="fas fa-landmark"></i> Large-Scale Conventions</div>
          <h2 class="srv-title">Conference Management & <span class="srv-title-gradient">Global Plenaries</span></h2>
          <p class="srv-subtitle">Orchestrating world-class international congresses, leadership summits, and multi-day convention experiences with synchronized stagecraft, simultaneous interpretation, and high-impact delegate engagement.</p>
        </div>

        <!-- Panoramic Plenary Stagecraft Deck -->
        <div class="srv-amphitheater-showcase framer-plenary-amphitheater">
          <div class="srv-amp-img-box">
            <img src="images/service_conference_management.jpg" alt="Grand International Conference Plenary Hall">
            <div class="srv-amp-overlay-ribbon">
              <div>
                <div style="font-size: 0.8rem; font-weight: 700; color: #fbbf24; text-transform: uppercase;">Flagship Arena Capability</div>
                <div style="font-size: 1.25rem; font-weight: 800;">Global Innovation Summit • Tier-1 Plenary Hall</div>
              </div>
              <div class="srv-amp-stat-group">
                <div class="srv-amp-stat-item">
                  <span class="srv-amp-sval">5,000+</span>
                  <span class="srv-amp-slbl">Plenary Capacity</span>
                </div>
                <div class="srv-amp-stat-item">
                  <span class="srv-amp-sval">18</span>
                  <span class="srv-amp-slbl">Translation Channels</span>
                </div>
                <div class="srv-amp-stat-item">
                  <span class="srv-amp-sval">4K120</span>
                  <span class="srv-amp-slbl">Curved Stage LED</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 5-Pillar Horizontal Conference Architecture Deck -->
        <div class="srv-conf-pillars-grid">
          <!-- 1. International Conferences -->
          <div class="srv-cpillar-card framer-plenary-amphitheater">
            <div class="srv-cpillar-icon"><i class="fas fa-globe"></i></div>
            <h4 class="srv-cpillar-title">International Conferences</h4>
            <p class="srv-cpillar-desc">Cross-border multilateral summits, diplomatic protocol, foreign delegation escorts, and ISO-standard bilingual interpretation.</p>
          </div>

          <!-- 2. Industry Conferences -->
          <div class="srv-cpillar-card framer-plenary-amphitheater">
            <div class="srv-cpillar-icon"><i class="fas fa-chart-pie"></i></div>
            <h4 class="srv-cpillar-title">Industry Conferences</h4>
            <p class="srv-cpillar-desc">Sector-specific expos featuring simultaneous technical breakout tracks, dynamic speaker rotations, and peer-to-peer workshops.</p>
          </div>

          <!-- 3. Leadership Summits -->
          <div class="srv-cpillar-card framer-plenary-amphitheater">
            <div class="srv-cpillar-icon"><i class="fas fa-chess-king"></i></div>
            <h4 class="srv-cpillar-title">Leadership Summits</h4>
            <p class="srv-cpillar-desc">Chatham House Rule executive symposiums designed for bilateral deal acceleration, C-suite networking, and policy steering.</p>
          </div>

          <!-- 4. Business Conventions -->
          <div class="srv-cpillar-card framer-plenary-amphitheater">
            <div class="srv-cpillar-icon"><i class="fas fa-building-columns"></i></div>
            <h4 class="srv-cpillar-title">Business Conventions</h4>
            <p class="srv-cpillar-desc">Mass-attendance corporate conventions, franchise assemblies, and trade association congresses requiring robust badge flow logistics.</p>
          </div>

          <!-- 5. Multi-Day Conferences -->
          <div class="srv-cpillar-card framer-plenary-amphitheater">
            <div class="srv-cpillar-icon"><i class="fas fa-calendar-days"></i></div>
            <h4 class="srv-cpillar-title">Multi-Day Conferences</h4>
            <p class="srv-cpillar-desc">Complete 3-to-5 day master scheduling, gala dinner crossovers, off-site networking itineraries, and continuous guest concierge support.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 3: VENUE SOURCING (SPATIAL GEOMETRY & 5-DIMENSION VAULT)
         ===================================================================== -->
    <section id="venue-sourcing" class="srv-section-venue">
      <div class="srv-container">
        <!-- Section Header -->
        <div class="srv-section-head framer-spatial-cadence">
          <div class="srv-badge"><i class="fas fa-compass-drafting"></i> Spatial Engineering</div>
          <h2 class="srv-title">Venue Sourcing & <span class="srv-title-gradient">Capacity Planning</span></h2>
          <p class="srv-subtitle">We negotiate, audit, and model premier global real estate—securing optimal commercial terms, electrical clearance, acoustic isolation, and algorithmic delegate flow.</p>
        </div>

        <div class="srv-venue-split-grid">
          <!-- Left Visual Frame -->
          <div class="srv-venue-visual-frame framer-spatial-cadence">
            <div class="srv-vimg-wrap">
              <img src="images/service_venue_sourcing.jpg" alt="Architectural Convention Center Venue & Capacity Planning">
              <div class="srv-vblueprint-overlay">
                <i class="fas fa-cube"></i> Interactive 3D LiDAR Capacity Modeling
              </div>
            </div>
          </div>

          <!-- Right 5-Category Venue Navigator -->
          <div class="srv-venue-category-stack">
            <!-- 1. Conference Halls -->
            <div class="srv-vcat-card active framer-spatial-cadence" onclick="highlightService(this, 'Conference Halls')">
              <div class="srv-vcat-head">
                <span class="srv-vcat-tag">Spatial Domain 01</span>
                <span style="font-size: 0.8rem; font-weight: 700; color: var(--srv-text-muted);">Pillarless Up to 80,000 Sqft</span>
              </div>
              <h4 class="srv-vcat-title">Colossal Conference Halls</h4>
              <p class="srv-vcat-desc">Acoustically certified column-free exhibition halls with 30ft+ clear ceiling rigging height, heavy machinery floor loading, and high-amperage 3-phase power drops.</p>
            </div>

            <!-- 2. Hotels & Resorts -->
            <div class="srv-vcat-card framer-spatial-cadence" onclick="highlightService(this, 'Hotels & Resorts')">
              <div class="srv-vcat-head">
                <span class="srv-vcat-tag">Spatial Domain 02</span>
                <span style="font-size: 0.8rem; font-weight: 700; color: var(--srv-text-muted);">5-Star Luxury Room Blocks</span>
              </div>
              <h4 class="srv-vcat-title">Luxury Hotels & Resorts</h4>
              <p class="srv-vcat-desc">Complete property buyouts and luxury room-block contracting with pre-negotiated attrition clauses, VIP executive suites, and private beachfront breakout grounds.</p>
            </div>

            <!-- 3. Convention Centres -->
            <div class="srv-vcat-card framer-spatial-cadence" onclick="highlightService(this, 'Convention Centres')">
              <div class="srv-vcat-head">
                <span class="srv-vcat-tag">Spatial Domain 03</span>
                <span style="font-size: 0.8rem; font-weight: 700; color: var(--srv-text-muted);">Tier-1 Global Convention Hubs</span>
              </div>
              <h4 class="srv-vcat-title">Metropolitan Convention Centres</h4>
              <p class="srv-vcat-desc">Prime convention centers in major financial capitals featuring dedicated multi-trailer freight bays, direct mass transit corridors, and bonded customs escrow.</p>
            </div>

            <!-- 4. Outdoor Event Spaces -->
            <div class="srv-vcat-card framer-spatial-cadence" onclick="highlightService(this, 'Outdoor Event Spaces')">
              <div class="srv-vcat-head">
                <span class="srv-vcat-tag">Spatial Domain 04</span>
                <span style="font-size: 0.8rem; font-weight: 700; color: var(--srv-text-muted);">Geodesic Domes & Clear-Span Pavilions</span>
              </div>
              <h4 class="srv-vcat-title">Bespoke Outdoor Event Spaces</h4>
              <p class="srv-vcat-desc">Waterfront promenades, palace courtyards, and alpine plateaus transformed with weather-sealed climate-controlled geodesic domes and architectural lighting.</p>
            </div>

            <!-- 5. Venue Capacity Planning -->
            <div class="srv-vcat-card framer-spatial-cadence" onclick="highlightService(this, 'Capacity Planning')">
              <div class="srv-vcat-head">
                <span class="srv-vcat-tag">Spatial Domain 05</span>
                <span style="font-size: 0.8rem; font-weight: 700; color: var(--srv-text-muted);">3D Algorithmic Simulation</span>
              </div>
              <h4 class="srv-vcat-title">Algorithmic Venue Capacity Planning</h4>
              <p class="srv-vcat-desc">3D digital twin rendering simulating delegate circulation velocities, sightline obstruction checks, NFPA fire egress dispersion, and ADA accessibility paths.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 4: AUDIO-VISUAL PRODUCTION (BROADCAST SYNTHESIS CONSOLE)
         ===================================================================== -->
    <section id="audiovisual-production" class="srv-section-av">
      <div class="srv-container">
        <!-- Section Header -->
        <div class="srv-section-head framer-broadcast-matrix">
          <div class="srv-badge"><i class="fas fa-satellite-dish"></i> Hardware & Broadcast</div>
          <h2 class="srv-title">Audio-Visual Production & <span class="srv-title-gradient">Hybrid Engineering</span></h2>
          <p class="srv-subtitle">Immersive 0.9mm microLED stage walls, studio-grade Dante audio networks, dynamic stage lighting, and synchronized global hybrid satellite broadcasts.</p>
        </div>

        <div class="srv-av-console-grid">
          <!-- Master Broadcast Monitor Card -->
          <div class="srv-av-monitor-card framer-broadcast-matrix">
            <div class="srv-av-screen-box">
              <img src="images/service_av_production.jpg" alt="Master Live Event Broadcast Control Center">
              <div class="srv-av-tally-bar">
                <i class="fas fa-circle" style="font-size: 0.6rem;"></i> ON-AIR • BROADCAST ACTIVE
              </div>
            </div>
            <div style="padding: 1.5rem; background: var(--srv-surface); display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--srv-card-border);">
              <span style="font-size: 0.85rem; font-weight: 700; color: var(--srv-text-muted);"><i class="fas fa-microchip text-primary"></i> 4K120 SMPTE ST 2110 IP Routing</span>
              <button class="srv-btn srv-btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;" onclick="openServiceModal('AV Technical Rider & Hardware Inventory')">
                <i class="fas fa-sliders"></i> Inquire AV Rider
              </button>
            </div>
          </div>

          <!-- 5-Layer Technical Specification Matrix -->
          <div class="srv-av-layer-deck">
            <!-- 1. Sound Systems -->
            <div class="srv-layer-card framer-broadcast-matrix">
              <h4 class="srv-layer-title"><i class="fas fa-volume-high"></i> Professional Stadium Sound Systems</h4>
              <p class="srv-layer-desc">L-Acoustics K2 line arrays, beam-steering arrays, and Shure Axient Quadversity wireless microphones delivering pristine clarity with zero acoustic feedback.</p>
            </div>

            <!-- 2. LED Walls & Projectors -->
            <div class="srv-layer-card framer-broadcast-matrix">
              <h4 class="srv-layer-title"><i class="fas fa-tv"></i> LED Walls & Pure Laser Projectors</h4>
              <p class="srv-layer-desc">Seamless 0.9mm curved microLED video canvases and Christie 45,000-lumen 4K RGB laser projectors calibrated for perfect HDR color reproduction.</p>
            </div>

            <!-- 3. Stage Lighting -->
            <div class="srv-layer-card framer-broadcast-matrix">
              <h4 class="srv-layer-title"><i class="fas fa-lightbulb"></i> Intelligent Stage & Broadcast Lighting</h4>
              <p class="srv-layer-desc">Robotic moving heads, circadian-aligned key lighting for broadcast cameras, grandMA3 computerized consoles, and kinetic motorized trussing.</p>
            </div>

            <!-- 4. Live Streaming Setup -->
            <div class="srv-layer-card framer-broadcast-matrix">
              <h4 class="srv-layer-title"><i class="fas fa-tower-broadcast"></i> 4K Redundant Live Streaming Setup</h4>
              <p class="srv-layer-desc">Bonded dark fiber, dual satellite uplinks, multi-bitrate cloud CDN encoding, and multi-camera broadcast switchers with N+2 automated failover.</p>
            </div>

            <!-- 5. Hybrid Conference Technology -->
            <div class="srv-layer-card framer-broadcast-matrix">
              <h4 class="srv-layer-title"><i class="fas fa-network-wired"></i> Hybrid Conference Technology</h4>
              <p class="srv-layer-desc">Sub-45ms latency linking remote speakers to live physical stages, interactive real-time audience sentiment polling, and 18-language AI closed captioning.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 5: EVENT DESIGN & BRANDING (SCULPTURAL PRISM ATELIER)
         ===================================================================== -->
    <section id="design-branding" class="srv-section-design">
      <div class="srv-container">
        <!-- Section Header -->
        <div class="srv-section-head framer-sculptural-prism">
          <div class="srv-badge"><i class="fas fa-pen-ruler"></i> Spatial Identity</div>
          <h2 class="srv-title">Event Design, Staging & <span class="srv-title-gradient">Corporate Branding</span></h2>
          <p class="srv-subtitle">Transforming abstract corporate vision into tangible architectural set pieces, illuminated exhibition pavilions, holographic staging, and immersive digital brand touchpoints.</p>
        </div>

        <div class="srv-design-grid">
          <!-- Left Visual Card -->
          <div class="srv-design-visual-card framer-sculptural-prism">
            <div class="srv-dimg-wrap">
              <img src="images/service_design_branding.jpg" alt="Architectural Stage Design & Corporate Event Branding Atelier">
            </div>
            <div style="padding: 1.5rem; background: var(--srv-surface); border-top: 1px solid var(--srv-card-border);">
              <div style="font-size: 0.8rem; font-weight: 700; color: var(--srv-accent); text-transform: uppercase;">Experiential Design Studio</div>
              <h4 style="font-size: 1.2rem; font-weight: 800; color: var(--srv-text-main); margin-top: 0.25rem;">Bespoke 3D Holographic Staging & Custom Exhibition Pavilions</h4>
            </div>
          </div>

          <!-- Right 5 Pillars of Experiential Event Design -->
          <div class="srv-design-pillars-stack">
            <!-- 1. Stage & Set Design -->
            <div class="srv-dpillar-card framer-sculptural-prism">
              <h4 class="srv-dpillar-title"><i class="fas fa-archway text-warning"></i> Custom Stage & Set Architecture</h4>
              <p class="srv-dpillar-desc">Architectural 3D CAD modeling, CNC-milled stage fascias, illuminated proscenium arches, and motorized presenter rostrums engineered for awe.</p>
            </div>

            <!-- 2. Corporate Event Branding -->
            <div class="srv-dpillar-card framer-sculptural-prism">
              <h4 class="srv-dpillar-title"><i class="fas fa-palette text-warning"></i> Corporate Event Branding Identity</h4>
              <p class="srv-dpillar-desc">Harmonized environmental brand styling, bespoke color palettes, lanyard credentials, premium delegate gift packaging, and architectural vinyl wrapping.</p>
            </div>

            <!-- 3. Exhibition Booth Design -->
            <div class="srv-dpillar-card framer-sculptural-prism">
              <h4 class="srv-dpillar-title"><i class="fas fa-store text-warning"></i> Exhibition Booth & Pavilion Design</h4>
              <p class="srv-dpillar-desc">Multi-tier sponsor exhibition spaces, custom double-decker structures, hospitality bars, product demo pods, and high-throughput attendee traffic layouts.</p>
            </div>

            <!-- 4. Event Signage -->
            <div class="srv-dpillar-card framer-sculptural-prism">
              <h4 class="srv-dpillar-title"><i class="fas fa-signs-post text-warning"></i> Wayfinding & Digital Signage</h4>
              <p class="srv-dpillar-desc">Touchless interactive directory totems, illuminated dynamic agenda displays, acoustic directional signage, and ADA-compliant concourse wayfinding.</p>
            </div>

            <!-- 5. Digital Presentation Design -->
            <div class="srv-dpillar-card framer-sculptural-prism">
              <h4 class="srv-dpillar-title"><i class="fas fa-photo-film text-warning"></i> Digital Keynote & Motion Design</h4>
              <p class="srv-dpillar-desc">Unreal Engine real-time 3D motion backgrounds, cinematic 4K keynote slide decks, speaker sting animations, and generative visual storytelling.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 6: CATERING & HOSPITALITY (GASTRONOMIC CONCIERGE ATELIER)
         ===================================================================== -->
    <section id="hospitality-catering" class="srv-section-hospitality">
      <div class="srv-container">
        <!-- Section Header -->
        <div class="srv-section-head framer-gastronomic-concierge">
          <div class="srv-badge"><i class="fas fa-champagne-glasses"></i> Michelin-Standard Hospitality</div>
          <h2 class="srv-title">Catering, Hospitality & <span class="srv-title-gradient">VIP Concierge</span></h2>
          <p class="srv-subtitle">From farm-to-table corporate gala banquets and artisanal continuous refreshment stations to secluded VIP executive lounges and 5-star hotel concierge coordination.</p>
        </div>

        <div class="srv-hospitality-3col-grid">
          <!-- Col 1: Catering & Refreshments -->
          <div class="srv-hosp-side-card framer-gastronomic-concierge">
            <div class="srv-hitem-box">
              <h4><i class="fas fa-utensils text-warning"></i> Curated Corporate Catering</h4>
              <p>Michelin-mentored executive chefs delivering synchronized plated gala service for up to 3,000 delegates with zero dining room lag.</p>
            </div>
            <div class="srv-hitem-box">
              <h4><i class="fas fa-mug-hot text-warning"></i> Delegate Refreshment Stations</h4>
              <p>Continuous artisanal espresso bars, fresh cold-pressed botanical tonics, brain-boosting superfood pastries, and hydration hubs.</p>
            </div>
          </div>

          <!-- Col 2: Centerpiece Visual Showcase -->
          <div class="srv-hosp-center-card framer-gastronomic-concierge">
            <div class="srv-himg-wrap">
              <img src="images/service_hospitality_catering.jpg" alt="Luxury Corporate Summit VIP Hospitality Lounge and Gourmet Catering">
            </div>
            <div style="padding: 1.25rem 1.5rem; background: var(--srv-surface); text-align: center;">
              <span style="font-size: 0.8rem; font-weight: 800; color: var(--srv-accent); text-transform: uppercase;">Hospitality Excellence Standard</span>
              <div style="font-size: 1.1rem; font-weight: 800; color: var(--srv-text-main); margin-top: 0.2rem;">ISO-22000 Certified Clean-Room Kitchen Lines</div>
            </div>
          </div>

          <!-- Col 3: VIP Hospitality, Dietary & Accommodations -->
          <div class="srv-hosp-side-card framer-gastronomic-concierge">
            <div class="srv-hitem-box">
              <h4><i class="fas fa-wine-glass text-warning"></i> VIP Hospitality Lounges</h4>
              <p>Dedicated master sommelier wine flights, private caviar bars, soundproofed negotiation suites, and discrete private security service.</p>
            </div>
            <div class="srv-hitem-box">
              <h4><i class="fas fa-leaf text-warning"></i> Dietary Planning Precision</h4>
              <p>Rigorous management of vegan, gluten-free, halal, kosher, and allergen protocols with isolated kitchen prep and digital meal tags.</p>
            </div>
            <div class="srv-hitem-box">
              <h4><i class="fas fa-hotel text-warning"></i> 5-Star Hotel Accommodations</h4>
              <p>Turn-key room block sourcing, executive check-in priority desks, VIP airport-hotel transfers, and 24/7 guest concierge dispatch.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 7: DELEGATE LOGISTICS (CONCOURSE & OPERATIONS COMMAND)
         ===================================================================== -->
    <section id="delegate-logistics" class="srv-section-logistics">
      <div class="srv-container">
        <!-- Section Header -->
        <div class="srv-section-head framer-concourse-dispatch">
          <div class="srv-badge"><i class="fas fa-qrcode"></i> Operations Command</div>
          <h2 class="srv-title">Delegate Operations & <span class="srv-title-gradient">On-Site Logistics Command</span></h2>
          <p class="srv-subtitle">Touchless digital registration, instant QR badge printing kiosks, VIP speaker green room handling, motorized transport fleets, and 24/7 incident risk management.</p>
        </div>

        <div class="srv-logistics-split-grid">
          <!-- Left Visual Frame -->
          <div class="srv-logistics-visual-card framer-concourse-dispatch">
            <div class="srv-limg-wrap">
              <img src="images/service_delegate_logistics.jpg" alt="Executive Summit Registration Concourse and Logistics Command Center">
            </div>
            <div style="padding: 1.5rem; background: var(--srv-surface); border-top: 1px solid var(--srv-card-border); display: flex; justify-content: space-between; align-items: center;">
              <div>
                <div style="font-size: 0.8rem; font-weight: 700; color: var(--srv-accent); text-transform: uppercase;">Concourse Velocity</div>
                <div style="font-size: 1.1rem; font-weight: 800; color: var(--srv-text-main);">&lt; 15 Seconds Average Check-In</div>
              </div>
              <button class="srv-btn srv-btn-primary" onclick="openServiceModal('Full Logistics & Delegate Operations Blueprint')">
                <i class="fas fa-headset"></i> Consult Logistics Lead
              </button>
            </div>
          </div>

          <!-- Right Comprehensive Dual-Wing Breakdown -->
          <div class="srv-logistics-wings-stack">
            <!-- Wing A: Delegate & Guest Management -->
            <div class="srv-lwing-card framer-concourse-dispatch">
              <h4 class="srv-lwing-title"><i class="fas fa-id-card-clip"></i> Delegate & Guest Management</h4>
              <div class="srv-lwing-list">
                <div class="srv-lrow">
                  <i class="fas fa-check-circle"></i>
                  <span><strong>Guest Registration & Digital Invitations:</strong> Custom branded micro-sites, encrypted RSVP portals, and tiered guest category access controls.</span>
                </div>
                <div class="srv-lrow">
                  <i class="fas fa-check-circle"></i>
                  <span><strong>Touchless QR & NFC Check-In:</strong> High-throughput kiosks printing smart badges with RFID access tracking in under 12 seconds per attendee.</span>
                </div>
                <div class="srv-lrow">
                  <i class="fas fa-check-circle"></i>
                  <span><strong>Speaker Coordination & Briefing:</strong> Dedicated VIP speaker concierges, teleprompter rehearsals, slide deck management, and green room hospitality.</span>
                </div>
                <div class="srv-lrow">
                  <i class="fas fa-check-circle"></i>
                  <span><strong>Multi-Channel Delegate Communications:</strong> Real-time SMS push notifications, custom native conference mobile apps, and personalized agenda itineraries.</span>
                </div>
              </div>
            </div>

            <!-- Wing B: Event Logistics & Risk Command -->
            <div class="srv-lwing-card framer-concourse-dispatch">
              <h4 class="srv-lwing-title"><i class="fas fa-truck-ramp-box"></i> Event Logistics & Risk Command</h4>
              <div class="srv-lwing-list">
                <div class="srv-lrow">
                  <i class="fas fa-check-circle"></i>
                  <span><strong>VIP Transportation Coordination:</strong> Armored motorcades, luxury electric executive coaches, airport tarmac escorts, and helicopter charters.</span>
                </div>
                <div class="srv-lrow">
                  <i class="fas fa-check-circle"></i>
                  <span><strong>Equipment Management:</strong> ATA Carnet international customs clearing, airside freight staging, hardware inventory tracking, and secure overnight warehousing.</span>
                </div>
                <div class="srv-lrow">
                  <i class="fas fa-check-circle"></i>
                  <span><strong>Vendor Coordination & On-Site Command:</strong> Multi-frequency radio operations, central production dispatch desk, and minute-by-minute show calling.</span>
                </div>
                <div class="srv-lrow">
                  <i class="fas fa-check-circle"></i>
                  <span><strong>Comprehensive Event Risk Management:</strong> NFPA fire marshal compliance, discrete dignitary security perimeters, on-site medical hubs, and emergency plans.</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Interactive Service Modal -->
  <div id="srvModalOverlay" class="srv-modal-overlay">
    <div class="srv-modal-card">
      <button class="srv-modal-close" onclick="closeServiceModal()">&times;</button>
      <div style="width: 3.5rem; height: 3.5rem; border-radius: 0.85rem; background: var(--srv-accent-glow); color: var(--srv-accent); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; margin: 0 auto 1.25rem auto;">
        <i class="fas fa-file-circle-check"></i>
      </div>
      <h3 id="srvModalTitle" style="font-size: 1.4rem; font-weight: 800; color: var(--srv-text-main); margin-bottom: 0.5rem;">Service Specification Queued</h3>
      <p id="srvModalDesc" style="font-size: 0.95rem; color: var(--srv-text-muted); line-height: 1.6; margin-bottom: 1.5rem;">Detailed production riders and pricing structures for this service capability have been compiled for your enterprise review.</p>
      <button class="srv-btn srv-btn-primary" style="width: 100%;" onclick="closeServiceModal()">Continue Browsing Suite</button>
    </div>
  </div>
"""

    # Page Interactive Scripts
    new_srv_scripts = """
  <!-- =====================================================================
       INTERACTIVE SERVICES PAGE CONTROLLER SCRIPT
       ===================================================================== -->
  <script>
    // 1. Intersection Observer for Unique Framer Motion Animations
    document.addEventListener('DOMContentLoaded', function() {
      var framerElements = document.querySelectorAll(
        '.framer-boardroom-elevation, ' +
        '.framer-plenary-amphitheater, ' +
        '.framer-spatial-cadence, ' +
        '.framer-broadcast-matrix, ' +
        '.framer-sculptural-prism, ' +
        '.framer-gastronomic-concierge, ' +
        '.framer-concourse-dispatch'
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

    // 2. Interactive Service Highlighter
    function highlightService(card, serviceName) {
      var siblings = card.parentElement.children;
      for (var i = 0; i < siblings.length; i++) {
        siblings[i].classList.remove('active');
      }
      card.classList.add('active');
    }

    // 3. Interactive Service Modal
    function openServiceModal(serviceName) {
      var modal = document.getElementById('srvModalOverlay');
      var title = document.getElementById('srvModalTitle');
      var desc = document.getElementById('srvModalDesc');

      if (title) title.textContent = serviceName;
      if (desc) desc.textContent = 'Detailed specifications, technical riders, and staffing matrices for "' + serviceName + '" are initialized for review. Our senior advisory leads are prepared to assist.';
      if (modal) modal.style.display = 'flex';
    }

    function closeServiceModal() {
      var modal = document.getElementById('srvModalOverlay');
      if (modal) modal.style.display = 'none';
    }
  </script>
"""

    # Assemble complete document
    final_html = (
        nav_head_up_to_style
        + new_srv_css
        + "\n  </style>"
        + nav_mid[len("</style>"):]
        + new_srv_content
        + footer_full
        + new_srv_scripts
        + closing_part
    )

    with open('services.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print("Successfully built redesigned services.html! Total length:", len(final_html))

if __name__ == '__main__':
    generate_services()
