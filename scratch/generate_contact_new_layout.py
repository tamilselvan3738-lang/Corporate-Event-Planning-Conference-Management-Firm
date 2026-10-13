import os

def build_contact_new_layout():
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

    # CSS for the new contact.html layout
    new_contact_css = """
    /* =====================================================================
       REDESIGNED CONTACT ARCHITECTURE: PANORAMIC & MULTI-DIMENSIONAL
       Supports Light Mode, Dark Mode (body.dark), and RTL (body.rtl)
       ===================================================================== */
    :root {
      --cnt-primary: #1e3a8a;
      --cnt-primary-dark: #0f172a;
      --cnt-accent: #d97706;
      --cnt-accent-light: #fbbf24;
      --cnt-accent-glow: rgba(217, 119, 6, 0.16);
      --cnt-danger: #dc2626;
      --cnt-danger-glow: rgba(220, 38, 38, 0.18);
      --cnt-bg: #f8fafc;
      --cnt-surface: #ffffff;
      --cnt-surface-muted: #f1f5f9;
      --cnt-card-border: #e2e8f0;
      --cnt-text-main: #0f172a;
      --cnt-text-muted: #64748b;
      --cnt-text-light: #94a3b8;
      --cnt-gold-gradient: linear-gradient(135deg, #b45309 0%, #d97706 50%, #f59e0b 100%);
      --cnt-red-gradient: linear-gradient(135deg, #991b1b 0%, #dc2626 50%, #f87171 100%);
      --cnt-blue-gradient: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      --cnt-shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --cnt-shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.07), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
      --cnt-shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      --cnt-shadow-glow: 0 0 25px rgba(217, 119, 6, 0.22);
    }

    body.dark {
      --cnt-bg: #070b14;
      --cnt-surface: #0f172a;
      --cnt-surface-muted: #131d33;
      --cnt-card-border: #1e293b;
      --cnt-text-main: #f8fafc;
      --cnt-text-muted: #94a3b8;
      --cnt-text-light: #64748b;
      --cnt-blue-gradient: linear-gradient(135deg, #070b14 0%, #172554 100%);
    }

    /* RTL Support */
    body.rtl .cnt-section-head { text-align: right; }
    body.rtl .cnt-badge i { margin-left: 0.5rem; margin-right: 0; }
    body.rtl .cnt-btn i { margin-right: 0.5rem; margin-left: 0; }

    /* Base Reset for Contact Container */
    .cnt-page-wrap {
      background-color: var(--cnt-bg);
      color: var(--cnt-text-main);
      font-family: 'Inter', system-ui, sans-serif;
      overflow-x: hidden;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    .cnt-container {
      max-width: 1320px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }

    /* SECTION HEADER STYLING */
    .cnt-section-head {
      margin-bottom: 3.5rem;
      position: relative;
    }

    .cnt-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.45rem 1.1rem;
      border-radius: 9999px;
      background: var(--cnt-accent-glow);
      border: 1px solid rgba(217, 119, 6, 0.35);
      color: var(--cnt-accent);
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      margin-bottom: 1rem;
    }

    .cnt-badge-danger {
      background: var(--cnt-danger-glow);
      border-color: rgba(220, 38, 38, 0.35);
      color: #ef4444;
    }

    .cnt-title {
      font-size: clamp(2rem, 3.5vw, 2.75rem);
      font-weight: 800;
      line-height: 1.18;
      color: var(--cnt-text-main);
      letter-spacing: -0.025em;
      margin-bottom: 1rem;
    }

    .cnt-title-gradient {
      background: var(--cnt-gold-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .cnt-title-danger {
      background: var(--cnt-red-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .cnt-subtitle {
      font-size: 1.1rem;
      color: var(--cnt-text-muted);
      line-height: 1.65;
      max-width: 780px;
    }

    /* HERO JUMP NAV STRIP */
    .cnt-hero-strip {
      background: var(--cnt-surface);
      border-bottom: 1px solid var(--cnt-card-border);
      padding: 2.75rem 0 2.25rem;
      position: relative;
    }
    .cnt-hero-content {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 1.25rem;
    }
    .cnt-hero-title {
      font-size: clamp(2.2rem, 4vw, 3.25rem);
      font-weight: 900;
      color: var(--cnt-text-main);
      letter-spacing: -0.03em;
    }
    .cnt-hero-desc {
      font-size: 1.15rem;
      color: var(--cnt-text-muted);
      max-width: 840px;
      line-height: 1.65;
    }
    .cnt-nav-pills {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.65rem;
      margin-top: 1rem;
    }
    .cnt-nav-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.55rem 1.15rem;
      border-radius: 9999px;
      background: var(--cnt-surface-muted);
      border: 1px solid var(--cnt-card-border);
      color: var(--cnt-text-main);
      font-size: 0.88rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
    }
    .cnt-nav-pill:hover {
      background: var(--cnt-accent);
      color: #ffffff;
      border-color: var(--cnt-accent);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(217, 119, 6, 0.25);
    }
    .cnt-nav-pill i {
      color: var(--cnt-accent);
      transition: color 0.3s ease;
    }
    .cnt-nav-pill:hover i {
      color: #ffffff;
    }

    /* GLOBAL BUTTONS */
    .cnt-btn {
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
    .cnt-btn-primary {
      background: var(--cnt-gold-gradient);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(217, 119, 6, 0.3);
    }
    .cnt-btn-primary:hover {
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 8px 24px rgba(217, 119, 6, 0.45);
      color: #ffffff;
    }
    .cnt-btn-danger {
      background: var(--cnt-red-gradient);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(220, 38, 38, 0.35);
    }
    .cnt-btn-danger:hover {
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 8px 24px rgba(220, 38, 38, 0.5);
      color: #ffffff;
    }
    .cnt-btn-outline {
      background: transparent;
      color: var(--cnt-text-main);
      border: 1.5px solid var(--cnt-card-border);
    }
    .cnt-btn-outline:hover {
      background: var(--cnt-surface-muted);
      border-color: var(--cnt-accent);
      color: var(--cnt-accent);
      transform: translateY(-2px);
    }

    /* =====================================================================
       FRAMER MOTION OBSERVER SYSTEM (7 DISTINCT SECTION ANIMATIONS)
       ===================================================================== */
    /* Section 1: Monolith Panoramic Incline */
    .framer-monolith-panoramic {
      opacity: 0;
      transform: perspective(1400px) rotateX(14deg) scale(0.96);
      transition: opacity 0.85s cubic-bezier(0.16, 1, 0.3, 1), transform 0.85s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform, opacity;
    }
    .framer-monolith-panoramic.framer-in-view {
      opacity: 1;
      transform: perspective(1400px) rotateX(0deg) scale(1);
    }

    /* Section 2: Rotary Frequency Dial Snap */
    .framer-rotary-dial {
      opacity: 0;
      transform: rotate(-4deg) translateY(45px);
      transition: opacity 0.75s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.75s cubic-bezier(0.34, 1.56, 0.64, 1);
      will-change: transform, opacity;
    }
    .framer-rotary-dial.framer-in-view {
      opacity: 1;
      transform: rotate(0deg) translateY(0);
    }

    /* Section 3: Keycard Skewed Matrix */
    .framer-keycard-matrix {
      opacity: 0;
      transform: translateX(55px) skewX(-2deg);
      transition: opacity 0.8s cubic-bezier(0.25, 1, 0.5, 1), transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);
      will-change: transform, opacity;
    }
    .framer-keycard-matrix.framer-in-view {
      opacity: 1;
      transform: translateX(0) skewX(0deg);
    }

    /* Section 4: Meridian Wave Elastic Rise */
    .framer-meridian-wave {
      opacity: 0;
      transform: scale(0.92) translateY(50px);
      transition: opacity 0.85s cubic-bezier(0.175, 0.885, 0.32, 1.275), transform 0.85s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      will-change: transform, opacity;
    }
    .framer-meridian-wave.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    /* Section 5: Radar Viewport Sweep */
    .framer-radar-sweep {
      opacity: 0;
      transform: perspective(1200px) rotateY(10deg) translateX(-40px);
      transition: opacity 0.85s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1);
      will-change: transform, opacity;
    }
    .framer-radar-sweep.framer-in-view {
      opacity: 1;
      transform: perspective(1200px) rotateY(0deg) translateX(0);
    }

    /* Section 6: Foundry Studio Axial Expansion */
    .framer-foundry-studio {
      opacity: 0;
      transform: translateY(40px) scale(0.95);
      transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform, opacity;
    }
    .framer-foundry-studio.framer-in-view {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    /* Section 7: Beacon Alert Pulse Impact */
    .framer-beacon-alert {
      opacity: 0;
      transform: scale(1.08) translateY(-30px);
      transition: opacity 0.7s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.7s cubic-bezier(0.34, 1.56, 0.64, 1);
      will-change: transform, opacity;
    }
    .framer-beacon-alert.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    /* =====================================================================
       SECTION 1: NEW LAYOUT - PANORAMIC RIBBON & MONOLITH PEDESTALS
       ===================================================================== */
    .cnt-section-address-new {
      padding: 6.5rem 0;
      position: relative;
    }
    .cnt-panoramic-hero-banner {
      position: relative;
      border-radius: 2rem;
      overflow: hidden;
      border: 1px solid var(--cnt-card-border);
      box-shadow: var(--cnt-shadow-lg);
      margin-bottom: 2.5rem;
      height: 440px;
    }
    .cnt-panoramic-hero-banner img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .cnt-panoramic-glass-ribbon {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(0deg, rgba(7, 11, 20, 0.96) 0%, rgba(7, 11, 20, 0.65) 60%, transparent 100%);
      padding: 2.25rem 2.5rem;
      color: #ffffff;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      flex-wrap: wrap;
      gap: 1.5rem;
    }
    .cnt-monolith-triad-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.75rem;
    }
    .cnt-monolith-card {
      background: var(--cnt-surface);
      border: 1px solid var(--cnt-card-border);
      border-radius: 1.5rem;
      padding: 2rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 1.25rem;
      box-shadow: var(--cnt-shadow-sm);
      transition: all 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
      cursor: pointer;
    }
    .cnt-monolith-card:hover {
      border-color: var(--cnt-accent);
      transform: translateY(-5px);
      box-shadow: var(--cnt-shadow-lg);
    }
    .cnt-monolith-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }
    .cnt-monolith-icon {
      width: 48px;
      height: 48px;
      border-radius: 1rem;
      background: var(--cnt-accent-glow);
      color: var(--cnt-accent);
      font-size: 1.25rem;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .cnt-monolith-coord {
      font-size: 0.75rem;
      font-family: monospace;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      background: var(--cnt-surface-muted);
      color: var(--cnt-text-muted);
      border: 1px solid var(--cnt-card-border);
    }

    /* =====================================================================
       SECTION 2: NEW LAYOUT - ROTARY FREQUENCY & 4-PILLAR TELEPHONY MATRIX
       ===================================================================== */
    .cnt-section-telephony-new {
      padding: 6.5rem 0;
      background: var(--cnt-surface-muted);
      border-top: 1px solid var(--cnt-card-border);
      border-bottom: 1px solid var(--cnt-card-border);
      position: relative;
    }
    .cnt-hotline-frequency-strip {
      background: var(--cnt-surface);
      border: 1px solid var(--cnt-card-border);
      border-radius: 1.75rem;
      padding: 2rem 2.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1.5rem;
      box-shadow: var(--cnt-shadow-md);
      margin-bottom: 2.5rem;
    }
    .cnt-pillars-quad-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.5rem;
      margin-bottom: 2.5rem;
    }
    .cnt-pillar-voice-card {
      background: var(--cnt-surface);
      border: 1px solid var(--cnt-card-border);
      border-radius: 1.5rem;
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 1.25rem;
      box-shadow: var(--cnt-shadow-sm);
      transition: all 0.3s ease;
    }
    .cnt-pillar-voice-card:hover {
      border-color: var(--cnt-accent);
      transform: translateY(-4px);
      box-shadow: var(--cnt-shadow-md);
    }
    .cnt-voice-num-link {
      font-size: 1.15rem;
      font-weight: 900;
      font-family: monospace;
      color: var(--cnt-primary);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: color 0.2s ease;
    }
    body.dark .cnt-voice-num-link {
      color: #38bdf8;
    }
    .cnt-voice-num-link:hover {
      color: var(--cnt-accent);
    }
    .cnt-telephony-centerpiece-banner {
      position: relative;
      border-radius: 1.5rem;
      overflow: hidden;
      height: 260px;
      border: 1px solid var(--cnt-card-border);
    }
    .cnt-telephony-centerpiece-banner img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    /* =====================================================================
       SECTION 3: NEW LAYOUT - ASYMMETRIC KEYCARD MATRIX & PGP VAULT
       ===================================================================== */
    .cnt-section-email-new {
      padding: 6.5rem 0;
      position: relative;
    }
    .cnt-asymmetric-email-layout {
      display: grid;
      grid-template-columns: 1.25fr 0.75fr;
      gap: 2.5rem;
      align-items: stretch;
    }
    .cnt-keycards-2x2-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.5rem;
    }
    .cnt-keycard-box {
      background: var(--cnt-surface);
      border: 1px solid var(--cnt-card-border);
      border-radius: 1.5rem;
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 1rem;
      box-shadow: var(--cnt-shadow-sm);
      transition: all 0.3s ease;
    }
    .cnt-keycard-box:hover {
      border-color: var(--cnt-accent);
      transform: translateY(-3px);
      box-shadow: var(--cnt-shadow-md);
    }
    .cnt-pgp-aside-monolith {
      background: var(--cnt-surface);
      border: 1px solid var(--cnt-card-border);
      border-radius: 1.75rem;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--cnt-shadow-lg);
    }
    .cnt-pgp-aside-img {
      height: 240px;
      position: relative;
    }
    .cnt-pgp-aside-img img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .cnt-pgp-aside-body {
      padding: 2rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      flex-grow: 1;
      justify-content: space-between;
    }

    /* =====================================================================
       SECTION 4: NEW LAYOUT - HORIZONTAL MERIDIAN TIMEBAND & OPERATIONS DECK
       ===================================================================== */
    .cnt-section-hours-new {
      padding: 6.5rem 0;
      background: var(--cnt-surface-muted);
      border-top: 1px solid var(--cnt-card-border);
      border-bottom: 1px solid var(--cnt-card-border);
      position: relative;
    }
    .cnt-meridian-timeband-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.25rem;
      margin-bottom: 2.5rem;
    }
    .cnt-meridian-pill-card {
      background: var(--cnt-surface);
      border: 1px solid var(--cnt-card-border);
      border-radius: 1.5rem;
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      box-shadow: var(--cnt-shadow-sm);
      position: relative;
      overflow: hidden;
    }
    .cnt-meridian-city {
      font-size: 0.88rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--cnt-text-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .cnt-meridian-clock {
      font-size: 2.2rem;
      font-weight: 900;
      font-family: monospace;
      color: var(--cnt-text-main);
      line-height: 1;
    }
    .cnt-ops-schedule-split {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.5rem;
      align-items: center;
      background: var(--cnt-surface);
      border: 1px solid var(--cnt-card-border);
      border-radius: 1.75rem;
      padding: 2.5rem;
      box-shadow: var(--cnt-shadow-md);
    }
    .cnt-ops-img-frame {
      border-radius: 1.25rem;
      overflow: hidden;
      height: 320px;
      border: 1px solid var(--cnt-card-border);
    }
    .cnt-ops-img-frame img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    /* =====================================================================
       SECTION 5: NEW LAYOUT - SPLIT-SCREEN RADAR VIEWPORT & INGRESS DOCK
       ===================================================================== */
    .cnt-section-map-new {
      padding: 6.5rem 0;
      position: relative;
    }
    .cnt-radar-deck-layout {
      display: grid;
      grid-template-columns: 0.75fr 1.25fr;
      gap: 2.5rem;
      align-items: stretch;
      margin-bottom: 2.5rem;
    }
    .cnt-radar-selector-card {
      background: var(--cnt-surface);
      border: 1px solid var(--cnt-card-border);
      border-radius: 1.75rem;
      padding: 2rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      justify-content: space-between;
      box-shadow: var(--cnt-shadow-md);
    }
    .cnt-radar-city-btn {
      padding: 1.15rem 1.25rem;
      border-radius: 1rem;
      border: 1px solid var(--cnt-card-border);
      background: var(--cnt-surface-muted);
      color: var(--cnt-text-main);
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      font-weight: 700;
      font-size: 0.95rem;
      transition: all 0.3s ease;
    }
    .cnt-radar-city-btn.active,
    .cnt-radar-city-btn:hover {
      background: var(--cnt-surface);
      border-color: var(--cnt-accent);
      box-shadow: var(--cnt-shadow-sm);
      color: var(--cnt-accent);
    }
    .cnt-radar-viewport-frame {
      position: relative;
      border-radius: 1.75rem;
      overflow: hidden;
      border: 1px solid var(--cnt-card-border);
      box-shadow: var(--cnt-shadow-lg);
      min-height: 420px;
    }
    .cnt-radar-viewport-frame img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .cnt-radar-sweep-hud {
      position: absolute;
      top: 1.5rem;
      left: 1.5rem;
      background: rgba(15, 23, 42, 0.9);
      backdrop-filter: blur(8px);
      padding: 0.6rem 1.25rem;
      border-radius: 0.75rem;
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #38bdf8;
      font-family: monospace;
      font-size: 0.85rem;
      font-weight: 800;
    }
    body.rtl .cnt-radar-sweep-hud {
      left: auto;
      right: 1.5rem;
    }
    .cnt-ingress-dock-triad {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
    }
    .cnt-dock-pod {
      background: var(--cnt-surface);
      border: 1px solid var(--cnt-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      box-shadow: var(--cnt-shadow-sm);
      transition: all 0.3s ease;
    }
    .cnt-dock-pod:hover {
      border-color: var(--cnt-accent);
      transform: translateY(-2px);
    }

    /* =====================================================================
       SECTION 6: NEW LAYOUT - 3-COLUMN CONSULTATION FORGE & FOUNDRY STUDIO
       ===================================================================== */
    .cnt-section-forge-new {
      padding: 6.5rem 0;
      background: var(--cnt-surface-muted);
      border-top: 1px solid var(--cnt-card-border);
      border-bottom: 1px solid var(--cnt-card-border);
      position: relative;
    }
    .cnt-foundry-studio-card {
      background: var(--cnt-surface);
      border: 1px solid var(--cnt-card-border);
      border-radius: 2rem;
      padding: 3rem;
      box-shadow: var(--cnt-shadow-lg);
    }
    .cnt-mode-segment-bar {
      display: flex;
      max-width: 580px;
      margin: 0 auto 2.5rem;
      background: var(--cnt-surface-muted);
      padding: 0.35rem;
      border-radius: 1rem;
      border: 1px solid var(--cnt-card-border);
    }
    .cnt-segment-btn {
      flex: 1;
      padding: 0.85rem 1.25rem;
      border-radius: 0.75rem;
      font-size: 0.92rem;
      font-weight: 800;
      border: none;
      cursor: pointer;
      background: transparent;
      color: var(--cnt-text-muted);
      transition: all 0.3s ease;
      text-align: center;
    }
    .cnt-segment-btn.active {
      background: var(--cnt-surface);
      color: var(--cnt-accent);
      box-shadow: var(--cnt-shadow-sm);
    }
    .cnt-tri-col-form-grid {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 2rem;
    }
    .cnt-form-column {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }
    .cnt-field-box {
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
    }
    .cnt-field-label {
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--cnt-text-main);
    }
    .cnt-input,
    .cnt-select,
    .cnt-textarea {
      width: 100%;
      padding: 0.85rem 1.15rem;
      border-radius: 0.75rem;
      border: 1px solid var(--cnt-card-border);
      background: var(--cnt-surface-muted);
      color: var(--cnt-text-main);
      font-family: inherit;
      font-size: 0.95rem;
      outline: none;
      transition: all 0.3s ease;
    }
    .cnt-input:focus,
    .cnt-select:focus,
    .cnt-textarea:focus {
      border-color: var(--cnt-accent);
      box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.15);
      background: var(--cnt-surface);
    }

    /* =====================================================================
       SECTION 7: NEW LAYOUT - MARQUEE ALERT TICKER & 3-TIER CRISIS TRIAD
       ===================================================================== */
    .cnt-section-emergency-new {
      padding: 6.5rem 0 8.5rem;
      position: relative;
    }
    .cnt-crisis-marquee-banner {
      background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 50%, #450a0a 100%);
      border: 2px solid rgba(220, 38, 38, 0.5);
      border-radius: 1.75rem;
      padding: 2.25rem 2.5rem;
      color: #ffffff;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1.5rem;
      margin-bottom: 2.5rem;
      box-shadow: 0 15px 35px -5px rgba(220, 38, 38, 0.2);
    }
    .cnt-crisis-triad-layout {
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      gap: 2.5rem;
      align-items: stretch;
    }
    .cnt-crisis-triad-col {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      justify-content: space-between;
    }
    .cnt-crisis-pod {
      background: var(--cnt-surface);
      border: 1px solid var(--cnt-card-border);
      border-left: 4px solid #ef4444;
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
      box-shadow: var(--cnt-shadow-sm);
    }
    body.rtl .cnt-crisis-pod {
      border-left: 1px solid var(--cnt-card-border);
      border-right: 4px solid #ef4444;
    }
    .cnt-crisis-media-frame {
      border-radius: 1.75rem;
      overflow: hidden;
      border: 1px solid var(--cnt-card-border);
      box-shadow: var(--cnt-shadow-lg);
      position: relative;
      min-height: 380px;
    }
    .cnt-crisis-media-frame img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    /* MODAL POPUP */
    .cnt-modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.8);
      backdrop-filter: blur(8px);
      z-index: 9999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }
    .cnt-modal-box {
      background: var(--cnt-surface);
      border: 1px solid var(--cnt-card-border);
      border-radius: 1.75rem;
      max-width: 520px;
      width: 100%;
      padding: 2.75rem 2.25rem;
      text-align: center;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.35);
      position: relative;
      animation: cntModalPop 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    @keyframes cntModalPop {
      0% { transform: scale(0.85); opacity: 0; }
      100% { transform: scale(1); opacity: 1; }
    }
    .cnt-modal-icon {
      width: 72px;
      height: 72px;
      border-radius: 50%;
      background: rgba(16, 185, 129, 0.15);
      color: #10b981;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2.25rem;
      margin: 0 auto 1.5rem;
    }

    /* RESPONSIVE BREAKPOINTS */
    @media (max-width: 1024px) {
      .cnt-monolith-triad-grid,
      .cnt-pillars-quad-grid,
      .cnt-meridian-timeband-grid,
      .cnt-tri-col-form-grid,
      .cnt-ingress-dock-triad {
        grid-template-columns: 1fr;
        gap: 1.5rem;
      }
      .cnt-asymmetric-email-layout,
      .cnt-ops-schedule-split,
      .cnt-radar-deck-layout,
      .cnt-crisis-triad-layout {
        grid-template-columns: 1fr;
        gap: 2rem;
      }
      .cnt-panoramic-hero-banner,
      .cnt-radar-viewport-frame,
      .cnt-crisis-media-frame {
        height: 320px;
        min-height: 320px;
      }
    }
    @media (max-width: 640px) {
      .cnt-keycards-2x2-grid {
        grid-template-columns: 1fr;
      }
    }
    """

    # HTML Body Content for the Redesigned 7 Sections
    new_contact_content = """
    <!-- =====================================================================
         MAIN CONTENT: 7 RADICALLY REDESIGNED CONTACT & LIAISON SECTIONS
         ===================================================================== -->
    <main class="cnt-page-wrap">

      <!-- SUB-HERO STRIP -->
      <section class="cnt-hero-strip">
        <div class="cnt-container">
          <div class="cnt-hero-content">
            <span class="cnt-badge"><i class="fas fa-tower-broadcast"></i> Executive Communications Command</span>
            <h1 class="cnt-hero-title">Global Liaison &amp; Corporate Headquarters Directory</h1>
            <p class="cnt-hero-desc">
              Direct master access to executive event directors, technical broadcast engineers, and 24/7 incident response commanders across our quadrilateral financial embassies.
            </p>
            <div class="cnt-nav-pills">
              <a href="#office-address" class="cnt-nav-pill"><i class="fas fa-building"></i> Office Address</a>
              <a href="#phone-telephony" class="cnt-nav-pill"><i class="fas fa-phone"></i> Phone Directory</a>
              <a href="#business-email" class="cnt-nav-pill"><i class="fas fa-envelope"></i> Business Email</a>
              <a href="#office-hours" class="cnt-nav-pill"><i class="fas fa-clock"></i> Office Hours</a>
              <a href="#location-map" class="cnt-nav-pill"><i class="fas fa-map-location-dot"></i> Location Map</a>
              <a href="#enquiry-consultation" class="cnt-nav-pill"><i class="fas fa-file-signature"></i> Consultation &amp; Inquiry</a>
              <a href="#emergency-support" class="cnt-nav-pill"><i class="fas fa-triangle-exclamation"></i> Emergency Support</a>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 1: OFFICE ADDRESS & GLOBAL HEADQUARTERS -->
      <section id="office-address" class="cnt-section-address-new">
        <div class="cnt-container">
          <div class="cnt-section-head framer-monolith-panoramic">
            <span class="cnt-badge"><i class="fas fa-building"></i> Sovereign Real Estate</span>
            <h2 class="cnt-title">Panoramic Global Ribbon &amp; <span class="cnt-title-gradient">Embassy Pedestals</span></h2>
            <p class="cnt-subtitle">
              Headquartered at Rockefeller Plaza, New York, with fully staffed regional diplomatic hubs in Mayfair London, Marina Bay Singapore, and Paradeplatz Zurich.
            </p>
          </div>

          <!-- Top Panoramic Ribbon Banner -->
          <div class="cnt-panoramic-hero-banner framer-monolith-panoramic">
            <img src="images/contact_office_address.jpg" alt="EventSphere Corporate Headquarters Building and Glass Facade" loading="lazy">
            <div class="cnt-panoramic-glass-ribbon">
              <div>
                <span style="font-size: 0.8rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em; color: #fbbf24;">Global Flagship Headquarters</span>
                <div style="font-size: 1.85rem; font-weight: 900; margin-top: 0.25rem;">Rockefeller Plaza Executive Tower, 48th Floor</div>
                <div style="font-size: 0.95rem; color: #cbd5e1; margin-top: 0.35rem;">
                  30 Rockefeller Plaza, New York, NY 10112 &bull; Coordinates: 40.7580° N, 73.9855° W
                </div>
              </div>
              <div style="display: flex; gap: 1rem; align-items: center;">
                <button class="cnt-btn cnt-btn-primary" onclick="window.location.href='#enquiry-consultation'"><i class="fas fa-calendar-check"></i> Book Executive Suite</button>
                <button class="cnt-btn cnt-btn-outline" style="color: #ffffff; border-color: rgba(255,255,255,0.4);" onclick="window.location.href='#location-map'"><i class="fas fa-route"></i> Ingress Map</button>
              </div>
            </div>
          </div>

          <!-- Bottom 3 Monolith Pedestals -->
          <div class="cnt-monolith-triad-grid framer-monolith-panoramic">
            <div class="cnt-monolith-card" onclick="alert('Connecting to London Mayfair Diplomatic Hub liaison...');">
              <div class="cnt-monolith-top">
                <div class="cnt-monolith-icon"><i class="fas fa-landmark"></i></div>
                <span class="cnt-monolith-coord">51.5074° N, 0.1278° W</span>
              </div>
              <div>
                <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--cnt-text-main); margin-bottom: 0.5rem;">London Mayfair Hub</h3>
                <p style="font-size: 0.9rem; color: var(--cnt-text-muted); line-height: 1.5;">
                  14 Curzon Street, Mayfair, London W1J 7TX, UK.<br>
                  Direct Liaison: <strong>+44 20 7946 0920</strong>
                </p>
              </div>
              <div style="font-size: 0.8rem; font-weight: 700; color: var(--cnt-accent); display: flex; align-items: center; gap: 0.4rem;">
                Connect Regional Office <i class="fas fa-arrow-right"></i>
              </div>
            </div>

            <div class="cnt-monolith-card" onclick="alert('Connecting to Singapore Marina Bay Hub liaison...');">
              <div class="cnt-monolith-top">
                <div class="cnt-monolith-icon"><i class="fas fa-city"></i></div>
                <span class="cnt-monolith-coord">1.2838° N, 103.8591° E</span>
              </div>
              <div>
                <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--cnt-text-main); margin-bottom: 0.5rem;">Singapore Marina Bay Hub</h3>
                <p style="font-size: 0.9rem; color: var(--cnt-text-muted); line-height: 1.5;">
                  10 Marina Boulevard, Tower 2, Level 38, Singapore 018983.<br>
                  Direct Liaison: <strong>+65 6789 0123</strong>
                </p>
              </div>
              <div style="font-size: 0.8rem; font-weight: 700; color: var(--cnt-accent); display: flex; align-items: center; gap: 0.4rem;">
                Connect Regional Office <i class="fas fa-arrow-right"></i>
              </div>
            </div>

            <div class="cnt-monolith-card" onclick="alert('Connecting to Zurich Paradeplatz Hub liaison...');">
              <div class="cnt-monolith-top">
                <div class="cnt-monolith-icon"><i class="fas fa-mountain"></i></div>
                <span class="cnt-monolith-coord">47.3690° N, 8.5390° E</span>
              </div>
              <div>
                <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--cnt-text-main); margin-bottom: 0.5rem;">Zurich Paradeplatz Hub</h3>
                <p style="font-size: 0.9rem; color: var(--cnt-text-muted); line-height: 1.5;">
                  Poststrasse 9, 8001 Zürich, Switzerland.<br>
                  Direct Liaison: <strong>+41 44 215 8800</strong>
                </p>
              </div>
              <div style="font-size: 0.8rem; font-weight: 700; color: var(--cnt-accent); display: flex; align-items: center; gap: 0.4rem;">
                Connect Regional Office <i class="fas fa-arrow-right"></i>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 2: PHONE NUMBER & DIRECT TELEPHONY DESK -->
      <section id="phone-telephony" class="cnt-section-telephony-new">
        <div class="cnt-container">
          <div class="cnt-section-head framer-rotary-dial">
            <span class="cnt-badge"><i class="fas fa-phone-volume"></i> Telephony Frequency Matrix</span>
            <h2 class="cnt-title">Direct Dialing Switchboard &amp; <span class="cnt-title-gradient">Telephony Desk</span></h2>
            <p class="cnt-subtitle">
              Zero call centers. Connect directly to lead executive producers, media liaison directors, and procurement counsels with dedicated direct inward dialing (DID) extensions.
            </p>
          </div>

          <!-- Top Hotline Frequency Banner -->
          <div class="cnt-hotline-frequency-strip framer-rotary-dial">
            <div>
              <span style="font-size: 0.8rem; font-weight: 800; text-transform: uppercase; color: var(--cnt-accent); letter-spacing: 0.05em;">Global Toll-Free Priority Line</span>
              <div style="font-size: 2.2rem; font-weight: 900; font-family: monospace; color: var(--cnt-text-main); margin-top: 0.2rem;">
                +1 (800) 555-SUMMIT
              </div>
              <div style="font-size: 0.85rem; color: var(--cnt-text-muted); margin-top: 0.25rem;">
                Freecall worldwide from USA, UK, EU, Singapore, and Canada &bull; 24/7 Staffed
              </div>
            </div>
            <div style="display: flex; gap: 1rem; align-items: center;">
              <a href="tel:+18005557864" class="cnt-btn cnt-btn-primary"><i class="fas fa-phone"></i> Instant Call Toll-Free</a>
              <button class="cnt-btn cnt-btn-outline" onclick="alert('Downloading Executive Digital vCard...');"><i class="fas fa-address-book"></i> Export vCard</button>
            </div>
          </div>

          <!-- 4 Pillars Telephony Quad -->
          <div class="cnt-pillars-quad-grid framer-rotary-dial">
            <div class="cnt-pillar-voice-card">
              <div>
                <span class="cnt-badge" style="font-size: 0.72rem; padding: 0.25rem 0.65rem;"><i class="fas fa-tv"></i> Plenary Production</span>
                <h4 style="font-size: 1.15rem; font-weight: 800; color: var(--cnt-text-main); margin: 0.65rem 0 0.4rem;">Mainstage Staging</h4>
                <p style="font-size: 0.85rem; color: var(--cnt-text-muted); line-height: 1.45;">Keynote rigging, 8K MicroLED walls, and acoustic sound reinforcement.</p>
              </div>
              <div>
                <a href="tel:+12125550190" class="cnt-voice-num-link"><i class="fas fa-phone-alt"></i> +1 (212) 555-0190</a>
                <span style="font-size: 0.75rem; color: var(--cnt-text-light);">Direct Ext: 101</span>
              </div>
            </div>

            <div class="cnt-pillar-voice-card">
              <div>
                <span class="cnt-badge" style="font-size: 0.72rem; padding: 0.25rem 0.65rem;"><i class="fas fa-newspaper"></i> Media Liaison</span>
                <h4 style="font-size: 1.15rem; font-weight: 800; color: var(--cnt-text-main); margin: 0.65rem 0 0.4rem;">Press &amp; Broadcast</h4>
                <p style="font-size: 0.85rem; color: var(--cnt-text-muted); line-height: 1.45;">Journalist accreditation, satellite trucks, and interview rooms.</p>
              </div>
              <div>
                <a href="tel:+12125550194" class="cnt-voice-num-link"><i class="fas fa-phone-alt"></i> +1 (212) 555-0194</a>
                <span style="font-size: 0.75rem; color: var(--cnt-text-light);">Direct Ext: 104</span>
              </div>
            </div>

            <div class="cnt-pillar-voice-card">
              <div>
                <span class="cnt-badge" style="font-size: 0.72rem; padding: 0.25rem 0.65rem;"><i class="fas fa-handshake"></i> Procurement</span>
                <h4 style="font-size: 1.15rem; font-weight: 800; color: var(--cnt-text-main); margin: 0.65rem 0 0.4rem;">Master Vendor MSAs</h4>
                <p style="font-size: 0.85rem; color: var(--cnt-text-muted); line-height: 1.45;">Supplier onboarding, COI verification, and commercial billing.</p>
              </div>
              <div>
                <a href="tel:+12125550198" class="cnt-voice-num-link"><i class="fas fa-phone-alt"></i> +1 (212) 555-0198</a>
                <span style="font-size: 0.75rem; color: var(--cnt-text-light);">Direct Ext: 108</span>
              </div>
            </div>

            <div class="cnt-pillar-voice-card">
              <div>
                <span class="cnt-badge" style="font-size: 0.72rem; padding: 0.25rem 0.65rem;"><i class="fas fa-scale-balanced"></i> Legal &amp; NDAs</span>
                <h4 style="font-size: 1.15rem; font-weight: 800; color: var(--cnt-text-main); margin: 0.65rem 0 0.4rem;">General Counsel</h4>
                <p style="font-size: 0.85rem; color: var(--cnt-text-muted); line-height: 1.45;">Confidential non-disclosure terms, permits, and risk governance.</p>
              </div>
              <div>
                <a href="tel:+12125550199" class="cnt-voice-num-link"><i class="fas fa-phone-alt"></i> +1 (212) 555-0199</a>
                <span style="font-size: 0.75rem; color: var(--cnt-text-light);">Direct Ext: 110</span>
              </div>
            </div>
          </div>

          <!-- Bottom Telephony Centerpiece Image -->
          <div class="cnt-telephony-centerpiece-banner framer-rotary-dial">
            <img src="images/contact_phone_telephony.jpg" alt="Voice Operations Telephony Center and Support Specialists" loading="lazy">
            <div style="position: absolute; bottom: 1.25rem; left: 1.5rem; background: rgba(15, 23, 42, 0.88); backdrop-filter: blur(8px); padding: 0.65rem 1.25rem; border-radius: 0.85rem; color: #ffffff; font-size: 0.85rem; font-weight: 700;">
              <i class="fas fa-headset" style="color: var(--cnt-accent);"></i> Dedicated Client Production Desks Staffed Mon–Fri 07:30 – 21:00 EST
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 3: BUSINESS EMAIL & ENCRYPTED DISPATCH GATEWAY -->
      <section id="business-email" class="cnt-section-email-new">
        <div class="cnt-container">
          <div class="cnt-section-head framer-keycard-matrix">
            <span class="cnt-badge"><i class="fas fa-envelope-open-text"></i> Cryptographic Dispatch</span>
            <h2 class="cnt-title">Asymmetric Email Matrix &amp; <span class="cnt-title-gradient">PGP Keycard Vault</span></h2>
            <p class="cnt-subtitle">
              Guaranteed under-2-hour SLA email response times. Route your corporate communications directly to departmental inboxes with cryptographic verification.
            </p>
          </div>

          <div class="cnt-asymmetric-email-layout">
            <!-- Left 2x2 Keycard Grid -->
            <div class="cnt-keycards-2x2-grid framer-keycard-matrix">
              <div class="cnt-keycard-box">
                <div>
                  <span class="cnt-badge" style="font-size: 0.72rem; padding: 0.25rem 0.65rem;"><i class="fas fa-file-contract"></i> Proposals &amp; RFPs</span>
                  <h4 style="font-size: 1.15rem; font-weight: 800; color: var(--cnt-text-main); margin: 0.5rem 0;">Conference RFPs</h4>
                  <div style="font-family: monospace; font-size: 1.05rem; font-weight: 800; color: var(--cnt-accent);">rfp@corporateevents.com</div>
                  <div style="font-size: 0.82rem; color: var(--cnt-text-muted); margin-top: 0.35rem;">Guaranteed preliminary proposal review under 2 hours.</div>
                </div>
                <button class="cnt-btn cnt-btn-outline" style="padding: 0.5rem 1rem; font-size: 0.82rem;" onclick="copyEmailToClipboard('rfp@corporateevents.com', this)">
                  <i class="fas fa-copy"></i> Copy Address
                </button>
              </div>

              <div class="cnt-keycard-box">
                <div>
                  <span class="cnt-badge" style="font-size: 0.72rem; padding: 0.25rem 0.65rem;"><i class="fas fa-user-tie"></i> Executive Steering</span>
                  <h4 style="font-size: 1.15rem; font-weight: 800; color: var(--cnt-text-main); margin: 0.5rem 0;">Managing Partners</h4>
                  <div style="font-family: monospace; font-size: 1.05rem; font-weight: 800; color: var(--cnt-accent);">executive@corporateevents.com</div>
                  <div style="font-size: 0.82rem; color: var(--cnt-text-muted); margin-top: 0.35rem;">Direct channel for C-suite sponsors and board directors.</div>
                </div>
                <button class="cnt-btn cnt-btn-outline" style="padding: 0.5rem 1rem; font-size: 0.82rem;" onclick="copyEmailToClipboard('executive@corporateevents.com', this)">
                  <i class="fas fa-copy"></i> Copy Address
                </button>
              </div>

              <div class="cnt-keycard-box">
                <div>
                  <span class="cnt-badge" style="font-size: 0.72rem; padding: 0.25rem 0.65rem;"><i class="fas fa-dolly"></i> Vendor Network</span>
                  <h4 style="font-size: 1.15rem; font-weight: 800; color: var(--cnt-text-main); margin: 0.5rem 0;">Supplier Relations</h4>
                  <div style="font-family: monospace; font-size: 1.05rem; font-weight: 800; color: var(--cnt-accent);">procurement@corporateevents.com</div>
                  <div style="font-size: 0.82rem; color: var(--cnt-text-muted); margin-top: 0.35rem;">Accreditation, venue bidding, and hardware riders.</div>
                </div>
                <button class="cnt-btn cnt-btn-outline" style="padding: 0.5rem 1rem; font-size: 0.82rem;" onclick="copyEmailToClipboard('procurement@corporateevents.com', this)">
                  <i class="fas fa-copy"></i> Copy Address
                </button>
              </div>

              <div class="cnt-keycard-box">
                <div>
                  <span class="cnt-badge" style="font-size: 0.72rem; padding: 0.25rem 0.65rem;"><i class="fas fa-gavel"></i> Legal &amp; Compliance</span>
                  <h4 style="font-size: 1.15rem; font-weight: 800; color: var(--cnt-text-main); margin: 0.5rem 0;">Risk &amp; Non-Disclosure</h4>
                  <div style="font-family: monospace; font-size: 1.05rem; font-weight: 800; color: var(--cnt-accent);">legal@corporateevents.com</div>
                  <div style="font-size: 0.82rem; color: var(--cnt-text-muted); margin-top: 0.35rem;">Mutual NDAs, insurance certificates, force majeure.</div>
                </div>
                <button class="cnt-btn cnt-btn-outline" style="padding: 0.5rem 1rem; font-size: 0.82rem;" onclick="copyEmailToClipboard('legal@corporateevents.com', this)">
                  <i class="fas fa-copy"></i> Copy Address
                </button>
              </div>
            </div>

            <!-- Right PGP Aside Monolith -->
            <div class="cnt-pgp-aside-monolith framer-keycard-matrix">
              <div class="cnt-pgp-aside-img">
                <img src="images/contact_business_email.jpg" alt="Encrypted Corporate Email Terminal and Digital Security Card" loading="lazy">
                <div style="position: absolute; top: 1.25rem; left: 1.25rem; background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(8px); padding: 0.5rem 1rem; border-radius: 0.75rem; color: #10b981; font-size: 0.82rem; font-weight: 700;">
                  <i class="fas fa-lock"></i> 4096-Bit PGP Vault Active
                </div>
              </div>
              <div class="cnt-pgp-aside-body">
                <div>
                  <h4 style="font-size: 1.25rem; font-weight: 800; color: var(--cnt-text-main); margin-bottom: 0.5rem;">Sovereign Communications</h4>
                  <p style="font-size: 0.88rem; color: var(--cnt-text-muted); line-height: 1.5;">
                    For sensitive M&amp;A gatherings or confidential keynote speeches, use our encrypted PGP key:
                  </p>
                  <div style="background: var(--cnt-surface-muted); padding: 0.85rem; border-radius: 0.75rem; font-family: monospace; font-size: 0.78rem; word-break: break-all; color: var(--cnt-text-muted); margin-top: 0.75rem; border: 1px solid var(--cnt-card-border);">
                    PGP: B4C8 920A 11DF 34EE 87B1 502C 9A4D E33F 7102 99BA
                  </div>
                </div>
                <button class="cnt-btn cnt-btn-primary" style="width: 100%; font-size: 0.88rem;" onclick="alert('Downloading EventSphere Public PGP Key (.asc)...');">
                  <i class="fas fa-key"></i> Download PGP Public Key
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 4: OFFICE HOURS & 24/7 TIMEZONE OPERATIONS -->
      <section id="office-hours" class="cnt-section-hours-new">
        <div class="cnt-container">
          <div class="cnt-section-head framer-meridian-wave">
            <span class="cnt-badge"><i class="fas fa-clock"></i> Global Telemetry Clocks</span>
            <h2 class="cnt-title">Synchronized Meridian Timeband &amp; <span class="cnt-title-gradient">Operating Hours</span></h2>
            <p class="cnt-subtitle">
              Follow our worldwide operating hours in real time across four continuous financial time zones with live shift status.
            </p>
          </div>

          <!-- 4-City Meridian Timeband -->
          <div class="cnt-meridian-timeband-grid framer-meridian-wave">
            <div class="cnt-meridian-pill-card">
              <div class="cnt-meridian-city">
                <span>New York (EST)</span>
                <i class="fas fa-sun" style="color: #f59e0b;"></i>
              </div>
              <div class="cnt-meridian-clock" id="clockNYC">--:--:--</div>
              <div style="font-size: 0.75rem; font-weight: 800; color: #10b981; display: flex; align-items: center; gap: 0.4rem;">
                <span style="width: 8px; height: 8px; border-radius: 50%; background: #10b981; display: inline-block;"></span>
                Primary Command Active
              </div>
            </div>

            <div class="cnt-meridian-pill-card">
              <div class="cnt-meridian-city">
                <span>London (GMT)</span>
                <i class="fas fa-building-columns" style="color: #3b82f6;"></i>
              </div>
              <div class="cnt-meridian-clock" id="clockLON">--:--:--</div>
              <div style="font-size: 0.75rem; font-weight: 800; color: #10b981; display: flex; align-items: center; gap: 0.4rem;">
                <span style="width: 8px; height: 8px; border-radius: 50%; background: #10b981; display: inline-block;"></span>
                European Liaison Open
              </div>
            </div>

            <div class="cnt-meridian-pill-card">
              <div class="cnt-meridian-city">
                <span>Singapore (SGT)</span>
                <i class="fas fa-compass" style="color: #8b5cf6;"></i>
              </div>
              <div class="cnt-meridian-clock" id="clockSGP">--:--:--</div>
              <div style="font-size: 0.75rem; font-weight: 800; color: #10b981; display: flex; align-items: center; gap: 0.4rem;">
                <span style="width: 8px; height: 8px; border-radius: 50%; background: #10b981; display: inline-block;"></span>
                APAC Hub Operating
              </div>
            </div>

            <div class="cnt-meridian-pill-card">
              <div class="cnt-meridian-city">
                <span>Zurich (CET)</span>
                <i class="fas fa-snowflake" style="color: #06b6d4;"></i>
              </div>
              <div class="cnt-meridian-clock" id="clockZUR">--:--:--</div>
              <div style="font-size: 0.75rem; font-weight: 800; color: #10b981; display: flex; align-items: center; gap: 0.4rem;">
                <span style="width: 8px; height: 8px; border-radius: 50%; background: #10b981; display: inline-block;"></span>
                Alpine Desk Live
              </div>
            </div>
          </div>

          <!-- Bottom Schedule Split Deck -->
          <div class="cnt-ops-schedule-split framer-meridian-wave">
            <div class="cnt-ops-img-frame">
              <img src="images/contact_office_hours.jpg" alt="Corporate Reception Atrium and Operations Suite" loading="lazy">
            </div>

            <div>
              <span class="cnt-badge"><i class="fas fa-calendar-week"></i> Weekly Service Cadence</span>
              <h3 style="font-size: 1.45rem; font-weight: 800; color: var(--cnt-text-main); margin: 0.5rem 0 1rem;">Operating Hours Matrix</h3>
              <div style="display: flex; flex-direction: column; gap: 0.85rem;">
                <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--cnt-card-border); padding-bottom: 0.5rem; font-size: 0.92rem;">
                  <span style="font-weight: 700; color: var(--cnt-text-main);">Monday – Thursday:</span>
                  <span style="font-family: monospace; color: var(--cnt-text-muted);">07:30 – 21:00 EST (Full Concierge)</span>
                </div>
                <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--cnt-card-border); padding-bottom: 0.5rem; font-size: 0.92rem;">
                  <span style="font-weight: 700; color: var(--cnt-text-main);">Friday:</span>
                  <span style="font-family: monospace; color: var(--cnt-text-muted);">07:30 – 19:30 EST (Full Concierge)</span>
                </div>
                <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--cnt-card-border); padding-bottom: 0.5rem; font-size: 0.92rem;">
                  <span style="font-weight: 700; color: var(--cnt-text-main);">Saturday:</span>
                  <span style="font-family: monospace; color: var(--cnt-text-muted);">09:00 – 17:00 EST (On-Site Rehearsals)</span>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 0.92rem;">
                  <span style="font-weight: 700; color: var(--cnt-text-main);">Sunday &amp; Holidays:</span>
                  <span style="font-family: monospace; color: #ef4444; font-weight: 800;">24/7 Redundant Crisis Standby Only</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 5: LOCATION MAP & GEOSPATIAL INGRESS DECK -->
      <section id="location-map" class="cnt-section-map-new">
        <div class="cnt-container">
          <div class="cnt-section-head framer-radar-sweep">
            <span class="cnt-badge"><i class="fas fa-map-location-dot"></i> Geospatial Navigation</span>
            <h2 class="cnt-title">Split-Screen Radar Viewport &amp; <span class="cnt-title-gradient">Ingress Terminal</span></h2>
            <p class="cnt-subtitle">
              Comprehensive wayfinding logistics. Switch between global hub pins and review subterranean motorcade clearances and aviation corridors.
            </p>
          </div>

          <!-- Split Screen Radar Layout -->
          <div class="cnt-radar-deck-layout framer-radar-sweep">
            <div class="cnt-radar-selector-card">
              <div>
                <span class="cnt-badge"><i class="fas fa-crosshairs"></i> Target Geofence</span>
                <h3 style="font-size: 1.35rem; font-weight: 800; color: var(--cnt-text-main); margin-bottom: 0.5rem;">Select Hub Viewport</h3>
                <p style="font-size: 0.88rem; color: var(--cnt-text-muted); line-height: 1.5;">
                  Toggle destination coordinates to update the live navigation vector:
                </p>
              </div>

              <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                <div class="cnt-radar-city-btn active" onclick="switchRadarPin('New York', '40.7580° N, 73.9855° W', '30 Rockefeller Plaza, 48th Floor, Manhattan', this)">
                  <span><i class="fas fa-location-dot" style="color: var(--cnt-accent); margin-right: 0.5rem;"></i> New York Flagship HQ</span>
                  <span style="font-size: 0.75rem; color: #10b981;">Active</span>
                </div>
                <div class="cnt-radar-city-btn" onclick="switchRadarPin('London', '51.5074° N, 0.1278° W', '14 Curzon Street, Mayfair, London W1J 7TX', this)">
                  <span><i class="fas fa-location-dot" style="margin-right: 0.5rem;"></i> London Mayfair Hub</span>
                  <span style="font-size: 0.75rem; color: var(--cnt-text-muted);">GMT</span>
                </div>
                <div class="cnt-radar-city-btn" onclick="switchRadarPin('Singapore', '1.2838° N, 103.8591° E', '10 Marina Boulevard, Tower 2, Level 38', this)">
                  <span><i class="fas fa-location-dot" style="margin-right: 0.5rem;"></i> Singapore Marina Bay</span>
                  <span style="font-size: 0.75rem; color: var(--cnt-text-muted);">SGT</span>
                </div>
              </div>

              <div style="background: var(--cnt-surface-muted); padding: 1rem; border-radius: 0.75rem; border: 1px solid var(--cnt-card-border);">
                <div style="font-size: 0.75rem; text-transform: uppercase; font-weight: 800; color: var(--cnt-text-muted);">Current Active Target</div>
                <div id="radarTargetName" style="font-size: 1rem; font-weight: 800; color: var(--cnt-text-main); margin-top: 0.2rem;">New York Flagship HQ</div>
                <div id="radarTargetCoords" style="font-family: monospace; font-size: 0.8rem; color: var(--cnt-accent);">40.7580° N, 73.9855° W</div>
              </div>
            </div>

            <div class="cnt-radar-viewport-frame">
              <img src="images/contact_location_map.jpg" alt="Interactive Geospatial Digital Navigation Map Interface" loading="lazy">
              <div class="cnt-radar-sweep-hud">
                <i class="fas fa-radar"></i> GEOFENCE RADAR LOCK: <span id="radarHudCity">NEW YORK</span>
              </div>
              <div style="position: absolute; bottom: 1.5rem; right: 1.5rem;">
                <button class="cnt-btn cnt-btn-primary" onclick="alert('Exporting executive transit coordinates to Google Maps...');">
                  <i class="fas fa-arrow-up-right-from-square"></i> Open In Google Maps
                </button>
              </div>
            </div>
          </div>

          <!-- Bottom Ingress Dock Triad -->
          <div class="cnt-ingress-dock-triad framer-radar-sweep">
            <div class="cnt-dock-pod">
              <div style="display: flex; align-items: center; gap: 0.5rem; font-weight: 800; color: var(--cnt-text-main);">
                <i class="fas fa-helicopter" style="color: var(--cnt-accent);"></i> Aviation &amp; Helipad Corridor
              </div>
              <div style="font-size: 0.85rem; color: var(--cnt-text-muted); line-height: 1.45;">
                6-minute executive transfer from HeliNY Downtown Manhattan Heliport (JRB) or West 30th St (JRA).
              </div>
            </div>

            <div class="cnt-dock-pod">
              <div style="display: flex; align-items: center; gap: 0.5rem; font-weight: 800; color: var(--cnt-text-main);">
                <i class="fas fa-car-side" style="color: var(--cnt-accent);"></i> Subterranean Motorcade Ingress
              </div>
              <div style="font-size: 0.85rem; color: var(--cnt-text-muted); line-height: 1.45;">
                Private below-grade vehicle concourse entrance off West 49th St with automated bollards and armored clearance.
              </div>
            </div>

            <div class="cnt-dock-pod">
              <div style="display: flex; align-items: center; gap: 0.5rem; font-weight: 800; color: var(--cnt-text-main);">
                <i class="fas fa-train-subway" style="color: var(--cnt-accent);"></i> Executive Rail Ingress
              </div>
              <div style="font-size: 0.85rem; color: var(--cnt-text-muted); line-height: 1.45;">
                Direct climate-controlled concourse linking Grand Central Terminal and B, D, F, M subway platforms.
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 6: GENERAL ENQUIRY FORM & CORPORATE CONSULTATION REQUEST -->
      <section id="enquiry-consultation" class="cnt-section-forge-new">
        <div class="cnt-container">
          <div class="cnt-section-head framer-foundry-studio">
            <span class="cnt-badge"><i class="fas fa-file-signature"></i> Communications Foundry</span>
            <h2 class="cnt-title">3-Column Consultation Studio &amp; <span class="cnt-title-gradient">Inquiry Forge</span></h2>
            <p class="cnt-subtitle">
              Whether requesting a confidential conference proposal or submitting general inquiries, our 3-column studio allows comprehensive requirement submission.
            </p>
          </div>

          <div class="cnt-foundry-studio-card framer-foundry-studio">
            <!-- Mode Segment Bar -->
            <div class="cnt-mode-segment-bar">
              <button type="button" class="cnt-segment-btn active" id="btnModeConsultation" onclick="setFoundryMode('consultation')">
                <i class="fas fa-handshake"></i> Corporate Consultation Request
              </button>
              <button type="button" class="cnt-segment-btn" id="btnModeGeneral" onclick="setFoundryMode('general')">
                <i class="fas fa-envelope"></i> General Enquiry Form
              </button>
            </div>

            <form id="foundryStudioForm" onsubmit="handleFoundrySubmit(event)">
              <div class="cnt-tri-col-form-grid">
                <!-- Column 1: Client Credentials -->
                <div class="cnt-form-column">
                  <div style="font-size: 1.05rem; font-weight: 800; color: var(--cnt-text-main); border-bottom: 2px solid var(--cnt-accent); padding-bottom: 0.5rem;">
                    1. Executive Credentials
                  </div>

                  <div class="cnt-field-box">
                    <label class="cnt-field-label">Full Name *</label>
                    <input type="text" class="cnt-input" placeholder="e.g. Julian Rivera" required>
                  </div>

                  <div class="cnt-field-box">
                    <label class="cnt-field-label">Official Corporate Email *</label>
                    <input type="email" class="cnt-input" placeholder="e.g. jrivera@enterprise.com" required>
                  </div>

                  <div class="cnt-field-box">
                    <label class="cnt-field-label">Organization Legal Name *</label>
                    <input type="text" class="cnt-input" placeholder="e.g. Vanguard Dynamics Ltd." required>
                  </div>

                  <div class="cnt-field-box">
                    <label class="cnt-field-label">Direct Phone Line *</label>
                    <input type="tel" class="cnt-input" placeholder="+1 (555) 019-4820" required>
                  </div>
                </div>

                <!-- Column 2: Event Parameters -->
                <div class="cnt-form-column">
                  <div style="font-size: 1.05rem; font-weight: 800; color: var(--cnt-text-main); border-bottom: 2px solid var(--cnt-accent); padding-bottom: 0.5rem;">
                    2. Event Parameters
                  </div>

                  <div id="foundryConsultationFields" style="display: flex; flex-direction: column; gap: 1.25rem;">
                    <div class="cnt-field-box">
                      <label class="cnt-field-label">Delegate Attendance Target</label>
                      <select class="cnt-select">
                        <option value="300-1000">300 – 1,000 Delegates (Executive Summit)</option>
                        <option value="1000-5000" selected>1,000 – 5,000 Delegates (Major Congress)</option>
                        <option value="5000+">5,000+ Delegates (Global Plenary Expo)</option>
                      </select>
                    </div>

                    <div class="cnt-field-box">
                      <label class="cnt-field-label">Estimated CapEx Budget Range</label>
                      <select class="cnt-select">
                        <option value="250k-500k">$250,000 – $500,000</option>
                        <option value="500k-1.5m" selected>$500,000 – $1,500,000</option>
                        <option value="1.5m-5m">$1,500,000 – $5,000,000</option>
                        <option value="5m+">$5,000,000+</option>
                      </select>
                    </div>

                    <div class="cnt-field-box">
                      <label class="cnt-field-label">Target Destination City</label>
                      <input type="text" class="cnt-input" placeholder="e.g. New York, London, Geneva...">
                    </div>
                  </div>

                  <div id="foundryGeneralFields" style="display: none; flex-direction: column; gap: 1.25rem;">
                    <div class="cnt-field-box">
                      <label class="cnt-field-label">Inquiry Department Category</label>
                      <select class="cnt-select">
                        <option value="general">General Corporate Inquiry</option>
                        <option value="media">Press &amp; Media Accreditation</option>
                        <option value="vendor">Vendor Procurement Query</option>
                        <option value="career">Executive Talent &amp; Careers</option>
                      </select>
                    </div>
                  </div>
                </div>

                <!-- Column 3: Briefing Dossier & Submit -->
                <div class="cnt-form-column" style="justify-content: space-between;">
                  <div>
                    <div style="font-size: 1.05rem; font-weight: 800; color: var(--cnt-text-main); border-bottom: 2px solid var(--cnt-accent); padding-bottom: 0.5rem; margin-bottom: 1.25rem;">
                      3. Scope &amp; Dispatch
                    </div>

                    <div class="cnt-field-box">
                      <label class="cnt-field-label" id="foundryMessageLabel">Project Scope &amp; Strategic Objectives *</label>
                      <textarea class="cnt-textarea" rows="4" placeholder="Detail your target summit dates, staging requirements, and confidential briefing topics..." required></textarea>
                    </div>

                    <div style="margin-top: 1rem; border-radius: 0.85rem; overflow: hidden; height: 110px; border: 1px solid var(--cnt-card-border);">
                      <img src="images/contact_consultation_form.jpg" alt="Corporate Event Consultation Room and Floorplans" style="width: 100%; height: 100%; object-fit: cover;">
                    </div>
                  </div>

                  <div>
                    <button type="submit" class="cnt-btn cnt-btn-primary" style="width: 100%; font-size: 1rem; padding: 0.95rem;">
                      <i class="fas fa-paper-plane"></i> Dispatch Strategic Briefing
                    </button>
                    <div style="text-align: center; font-size: 0.75rem; color: var(--cnt-text-muted); margin-top: 0.65rem;">
                      <i class="fas fa-shield-alt" style="color: #10b981;"></i> Bilateral NDA executed upon intake.
                    </div>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </section>

      <!-- SECTION 7: EMERGENCY EVENT SUPPORT CONTACT & 24/7 COMMAND BUNKER -->
      <section id="emergency-support" class="cnt-section-emergency-new">
        <div class="cnt-container">
          <div class="cnt-section-head framer-beacon-alert">
            <span class="cnt-badge cnt-badge-danger"><i class="fas fa-triangle-exclamation"></i> Mission Continuity Command</span>
            <h2 class="cnt-title">Crisis Incident Bunker &amp; <span class="cnt-title-danger">Rapid Emergency Support</span></h2>
            <p class="cnt-subtitle">
              Live conference underway and facing critical power loss, rigging failure, or broadcast disruption? Our emergency response unit deploys with a guaranteed 15-minute response SLA.
            </p>
          </div>

          <!-- Crisis Marquee Banner -->
          <div class="cnt-crisis-marquee-banner framer-beacon-alert">
            <div>
              <div style="display: flex; align-items: center; gap: 0.75rem;">
                <span style="width: 12px; height: 12px; border-radius: 50%; background: #ef4444; box-shadow: 0 0 12px #ef4444; display: inline-block;"></span>
                <span style="font-size: 0.85rem; font-weight: 800; letter-spacing: 0.06em; text-transform: uppercase;">24/7 Redundant Incident Bunker Active</span>
              </div>
              <div style="font-size: 2.2rem; font-weight: 900; font-family: monospace; margin-top: 0.35rem; color: #f87171;">
                +1 (888) 911-EVENT
              </div>
              <div style="font-size: 0.85rem; color: #cbd5e1;">Unlisted direct crisis dispatch line for active event directors</div>
            </div>
            <button class="cnt-btn cnt-btn-danger" style="font-size: 1rem; padding: 1rem 2rem;" onclick="alert('CONNECTING TO ON-DUTY CRISIS INCIDENT COMMANDER...');">
              <i class="fas fa-phone-volume"></i> Connect Immediate Priority Dispatch
            </button>
          </div>

          <!-- Crisis Triad & Control Room Feature -->
          <div class="cnt-crisis-triad-layout framer-beacon-alert">
            <div class="cnt-crisis-triad-col">
              <div class="cnt-crisis-pod">
                <div style="font-weight: 800; font-size: 1.05rem; color: var(--cnt-text-main); display: flex; align-items: center; gap: 0.5rem;">
                  <i class="fas fa-plug-circle-bolt" style="color: #ef4444;"></i> Electrical &amp; Rigging Emergency Failover
                </div>
                <div style="font-size: 0.88rem; color: var(--cnt-text-muted); line-height: 1.45;">
                  Instant automatic transfer switch (ATS) activation of mobile 2MW Caterpillar diesel generators and UPS power banks within 1.2 seconds.
                </div>
              </div>

              <div class="cnt-crisis-pod">
                <div style="font-weight: 800; font-size: 1.05rem; color: var(--cnt-text-main); display: flex; align-items: center; gap: 0.5rem;">
                  <i class="fas fa-satellite" style="color: #ef4444;"></i> Bonded Satellite &amp; Starlink Broadcast Reroute
                </div>
                <div style="font-size: 0.88rem; color: var(--cnt-text-muted); line-height: 1.45;">
                  Terrestrial fiber cut fallback to multi-homed low-earth-orbit Starlink constellation terminals ensuring zero conference livestream interruption.
                </div>
              </div>

              <div class="cnt-crisis-pod">
                <div style="font-weight: 800; font-size: 1.05rem; color: var(--cnt-text-main); display: flex; align-items: center; gap: 0.5rem;">
                  <i class="fas fa-shield-virus" style="color: #ef4444;"></i> Diplomatic Security &amp; Medical Evacuation
                </div>
                <div style="font-size: 0.88rem; color: var(--cnt-text-muted); line-height: 1.45;">
                  Dedicated emergency liaison with municipal law enforcement, bomb sweeps, and private trauma helicopter corridors for VIP speakers.
                </div>
              </div>
            </div>

            <div class="cnt-crisis-media-frame">
              <img src="images/contact_emergency_support.jpg" alt="High-Tech Incident Command Room and Telemetry Monitors" loading="lazy">
              <div style="position: absolute; bottom: 1.5rem; left: 1.5rem; right: 1.5rem; background: rgba(15, 23, 42, 0.9); backdrop-filter: blur(8px); padding: 1rem 1.25rem; border-radius: 1rem; color: #ffffff; font-size: 0.85rem; border: 1px solid rgba(220, 38, 38, 0.35);">
                <i class="fas fa-stopwatch" style="color: #ef4444;"></i> <strong>Guaranteed 15-Minute Intervention SLA:</strong> Lead technical specialists mobilized immediately upon incident receipt.
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SUCCESS MODAL POPUP -->
      <div class="cnt-modal-backdrop" id="contactSuccessModal">
        <div class="cnt-modal-box">
          <div class="cnt-modal-icon">
            <i class="fas fa-check"></i>
          </div>
          <h3 style="font-size: 1.65rem; font-weight: 800; color: var(--cnt-text-main); margin-bottom: 0.5rem;">Communications Dossier Dispatched!</h3>
          <p style="font-size: 0.95rem; color: var(--cnt-text-muted); line-height: 1.6; margin-bottom: 1.75rem;">
            Your inquiry has been encrypted and routed to our Senior Vice President of Production. Reference Tracking Code: <strong id="trackingRefCode" style="color: var(--cnt-accent); font-family: monospace;">INQ-2026-9142</strong>. Our team will initiate dialogue within 2 business hours.
          </p>
          <button class="cnt-btn cnt-btn-primary" onclick="closeContactModal()" style="width: 100%;">
            <i class="fas fa-arrow-left"></i> Return to Directory
          </button>
        </div>
      </div>

    </main>
    """

    # Page Interactive Scripts
    new_contact_scripts = """
  <!-- =====================================================================
       INTERACTIVE CLIENT CONTROLS & FRAMER MOTION OBSERVERS
       ===================================================================== -->
  <script>
    // 1. Framer Motion Scroll Trigger Observers
    document.addEventListener('DOMContentLoaded', function () {
      var motionClasses = [
        '.framer-monolith-panoramic',
        '.framer-rotary-dial',
        '.framer-keycard-matrix',
        '.framer-meridian-wave',
        '.framer-radar-sweep',
        '.framer-foundry-studio',
        '.framer-beacon-alert'
      ];

      var motionObserver = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('framer-in-view');
            var children = entry.target.querySelectorAll('.framer-monolith-panoramic, .framer-rotary-dial, .framer-keycard-matrix, .framer-meridian-wave, .framer-radar-sweep, .framer-foundry-studio, .framer-beacon-alert');
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

      // 2. Start Live World Clocks
      updateLiveClocks();
      setInterval(updateLiveClocks, 1000);
    });

    // World Clocks Updater
    function updateLiveClocks() {
      var now = new Date();

      function formatTime(date, timeZone) {
        try {
          return new Intl.DateTimeFormat('en-US', {
            timeZone: timeZone,
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: false
          }).format(date);
        } catch (e) {
          return date.toTimeString().split(' ')[0];
        }
      }

      var nycEl = document.getElementById('clockNYC');
      var lonEl = document.getElementById('clockLON');
      var sgpEl = document.getElementById('clockSGP');
      var zurEl = document.getElementById('clockZUR');

      if (nycEl) nycEl.textContent = formatTime(now, 'America/New_York');
      if (lonEl) lonEl.textContent = formatTime(now, 'Europe/London');
      if (sgpEl) sgpEl.textContent = formatTime(now, 'Asia/Singapore');
      if (zurEl) zurEl.textContent = formatTime(now, 'Europe/Zurich');
    }

    // 3. Copy Email to Clipboard
    function copyEmailToClipboard(email, btn) {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(email).then(function () {
          var original = btn.innerHTML;
          btn.innerHTML = '<i class="fas fa-check" style="color:#10b981;"></i> Copied!';
          setTimeout(function () { btn.innerHTML = original; }, 2000);
        });
      } else {
        prompt('Copy email address:', email);
      }
    }

    // 4. Radar Pin Switcher
    function switchRadarPin(cityName, coords, address, btn) {
      document.querySelectorAll('.cnt-radar-city-btn').forEach(function (b) {
        b.classList.remove('active');
      });
      btn.classList.add('active');

      var nameEl = document.getElementById('radarTargetName');
      var coordsEl = document.getElementById('radarTargetCoords');
      var hudCityEl = document.getElementById('radarHudCity');

      if (nameEl) nameEl.textContent = cityName + ' Hub';
      if (coordsEl) coordsEl.textContent = coords;
      if (hudCityEl) hudCityEl.textContent = cityName.toUpperCase();
    }

    // 5. Foundry Studio Mode Switcher
    function setFoundryMode(mode) {
      var btnConsult = document.getElementById('btnModeConsultation');
      var btnGen = document.getElementById('btnModeGeneral');
      var consultFields = document.getElementById('foundryConsultationFields');
      var genFields = document.getElementById('foundryGeneralFields');
      var msgLabel = document.getElementById('foundryMessageLabel');

      if (mode === 'consultation') {
        if (btnConsult) btnConsult.classList.add('active');
        if (btnGen) btnGen.classList.remove('active');
        if (consultFields) consultFields.style.display = 'flex';
        if (genFields) genFields.style.display = 'none';
        if (msgLabel) msgLabel.textContent = 'Project Scope & Strategic Objectives *';
      } else {
        if (btnGen) btnGen.classList.add('active');
        if (btnConsult) btnConsult.classList.remove('active');
        if (consultFields) consultFields.style.display = 'none';
        if (genFields) genFields.style.display = 'flex';
        if (msgLabel) msgLabel.textContent = 'General Inquiry & Subject Details *';
      }
    }

    // 6. Form Submission & Modal
    function handleFoundrySubmit(e) {
      e.preventDefault();
      var code = 'INQ-2026-' + Math.floor(1000 + Math.random() * 9000);
      var codeEl = document.getElementById('trackingRefCode');
      if (codeEl) codeEl.textContent = code;

      var modal = document.getElementById('contactSuccessModal');
      if (modal) modal.style.display = 'flex';
    }

    function closeContactModal() {
      var modal = document.getElementById('contactSuccessModal');
      if (modal) modal.style.display = 'none';
      var form = document.getElementById('foundryStudioForm');
      if (form) form.reset();
    }
  </script>
"""

    # Assemble complete document
    final_html = (
        nav_head_up_to_style
        + new_contact_css
        + "\n  </style>"
        + nav_mid[len("</style>"):]
        + new_contact_content
        + footer_full
        + new_contact_scripts
        + closing_part
    )

    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print("Successfully built redesigned contact.html! Total length:", len(final_html))

if __name__ == '__main__':
    build_contact_new_layout()
