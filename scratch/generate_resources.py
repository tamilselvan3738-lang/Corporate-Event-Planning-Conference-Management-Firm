import os

def build_resources_html():
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

    # CSS for resources.html
    resources_css = """
    /* =====================================================================
       KNOWLEDGE & RESOURCES HUB - CUSTOM PAGE STYLES
       Supports Light Mode, Dark Mode (body.dark), and RTL (body.rtl)
       ===================================================================== */
    :root {
      --rc-primary: #1e3a8a;
      --rc-primary-dark: #0f172a;
      --rc-accent: #d97706;
      --rc-accent-light: #fbbf24;
      --rc-accent-glow: rgba(217, 119, 6, 0.16);
      --rc-bg: #f8fafc;
      --rc-surface: #ffffff;
      --rc-surface-muted: #f1f5f9;
      --rc-card-border: #e2e8f0;
      --rc-text-main: #0f172a;
      --rc-text-muted: #64748b;
      --rc-text-light: #94a3b8;
      --rc-gold-gradient: linear-gradient(135deg, #b45309 0%, #d97706 50%, #f59e0b 100%);
      --rc-blue-gradient: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      --rc-shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --rc-shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.07), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
      --rc-shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      --rc-shadow-glow: 0 0 25px rgba(217, 119, 6, 0.22);
    }

    body.dark {
      --rc-bg: #070b14;
      --rc-surface: #0f172a;
      --rc-surface-muted: #131d33;
      --rc-card-border: #1e293b;
      --rc-text-main: #f8fafc;
      --rc-text-muted: #94a3b8;
      --rc-text-light: #64748b;
      --rc-blue-gradient: linear-gradient(135deg, #070b14 0%, #172554 100%);
    }

    /* RTL Support */
    body.rtl .rc-section-head { text-align: right; }
    body.rtl .rc-badge i { margin-left: 0.5rem; margin-right: 0; }
    body.rtl .rc-btn i { margin-right: 0.5rem; margin-left: 0; }

    /* Base Reset for Resources Container */
    .rc-page-wrap {
      background-color: var(--rc-bg);
      color: var(--rc-text-main);
      font-family: 'Inter', system-ui, sans-serif;
      overflow-x: hidden;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    .rc-container {
      max-width: 1320px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }

    /* SECTION HEADER STYLING */
    .rc-section-head {
      margin-bottom: 3.5rem;
      position: relative;
    }

    .rc-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.45rem 1.1rem;
      border-radius: 9999px;
      background: var(--rc-accent-glow);
      border: 1px solid rgba(217, 119, 6, 0.35);
      color: var(--rc-accent);
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      margin-bottom: 1rem;
    }

    .rc-title {
      font-size: clamp(2rem, 3.5vw, 2.75rem);
      font-weight: 800;
      line-height: 1.18;
      color: var(--rc-text-main);
      letter-spacing: -0.025em;
      margin-bottom: 1rem;
    }

    .rc-title-gradient {
      background: var(--rc-gold-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .rc-subtitle {
      font-size: 1.1rem;
      color: var(--rc-text-muted);
      line-height: 1.65;
      max-width: 780px;
    }

    /* HERO JUMP NAV STRIP */
    .rc-hero-strip {
      background: var(--rc-surface);
      border-bottom: 1px solid var(--rc-card-border);
      padding: 2.75rem 0 2.25rem;
      position: relative;
    }
    .rc-hero-content {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 1.25rem;
    }
    .rc-hero-title {
      font-size: clamp(2.2rem, 4vw, 3.25rem);
      font-weight: 900;
      color: var(--rc-text-main);
      letter-spacing: -0.03em;
    }
    .rc-hero-desc {
      font-size: 1.15rem;
      color: var(--rc-text-muted);
      max-width: 840px;
      line-height: 1.65;
    }
    .rc-nav-pills {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.65rem;
      margin-top: 1rem;
    }
    .rc-nav-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.55rem 1.15rem;
      border-radius: 9999px;
      background: var(--rc-surface-muted);
      border: 1px solid var(--rc-card-border);
      color: var(--rc-text-main);
      font-size: 0.88rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
    }
    .rc-nav-pill:hover {
      background: var(--rc-accent);
      color: #ffffff;
      border-color: var(--rc-accent);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(217, 119, 6, 0.25);
    }
    .rc-nav-pill i {
      color: var(--rc-accent);
      transition: color 0.3s ease;
    }
    .rc-nav-pill:hover i {
      color: #ffffff;
    }

    /* GLOBAL BUTTONS */
    .rc-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.65rem;
      padding: 0.85rem 1.75rem;
      border-radius: 0.75rem;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
      border: none;
    }
    .rc-btn-primary {
      background: var(--rc-gold-gradient);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(217, 119, 6, 0.3);
    }
    .rc-btn-primary:hover {
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 8px 24px rgba(217, 119, 6, 0.45);
      color: #ffffff;
    }
    .rc-btn-outline {
      background: transparent;
      color: var(--rc-text-main);
      border: 1.5px solid var(--rc-card-border);
    }
    .rc-btn-outline:hover {
      background: var(--rc-surface-muted);
      border-color: var(--rc-accent);
      color: var(--rc-accent);
      transform: translateY(-2px);
    }

    /* =====================================================================
       FRAMER MOTION OBSERVER SYSTEM (7 DISTINCT SECTION ANIMATIONS)
       ===================================================================== */
    /* Section 1: Folio 3D Diagonal Unfold */
    .framer-folio-glide {
      opacity: 0;
      transform: perspective(1100px) rotateY(-8deg) translateX(-45px);
      transition: opacity 0.85s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1);
      will-change: transform, opacity;
    }
    .framer-folio-glide.framer-in-view {
      opacity: 1;
      transform: perspective(1100px) rotateY(0deg) translateX(0);
    }

    /* Section 2: Countdown Stepper Elastic Snap */
    .framer-countdown-snap {
      opacity: 0;
      transform: scale(0.92) translateY(50px);
      transition: opacity 0.75s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.75s cubic-bezier(0.34, 1.56, 0.64, 1);
      will-change: transform, opacity;
    }
    .framer-countdown-snap.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    /* Section 3: CapEx Financial Lift & Flare */
    .framer-capex-reveal {
      opacity: 0;
      transform: translateY(40px) scale(0.95);
      transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform, opacity;
    }
    .framer-capex-reveal.framer-in-view {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    /* Section 4: Blueprint Architectural Perspective Draft */
    .framer-blueprint-draft {
      opacity: 0;
      transform: perspective(1200px) rotateX(10deg) translateY(40px);
      transition: opacity 0.85s cubic-bezier(0.25, 1, 0.5, 1), transform 0.85s cubic-bezier(0.25, 1, 0.5, 1);
      will-change: transform, opacity;
    }
    .framer-blueprint-draft.framer-in-view {
      opacity: 1;
      transform: perspective(1200px) rotateX(0deg) translateY(0);
    }

    /* Section 5: Dual Hemisphere Lateral Convergence */
    .framer-dual-hemisphere {
      opacity: 0;
      transform: translateY(35px) skewY(-1deg);
      transition: opacity 0.8s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
      will-change: transform, opacity;
    }
    .framer-dual-hemisphere.framer-in-view {
      opacity: 1;
      transform: translateY(0) skewY(0deg);
    }

    /* Section 6: Editorial Monograph Elevation */
    .framer-editorial-rise {
      opacity: 0;
      transform: translateY(45px);
      transition: opacity 0.9s cubic-bezier(0.16, 1, 0.3, 1), transform 0.9s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform, opacity;
    }
    .framer-editorial-rise.framer-in-view {
      opacity: 1;
      transform: translateY(0);
    }

    /* Section 7: Diagnostic Vault Accordion Unfurl */
    .framer-vault-open {
      opacity: 0;
      transform: scale(0.96) translateY(35px);
      transition: opacity 0.8s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
      will-change: transform, opacity;
    }
    .framer-vault-open.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    /* =====================================================================
       SECTION 1: CORPORATE EVENT PLANNING GUIDES - FOLIO DECK
       ===================================================================== */
    .rc-section-guides {
      padding: 6.5rem 0;
      position: relative;
    }
    .rc-folio-deck-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 3rem;
      align-items: stretch;
    }
    .rc-folio-book-showcase {
      background: var(--rc-surface);
      border: 1px solid var(--rc-card-border);
      border-radius: 1.75rem;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--rc-shadow-lg);
      transition: border-color 0.4s ease, transform 0.4s ease;
    }
    .rc-folio-book-showcase:hover {
      border-color: rgba(217, 119, 6, 0.45);
      transform: translateY(-4px);
    }
    .rc-folio-img-box {
      position: relative;
      height: 380px;
      overflow: hidden;
    }
    .rc-folio-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.7s cubic-bezier(0.2, 0.8, 0.2, 1);
    }
    .rc-folio-book-showcase:hover .rc-folio-img-box img {
      transform: scale(1.04);
    }
    .rc-folio-edition-tag {
      position: absolute;
      top: 1.25rem;
      left: 1.25rem;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(10px);
      padding: 0.5rem 1rem;
      border-radius: 0.75rem;
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #ffffff;
      font-size: 0.82rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    body.rtl .rc-folio-edition-tag {
      left: auto;
      right: 1.25rem;
    }
    .rc-folio-body {
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
      justify-content: space-between;
    }
    .rc-folio-stats-strip {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
      padding: 1.25rem 0;
      margin: 1.25rem 0;
      border-top: 1px solid var(--rc-card-border);
      border-bottom: 1px solid var(--rc-card-border);
    }
    .rc-folio-stat-item {
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }
    .rc-folio-stat-lbl {
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--rc-text-light);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .rc-folio-stat-val {
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--rc-text-main);
    }

    /* Right Chapters List */
    .rc-chapters-col {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      justify-content: space-between;
    }
    .rc-chapter-card {
      background: var(--rc-surface);
      border: 1px solid var(--rc-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      gap: 1.25rem;
      align-items: flex-start;
      box-shadow: var(--rc-shadow-sm);
      cursor: pointer;
      transition: all 0.35s ease;
    }
    .rc-chapter-card.active,
    .rc-chapter-card:hover {
      border-color: var(--rc-accent);
      background: var(--rc-surface-muted);
      transform: translateX(6px);
      box-shadow: var(--rc-shadow-md);
    }
    body.rtl .rc-chapter-card.active,
    body.rtl .rc-chapter-card:hover {
      transform: translateX(-6px);
    }
    .rc-chapter-badge-num {
      width: 44px;
      height: 44px;
      border-radius: 1rem;
      background: var(--rc-gold-gradient);
      color: #ffffff;
      font-size: 1.1rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      box-shadow: 0 4px 10px rgba(217, 119, 6, 0.3);
    }
    .rc-chapter-info {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }
    .rc-chapter-title {
      font-size: 1.08rem;
      font-weight: 800;
      color: var(--rc-text-main);
    }
    .rc-chapter-desc {
      font-size: 0.88rem;
      color: var(--rc-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 2: CONFERENCE PREPARATION CHECKLIST - COUNTDOWN TIMELINE
       ===================================================================== */
    .rc-section-checklist {
      padding: 6.5rem 0;
      background: var(--rc-surface-muted);
      border-top: 1px solid var(--rc-card-border);
      border-bottom: 1px solid var(--rc-card-border);
      position: relative;
    }
    .rc-countdown-layout {
      display: grid;
      grid-template-columns: 0.95fr 1.05fr;
      gap: 3rem;
      align-items: stretch;
    }
    .rc-audit-bench-card {
      background: var(--rc-surface);
      border: 1px solid var(--rc-card-border);
      border-radius: 1.75rem;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--rc-shadow-lg);
    }
    .rc-audit-img-box {
      position: relative;
      height: 300px;
    }
    .rc-audit-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .rc-audit-card-body {
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      flex-grow: 1;
      justify-content: space-between;
    }
    .rc-readiness-meter-box {
      background: var(--rc-surface-muted);
      border: 1px solid var(--rc-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }
    .rc-readiness-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .rc-meter-track {
      height: 8px;
      background: var(--rc-card-border);
      border-radius: 4px;
      overflow: hidden;
    }
    .rc-meter-fill {
      height: 100%;
      background: #10b981;
      border-radius: 4px;
      transition: width 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    /* Right Timeline Milestone Pods */
    .rc-timeline-pods-wrap {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }
    .rc-milestone-pod {
      background: var(--rc-surface);
      border: 1px solid var(--rc-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      box-shadow: var(--rc-shadow-sm);
      transition: all 0.3s ease;
    }
    .rc-milestone-pod:hover {
      border-color: var(--rc-accent);
      transform: translateY(-2px);
      box-shadow: var(--rc-shadow-md);
    }
    .rc-milestone-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .rc-milestone-title {
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--rc-text-main);
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }
    .rc-milestone-tag {
      font-size: 0.75rem;
      font-weight: 800;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      background: var(--rc-accent-glow);
      color: var(--rc-accent);
      letter-spacing: 0.04em;
    }
    .rc-check-item-row {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      font-size: 0.88rem;
      color: var(--rc-text-muted);
    }
    .rc-check-item-row input[type="checkbox"] {
      width: 18px;
      height: 18px;
      accent-color: var(--rc-accent);
      cursor: pointer;
    }

    /* =====================================================================
       SECTION 3: EVENT BUDGET PLANNING GUIDE - CAPEX SIMULATOR
       ===================================================================== */
    .rc-section-budget {
      padding: 6.5rem 0;
      position: relative;
    }
    .rc-budget-cockpit-grid {
      display: grid;
      grid-template-columns: 1fr 1.15fr;
      gap: 3rem;
      align-items: stretch;
    }
    .rc-budget-media-card {
      background: var(--rc-surface);
      border: 1px solid var(--rc-card-border);
      border-radius: 1.75rem;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--rc-shadow-lg);
    }
    .rc-budget-img-box {
      position: relative;
      height: 320px;
    }
    .rc-budget-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .rc-budget-roi-strip {
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      flex-grow: 1;
      justify-content: space-between;
    }
    .rc-budget-metrics-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
      background: var(--rc-surface-muted);
      border: 1px solid var(--rc-card-border);
      border-radius: 1rem;
      padding: 1.25rem;
    }
    .rc-bmetric-item {
      display: flex;
      flex-direction: column;
    }
    .rc-bmetric-val {
      font-size: 1.2rem;
      font-weight: 900;
      color: var(--rc-accent);
      font-family: monospace;
    }
    .rc-bmetric-lbl {
      font-size: 0.72rem;
      color: var(--rc-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    /* Right Interactive Simulator */
    .rc-simulator-panel {
      background: var(--rc-surface);
      border: 1px solid var(--rc-card-border);
      border-radius: 1.75rem;
      padding: 2.5rem;
      box-shadow: var(--rc-shadow-lg);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .rc-allocation-bars-box {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin: 1.5rem 0 2rem;
    }
    .rc-alloc-item {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }
    .rc-alloc-header {
      display: flex;
      justify-content: space-between;
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--rc-text-main);
    }
    .rc-alloc-bar-bg {
      height: 8px;
      background: var(--rc-surface-muted);
      border-radius: 4px;
      overflow: hidden;
      border: 1px solid var(--rc-card-border);
    }
    .rc-alloc-bar-fill {
      height: 100%;
      border-radius: 4px;
    }
    .rc-sim-calc-box {
      background: var(--rc-surface-muted);
      border: 1px solid var(--rc-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
    }

    /* =====================================================================
       SECTION 4: VENUE SELECTION GUIDE - BLUEPRINT MATRIX
       ===================================================================== */
    .rc-section-venue-guide {
      padding: 6.5rem 0;
      background: var(--rc-surface-muted);
      border-top: 1px solid var(--rc-card-border);
      border-bottom: 1px solid var(--rc-card-border);
      position: relative;
    }
    .rc-venue-guide-layout {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 3rem;
      align-items: stretch;
    }
    .rc-blueprint-visual-card {
      background: var(--rc-surface);
      border: 1px solid var(--rc-card-border);
      border-radius: 1.75rem;
      overflow: hidden;
      box-shadow: var(--rc-shadow-lg);
      display: flex;
      flex-direction: column;
    }
    .rc-blueprint-img-box {
      position: relative;
      height: 380px;
    }
    .rc-blueprint-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .rc-cad-badge-floating {
      position: absolute;
      top: 1.25rem;
      right: 1.25rem;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(8px);
      padding: 0.5rem 1rem;
      border-radius: 0.75rem;
      color: #38bdf8;
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 0.05em;
      border: 1px solid rgba(56, 189, 248, 0.3);
    }
    body.rtl .rc-cad-badge-floating {
      right: auto;
      left: 1.25rem;
    }
    .rc-blueprint-body {
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex-grow: 1;
    }

    /* Right Vetting Grid */
    .rc-vetting-pillars {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      justify-content: space-between;
    }
    .rc-vetting-card {
      background: var(--rc-surface);
      border: 1px solid var(--rc-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      box-shadow: var(--rc-shadow-sm);
      transition: all 0.3s ease;
    }
    .rc-vetting-card:hover {
      border-color: var(--rc-accent);
      transform: translateY(-2px);
      box-shadow: var(--rc-shadow-md);
    }
    .rc-vetting-title {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--rc-text-main);
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }
    .rc-vetting-title i {
      color: var(--rc-accent);
    }
    .rc-vetting-desc {
      font-size: 0.88rem;
      color: var(--rc-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 5: HYBRID EVENT BEST PRACTICES - DUAL-HEMISPHERE GRID
       ===================================================================== */
    .rc-section-hybrid {
      padding: 6.5rem 0;
      position: relative;
    }
    .rc-dual-hemisphere-wrap {
      background: var(--rc-surface);
      border: 1px solid var(--rc-card-border);
      border-radius: 1.75rem;
      padding: 2.5rem;
      box-shadow: var(--rc-shadow-lg);
    }
    .rc-telemetry-hero-banner {
      position: relative;
      border-radius: 1.25rem;
      overflow: hidden;
      height: 360px;
      margin-bottom: 2.5rem;
      border: 1px solid var(--rc-card-border);
    }
    .rc-telemetry-hero-banner img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .rc-broadcast-telemetry-bar {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(0deg, rgba(7, 11, 20, 0.95) 0%, rgba(7, 11, 20, 0.35) 75%, transparent 100%);
      padding: 1.75rem 2rem;
      color: #ffffff;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }
    .rc-split-spheres-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
    }
    .rc-sphere-card {
      background: var(--rc-surface-muted);
      border: 1px solid var(--rc-card-border);
      border-radius: 1.25rem;
      padding: 2rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    .rc-sphere-head {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--rc-text-main);
    }
    .rc-sphere-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }
    .rc-sphere-item {
      display: flex;
      align-items: flex-start;
      gap: 0.65rem;
      font-size: 0.9rem;
      color: var(--rc-text-muted);
      line-height: 1.45;
    }
    .rc-sphere-item i {
      color: var(--rc-accent);
      margin-top: 0.2rem;
    }

    /* =====================================================================
       SECTION 6: INDUSTRY INSIGHTS & ARTICLES - EDITORIAL MONOGRAPH
       ===================================================================== */
    .rc-section-insights {
      padding: 6.5rem 0;
      background: var(--rc-surface-muted);
      border-top: 1px solid var(--rc-card-border);
      border-bottom: 1px solid var(--rc-card-border);
      position: relative;
    }
    .rc-insights-editorial-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 3rem;
      align-items: stretch;
    }
    .rc-featured-monograph-card {
      background: var(--rc-surface);
      border: 1px solid var(--rc-card-border);
      border-radius: 1.75rem;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--rc-shadow-lg);
    }
    .rc-monograph-img-box {
      position: relative;
      height: 320px;
    }
    .rc-monograph-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .rc-monograph-body {
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      flex-grow: 1;
      justify-content: space-between;
    }
    .rc-curated-articles-stack {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      justify-content: space-between;
    }
    .rc-article-card {
      background: var(--rc-surface);
      border: 1px solid var(--rc-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      box-shadow: var(--rc-shadow-sm);
      transition: all 0.3s ease;
      cursor: pointer;
    }
    .rc-article-card:hover {
      border-color: var(--rc-accent);
      transform: translateX(-4px);
      box-shadow: var(--rc-shadow-md);
    }
    body.rtl .rc-article-card:hover {
      transform: translateX(4px);
    }
    .rc-article-meta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.78rem;
      color: var(--rc-text-light);
    }
    .rc-article-title {
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--rc-text-main);
      line-height: 1.35;
    }
    .rc-article-excerpt {
      font-size: 0.88rem;
      color: var(--rc-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 7: FREQUENTLY ASKED QUESTIONS - DIAGNOSTIC VAULT
       ===================================================================== */
    .rc-section-faq {
      padding: 6.5rem 0 8rem;
      position: relative;
    }
    .rc-faq-layout-grid {
      display: grid;
      grid-template-columns: 0.85fr 1.15fr;
      gap: 3rem;
      align-items: stretch;
    }
    .rc-faq-concierge-card {
      background: var(--rc-surface);
      border: 1px solid var(--rc-card-border);
      border-radius: 1.75rem;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--rc-shadow-lg);
    }
    .rc-faq-concierge-img {
      position: relative;
      height: 280px;
    }
    .rc-faq-concierge-img img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .rc-concierge-details {
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      flex-grow: 1;
      justify-content: space-between;
    }

    /* Right Accordion Panel */
    .rc-accordion-panel {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    .rc-faq-search-box {
      margin-bottom: 1.5rem;
      position: relative;
    }
    .rc-faq-search-input {
      width: 100%;
      padding: 0.95rem 1.25rem 0.95rem 3rem;
      border-radius: 0.85rem;
      border: 1px solid var(--rc-card-border);
      background: var(--rc-surface);
      color: var(--rc-text-main);
      font-size: 0.95rem;
      outline: none;
      transition: all 0.3s ease;
    }
    body.rtl .rc-faq-search-input {
      padding: 0.95rem 3rem 0.95rem 1.25rem;
    }
    .rc-faq-search-input:focus {
      border-color: var(--rc-accent);
      box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.15);
    }
    .rc-faq-search-icon {
      position: absolute;
      left: 1.15rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--rc-text-muted);
      font-size: 1.1rem;
    }
    body.rtl .rc-faq-search-icon {
      left: auto;
      right: 1.15rem;
    }
    .rc-accordion-item {
      background: var(--rc-surface);
      border: 1px solid var(--rc-card-border);
      border-radius: 1rem;
      overflow: hidden;
      box-shadow: var(--rc-shadow-sm);
      transition: all 0.3s ease;
    }
    .rc-accordion-item.active {
      border-color: var(--rc-accent);
    }
    .rc-accordion-header {
      padding: 1.25rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--rc-text-main);
      user-select: none;
    }
    .rc-accordion-chevron {
      color: var(--rc-accent);
      transition: transform 0.35s ease;
    }
    .rc-accordion-item.active .rc-accordion-chevron {
      transform: rotate(180deg);
    }
    .rc-accordion-body {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
      background: var(--rc-surface-muted);
    }
    .rc-accordion-content {
      padding: 1.25rem 1.5rem;
      font-size: 0.92rem;
      color: var(--rc-text-muted);
      line-height: 1.6;
    }

    /* RESPONSIVE MEDIA QUERIES */
    @media (max-width: 1024px) {
      .rc-folio-deck-grid,
      .rc-countdown-layout,
      .rc-budget-cockpit-grid,
      .rc-venue-guide-layout,
      .rc-split-spheres-grid,
      .rc-insights-editorial-grid,
      .rc-faq-layout-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
      }
      .rc-folio-img-box,
      .rc-blueprint-img-box,
      .rc-telemetry-hero-banner {
        height: 320px;
      }
    }
    @media (max-width: 640px) {
      .rc-folio-stats-strip,
      .rc-budget-metrics-grid {
        grid-template-columns: 1fr;
        gap: 0.5rem;
      }
    }
    """

    # HTML Body Content for the 7 Sections
    resources_html_content = """
    <!-- =====================================================================
         MAIN CONTENT: 7 UNIQUE KNOWLEDGE & STRATEGY SECTIONS
         ===================================================================== -->
    <main class="rc-page-wrap">

      <!-- SUB-HERO / KNOWLEDGE HUB HEADER STRIP -->
      <section class="rc-hero-strip">
        <div class="rc-container">
          <div class="rc-hero-content">
            <span class="rc-badge"><i class="fas fa-book-open"></i> Executive Event Architecture</span>
            <h1 class="rc-hero-title">Corporate Event Planning &amp; Conference Resources</h1>
            <p class="rc-hero-desc">
              Comprehensive strategic playbooks, T-minus operational checklists, budget variance models, architectural venue vetting criteria, and peer-reviewed event management insights.
            </p>
            <div class="rc-nav-pills">
              <a href="#planning-guides" class="rc-nav-pill"><i class="fas fa-book"></i> Planning Guides</a>
              <a href="#preparation-checklist" class="rc-nav-pill"><i class="fas fa-clipboard-check"></i> Readiness Checklist</a>
              <a href="#budget-guide" class="rc-nav-pill"><i class="fas fa-coins"></i> Budget Simulator</a>
              <a href="#venue-guide" class="rc-nav-pill"><i class="fas fa-compass-drafting"></i> Venue Selection</a>
              <a href="#hybrid-practices" class="rc-nav-pill"><i class="fas fa-broadcast-tower"></i> Hybrid Best Practices</a>
              <a href="#industry-insights" class="rc-nav-pill"><i class="fas fa-newspaper"></i> Industry Insights</a>
              <a href="#faq" class="rc-nav-pill"><i class="fas fa-circle-question"></i> Frequently Asked Questions</a>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 1: CORPORATE EVENT PLANNING GUIDES -->
      <section id="planning-guides" class="rc-section-guides">
        <div class="rc-container">
          <div class="rc-section-head framer-folio-glide">
            <span class="rc-badge"><i class="fas fa-book-bookmark"></i> Strategic Field Manuals</span>
            <h2 class="rc-title">Executive Folio Deck &amp; <span class="rc-title-gradient">Planning Playbooks</span></h2>
            <p class="rc-subtitle">
              Distilled from over 450 Fortune 500 summits and global symposiums. Access our complete framework for corporate governance, delegate orchestration, and mission control.
            </p>
          </div>

          <div class="rc-folio-deck-grid">
            <!-- Left: Featured Playbook Showcase -->
            <div class="rc-folio-book-showcase framer-folio-glide">
              <div class="rc-folio-img-box">
                <img src="images/resource_planning_guides.jpg" alt="Executive Event Planning Playbook and Leather Binder" loading="lazy">
                <div class="rc-folio-edition-tag">
                  <i class="fas fa-award" style="color: var(--rc-accent);"></i> 2026 Master Standard Edition
                </div>
              </div>
              <div class="rc-folio-body">
                <div>
                  <h3 id="currentFolioTitle" style="font-size: 1.5rem; font-weight: 800; color: var(--rc-text-main); margin-bottom: 0.5rem;">The Sovereign Summit Master Playbook (240 Pages)</h3>
                  <p id="currentFolioDesc" style="font-size: 0.95rem; color: var(--rc-text-muted); line-height: 1.6;">
                    Comprehensive blueprint detailing executive sponsor alignment, multi-track agenda design, crisis communication escalation trees, and real-time incident dispatching.
                  </p>
                </div>

                <div class="rc-folio-stats-strip">
                  <div class="rc-folio-stat-item">
                    <span class="rc-folio-stat-lbl">Target Audience</span>
                    <span id="folioAudienceVal" class="rc-folio-stat-val">C-Suite &amp; Directors</span>
                  </div>
                  <div class="rc-folio-stat-item">
                    <span class="rc-folio-stat-lbl">Scale Tested</span>
                    <span id="folioScaleVal" class="rc-folio-stat-val">500 – 15,000 Pax</span>
                  </div>
                  <div class="rc-folio-stat-item">
                    <span class="rc-folio-stat-lbl">Format &amp; Templates</span>
                    <span id="folioFormatVal" class="rc-folio-stat-val">PDF + Excel Toolkit</span>
                  </div>
                </div>

                <div style="display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;">
                  <button class="rc-btn rc-btn-primary" onclick="alert('Downloading The Sovereign Summit Master Playbook (PDF + XLS Toolkit)...');"><i class="fas fa-file-arrow-down"></i> Download Master Playbook</button>
                  <button class="rc-btn rc-btn-outline" onclick="window.location.href='#preparation-checklist'"><i class="fas fa-arrow-right"></i> View Checklist</button>
                </div>
              </div>
            </div>

            <!-- Right: 3 Folio Chapters Stack -->
            <div class="rc-chapters-col">
              <div class="rc-chapter-card active framer-folio-glide" onclick="selectFolioChapter(0)">
                <div class="rc-chapter-badge-num">01</div>
                <div class="rc-chapter-info">
                  <div class="rc-chapter-title">Pre-Event Strategic Architecture &amp; Governance</div>
                  <div class="rc-chapter-desc">Establishing core steering committees, defining ROI milestones, and drafting master procurement charters.</div>
                </div>
              </div>

              <div class="rc-chapter-card framer-folio-glide" onclick="selectFolioChapter(1)">
                <div class="rc-chapter-badge-num">02</div>
                <div class="rc-chapter-info">
                  <div class="rc-chapter-title">Production Logistics &amp; Redundancy Protocols</div>
                  <div class="rc-chapter-desc">Dual-ring optical fiber routing, backup diesel power generation, and broadcast transmission SLAs.</div>
                </div>
              </div>

              <div class="rc-chapter-card framer-folio-glide" onclick="selectFolioChapter(2)">
                <div class="rc-chapter-badge-num">03</div>
                <div class="rc-chapter-info">
                  <div class="rc-chapter-title">Post-Event Synthesis &amp; Sentiment Analytics</div>
                  <div class="rc-chapter-desc">Automated attendee sentiment tracking, sponsor attribution modeling, and executive summary debriefs.</div>
                </div>
              </div>

              <div style="background: var(--rc-surface); border: 1px dashed var(--rc-accent); border-radius: 1rem; padding: 1.15rem; display: flex; align-items: center; gap: 0.85rem;" class="framer-folio-glide">
                <i class="fas fa-shield-halved" style="color: var(--rc-accent); font-size: 1.35rem;"></i>
                <div style="font-size: 0.84rem; color: var(--rc-text-muted); line-height: 1.45;">
                  <strong style="color: var(--rc-text-main);">Verified Governance Standard:</strong> All guides align with MPI (Meeting Professionals International) and ISO 20121 certified sustainable protocols.
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 2: CONFERENCE PREPARATION CHECKLIST -->
      <section id="preparation-checklist" class="rc-section-checklist">
        <div class="rc-container">
          <div class="rc-section-head framer-countdown-snap">
            <span class="rc-badge"><i class="fas fa-clipboard-check"></i> Operational Readiness</span>
            <h2 class="rc-title">Countdown T-Minus Timeline &amp; <span class="rc-title-gradient">Readiness Matrix</span></h2>
            <p class="rc-subtitle">
              Track your summit preparation down to the minute. Complete the checklist items below to dynamically assess your organization's event readiness score.
            </p>
          </div>

          <div class="rc-countdown-layout">
            <!-- Left: Audit Bench Visual & Readiness Meter -->
            <div class="rc-audit-bench-card framer-countdown-snap">
              <div class="rc-audit-img-box">
                <img src="images/resource_conference_checklist.jpg" alt="Conference Audit Desk with Precision Magnifier and Checklist" loading="lazy">
                <div style="position: absolute; bottom: 1.25rem; left: 1.25rem; background: rgba(15, 23, 42, 0.88); backdrop-filter: blur(8px); padding: 0.5rem 1rem; border-radius: 0.75rem; color: #ffffff; font-size: 0.82rem; font-weight: 700;">
                  <i class="fas fa-magnifying-glass" style="color: var(--rc-accent);"></i> 180-Day Mission Countdown Control
                </div>
              </div>

              <div class="rc-audit-card-body">
                <div>
                  <h3 style="font-size: 1.35rem; font-weight: 800; color: var(--rc-text-main); margin-bottom: 0.5rem;">Real-Time Operational Audit</h3>
                  <p style="font-size: 0.9rem; color: var(--rc-text-muted); line-height: 1.5;">
                    Verify key mission milestones across the 4 critical conference planning horizons:
                  </p>
                </div>

                <div class="rc-readiness-meter-box">
                  <div class="rc-readiness-row">
                    <span style="font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--rc-text-muted);">Overall Readiness Status</span>
                    <span id="readinessScoreText" style="font-size: 1.15rem; font-weight: 900; color: #10b981;">100% Prepared</span>
                  </div>
                  <div class="rc-meter-track">
                    <div id="readinessBarFill" class="rc-meter-fill" style="width: 100%;"></div>
                  </div>
                  <div style="font-size: 0.78rem; color: var(--rc-text-light);">
                    <i class="fas fa-check-circle" style="color: #10b981;"></i> All primary security, legal, and AV production gates satisfied.
                  </div>
                </div>

                <div>
                  <button class="rc-btn rc-btn-outline" style="width: 100%;" onclick="alert('Exporting Interactive Readiness Checklist to CSV...');">
                    <i class="fas fa-file-csv"></i> Export Full Checklist to CSV
                  </button>
                </div>
              </div>
            </div>

            <!-- Right: 4 Chronological Countdown Milestone Pods -->
            <div class="rc-timeline-pods-wrap framer-countdown-snap">
              <div class="rc-milestone-pod">
                <div class="rc-milestone-head">
                  <div class="rc-milestone-title"><i class="fas fa-flag-checkered" style="color: var(--rc-accent);"></i> T-180 Days: Charter &amp; Venue Lock</div>
                  <span class="rc-milestone-tag">Phase 1</span>
                </div>
                <div class="rc-check-item-row">
                  <input type="checkbox" checked onchange="updateReadinessScore(this, 10)">
                  <span>Finalize Master Service Agreement (MSA) with host convention facility</span>
                </div>
                <div class="rc-check-item-row">
                  <input type="checkbox" checked onchange="updateReadinessScore(this, 10)">
                  <span>Form Executive Steering Committee and approve preliminary CapEx budget</span>
                </div>
              </div>

              <div class="rc-milestone-pod">
                <div class="rc-milestone-head">
                  <div class="rc-milestone-title"><i class="fas fa-microphone" style="color: var(--rc-accent);"></i> T-90 Days: Keynote &amp; AV Rigging Lock</div>
                  <span class="rc-milestone-tag">Phase 2</span>
                </div>
                <div class="rc-check-item-row">
                  <input type="checkbox" checked onchange="updateReadinessScore(this, 10)">
                  <span>Confirm headline keynote talent, technical riders, and VIP security protocols</span>
                </div>
                <div class="rc-check-item-row">
                  <input type="checkbox" checked onchange="updateReadinessScore(this, 10)">
                  <span>Finalize scenic CAD drawings, 8K MicroLED wall pitch, and spatial acoustic plots</span>
                </div>
              </div>

              <div class="rc-milestone-pod">
                <div class="rc-milestone-head">
                  <div class="rc-milestone-title"><i class="fas fa-id-card" style="color: var(--rc-accent);"></i> T-30 Days: Credentials &amp; Run-of-Show</div>
                  <span class="rc-milestone-tag">Phase 3</span>
                </div>
                <div class="rc-check-item-row">
                  <input type="checkbox" checked onchange="updateReadinessScore(this, 15)">
                  <span>Print RFID smart badges and configure encrypted contactless registration desks</span>
                </div>
                <div class="rc-check-item-row">
                  <input type="checkbox" checked onchange="updateReadinessScore(this, 15)">
                  <span>Execute minute-by-minute technical run-of-show dry runs with show caller</span>
                </div>
              </div>

              <div class="rc-milestone-pod">
                <div class="rc-milestone-head">
                  <div class="rc-milestone-title"><i class="fas fa-bolt" style="color: var(--rc-accent);"></i> T-0 Days: On-Site Command Dispatch</div>
                  <span class="rc-milestone-tag">Live Show</span>
                </div>
                <div class="rc-check-item-row">
                  <input type="checkbox" checked onchange="updateReadinessScore(this, 15)">
                  <span>Initialize redundant fiber rings, comms headsets, and emergency medical team</span>
                </div>
                <div class="rc-check-item-row">
                  <input type="checkbox" checked onchange="updateReadinessScore(this, 15)">
                  <span>Commence continuous telemetry monitoring of attendee flow and VIP ingress</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 3: EVENT BUDGET PLANNING GUIDE -->
      <section id="budget-guide" class="rc-section-budget">
        <div class="rc-container">
          <div class="rc-section-head framer-capex-reveal">
            <span class="rc-badge"><i class="fas fa-coins"></i> Fiscal Governance &amp; Variance</span>
            <h2 class="rc-title">Variance Analysis &amp; <span class="rc-title-gradient">CapEx Allocation Simulator</span></h2>
            <p class="rc-subtitle">
              Avoid unexpected budget creep. Benchmark your conference expenditures against standard enterprise percentage models and project cost allocations in real time.
            </p>
          </div>

          <div class="rc-budget-cockpit-grid">
            <!-- Left: Financial Media Card & Key Ratios -->
            <div class="rc-budget-media-card framer-capex-reveal">
              <div class="rc-budget-img-box">
                <img src="images/resource_budget_guide.jpg" alt="Executive Financial Planner Reviewing Event Budget Allocation" loading="lazy">
                <div style="position: absolute; top: 1.25rem; left: 1.25rem; background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(8px); padding: 0.5rem 1rem; border-radius: 0.75rem; color: #ffffff; font-size: 0.82rem; font-weight: 700;">
                  <i class="fas fa-chart-pie" style="color: var(--rc-accent);"></i> Enterprise CapEx Model
                </div>
              </div>

              <div class="rc-budget-roi-strip">
                <div>
                  <h3 style="font-size: 1.35rem; font-weight: 800; color: var(--rc-text-main); margin-bottom: 0.5rem;">Corporate Benchmark Ratios</h3>
                  <p style="font-size: 0.9rem; color: var(--rc-text-muted); line-height: 1.5;">
                    Data synthesized across top-tier international congresses and executive summits:
                  </p>
                </div>

                <div class="rc-budget-metrics-grid">
                  <div class="rc-bmetric-item">
                    <span class="rc-bmetric-val">$485</span>
                    <span class="rc-bmetric-lbl">Avg Cost / Pax</span>
                  </div>
                  <div class="rc-bmetric-item">
                    <span class="rc-bmetric-val">12.5%</span>
                    <span class="rc-bmetric-lbl">Buffer Reserve</span>
                  </div>
                  <div class="rc-bmetric-item">
                    <span class="rc-bmetric-val">42%</span>
                    <span class="rc-bmetric-lbl">Sponsor Offset</span>
                  </div>
                </div>

                <div>
                  <button class="rc-btn rc-btn-primary" style="width: 100%;" onclick="alert('Downloading Enterprise Budget Model Template (Excel)...');">
                    <i class="fas fa-file-excel"></i> Download Excel Budget Model
                  </button>
                </div>
              </div>
            </div>

            <!-- Right: Interactive Budget Simulator -->
            <div class="rc-simulator-panel framer-capex-reveal">
              <div>
                <span class="rc-badge"><i class="fas fa-calculator"></i> Interactive Cost Model</span>
                <h3 style="font-size: 1.5rem; font-weight: 800; color: var(--rc-text-main); margin-bottom: 0.5rem;">CapEx Projection Calculator</h3>
                <p style="font-size: 0.9rem; color: var(--rc-text-muted); line-height: 1.5;">
                  Select your expected delegate attendance volume to recalculate recommended tier budgets:
                </p>

                <!-- Attendance Volume Selector Buttons -->
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 1rem;">
                  <button class="rc-btn rc-btn-outline" id="btnCap500" onclick="simulateBudget(500, this)" style="padding: 0.5rem 1rem; font-size: 0.85rem;">500 Delegates</button>
                  <button class="rc-btn rc-btn-primary" id="btnCap1500" onclick="simulateBudget(1500, this)" style="padding: 0.5rem 1rem; font-size: 0.85rem;">1,500 Delegates</button>
                  <button class="rc-btn rc-btn-outline" id="btnCap5000" onclick="simulateBudget(5000, this)" style="padding: 0.5rem 1rem; font-size: 0.85rem;">5,000 Delegates</button>
                </div>

                <!-- 5 Dynamic Allocation Progress Bars -->
                <div class="rc-allocation-bars-box">
                  <div class="rc-alloc-item">
                    <div class="rc-alloc-header">
                      <span>Venue &amp; Haute Banqueting (35%)</span>
                      <span id="allocVenueText">$254,625</span>
                    </div>
                    <div class="rc-alloc-bar-bg"><div class="rc-alloc-bar-fill" style="width: 35%; background: #3b82f6;"></div></div>
                  </div>

                  <div class="rc-alloc-item">
                    <div class="rc-alloc-header">
                      <span>Audiovisual &amp; Broadcast Lighting (28%)</span>
                      <span id="allocAvText">$203,700</span>
                    </div>
                    <div class="rc-alloc-bar-bg"><div class="rc-alloc-bar-fill" style="width: 28%; background: #d97706;"></div></div>
                  </div>

                  <div class="rc-alloc-item">
                    <div class="rc-alloc-header">
                      <span>Keynote Honorariums &amp; VIP Logistics (18%)</span>
                      <span id="allocSpeakerText">$130,950</span>
                    </div>
                    <div class="rc-alloc-bar-bg"><div class="rc-alloc-bar-fill" style="width: 18%; background: #10b981;"></div></div>
                  </div>

                  <div class="rc-alloc-item">
                    <div class="rc-alloc-header">
                      <span>Scenic Fabrication &amp; Technology (12%)</span>
                      <span id="allocScenicText">$87,300</span>
                    </div>
                    <div class="rc-alloc-bar-bg"><div class="rc-alloc-bar-fill" style="width: 12%; background: #8b5cf6;"></div></div>
                  </div>

                  <div class="rc-alloc-item">
                    <div class="rc-alloc-header">
                      <span>Contingency &amp; Force Majeure Reserve (7%)</span>
                      <span id="allocContingencyText">$50,925</span>
                    </div>
                    <div class="rc-alloc-bar-bg"><div class="rc-alloc-bar-fill" style="width: 7%; background: #ef4444;"></div></div>
                  </div>
                </div>
              </div>

              <!-- Output Total Banner -->
              <div class="rc-sim-calc-box">
                <div>
                  <span style="font-size: 0.78rem; text-transform: uppercase; font-weight: 700; color: var(--rc-text-light); letter-spacing: 0.05em;">Projected Total Budget</span>
                  <div id="simTotalBudget" style="font-size: 2rem; font-weight: 900; color: var(--rc-text-main); font-family: monospace;">$727,500</div>
                </div>
                <button class="rc-btn rc-btn-primary" onclick="alert('Budget parameters locked. Proceeding to proposal generator...');">
                  <i class="fas fa-check"></i> Lock Budget Parameters
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 4: VENUE SELECTION GUIDE -->
      <section id="venue-guide" class="rc-section-venue-guide">
        <div class="rc-container">
          <div class="rc-section-head framer-blueprint-draft">
            <span class="rc-badge"><i class="fas fa-compass-drafting"></i> Spatial Engineering</span>
            <h2 class="rc-title">Architectural Spatial Dimensioner &amp; <span class="rc-title-gradient">Vetting Matrix</span></h2>
            <p class="rc-subtitle">
              Evaluating ceiling clearance, load-in freight capacity, fiber connectivity, and acoustic absorption before signing facility lease commitments.
            </p>
          </div>

          <div class="rc-venue-guide-layout">
            <!-- Left: Blueprint Visual Card -->
            <div class="rc-blueprint-visual-card framer-blueprint-draft">
              <div class="rc-blueprint-img-box">
                <img src="images/resource_venue_guide.jpg" alt="Architectural Floorplan and Spatial Dimension Blueprint" loading="lazy">
                <div class="rc-cad-badge-floating">
                  <i class="fas fa-ruler-combined"></i> CAD Vector Dimensioned
                </div>
              </div>

              <div class="rc-blueprint-body">
                <div>
                  <h3 style="font-size: 1.35rem; font-weight: 800; color: var(--rc-text-main); margin-bottom: 0.5rem;">Spatial Density Formula</h3>
                  <p style="font-size: 0.9rem; color: var(--rc-text-muted); line-height: 1.5;">
                    Never compromise on delegate comfort. Standard seating allocations used by our architectural planners:
                  </p>
                </div>

                <div style="background: var(--rc-surface-muted); border: 1px solid var(--rc-card-border); border-radius: 1rem; padding: 1.25rem; margin: 1rem 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem;">
                  <div>
                    <div style="font-size: 1.1rem; font-weight: 800; color: var(--rc-text-main);">18 sq ft</div>
                    <div style="font-size: 0.72rem; color: var(--rc-text-muted); text-transform: uppercase;">Theater Style / Pax</div>
                  </div>
                  <div>
                    <div style="font-size: 1.1rem; font-weight: 800; color: var(--rc-text-main);">28 sq ft</div>
                    <div style="font-size: 0.72rem; color: var(--rc-text-muted); text-transform: uppercase;">Plated Gala / Pax</div>
                  </div>
                  <div>
                    <div style="font-size: 1.1rem; font-weight: 800; color: var(--rc-text-main);">45 sq ft</div>
                    <div style="font-size: 0.72rem; color: var(--rc-text-muted); text-transform: uppercase;">Trade Expo / Booth</div>
                  </div>
                </div>

                <div>
                  <button class="rc-btn rc-btn-outline" style="width: 100%;" onclick="alert('Downloading 12-Page Venue Selection Technical Audit Guide (PDF)...');">
                    <i class="fas fa-file-pdf"></i> Download Venue Vetting Audit Sheet (PDF)
                  </button>
                </div>
              </div>
            </div>

            <!-- Right: 4 Vetting Protocol Cards -->
            <div class="rc-vetting-pillars framer-blueprint-draft">
              <div class="rc-vetting-card">
                <div class="rc-vetting-title"><i class="fas fa-arrows-up-down"></i> Rigging &amp; Ceiling Clear-Span</div>
                <div class="rc-vetting-desc">
                  Ensure a minimum 24-foot vertical trim height for 8K video screens. Verify roof structural truss points hold at least 2,000 lbs per point.
                </div>
              </div>

              <div class="rc-vetting-card">
                <div class="rc-vetting-title"><i class="fas fa-truck-ramp-box"></i> Loading Dock Logistics &amp; Ingress</div>
                <div class="rc-vetting-desc">
                  Direct drive-in freight door access (minimum 14ft height) for articulated 53-foot production semi-trailers to avoid multi-day staging delays.
                </div>
              </div>

              <div class="rc-vetting-card">
                <div class="rc-vetting-title"><i class="fas fa-wifi"></i> Dual-Homed Gigabit Fiber &amp; Camlok Power</div>
                <div class="rc-vetting-desc">
                  Redundant fiber drops from separate Tier-1 transit providers (AT&amp;T / Lumen) and minimum 400A 3-phase electrical distribution with UPS bypass.
                </div>
              </div>

              <div class="rc-vetting-card">
                <div class="rc-vetting-title"><i class="fas fa-leaf"></i> ISO 20121 &amp; Carbon Neutrality Certs</div>
                <div class="rc-vetting-desc">
                  Verified green building certifications (LEED Gold or BREEAM Excellent) with 100% renewable grid power and graywater recycling systems.
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 5: HYBRID EVENT BEST PRACTICES -->
      <section id="hybrid-practices" class="rc-section-hybrid">
        <div class="rc-container">
          <div class="rc-section-head framer-dual-hemisphere">
            <span class="rc-badge"><i class="fas fa-broadcast-tower"></i> Global Simulcast Engineering</span>
            <h2 class="rc-title">Synchronous Dual-Hemisphere <span class="rc-title-gradient">Broadcast Framework</span></h2>
            <p class="rc-subtitle">
              Seamlessly unify physical ballroom delegates with thousands of live virtual participants through sub-second streaming, interactive spatial polling, and real-time AI translation.
            </p>
          </div>

          <div class="rc-dual-hemisphere-wrap framer-dual-hemisphere">
            <!-- Telemetry Hero Banner -->
            <div class="rc-telemetry-hero-banner">
              <img src="images/resource_hybrid_practices.jpg" alt="Synchronous Hybrid Event Broadcast Telemetry Map" loading="lazy">
              <div class="rc-broadcast-telemetry-bar">
                <div>
                  <span style="font-size: 0.78rem; text-transform: uppercase; font-weight: 800; color: #fbbf24; letter-spacing: 0.05em;">Global Broadcast Mesh</span>
                  <div style="font-size: 1.35rem; font-weight: 900; margin-top: 0.2rem;">Multi-Cloud WebRTC &amp; HLS CDN Active</div>
                </div>
                <div style="display: flex; gap: 1.5rem; flex-wrap: wrap;">
                  <div>
                    <span style="font-size: 0.72rem; color: #94a3b8; text-transform: uppercase;">Glass-to-Glass Latency</span>
                    <div style="font-family: monospace; font-size: 1.15rem; font-weight: 800; color: #38bdf8;">850 ms</div>
                  </div>
                  <div>
                    <span style="font-size: 0.72rem; color: #94a3b8; text-transform: uppercase;">Simultaneous Streams</span>
                    <div style="font-family: monospace; font-size: 1.15rem; font-weight: 800; color: #10b981;">32,000+ Active</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Dual Hemisphere Pillars: In-Person vs Remote -->
            <div class="rc-split-spheres-grid">
              <div class="rc-sphere-card">
                <div class="rc-sphere-head">
                  <i class="fas fa-users" style="color: var(--rc-accent);"></i> Physical Ballroom Sphere
                </div>
                <div class="rc-sphere-list">
                  <div class="rc-sphere-item">
                    <i class="fas fa-check"></i>
                    <span><strong>Confidence Monitors:</strong> Downstage 55-inch teleprompters displaying timing, presentation notes, and incoming remote delegate Q&amp;A.</span>
                  </div>
                  <div class="rc-sphere-item">
                    <i class="fas fa-check"></i>
                    <span><strong>Spatial Stage Audio:</strong> Dynamic beam-steered microphones isolating podium speakers with zero ambient echo back into the broadcast feed.</span>
                  </div>
                  <div class="rc-sphere-item">
                    <i class="fas fa-check"></i>
                    <span><strong>Tactile Networking Nodes:</strong> High-speed RFID badge tap kiosks syncing on-site connections with virtual attendee profiles.</span>
                  </div>
                </div>
              </div>

              <div class="rc-sphere-card">
                <div class="rc-sphere-head">
                  <i class="fas fa-globe" style="color: #38bdf8;"></i> Remote Cloud Experience
                </div>
                <div class="rc-sphere-list">
                  <div class="rc-sphere-item">
                    <i class="fas fa-check"></i>
                    <span><strong>Sub-Second Interactivity:</strong> Ultra-low latency WebRTC video transport enabling live remote attendees to ask questions verbally from home.</span>
                  </div>
                  <div class="rc-sphere-item">
                    <i class="fas fa-check"></i>
                    <span><strong>AI Simultaneous Translation:</strong> Neural multilingual closed captioning and synthesized audio dubbing in 14 languages simultaneously.</span>
                  </div>
                  <div class="rc-sphere-item">
                    <i class="fas fa-check"></i>
                    <span><strong>Digital Expo Salons:</strong> 3D interactive sponsor booths with calendar booking integrations and direct video breakout pods.</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 6: INDUSTRY INSIGHTS & ARTICLES -->
      <section id="industry-insights" class="rc-section-insights">
        <div class="rc-container">
          <div class="rc-section-head framer-editorial-rise">
            <span class="rc-badge"><i class="fas fa-newspaper"></i> Thought Leadership</span>
            <h2 class="rc-title">Executive Research Journal &amp; <span class="rc-title-gradient">Industry Monographs</span></h2>
            <p class="rc-subtitle">
              Peer-reviewed whitepapers, trend forecasts, and macroeconomic analysis on how the world's most innovative organizations execute transformative events.
            </p>
          </div>

          <div class="rc-insights-editorial-grid">
            <!-- Left: Featured Lead Monograph -->
            <div class="rc-featured-monograph-card framer-editorial-rise">
              <div class="rc-monograph-img-box">
                <img src="images/resource_industry_insights.jpg" alt="Executive Research Library and Thought Leadership Monographs" loading="lazy">
                <div style="position: absolute; top: 1.25rem; left: 1.25rem; background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(8px); padding: 0.5rem 1rem; border-radius: 0.75rem; color: #ffffff; font-size: 0.82rem; font-weight: 700;">
                  <i class="fas fa-star" style="color: #fbbf24;"></i> Q4 Flagship Research Paper
                </div>
              </div>

              <div class="rc-monograph-body">
                <div>
                  <div style="font-size: 0.8rem; color: var(--rc-accent); font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.35rem;">
                    GLOBAL SUMMIT BENCHMARK REPORT
                  </div>
                  <h3 style="font-size: 1.5rem; font-weight: 800; color: var(--rc-text-main); margin-bottom: 0.75rem; line-height: 1.3;">
                    The Economics of Immersive Corporate Gatherings: Why Physical Presence Outperforms Virtual-Only Engagements
                  </h3>
                  <p style="font-size: 0.92rem; color: var(--rc-text-muted); line-height: 1.6;">
                    An empirical survey across 320 global enterprise executives revealing a 310% higher contract close velocity when deal stages are advanced during private executive summits versus remote video conferencing.
                  </p>
                </div>

                <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--rc-card-border); padding-top: 1.25rem;">
                  <div style="font-size: 0.85rem; color: var(--rc-text-muted);">
                    <i class="fas fa-clock"></i> 8 Min Read &bull; By Dr. Eleanor Vance
                  </div>
                  <button class="rc-btn rc-btn-primary" style="padding: 0.65rem 1.25rem; font-size: 0.88rem;" onclick="alert('Opening Full Monograph: The Economics of Immersive Corporate Gatherings...');">
                    Read Monograph <i class="fas fa-arrow-right"></i>
                  </button>
                </div>
              </div>
            </div>

            <!-- Right: 3 Curated Research Articles -->
            <div class="rc-curated-articles-stack framer-editorial-rise">
              <div class="rc-article-card" onclick="alert('Opening article: The Sovereign AI Revolution in Conference Moderation...');">
                <div class="rc-article-meta">
                  <span style="color: var(--rc-accent); font-weight: 800;">TECHNOLOGY &amp; AI</span>
                  <span>Nov 2026 &bull; 5 Min</span>
                </div>
                <div class="rc-article-title">The Sovereign AI Revolution in Conference Moderation &amp; Dynamic Agenda Routing</div>
                <div class="rc-article-excerpt">
                  How autonomous real-time language agents dynamically adjust plenary discussion topics based on crowd sentiment telemetry.
                </div>
              </div>

              <div class="rc-article-card" onclick="alert('Opening article: Carbon-Neutral Banqueting: The Zero-Waste Sourcing Model...');">
                <div class="rc-article-meta">
                  <span style="color: #10b981; font-weight: 800;">SUSTAINABILITY &amp; ESG</span>
                  <span>Oct 2026 &bull; 6 Min</span>
                </div>
                <div class="rc-article-title">Carbon-Neutral Banqueting: Implementing 100% Zero-Waste Food Recovery at Scale</div>
                <div class="rc-article-excerpt">
                  Practical guidelines for redistributing surplus luxury banquet gastronomy to licensed charity networks within 90 minutes.
                </div>
              </div>

              <div class="rc-article-card" onclick="alert('Opening article: Neuro-Ergonomics of Keynote Stage Design...');">
                <div class="rc-article-meta">
                  <span style="color: #3b82f6; font-weight: 800;">EXECUTIVE STRATEGY</span>
                  <span>Sep 2026 &bull; 7 Min</span>
                </div>
                <div class="rc-article-title">Neuro-Ergonomics of Stage Lighting: Maximizing Executive Attention Span in Dim Auditoriums</div>
                <div class="rc-article-excerpt">
                  Circadian lighting temperature choreography that prevents attendee fatigue during grueling 8-hour plenary sessions.
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 7: FREQUENTLY ASKED QUESTIONS -->
      <section id="faq" class="rc-section-faq">
        <div class="rc-container">
          <div class="rc-section-head framer-vault-open">
            <span class="rc-badge"><i class="fas fa-circle-question"></i> Advisory &amp; Knowledge Base</span>
            <h2 class="rc-title">Concierge Knowledge Exchange &amp; <span class="rc-title-gradient">Diagnostic Vault</span></h2>
            <p class="rc-subtitle">
              Clear answers to mission-critical questions regarding contracts, force majeure, confidential intellectual property, and global event logistics.
            </p>
          </div>

          <div class="rc-faq-layout-grid">
            <!-- Left: Concierge Support Desk Card -->
            <div class="rc-faq-concierge-card framer-vault-open">
              <div class="rc-faq-concierge-img">
                <img src="images/resource_faq_desk.jpg" alt="Executive Event Advisory and Concierge Consultation Desk" loading="lazy">
                <div style="position: absolute; top: 1.25rem; left: 1.25rem; background: rgba(15, 23, 42, 0.88); backdrop-filter: blur(8px); padding: 0.5rem 1rem; border-radius: 0.75rem; color: #ffffff; font-size: 0.82rem; font-weight: 700;">
                  <i class="fas fa-headset" style="color: var(--rc-accent);"></i> Senior Advisory Desk
                </div>
              </div>

              <div class="rc-concierge-details">
                <div>
                  <h3 style="font-size: 1.35rem; font-weight: 800; color: var(--rc-text-main); margin-bottom: 0.5rem;">Need Specific Guidance?</h3>
                  <p style="font-size: 0.9rem; color: var(--rc-text-muted); line-height: 1.5;">
                    Our executive producers and legal procurement counsels are available for confidential briefing calls.
                  </p>
                </div>

                <div style="background: var(--rc-surface-muted); padding: 1.25rem; border-radius: 1rem; border: 1px solid var(--rc-card-border); font-size: 0.85rem; color: var(--rc-text-muted); line-height: 1.6;">
                  <div><strong style="color: var(--rc-text-main);"><i class="fas fa-envelope" style="color: var(--rc-accent);"></i> Direct Desk:</strong> advisory@corporateevents.com</div>
                  <div style="margin-top: 0.4rem;"><strong style="color: var(--rc-text-main);"><i class="fas fa-phone-alt" style="color: var(--rc-accent);"></i> Hotline:</strong> +1 (800) 555-SUMMIT</div>
                  <div style="margin-top: 0.4rem;"><strong style="color: var(--rc-text-main);"><i class="fas fa-clock" style="color: var(--rc-accent);"></i> Response Time:</strong> Under 2 business hours</div>
                </div>

                <div>
                  <button class="rc-btn rc-btn-primary" style="width: 100%;" onclick="alert('Opening Direct Advisory Scheduling Portal...');">
                    <i class="fas fa-calendar-check"></i> Book Executive Consultation
                  </button>
                </div>
              </div>
            </div>

            <!-- Right: Interactive Searchable Accordion Panel -->
            <div class="rc-accordion-panel framer-vault-open">
              <!-- Live Search Box -->
              <div class="rc-faq-search-box">
                <i class="fas fa-search rc-faq-search-icon"></i>
                <input type="text" id="faqSearchInput" class="rc-faq-search-input" placeholder="Search questions (e.g. budget, security, timeline, contract)..." oninput="filterFaqQuestions(this.value)">
              </div>

              <!-- Accordion Items -->
              <div class="rc-accordion-item active" data-keywords="timeline planning advance lead time date">
                <div class="rc-accordion-header" onclick="toggleAccordion(this)">
                  <span>What is the recommended planning runway for an international conference?</span>
                  <i class="fas fa-chevron-down rc-accordion-chevron"></i>
                </div>
                <div class="rc-accordion-body" style="max-height: 200px;">
                  <div class="rc-accordion-content">
                    For flagship congresses of 1,000 to 10,000 delegates, we recommend a minimum runway of <strong>6 to 9 months</strong> to ensure premier venue locks, international keynote clearances, and favorable hotel room block rates. However, our rapid-deployment team can execute summits within <strong>60 to 90 days</strong> under accelerated sprint protocols.
                  </div>
                </div>
              </div>

              <div class="rc-accordion-item" data-keywords="budget cost billing transparent pricing fee msa">
                <div class="rc-accordion-header" onclick="toggleAccordion(this)">
                  <span>How does your firm structure management fees and vendor procurement costs?</span>
                  <i class="fas fa-chevron-down rc-accordion-chevron"></i>
                </div>
                <div class="rc-accordion-body">
                  <div class="rc-accordion-content">
                    We practice <strong>100% transparent open-book accounting</strong>. Clients receive direct pass-through wholesale pricing from venues, catering, and audiovisual suppliers with zero hidden markups. Our firm operates on a pre-agreed fixed project management retainer or a tiered percentage fee based on scope complexity.
                  </div>
                </div>
              </div>

              <div class="rc-accordion-item" data-keywords="security nda privacy confidentiality vip protection sovereign">
                <div class="rc-accordion-header" onclick="toggleAccordion(this)">
                  <span>What non-disclosure and physical security protocols are implemented for private summits?</span>
                  <i class="fas fa-chevron-down rc-accordion-chevron"></i>
                </div>
                <div class="rc-accordion-body">
                  <div class="rc-accordion-content">
                    All full-time staff, technicians, and vendor crews sign stringent bilateral NDAs. For sovereign and high-profile gatherings, we integrate diplomatic close-protection motorcades, secure RFID biometric credential verification, RF counter-surveillance sweeps, and private encrypted Wi-Fi networks.
                  </div>
                </div>
              </div>

              <div class="rc-accordion-item" data-keywords="force majeure contingency weather cancellation insurance backup">
                <div class="rc-accordion-header" onclick="toggleAccordion(this)">
                  <span>How do you manage force majeure events, severe weather, or unforeseen cancellations?</span>
                  <i class="fas fa-chevron-down rc-accordion-chevron"></i>
                </div>
                <div class="rc-accordion-body">
                  <div class="rc-accordion-content">
                    Every production incorporates an active <strong>Emergency Continuity Matrix</strong>. This includes comprehensive Event Cancellation &amp; Non-Appearance insurance coverage ($20M+ policies), dual-homed power generation, and instant one-click fallback to a synchronous virtual broadcast studio within 4 hours.
                  </div>
                </div>
              </div>

              <div class="rc-accordion-item" data-keywords="hybrid virtual streaming international multi-city simultaneous">
                <div class="rc-accordion-header" onclick="toggleAccordion(this)">
                  <span>Can your team coordinate simultaneous multi-city global hub summits?</span>
                  <i class="fas fa-chevron-down rc-accordion-chevron"></i>
                </div>
                <div class="rc-accordion-body">
                  <div class="rc-accordion-content">
                    Yes. We specialize in synchronized multi-city hub architectures linking primary ballrooms in New York, London, and Singapore via dedicated satellite and fiber pipelines with genlocked live switching and low-latency audio interactivity.
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

    </main>
    """

    # Page Interactive Scripts (clean, standalone JavaScript)
    resources_scripts = """
  <!-- =====================================================================
       INTERACTIVE CLIENT CONTROLS & FRAMER MOTION OBSERVERS
       ===================================================================== -->
  <script>
    // 1. Framer Motion Scroll Trigger Observers
    document.addEventListener('DOMContentLoaded', function () {
      var motionClasses = [
        '.framer-folio-glide',
        '.framer-countdown-snap',
        '.framer-capex-reveal',
        '.framer-blueprint-draft',
        '.framer-dual-hemisphere',
        '.framer-editorial-rise',
        '.framer-vault-open'
      ];

      var motionObserver = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('framer-in-view');
            var children = entry.target.querySelectorAll('.framer-folio-glide, .framer-countdown-snap, .framer-capex-reveal, .framer-blueprint-draft, .framer-dual-hemisphere, .framer-editorial-rise, .framer-vault-open');
            children.forEach(function (c, idx) {
              setTimeout(function () {
                c.classList.add('framer-in-view');
              }, idx * 80);
            });
            obs.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
      });

      motionClasses.forEach(function (selector) {
        document.querySelectorAll(selector).forEach(function (el) {
          motionObserver.observe(el);
        });
      });
    });

    // 2. Section 1: Folio Chapter Selector
    var folioChaptersData = [
      {
        title: "The Sovereign Summit Master Playbook (240 Pages)",
        desc: "Comprehensive blueprint detailing executive sponsor alignment, multi-track agenda design, crisis communication escalation trees, and real-time incident dispatching.",
        audience: "C-Suite & Directors",
        scale: "500 – 15,000 Pax",
        format: "PDF + Excel Toolkit"
      },
      {
        title: "Technical Production & Redundancy Protocol (180 Pages)",
        desc: "Touring-grade broadcast audio/video specifications, dual-homed optical fiber ring deployment, and backup uninterruptible generator load calculations.",
        audience: "Technical Producers",
        scale: "Keynote & Hybrid",
        format: "CAD + Tech Spec PDF"
      },
      {
        title: "Post-Event Analytics & Executive ROI Synthesis (95 Pages)",
        desc: "Statistical methodologies for measuring sponsor brand equity attribution, attendee retention metrics, and post-conference feedback survey synthesis.",
        audience: "CMOs & Stakeholders",
        scale: "Enterprise Global",
        format: "Dashboard + Slide Deck"
      }
    ];

    function selectFolioChapter(index) {
      var cards = document.querySelectorAll('.rc-chapter-card');
      cards.forEach(function (c, idx) {
        if (idx === index) c.classList.add('active');
        else c.classList.remove('active');
      });

      var data = folioChaptersData[index];
      var titleEl = document.getElementById('currentFolioTitle');
      var descEl = document.getElementById('currentFolioDesc');
      var audEl = document.getElementById('folioAudienceVal');
      var scaEl = document.getElementById('folioScaleVal');
      var fmtEl = document.getElementById('folioFormatVal');

      if (titleEl) {
        titleEl.style.opacity = '0';
        setTimeout(function () {
          titleEl.textContent = data.title;
          if (descEl) descEl.textContent = data.desc;
          if (audEl) audEl.textContent = data.audience;
          if (scaEl) scaEl.textContent = data.scale;
          if (fmtEl) fmtEl.textContent = data.format;
          titleEl.style.opacity = '1';
        }, 180);
      }
    }

    // 3. Section 2: Readiness Checklist Meter
    var currentReadiness = 100;
    function updateReadinessScore(cb, weight) {
      if (cb.checked) {
        currentReadiness += weight;
      } else {
        currentReadiness -= weight;
      }
      currentReadiness = Math.max(0, Math.min(100, currentReadiness));

      var fillEl = document.getElementById('readinessBarFill');
      var textEl = document.getElementById('readinessScoreText');

      if (fillEl) fillEl.style.width = currentReadiness + '%';
      if (textEl) {
        textEl.textContent = currentReadiness + '% Prepared';
        if (currentReadiness >= 85) textEl.style.color = '#10b981';
        else if (currentReadiness >= 60) textEl.style.color = '#f59e0b';
        else textEl.style.color = '#ef4444';
      }
    }

    // 4. Section 3: CapEx Budget Simulator
    function simulateBudget(pax, btn) {
      ['btnCap500', 'btnCap1500', 'btnCap5000'].forEach(function (id) {
        var b = document.getElementById(id);
        if (b) {
          b.className = 'rc-btn rc-btn-outline';
          b.style.padding = '0.5rem 1rem';
          b.style.fontSize = '0.85rem';
        }
      });
      btn.className = 'rc-btn rc-btn-primary';
      btn.style.padding = '0.5rem 1rem';
      btn.style.fontSize = '0.85rem';

      var costPerPax = 485;
      var total = pax * costPerPax;

      var venue = Math.round(total * 0.35);
      var av = Math.round(total * 0.28);
      var speaker = Math.round(total * 0.18);
      var scenic = Math.round(total * 0.12);
      var cont = Math.round(total * 0.07);

      document.getElementById('simTotalBudget').textContent = '$' + total.toLocaleString();
      document.getElementById('allocVenueText').textContent = '$' + venue.toLocaleString();
      document.getElementById('allocAvText').textContent = '$' + av.toLocaleString();
      document.getElementById('allocSpeakerText').textContent = '$' + speaker.toLocaleString();
      document.getElementById('allocScenicText').textContent = '$' + scenic.toLocaleString();
      document.getElementById('allocContingencyText').textContent = '$' + cont.toLocaleString();
    }

    // 5. Section 7: FAQ Accordion Toggle & Live Keyword Search
    function toggleAccordion(header) {
      var item = header.closest('.rc-accordion-item');
      var body = item.querySelector('.rc-accordion-body');
      var isActive = item.classList.contains('active');

      document.querySelectorAll('.rc-accordion-item').forEach(function (i) {
        i.classList.remove('active');
        var b = i.querySelector('.rc-accordion-body');
        if (b) b.style.maxHeight = '0px';
      });

      if (!isActive) {
        item.classList.add('active');
        if (body) body.style.maxHeight = body.scrollHeight + 30 + 'px';
      }
    }

    function filterFaqQuestions(query) {
      var q = query.toLowerCase().trim();
      var items = document.querySelectorAll('.rc-accordion-item');
      items.forEach(function (item) {
        var text = item.textContent.toLowerCase();
        var keywords = item.getAttribute('data-keywords') || '';
        if (text.includes(q) || keywords.includes(q)) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    }
  </script>
"""

    # Assemble complete document
    final_html = (
        nav_head_up_to_style
        + resources_css
        + "\n  </style>"
        + nav_mid[len("</style>"):]
        + resources_html_content
        + footer_full
        + resources_scripts
        + closing_part
    )

    with open('resources.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print("Successfully rebuilt resources.html! Total length:", len(final_html))

if __name__ == '__main__':
    build_resources_html()
