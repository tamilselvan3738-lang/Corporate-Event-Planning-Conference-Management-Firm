import os

def build_contact_html():
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

    # CSS for contact.html
    contact_css = """
    /* =====================================================================
       GLOBAL CONTACT & EXECUTIVE DIRECTORY - CUSTOM PAGE STYLES
       Supports Light Mode, Dark Mode (body.dark), and RTL (body.rtl)
       ===================================================================== */
    :root {
      --ct-primary: #1e3a8a;
      --ct-primary-dark: #0f172a;
      --ct-accent: #d97706;
      --ct-accent-light: #fbbf24;
      --ct-accent-glow: rgba(217, 119, 6, 0.16);
      --ct-danger: #dc2626;
      --ct-danger-glow: rgba(220, 38, 38, 0.18);
      --ct-bg: #f8fafc;
      --ct-surface: #ffffff;
      --ct-surface-muted: #f1f5f9;
      --ct-card-border: #e2e8f0;
      --ct-text-main: #0f172a;
      --ct-text-muted: #64748b;
      --ct-text-light: #94a3b8;
      --ct-gold-gradient: linear-gradient(135deg, #b45309 0%, #d97706 50%, #f59e0b 100%);
      --ct-red-gradient: linear-gradient(135deg, #991b1b 0%, #dc2626 50%, #f87171 100%);
      --ct-blue-gradient: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      --ct-shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --ct-shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.07), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
      --ct-shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      --ct-shadow-glow: 0 0 25px rgba(217, 119, 6, 0.22);
    }

    body.dark {
      --ct-bg: #070b14;
      --ct-surface: #0f172a;
      --ct-surface-muted: #131d33;
      --ct-card-border: #1e293b;
      --ct-text-main: #f8fafc;
      --ct-text-muted: #94a3b8;
      --ct-text-light: #64748b;
      --ct-blue-gradient: linear-gradient(135deg, #070b14 0%, #172554 100%);
    }

    /* RTL Support */
    body.rtl .ct-section-head { text-align: right; }
    body.rtl .ct-badge i { margin-left: 0.5rem; margin-right: 0; }
    body.rtl .ct-btn i { margin-right: 0.5rem; margin-left: 0; }

    /* Base Reset for Contact Container */
    .ct-page-wrap {
      background-color: var(--ct-bg);
      color: var(--ct-text-main);
      font-family: 'Inter', system-ui, sans-serif;
      overflow-x: hidden;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    .ct-container {
      max-width: 1320px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }

    /* SECTION HEADER STYLING */
    .ct-section-head {
      margin-bottom: 3.5rem;
      position: relative;
    }

    .ct-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.45rem 1.1rem;
      border-radius: 9999px;
      background: var(--ct-accent-glow);
      border: 1px solid rgba(217, 119, 6, 0.35);
      color: var(--ct-accent);
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      margin-bottom: 1rem;
    }

    .ct-badge-danger {
      background: var(--ct-danger-glow);
      border-color: rgba(220, 38, 38, 0.35);
      color: #ef4444;
    }

    .ct-title {
      font-size: clamp(2rem, 3.5vw, 2.75rem);
      font-weight: 800;
      line-height: 1.18;
      color: var(--ct-text-main);
      letter-spacing: -0.025em;
      margin-bottom: 1rem;
    }

    .ct-title-gradient {
      background: var(--ct-gold-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .ct-title-danger {
      background: var(--ct-red-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .ct-subtitle {
      font-size: 1.1rem;
      color: var(--ct-text-muted);
      line-height: 1.65;
      max-width: 780px;
    }

    /* HERO JUMP NAV STRIP */
    .ct-hero-strip {
      background: var(--ct-surface);
      border-bottom: 1px solid var(--ct-card-border);
      padding: 2.75rem 0 2.25rem;
      position: relative;
    }
    .ct-hero-content {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 1.25rem;
    }
    .ct-hero-title {
      font-size: clamp(2.2rem, 4vw, 3.25rem);
      font-weight: 900;
      color: var(--ct-text-main);
      letter-spacing: -0.03em;
    }
    .ct-hero-desc {
      font-size: 1.15rem;
      color: var(--ct-text-muted);
      max-width: 840px;
      line-height: 1.65;
    }
    .ct-nav-pills {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.65rem;
      margin-top: 1rem;
    }
    .ct-nav-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.55rem 1.15rem;
      border-radius: 9999px;
      background: var(--ct-surface-muted);
      border: 1px solid var(--ct-card-border);
      color: var(--ct-text-main);
      font-size: 0.88rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
    }
    .ct-nav-pill:hover {
      background: var(--ct-accent);
      color: #ffffff;
      border-color: var(--ct-accent);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(217, 119, 6, 0.25);
    }
    .ct-nav-pill i {
      color: var(--ct-accent);
      transition: color 0.3s ease;
    }
    .ct-nav-pill:hover i {
      color: #ffffff;
    }

    /* GLOBAL BUTTONS */
    .ct-btn {
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
    .ct-btn-primary {
      background: var(--ct-gold-gradient);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(217, 119, 6, 0.3);
    }
    .ct-btn-primary:hover {
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 8px 24px rgba(217, 119, 6, 0.45);
      color: #ffffff;
    }
    .ct-btn-danger {
      background: var(--ct-red-gradient);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(220, 38, 38, 0.35);
    }
    .ct-btn-danger:hover {
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 8px 24px rgba(220, 38, 38, 0.5);
      color: #ffffff;
    }
    .ct-btn-outline {
      background: transparent;
      color: var(--ct-text-main);
      border: 1.5px solid var(--ct-card-border);
    }
    .ct-btn-outline:hover {
      background: var(--ct-surface-muted);
      border-color: var(--ct-accent);
      color: var(--ct-accent);
      transform: translateY(-2px);
    }

    /* =====================================================================
       FRAMER MOTION OBSERVER SYSTEM (7 DISTINCT SECTION ANIMATIONS)
       ===================================================================== */
    /* Section 1: Embassy Stately Perspective Rise */
    .framer-embassy-rise {
      opacity: 0;
      transform: perspective(1000px) rotateX(8deg) translateY(40px);
      transition: opacity 0.85s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1);
      will-change: transform, opacity;
    }
    .framer-embassy-rise.framer-in-view {
      opacity: 1;
      transform: perspective(1000px) rotateX(0deg) translateY(0);
    }

    /* Section 2: Telephony Switchboard High-Frequency Snap */
    .framer-telephony-snap {
      opacity: 0;
      transform: scale(0.93) translateY(45px);
      transition: opacity 0.75s cubic-bezier(0.175, 0.885, 0.32, 1.275), transform 0.75s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      will-change: transform, opacity;
    }
    .framer-telephony-snap.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    /* Section 3: PGP Cryptographic Horizontal Slide */
    .framer-pgp-decrypt {
      opacity: 0;
      transform: translateX(-50px);
      filter: blur(4px);
      transition: opacity 0.8s cubic-bezier(0.25, 1, 0.5, 1), transform 0.8s cubic-bezier(0.25, 1, 0.5, 1), filter 0.8s ease;
      will-change: transform, opacity, filter;
    }
    .framer-pgp-decrypt.framer-in-view {
      opacity: 1;
      transform: translateX(0);
      filter: blur(0);
    }

    /* Section 4: Chronometer Radial Time Sweep */
    .framer-chronometer-spin {
      opacity: 0;
      transform: scale(0.95) rotate(-1.5deg) translateY(35px);
      transition: opacity 0.85s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.85s cubic-bezier(0.34, 1.56, 0.64, 1);
      will-change: transform, opacity;
    }
    .framer-chronometer-spin.framer-in-view {
      opacity: 1;
      transform: scale(1) rotate(0deg) translateY(0);
    }

    /* Section 5: Wayfinding Cartographic Zoom */
    .framer-wayfinding-zoom {
      opacity: 0;
      transform: scale(1.06) translateY(30px);
      transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform, opacity;
    }
    .framer-wayfinding-zoom.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    /* Section 6: Bilateral Consultation Forge Expansion */
    .framer-forge-expand {
      opacity: 0;
      transform: scale(0.94) translateY(40px);
      transition: opacity 0.8s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
      will-change: transform, opacity;
    }
    .framer-forge-expand.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    /* Section 7: Incident Bunker Authoritative Pulse */
    .framer-bunker-pulse {
      opacity: 0;
      transform: scale(1.05) translateY(-25px);
      transition: opacity 0.7s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.7s cubic-bezier(0.34, 1.56, 0.64, 1);
      will-change: transform, opacity;
    }
    .framer-bunker-pulse.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    /* =====================================================================
       SECTION 1: OFFICE ADDRESS & GLOBAL HEADQUARTERS
       ===================================================================== */
    .ct-section-address {
      padding: 6.5rem 0;
      position: relative;
    }
    .ct-embassy-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 3rem;
      align-items: stretch;
    }
    .ct-hq-pylon-card {
      background: var(--ct-surface);
      border: 1px solid var(--ct-card-border);
      border-radius: 1.75rem;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--ct-shadow-lg);
      transition: border-color 0.4s ease, transform 0.4s ease;
    }
    .ct-hq-pylon-card:hover {
      border-color: rgba(217, 119, 6, 0.45);
      transform: translateY(-4px);
    }
    .ct-hq-img-box {
      position: relative;
      height: 380px;
      overflow: hidden;
    }
    .ct-hq-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.7s cubic-bezier(0.2, 0.8, 0.2, 1);
    }
    .ct-hq-pylon-card:hover .ct-hq-img-box img {
      transform: scale(1.04);
    }
    .ct-coordinates-tag {
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
    body.rtl .ct-coordinates-tag {
      left: auto;
      right: 1.25rem;
    }
    .ct-hq-body {
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
      justify-content: space-between;
    }
    .ct-hq-specs-strip {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
      padding: 1.25rem 0;
      margin: 1.25rem 0;
      border-top: 1px solid var(--ct-card-border);
      border-bottom: 1px solid var(--ct-card-border);
    }
    .ct-hq-spec-item {
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }
    .ct-hq-spec-lbl {
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--ct-text-light);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .ct-hq-spec-val {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--ct-text-main);
    }

    /* Right Regional Hubs */
    .ct-regional-hubs-col {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      justify-content: space-between;
    }
    .ct-hub-card {
      background: var(--ct-surface);
      border: 1px solid var(--ct-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      gap: 1.25rem;
      align-items: flex-start;
      box-shadow: var(--ct-shadow-sm);
      transition: all 0.35s ease;
      cursor: pointer;
    }
    .ct-hub-card:hover {
      border-color: var(--ct-accent);
      background: var(--ct-surface-muted);
      transform: translateX(6px);
      box-shadow: var(--ct-shadow-md);
    }
    body.rtl .ct-hub-card:hover {
      transform: translateX(-6px);
    }
    .ct-hub-flag {
      width: 44px;
      height: 44px;
      border-radius: 1rem;
      background: var(--ct-gold-gradient);
      color: #ffffff;
      font-size: 1.15rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      box-shadow: 0 4px 10px rgba(217, 119, 6, 0.3);
    }
    .ct-hub-info {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }
    .ct-hub-city {
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--ct-text-main);
    }
    .ct-hub-address {
      font-size: 0.88rem;
      color: var(--ct-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 2: PHONE NUMBER & DIRECT TELEPHONY DESK
       ===================================================================== */
    .ct-section-telephony {
      padding: 6.5rem 0;
      background: var(--ct-surface-muted);
      border-top: 1px solid var(--ct-card-border);
      border-bottom: 1px solid var(--ct-card-border);
      position: relative;
    }
    .ct-telephony-layout {
      display: grid;
      grid-template-columns: 0.95fr 1.05fr;
      gap: 3rem;
      align-items: stretch;
    }
    .ct-telephony-media-card {
      background: var(--ct-surface);
      border: 1px solid var(--ct-card-border);
      border-radius: 1.75rem;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--ct-shadow-lg);
    }
    .ct-telephony-img-box {
      position: relative;
      height: 320px;
    }
    .ct-telephony-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .ct-audio-waveform-hud {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(0deg, rgba(7, 11, 20, 0.95) 0%, rgba(7, 11, 20, 0.4) 70%, transparent 100%);
      padding: 1.5rem;
      color: #ffffff;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .ct-live-pulse-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 10px #10b981;
      display: inline-block;
      margin-right: 0.5rem;
    }
    body.rtl .ct-live-pulse-dot {
      margin-right: 0;
      margin-left: 0.5rem;
    }
    .ct-telephony-body {
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      flex-grow: 1;
      justify-content: space-between;
    }

    /* Right PBX Dialing Pods */
    .ct-pbx-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.25rem;
    }
    .ct-pbx-card {
      background: var(--ct-surface);
      border: 1px solid var(--ct-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      box-shadow: var(--ct-shadow-sm);
      transition: all 0.3s ease;
    }
    .ct-pbx-card:hover {
      border-color: var(--ct-accent);
      transform: translateY(-3px);
      box-shadow: var(--ct-shadow-md);
    }
    .ct-pbx-badge {
      font-size: 0.72rem;
      font-weight: 800;
      padding: 0.25rem 0.65rem;
      border-radius: 0.4rem;
      background: var(--ct-surface-muted);
      color: var(--ct-accent);
      align-self: flex-start;
      border: 1px solid var(--ct-card-border);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .ct-pbx-dept {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--ct-text-main);
    }
    .ct-pbx-number {
      font-size: 1.15rem;
      font-weight: 900;
      color: var(--ct-primary);
      font-family: monospace;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: color 0.2s ease;
    }
    body.dark .ct-pbx-number {
      color: #38bdf8;
    }
    .ct-pbx-number:hover {
      color: var(--ct-accent);
    }

    /* =====================================================================
       SECTION 3: BUSINESS EMAIL & ENCRYPTED DISPATCH GATEWAY
       ===================================================================== */
    .ct-section-email {
      padding: 6.5rem 0;
      position: relative;
    }
    .ct-email-gateway-grid {
      display: grid;
      grid-template-columns: 1fr 1.15fr;
      gap: 3rem;
      align-items: stretch;
    }
    .ct-pgp-vault-card {
      background: var(--ct-surface);
      border: 1px solid var(--ct-card-border);
      border-radius: 1.75rem;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--ct-shadow-lg);
    }
    .ct-pgp-img-box {
      position: relative;
      height: 300px;
    }
    .ct-pgp-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .ct-pgp-body {
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      flex-grow: 1;
      justify-content: space-between;
    }
    .ct-fingerprint-box {
      background: var(--ct-surface-muted);
      border: 1px solid var(--ct-card-border);
      border-radius: 1rem;
      padding: 1.25rem;
      font-family: monospace;
      font-size: 0.8rem;
      color: var(--ct-text-muted);
      word-break: break-all;
      line-height: 1.5;
    }

    /* Right Departmental Inboxes Stack */
    .ct-inbox-stack {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }
    .ct-inbox-row {
      background: var(--ct-surface);
      border: 1px solid var(--ct-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
      box-shadow: var(--ct-shadow-sm);
      transition: all 0.3s ease;
    }
    .ct-inbox-row:hover {
      border-color: var(--ct-accent);
      transform: translateY(-2px);
      box-shadow: var(--ct-shadow-md);
    }
    .ct-inbox-dept-info {
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }
    .ct-inbox-title {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--ct-text-main);
    }
    .ct-inbox-addr {
      font-size: 0.95rem;
      color: var(--ct-accent);
      font-weight: 700;
      font-family: monospace;
    }
    .ct-copy-btn {
      padding: 0.5rem 1rem;
      border-radius: 0.6rem;
      border: 1px solid var(--ct-card-border);
      background: var(--ct-surface-muted);
      color: var(--ct-text-main);
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
    }
    .ct-copy-btn:hover {
      background: var(--ct-accent);
      color: #ffffff;
      border-color: var(--ct-accent);
    }

    /* =====================================================================
       SECTION 4: OFFICE HOURS & 24/7 TIMEZONE OPERATIONS
       ===================================================================== */
    .ct-section-hours {
      padding: 6.5rem 0;
      background: var(--ct-surface-muted);
      border-top: 1px solid var(--ct-card-border);
      border-bottom: 1px solid var(--ct-card-border);
      position: relative;
    }
    .ct-hours-board-layout {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 3rem;
      align-items: stretch;
    }
    .ct-world-clocks-deck {
      background: var(--ct-surface);
      border: 1px solid var(--ct-card-border);
      border-radius: 1.75rem;
      padding: 2.5rem;
      box-shadow: var(--ct-shadow-lg);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .ct-clocks-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.25rem;
      margin: 1.5rem 0 2rem;
    }
    .ct-clock-tile {
      background: var(--ct-surface-muted);
      border: 1px solid var(--ct-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }
    .ct-clock-city {
      font-size: 0.88rem;
      font-weight: 800;
      color: var(--ct-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .ct-clock-time {
      font-size: 2rem;
      font-weight: 900;
      color: var(--ct-text-main);
      font-family: monospace;
      line-height: 1;
    }
    .ct-clock-status {
      font-size: 0.75rem;
      font-weight: 800;
      color: #10b981;
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }

    /* Right Schedule Card */
    .ct-schedule-card {
      background: var(--ct-surface);
      border: 1px solid var(--ct-card-border);
      border-radius: 1.75rem;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--ct-shadow-lg);
    }
    .ct-schedule-img-box {
      position: relative;
      height: 260px;
    }
    .ct-schedule-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .ct-schedule-body {
      padding: 2rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      flex-grow: 1;
      justify-content: space-between;
    }
    .ct-timetable-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }
    .ct-timetable-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.9rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--ct-card-border);
    }
    .ct-day-label {
      font-weight: 700;
      color: var(--ct-text-main);
    }
    .ct-hours-val {
      color: var(--ct-text-muted);
      font-family: monospace;
      font-weight: 600;
    }

    /* =====================================================================
       SECTION 5: LOCATION MAP & GEOSPATIAL INGRESS DECK
       ===================================================================== */
    .ct-section-map {
      padding: 6.5rem 0;
      position: relative;
    }
    .ct-map-terminal-wrap {
      background: var(--ct-surface);
      border: 1px solid var(--ct-card-border);
      border-radius: 1.75rem;
      padding: 2.5rem;
      box-shadow: var(--ct-shadow-lg);
    }
    .ct-map-hero-frame {
      position: relative;
      border-radius: 1.25rem;
      overflow: hidden;
      height: 400px;
      margin-bottom: 2.5rem;
      border: 1px solid var(--ct-card-border);
    }
    .ct-map-hero-frame img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .ct-map-pins-hud {
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
    .ct-ingress-tabs-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.75rem;
    }
    .ct-ingress-card {
      background: var(--ct-surface-muted);
      border: 1px solid var(--ct-card-border);
      border-radius: 1.25rem;
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      transition: all 0.3s ease;
    }
    .ct-ingress-card:hover {
      border-color: var(--ct-accent);
      transform: translateY(-3px);
      box-shadow: var(--ct-shadow-sm);
    }
    .ct-ingress-icon {
      width: 44px;
      height: 44px;
      border-radius: 0.85rem;
      background: var(--ct-accent-glow);
      color: var(--ct-accent);
      font-size: 1.2rem;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .ct-ingress-title {
      font-size: 1.08rem;
      font-weight: 800;
      color: var(--ct-text-main);
    }
    .ct-ingress-desc {
      font-size: 0.88rem;
      color: var(--ct-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 6: GENERAL ENQUIRY FORM & CORPORATE CONSULTATION REQUEST
       ===================================================================== */
    .ct-section-forms {
      padding: 6.5rem 0;
      background: var(--ct-surface-muted);
      border-top: 1px solid var(--ct-card-border);
      border-bottom: 1px solid var(--ct-card-border);
      position: relative;
    }
    .ct-forms-forge-layout {
      display: grid;
      grid-template-columns: 0.9fr 1.1fr;
      gap: 3rem;
      align-items: stretch;
    }
    .ct-forge-sidebar-card {
      background: var(--ct-surface);
      border: 1px solid var(--ct-card-border);
      border-radius: 1.75rem;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--ct-shadow-lg);
    }
    .ct-forge-img-box {
      position: relative;
      height: 320px;
    }
    .ct-forge-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .ct-forge-sidebar-body {
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      flex-grow: 1;
      justify-content: space-between;
    }

    /* Form Card Container */
    .ct-form-card {
      background: var(--ct-surface);
      border: 1px solid var(--ct-card-border);
      border-radius: 1.75rem;
      padding: 2.5rem;
      box-shadow: var(--ct-shadow-lg);
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }
    .ct-form-tab-switcher {
      display: flex;
      gap: 0.5rem;
      background: var(--ct-surface-muted);
      padding: 0.35rem;
      border-radius: 0.85rem;
      border: 1px solid var(--ct-card-border);
    }
    .ct-tab-btn {
      flex: 1;
      padding: 0.75rem 1rem;
      border-radius: 0.6rem;
      font-size: 0.9rem;
      font-weight: 700;
      border: none;
      cursor: pointer;
      background: transparent;
      color: var(--ct-text-muted);
      transition: all 0.3s ease;
      text-align: center;
    }
    .ct-tab-btn.active {
      background: var(--ct-surface);
      color: var(--ct-accent);
      box-shadow: var(--ct-shadow-sm);
    }
    .ct-input-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
    }
    .ct-input-group {
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
    }
    .ct-input-label {
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--ct-text-main);
    }
    .ct-input-field,
    .ct-select-field,
    .ct-textarea-field {
      width: 100%;
      padding: 0.85rem 1.15rem;
      border-radius: 0.75rem;
      border: 1px solid var(--ct-card-border);
      background: var(--ct-surface-muted);
      color: var(--ct-text-main);
      font-family: inherit;
      font-size: 0.95rem;
      outline: none;
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .ct-input-field:focus,
    .ct-select-field:focus,
    .ct-textarea-field:focus {
      border-color: var(--ct-accent);
      box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.15);
      background: var(--ct-surface);
    }

    /* =====================================================================
       SECTION 7: EMERGENCY EVENT SUPPORT CONTACT & 24/7 COMMAND BUNKER
       ===================================================================== */
    .ct-section-emergency {
      padding: 6.5rem 0 8.5rem;
      position: relative;
    }
    .ct-emergency-bunker-card {
      background: var(--ct-surface);
      border: 2px solid rgba(220, 38, 38, 0.4);
      border-radius: 2rem;
      overflow: hidden;
      box-shadow: 0 20px 40px -10px rgba(220, 38, 38, 0.15);
      display: grid;
      grid-template-columns: 1fr 1.15fr;
      align-items: stretch;
    }
    .ct-emergency-img-box {
      position: relative;
      min-height: 420px;
    }
    .ct-emergency-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .ct-crisis-status-overlay {
      position: absolute;
      top: 1.5rem;
      left: 1.5rem;
      background: rgba(15, 23, 42, 0.9);
      backdrop-filter: blur(8px);
      padding: 0.65rem 1.25rem;
      border-radius: 0.85rem;
      border: 1px solid rgba(220, 38, 38, 0.5);
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 0.65rem;
      font-size: 0.85rem;
      font-weight: 800;
      letter-spacing: 0.05em;
    }
    body.rtl .ct-crisis-status-overlay {
      left: auto;
      right: 1.5rem;
    }
    .ct-emergency-content {
      padding: 3rem 2.5rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 1.5rem;
    }
    .ct-crisis-protocols-list {
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }
    .ct-crisis-protocol-item {
      display: flex;
      align-items: flex-start;
      gap: 0.85rem;
      font-size: 0.9rem;
      color: var(--ct-text-muted);
      line-height: 1.45;
    }
    .ct-crisis-protocol-item i {
      color: #ef4444;
      font-size: 1.1rem;
      margin-top: 0.2rem;
    }
    .ct-hotline-dial-banner {
      background: var(--ct-surface-muted);
      border: 1px dashed rgba(220, 38, 38, 0.4);
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
    }

    /* MODAL POPUP */
    .ct-modal-backdrop {
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
    .ct-modal-box {
      background: var(--ct-surface);
      border: 1px solid var(--ct-card-border);
      border-radius: 1.75rem;
      max-width: 520px;
      width: 100%;
      padding: 2.75rem 2.25rem;
      text-align: center;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.35);
      position: relative;
      animation: ctModalPop 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    @keyframes ctModalPop {
      0% { transform: scale(0.85); opacity: 0; }
      100% { transform: scale(1); opacity: 1; }
    }
    .ct-modal-icon {
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
      .ct-embassy-grid,
      .ct-telephony-layout,
      .ct-email-gateway-grid,
      .ct-hours-board-layout,
      .ct-ingress-tabs-grid,
      .ct-forms-forge-layout,
      .ct-emergency-bunker-card {
        grid-template-columns: 1fr;
        gap: 2rem;
      }
      .ct-hq-img-box,
      .ct-telephony-img-box,
      .ct-map-hero-frame,
      .ct-emergency-img-box {
        min-height: 300px;
        height: 300px;
      }
    }
    @media (max-width: 640px) {
      .ct-input-row,
      .ct-pbx-grid,
      .ct-clocks-grid,
      .ct-hq-specs-strip {
        grid-template-columns: 1fr;
        gap: 0.5rem;
      }
    }
    """

    # HTML Body Content for the 7 Sections
    contact_html_content = """
    <!-- =====================================================================
         MAIN CONTENT: 7 UNIQUE CONTACT & EXECUTIVE COMMUNICATIONS SECTIONS
         ===================================================================== -->
    <main class="ct-page-wrap">

      <!-- SUB-HERO / STRATEGIC COMMUNICATIONS HEADER STRIP -->
      <section class="ct-hero-strip">
        <div class="ct-container">
          <div class="ct-hero-content">
            <span class="ct-badge"><i class="fas fa-headset"></i> Direct Executive Communications</span>
            <h1 class="ct-hero-title">Global Headquarters &amp; Strategic Liaison Office</h1>
            <p class="ct-hero-desc">
              Connect directly with our senior event producers, technical broadcast directors, and global logistics counsel across New York, London, Singapore, and Zurich.
            </p>
            <div class="ct-nav-pills">
              <a href="#office-address" class="ct-nav-pill"><i class="fas fa-building"></i> Office Address</a>
              <a href="#phone-telephony" class="ct-nav-pill"><i class="fas fa-phone"></i> Phone Numbers</a>
              <a href="#business-email" class="ct-nav-pill"><i class="fas fa-envelope"></i> Business Email</a>
              <a href="#office-hours" class="ct-nav-pill"><i class="fas fa-clock"></i> Office Hours</a>
              <a href="#location-map" class="ct-nav-pill"><i class="fas fa-map-location-dot"></i> Location Map</a>
              <a href="#enquiry-consultation" class="ct-nav-pill"><i class="fas fa-file-pen"></i> Consultation &amp; Inquiry</a>
              <a href="#emergency-support" class="ct-nav-pill"><i class="fas fa-triangle-exclamation"></i> Emergency Support</a>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 1: OFFICE ADDRESS & GLOBAL HEADQUARTERS -->
      <section id="office-address" class="ct-section-address">
        <div class="ct-container">
          <div class="ct-section-head framer-embassy-rise">
            <span class="ct-badge"><i class="fas fa-building"></i> Sovereign Real Estate</span>
            <h2 class="ct-title">Global Executive Headquarters &amp; <span class="ct-title-gradient">Embassy Directory</span></h2>
            <p class="ct-subtitle">
              Our flagship executive headquarters and international liaison offices operate in primary financial epicenters with private meeting suites and sovereign boardroom suites.
            </p>
          </div>

          <div class="ct-embassy-grid">
            <!-- Left: Flagship New York HQ Pylon -->
            <div class="ct-hq-pylon-card framer-embassy-rise">
              <div class="ct-hq-img-box">
                <img src="images/contact_office_address.jpg" alt="Global Corporate Headquarters Glass Facade and Entrance Foyer" loading="lazy">
                <div class="ct-coordinates-tag">
                  <i class="fas fa-location-crosshairs" style="color: var(--ct-accent);"></i> 40.7580° N, 73.9855° W &bull; Manhattan HQ
                </div>
              </div>
              <div class="ct-hq-body">
                <div>
                  <h3 style="font-size: 1.5rem; font-weight: 800; color: var(--ct-text-main); margin-bottom: 0.5rem;">EventSphere Global Headquarters</h3>
                  <p style="font-size: 0.95rem; color: var(--ct-text-muted); line-height: 1.6;">
                    Rockefeller Center Executive Tower, 30 Rockefeller Plaza, 48th Floor, New York, NY 10112, United States.
                  </p>
                </div>

                <div class="ct-hq-specs-strip">
                  <div class="ct-hq-spec-item">
                    <span class="ct-hq-spec-lbl">VIP Ingress</span>
                    <span class="ct-hq-spec-val">Subterranean Porte-Cochère</span>
                  </div>
                  <div class="ct-hq-spec-item">
                    <span class="ct-hq-spec-lbl">Security Clearance</span>
                    <span class="ct-hq-spec-val">Biometric Keycard</span>
                  </div>
                  <div class="ct-hq-spec-item">
                    <span class="ct-hq-spec-lbl">Meeting Capacity</span>
                    <span class="ct-hq-spec-val">3 Executive Boardrooms</span>
                  </div>
                </div>

                <div style="display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;">
                  <button class="ct-btn ct-btn-primary" onclick="window.location.href='#enquiry-consultation'"><i class="fas fa-calendar-check"></i> Schedule In-Person Briefing</button>
                  <button class="ct-btn ct-btn-outline" onclick="window.location.href='#location-map'"><i class="fas fa-route"></i> Wayfinding Directions</button>
                </div>
              </div>
            </div>

            <!-- Right: 3 Global Regional Hubs Stack -->
            <div class="ct-regional-hubs-col">
              <div class="ct-hub-card framer-embassy-rise" onclick="selectHubLocation('London')">
                <div class="ct-hub-flag"><i class="fas fa-landmark"></i></div>
                <div class="ct-hub-info">
                  <div class="ct-hub-city">London Mayfair Regional Hub</div>
                  <div class="ct-hub-address">
                    14 Curzon Street, Mayfair, London W1J 7TX, United Kingdom.<br>
                    <span style="font-size: 0.8rem; color: var(--ct-accent);">Direct Liaison: +44 20 7946 0920</span>
                  </div>
                </div>
              </div>

              <div class="ct-hub-card framer-embassy-rise" onclick="selectHubLocation('Singapore')">
                <div class="ct-hub-flag"><i class="fas fa-city"></i></div>
                <div class="ct-hub-info">
                  <div class="ct-hub-city">Singapore Marina Bay Financial Hub</div>
                  <div class="ct-hub-address">
                    10 Marina Boulevard, Tower 2, Level 38, Singapore 018983.<br>
                    <span style="font-size: 0.8rem; color: var(--ct-accent);">Direct Liaison: +65 6789 0123</span>
                  </div>
                </div>
              </div>

              <div class="ct-hub-card framer-embassy-rise" onclick="selectHubLocation('Zurich')">
                <div class="ct-hub-flag"><i class="fas fa-mountain"></i></div>
                <div class="ct-hub-info">
                  <div class="ct-hub-city">Zurich Paradeplatz Alpine Hub</div>
                  <div class="ct-hub-address">
                    Poststrasse 9, 8001 Zürich, Switzerland.<br>
                    <span style="font-size: 0.8rem; color: var(--ct-accent);">Direct Liaison: +41 44 215 8800</span>
                  </div>
                </div>
              </div>

              <div style="background: var(--ct-surface); border: 1px dashed var(--ct-accent); border-radius: 1rem; padding: 1.15rem; display: flex; align-items: center; gap: 0.85rem;" class="framer-embassy-rise">
                <i class="fas fa-id-badge" style="color: var(--ct-accent); font-size: 1.35rem;"></i>
                <div style="font-size: 0.84rem; color: var(--ct-text-muted); line-height: 1.45;">
                  <strong style="color: var(--ct-text-main);">Visitor Protocol:</strong> Advance appointment registration required for building biometric guest passes.
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 2: PHONE NUMBER & DIRECT TELEPHONY DESK -->
      <section id="phone-telephony" class="ct-section-telephony">
        <div class="ct-container">
          <div class="ct-section-head framer-telephony-snap">
            <span class="ct-badge"><i class="fas fa-phone"></i> Voice Operations</span>
            <h2 class="ct-title">Direct Telephony Desk &amp; <span class="ct-title-gradient">Switchboard Routing</span></h2>
            <p class="ct-subtitle">
              High-availability VoIP telecommunications routing calls directly to senior project directors without call center queues or automated Interactive Voice Response delays.
            </p>
          </div>

          <div class="ct-telephony-layout">
            <!-- Left: Operations Media Card -->
            <div class="ct-telephony-media-card framer-telephony-snap">
              <div class="ct-telephony-img-box">
                <img src="images/contact_phone_telephony.jpg" alt="Dedicated Executive Communications Telephony Desk and Headset" loading="lazy">
                <div class="ct-audio-waveform-hud">
                  <div>
                    <span class="ct-live-pulse-dot"></span>
                    <span style="font-size: 0.82rem; font-weight: 800; text-transform: uppercase;">PBX Active: Low Latency Opus Audio</span>
                  </div>
                  <span style="font-size: 0.75rem; color: #cbd5e1; font-family: monospace;">SIP Trunk 12/12 Live</span>
                </div>
              </div>
              <div class="ct-telephony-body">
                <div>
                  <h3 style="font-size: 1.35rem; font-weight: 800; color: var(--ct-text-main); margin-bottom: 0.5rem;">Executive Telephony Architecture</h3>
                  <p style="font-size: 0.9rem; color: var(--ct-text-muted); line-height: 1.5;">
                    Every incoming call routes directly to assigned project managers. Encrypted voice lines available upon client request.
                  </p>
                </div>

                <div style="background: var(--ct-surface-muted); border: 1px solid var(--ct-card-border); border-radius: 1rem; padding: 1.25rem;">
                  <div style="font-size: 0.82rem; color: var(--ct-text-muted); text-transform: uppercase; font-weight: 700;">Global Toll-Free Priority Line</div>
                  <a href="tel:+18005557864" style="font-size: 1.65rem; font-weight: 900; color: var(--ct-accent); text-decoration: none; font-family: monospace; display: block; margin-top: 0.25rem;">+1 (800) 555-SUMMIT</a>
                  <div style="font-size: 0.78rem; color: var(--ct-text-light); margin-top: 0.35rem;">Freecall from USA, Canada, UK, and Western Europe</div>
                </div>

                <div>
                  <button class="ct-btn ct-btn-outline" style="width: 100%;" onclick="alert('Downloading Executive Digital vCard (VCF format)...');">
                    <i class="fas fa-address-card"></i> Add EventSphere to Contacts (vCard)
                  </button>
                </div>
              </div>
            </div>

            <!-- Right: 4 Departmental Dialing Pods -->
            <div class="ct-pbx-grid framer-telephony-snap">
              <div class="ct-pbx-card">
                <span class="ct-pbx-badge"><i class="fas fa-tv"></i> Production</span>
                <div class="ct-pbx-dept">Executive Plenary &amp; Staging</div>
                <div style="font-size: 0.82rem; color: var(--ct-text-muted);">Keynote rigging, 8K MicroLED, and broadcast lines.</div>
                <a href="tel:+12125550190" class="ct-pbx-number"><i class="fas fa-phone-alt"></i> +1 (212) 555-0190</a>
                <span style="font-size: 0.75rem; color: var(--ct-text-light);">Direct Ext: 101 &bull; 08:00 – 20:00 EST</span>
              </div>

              <div class="ct-pbx-card">
                <span class="ct-pbx-badge"><i class="fas fa-newspaper"></i> Media</span>
                <div class="ct-pbx-dept">Press &amp; Media Credentials</div>
                <div style="font-size: 0.82rem; color: var(--ct-text-muted);">Journalist clearance, broadcast risers, and media kits.</div>
                <a href="tel:+12125550194" class="ct-pbx-number"><i class="fas fa-phone-alt"></i> +1 (212) 555-0194</a>
                <span style="font-size: 0.75rem; color: var(--ct-text-light);">Direct Ext: 104 &bull; 08:00 – 18:00 EST</span>
              </div>

              <div class="ct-pbx-card">
                <span class="ct-pbx-badge"><i class="fas fa-handshake"></i> Procurement</span>
                <div class="ct-pbx-dept">Supplier Master Agreements</div>
                <div style="font-size: 0.82rem; color: var(--ct-text-muted);">Vendor accreditation, COI verification, and contracting.</div>
                <a href="tel:+12125550198" class="ct-pbx-number"><i class="fas fa-phone-alt"></i> +1 (212) 555-0198</a>
                <span style="font-size: 0.75rem; color: var(--ct-text-light);">Direct Ext: 108 &bull; 09:00 – 17:00 EST</span>
              </div>

              <div class="ct-pbx-card">
                <span class="ct-pbx-badge"><i class="fas fa-scale-balanced"></i> Legal &amp; NDAs</span>
                <div class="ct-pbx-dept">Executive Legal Counsel</div>
                <div style="font-size: 0.82rem; color: var(--ct-text-muted);">Bilateral non-disclosure agreements &amp; compliance.</div>
                <a href="tel:+12125550199" class="ct-pbx-number"><i class="fas fa-phone-alt"></i> +1 (212) 555-0199</a>
                <span style="font-size: 0.75rem; color: var(--ct-text-light);">Direct Ext: 110 &bull; 09:00 – 17:00 EST</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 3: BUSINESS EMAIL & ENCRYPTED DISPATCH GATEWAY -->
      <section id="business-email" class="ct-section-email">
        <div class="ct-container">
          <div class="ct-section-head framer-pgp-decrypt">
            <span class="ct-badge"><i class="fas fa-envelope-open-text"></i> Encrypted Mailroom</span>
            <h2 class="ct-title">Corporate Correspondence &amp; <span class="ct-title-gradient">Business Email Gateway</span></h2>
            <p class="ct-subtitle">
              Encrypted messaging channels monitored by dedicated client liaisons with verified 2-hour Service Level Agreement response times during standard business hours.
            </p>
          </div>

          <div class="ct-email-gateway-grid">
            <!-- Left: Cryptographic Security Card -->
            <div class="ct-pgp-vault-card framer-pgp-decrypt">
              <div class="ct-pgp-img-box">
                <img src="images/contact_business_email.jpg" alt="Encrypted Corporate Communications and Digital Tablet" loading="lazy">
                <div style="position: absolute; top: 1.25rem; left: 1.25rem; background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(8px); padding: 0.5rem 1rem; border-radius: 0.75rem; color: #10b981; font-size: 0.82rem; font-weight: 700;">
                  <i class="fas fa-shield-halved"></i> TLS 1.3 &bull; 4096-Bit PGP Key Active
                </div>
              </div>
              <div class="ct-pgp-body">
                <div>
                  <h3 style="font-size: 1.35rem; font-weight: 800; color: var(--ct-text-main); margin-bottom: 0.5rem;">Sovereign Confidentiality</h3>
                  <p style="font-size: 0.9rem; color: var(--ct-text-muted); line-height: 1.5;">
                    For confidential corporate briefings, earnings releases, or M&amp;A summit proposals, please encrypt communications with our public PGP key:
                  </p>
                </div>

                <div class="ct-fingerprint-box">
                  <strong>PGP FINGERPRINT:</strong><br>
                  B4C8 920A 11DF 34EE 87B1 502C 9A4D E33F 7102 99BA
                </div>

                <div>
                  <button class="ct-btn ct-btn-outline" style="width: 100%;" onclick="alert('Downloading EventSphere Public PGP Key (.asc)...');">
                    <i class="fas fa-key"></i> Download Official PGP Public Key
                  </button>
                </div>
              </div>
            </div>

            <!-- Right: 4 Departmental Inboxes Stack -->
            <div class="ct-inbox-stack framer-pgp-decrypt">
              <div class="ct-inbox-row">
                <div class="ct-inbox-dept-info">
                  <span class="ct-inbox-title"><i class="fas fa-file-contract" style="color: var(--ct-accent);"></i> RFPs &amp; Event Proposals</span>
                  <span class="ct-inbox-addr">rfp@corporateevents.com</span>
                  <span style="font-size: 0.78rem; color: var(--ct-text-muted);">SLA: Guaranteed response under 2 business hours</span>
                </div>
                <button class="ct-copy-btn" onclick="copyEmailToClipboard('rfp@corporateevents.com', this)"><i class="fas fa-copy"></i> Copy Email</button>
              </div>

              <div class="ct-inbox-row">
                <div class="ct-inbox-dept-info">
                  <span class="ct-inbox-title"><i class="fas fa-user-tie" style="color: var(--ct-accent);"></i> Executive Advisory &amp; Steering</span>
                  <span class="ct-inbox-addr">executive@corporateevents.com</span>
                  <span style="font-size: 0.78rem; color: var(--ct-text-muted);">Direct line to Managing Partners and Strategy Leads</span>
                </div>
                <button class="ct-copy-btn" onclick="copyEmailToClipboard('executive@corporateevents.com', this)"><i class="fas fa-copy"></i> Copy Email</button>
              </div>

              <div class="ct-inbox-row">
                <div class="ct-inbox-dept-info">
                  <span class="ct-inbox-title"><i class="fas fa-dolly" style="color: var(--ct-accent);"></i> Vendor Partnerships &amp; Procurement</span>
                  <span class="ct-inbox-addr">procurement@corporateevents.com</span>
                  <span style="font-size: 0.78rem; color: var(--ct-text-muted);">Supplier accreditation, bidding submissions, and MSAs</span>
                </div>
                <button class="ct-copy-btn" onclick="copyEmailToClipboard('procurement@corporateevents.com', this)"><i class="fas fa-copy"></i> Copy Email</button>
              </div>

              <div class="ct-inbox-row">
                <div class="ct-inbox-dept-info">
                  <span class="ct-inbox-title"><i class="fas fa-gavel" style="color: var(--ct-accent);"></i> Legal, Risk &amp; Non-Disclosure</span>
                  <span class="ct-inbox-addr">legal@corporateevents.com</span>
                  <span style="font-size: 0.78rem; color: var(--ct-text-muted);">Contract revisions, compliance, insurance COIs</span>
                </div>
                <button class="ct-copy-btn" onclick="copyEmailToClipboard('legal@corporateevents.com', this)"><i class="fas fa-copy"></i> Copy Email</button>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 4: OFFICE HOURS & 24/7 TIMEZONE OPERATIONS -->
      <section id="office-hours" class="ct-section-hours">
        <div class="ct-container">
          <div class="ct-section-head framer-chronometer-spin">
            <span class="ct-badge"><i class="fas fa-clock"></i> Global Chronometer</span>
            <h2 class="ct-title">Global Concierge Operations &amp; <span class="ct-title-gradient">Office Hours</span></h2>
            <p class="ct-subtitle">
              Continuous multinational coverage synchronized across major financial markets. Live operating status updated in real time.
            </p>
          </div>

          <div class="ct-hours-board-layout">
            <!-- Left: World Clocks Interactive Deck -->
            <div class="ct-world-clocks-deck framer-chronometer-spin">
              <div>
                <span class="ct-badge"><i class="fas fa-earth-americas"></i> Continuous Operational Matrix</span>
                <h3 style="font-size: 1.45rem; font-weight: 800; color: var(--ct-text-main); margin-bottom: 0.5rem;">Live Regional Operating Telemetry</h3>
                <p style="font-size: 0.9rem; color: var(--ct-text-muted); line-height: 1.5;">
                  Local time clocks updated dynamically with current office availability status:
                </p>
              </div>

              <div class="ct-clocks-grid">
                <div class="ct-clock-tile">
                  <div class="ct-clock-city">New York (EST / UTC-5)</div>
                  <div class="ct-clock-time" id="clockNYC">--:--:--</div>
                  <div class="ct-clock-status"><span class="ct-live-pulse-dot"></span> Office Open &bull; Full Staff</div>
                </div>

                <div class="ct-clock-tile">
                  <div class="ct-clock-city">London (GMT / UTC+0)</div>
                  <div class="ct-clock-time" id="clockLON">--:--:--</div>
                  <div class="ct-clock-status"><span class="ct-live-pulse-dot"></span> Office Open &bull; Full Staff</div>
                </div>

                <div class="ct-clock-tile">
                  <div class="ct-clock-city">Singapore (SGT / UTC+8)</div>
                  <div class="ct-clock-time" id="clockSGP">--:--:--</div>
                  <div class="ct-clock-status"><span class="ct-live-pulse-dot"></span> Office Open &bull; Active Shift</div>
                </div>

                <div class="ct-clock-tile">
                  <div class="ct-clock-city">Zurich (CET / UTC+1)</div>
                  <div class="ct-clock-time" id="clockZUR">--:--:--</div>
                  <div class="ct-clock-status"><span class="ct-live-pulse-dot"></span> Office Open &bull; Active Shift</div>
                </div>
              </div>

              <div style="font-size: 0.85rem; color: var(--ct-text-muted); line-height: 1.5; border-top: 1px solid var(--ct-card-border); padding-top: 1.25rem;">
                <i class="fas fa-info-circle" style="color: var(--ct-accent);"></i> On-site production command bunkers operate <strong>24/7 uninterrupted</strong> during live conference execution weeks.
              </div>
            </div>

            <!-- Right: Standard Operating Schedule Table -->
            <div class="ct-schedule-card framer-chronometer-spin">
              <div class="ct-schedule-img-box">
                <img src="images/contact_office_hours.jpg" alt="Corporate Reception Atrium and Executive Meeting Suite" loading="lazy">
                <div style="position: absolute; bottom: 1.25rem; left: 1.25rem; background: rgba(15, 23, 42, 0.88); backdrop-filter: blur(8px); padding: 0.5rem 1rem; border-radius: 0.75rem; color: #ffffff; font-size: 0.82rem; font-weight: 700;">
                  <i class="fas fa-door-open" style="color: #10b981;"></i> Concierge Reception Foyer
                </div>
              </div>

              <div class="ct-schedule-body">
                <div>
                  <h4 style="font-size: 1.2rem; font-weight: 800; color: var(--ct-text-main); margin-bottom: 0.5rem;">Headquarters Standard Schedule</h4>
                  <div class="ct-timetable-list">
                    <div class="ct-timetable-item">
                      <span class="ct-day-label">Monday – Thursday:</span>
                      <span class="ct-hours-val">07:30 – 21:00 EST</span>
                    </div>
                    <div class="ct-timetable-item">
                      <span class="ct-day-label">Friday:</span>
                      <span class="ct-hours-val">07:30 – 19:30 EST</span>
                    </div>
                    <div class="ct-timetable-item">
                      <span class="ct-day-label">Saturday (Rehearsals):</span>
                      <span class="ct-hours-val">09:00 – 17:00 EST</span>
                    </div>
                    <div class="ct-timetable-item">
                      <span class="ct-day-label">Sunday &amp; Global Holidays:</span>
                      <span class="ct-hours-val">24/7 Crisis Dispatch Only</span>
                    </div>
                  </div>
                </div>

                <div>
                  <button class="ct-btn ct-btn-outline" style="width: 100%;" onclick="window.location.href='#emergency-support'">
                    <i class="fas fa-shield-alt"></i> Access 24/7 Crisis Standby
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 5: LOCATION MAP & GEOSPATIAL INGRESS DECK -->
      <section id="location-map" class="ct-section-map">
        <div class="ct-container">
          <div class="ct-section-head framer-wayfinding-zoom">
            <span class="ct-badge"><i class="fas fa-map-location-dot"></i> Geospatial Navigation</span>
            <h2 class="ct-title">Interactive Geospatial Map &amp; <span class="ct-title-gradient">Transit Ingress</span></h2>
            <p class="ct-subtitle">
              Seamless executive arrival logistics. Multi-modal arrival coordinates for motorcades, direct airport helicopters, and commercial rail links.
            </p>
          </div>

          <div class="ct-map-terminal-wrap framer-wayfinding-zoom">
            <!-- Map Hero Visual -->
            <div class="ct-map-hero-frame">
              <img src="images/contact_location_map.jpg" alt="Interactive Geospatial Digital Navigation Map Interface" loading="lazy">
              <div class="ct-map-pins-hud">
                <div>
                  <span style="font-size: 0.78rem; text-transform: uppercase; font-weight: 800; color: #fbbf24; letter-spacing: 0.05em;">Manhattan Geofence Active</span>
                  <div style="font-size: 1.35rem; font-weight: 900; margin-top: 0.2rem;">Rockefeller Plaza Executive Drop-Off Zone</div>
                </div>
                <div style="display: flex; gap: 1rem;">
                  <button class="ct-btn ct-btn-primary" style="padding: 0.6rem 1.25rem; font-size: 0.88rem;" onclick="alert('Opening Google Maps coordinates in new tab: 40.7580, -73.9855...');">
                    <i class="fas fa-arrow-up-right-from-square"></i> Open Google Maps
                  </button>
                </div>
              </div>
            </div>

            <!-- 3 Ingress Modes Grid -->
            <div class="ct-ingress-tabs-grid">
              <div class="ct-ingress-card">
                <div class="ct-ingress-icon"><i class="fas fa-helicopter"></i></div>
                <div class="ct-ingress-title">Aviation &amp; Helipad Transfer</div>
                <div class="ct-ingress-desc">
                  Direct connection via HeliNY Downtown Manhattan Heliport (JRB) or West 30th St Heliport (JRA). 6-minute executive transfer to HQ lobby.
                </div>
              </div>

              <div class="ct-ingress-card">
                <div class="ct-ingress-icon"><i class="fas fa-car-side"></i></div>
                <div class="ct-ingress-title">Subterranean VIP Motorcade</div>
                <div class="ct-ingress-desc">
                  Private below-grade vehicle concourse entrance off West 49th Street with high-security motorized bollards and armored vehicle clearance.
                </div>
              </div>

              <div class="ct-ingress-card">
                <div class="ct-ingress-icon"><i class="fas fa-train-subway"></i></div>
                <div class="ct-ingress-title">Executive Rail &amp; Transit Ingress</div>
                <div class="ct-ingress-desc">
                  Direct underground weather-protected pedestrian concourse connecting to B, D, F, M trains and 10-minute chauffeured link to Grand Central Terminal.
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 6: GENERAL ENQUIRY FORM & CORPORATE CONSULTATION REQUEST -->
      <section id="enquiry-consultation" class="ct-section-forms">
        <div class="ct-container">
          <div class="ct-section-head framer-forge-expand">
            <span class="ct-badge"><i class="fas fa-file-pen"></i> Communications Foundry</span>
            <h2 class="ct-title">Corporate Consultation &amp; <span class="ct-title-gradient">General Enquiry Forge</span></h2>
            <p class="ct-subtitle">
              Whether requesting a comprehensive conference proposal or submitting a general inquiry, select your inquiry track below to initiate immediate dialogue with our production directors.
            </p>
          </div>

          <div class="ct-forms-forge-layout">
            <!-- Left: Sidebar Visual & Commitment -->
            <div class="ct-forge-sidebar-card framer-forge-expand">
              <div class="ct-forge-img-box">
                <img src="images/contact_consultation_form.jpg" alt="Executive Event Consultation Table with Floorplans and Tablet" loading="lazy">
                <div style="position: absolute; top: 1.25rem; left: 1.25rem; background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(8px); padding: 0.5rem 1rem; border-radius: 0.75rem; color: #ffffff; font-size: 0.82rem; font-weight: 700;">
                  <i class="fas fa-lock" style="color: #10b981;"></i> ISO 27001 Certified Confidentiality
                </div>
              </div>

              <div class="ct-forge-sidebar-body">
                <div>
                  <h3 style="font-size: 1.35rem; font-weight: 800; color: var(--ct-text-main); margin-bottom: 0.5rem;">The EventSphere Guarantee</h3>
                  <p style="font-size: 0.9rem; color: var(--ct-text-muted); line-height: 1.5;">
                    Every consultation request is assigned directly to a Senior Vice President of Production. We prepare comprehensive preliminary feasibility studies within 48 business hours.
                  </p>
                </div>

                <div style="background: var(--ct-surface-muted); padding: 1.25rem; border-radius: 1rem; border: 1px solid var(--ct-card-border); font-size: 0.85rem; color: var(--ct-text-muted); line-height: 1.6;">
                  <div><strong style="color: var(--ct-text-main);"><i class="fas fa-check-circle" style="color: var(--ct-accent);"></i> Comprehensive NDA:</strong> Signed prior to initial call</div>
                  <div style="margin-top: 0.35rem;"><strong style="color: var(--ct-text-main);"><i class="fas fa-check-circle" style="color: var(--ct-accent);"></i> Feasibility Study:</strong> Venue capacity &amp; AV budget model</div>
                  <div style="margin-top: 0.35rem;"><strong style="color: var(--ct-text-main);"><i class="fas fa-check-circle" style="color: var(--ct-accent);"></i> No Commitment:</strong> Complimentary strategic advisory</div>
                </div>

                <div>
                  <a href="#emergency-support" class="ct-btn ct-btn-outline" style="width: 100%;">
                    <i class="fas fa-triangle-exclamation" style="color: #ef4444;"></i> Need Immediate Crisis Response?
                  </a>
                </div>
              </div>
            </div>

            <!-- Right: Interactive Dual-Track Form -->
            <div class="ct-form-card framer-forge-expand">
              <!-- Mode Switcher -->
              <div class="ct-form-tab-switcher">
                <button type="button" class="ct-tab-btn active" id="tabConsultation" onclick="switchFormMode('consultation')">
                  <i class="fas fa-handshake"></i> Corporate Consultation Request
                </button>
                <button type="button" class="ct-tab-btn" id="tabGeneral" onclick="switchFormMode('general')">
                  <i class="fas fa-envelope"></i> General Enquiry Form
                </button>
              </div>

              <form id="contactMainForm" onsubmit="handleContactFormSubmit(event)">
                <div class="ct-input-row">
                  <div class="ct-input-group">
                    <label class="ct-input-label">Executive Full Name *</label>
                    <input type="text" class="ct-input-field" placeholder="e.g. Julian Rivera" required>
                  </div>
                  <div class="ct-input-group">
                    <label class="ct-input-label">Corporate Email Address *</label>
                    <input type="email" class="ct-input-field" placeholder="e.g. jrivera@enterprise.com" required>
                  </div>
                </div>

                <div class="ct-input-row" style="margin-top: 1.25rem;">
                  <div class="ct-input-group">
                    <label class="ct-input-label">Company / Organization *</label>
                    <input type="text" class="ct-input-field" placeholder="e.g. Vanguard Dynamics Ltd." required>
                  </div>
                  <div class="ct-input-group">
                    <label class="ct-input-label">Direct Phone Number *</label>
                    <input type="tel" class="ct-input-field" placeholder="+1 (555) 019-4820" required>
                  </div>
                </div>

                <!-- Dynamic Fields: Consultation Track -->
                <div id="consultationFields" style="margin-top: 1.25rem;">
                  <div class="ct-input-row">
                    <div class="ct-input-group">
                      <label class="ct-input-label">Target Delegate Volume</label>
                      <select class="ct-select-field">
                        <option value="300-1000">300 – 1,000 Delegates (Executive Summit)</option>
                        <option value="1000-5000" selected>1,000 – 5,000 Delegates (Major Congress)</option>
                        <option value="5000+">5,000+ Delegates (Global Plenary Expo)</option>
                      </select>
                    </div>
                    <div class="ct-input-group">
                      <label class="ct-input-label">Estimated CapEx Budget Range ($ USD)</label>
                      <select class="ct-select-field">
                        <option value="250k-500k">$250,000 – $500,000</option>
                        <option value="500k-1.5m" selected>$500,000 – $1,500,000</option>
                        <option value="1.5m-5m">$1,500,000 – $5,000,000</option>
                        <option value="5m+">$5,000,000+</option>
                      </select>
                    </div>
                  </div>
                </div>

                <!-- Message Field -->
                <div class="ct-input-group" style="margin-top: 1.25rem;">
                  <label class="ct-input-label" id="messageFieldLabel">Project Scope &amp; Strategic Objectives *</label>
                  <textarea class="ct-textarea-field" rows="4" placeholder="Detail your target summit dates, preferred cities, technical AV ambitions, or specific inquiry..." required></textarea>
                </div>

                <div style="margin-top: 1.75rem;">
                  <button type="submit" class="ct-btn ct-btn-primary" style="width: 100%; font-size: 1.05rem; padding: 1rem 2rem;">
                    <i class="fas fa-paper-plane"></i> Submit Official Communications Dossier
                  </button>
                  <div style="text-align: center; font-size: 0.78rem; color: var(--ct-text-muted); margin-top: 0.75rem;">
                    <i class="fas fa-shield-alt" style="color: #10b981;"></i> Protected by enterprise-grade SSL encryption and mutual non-disclosure covenants.
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 7: EMERGENCY EVENT SUPPORT CONTACT & 24/7 COMMAND BUNKER -->
      <section id="emergency-support" class="ct-section-emergency">
        <div class="ct-container">
          <div class="ct-section-head framer-bunker-pulse">
            <span class="ct-badge ct-badge-danger"><i class="fas fa-triangle-exclamation"></i> Mission-Critical Continuity</span>
            <h2 class="ct-title">Rapid Emergency Event Support &amp; <span class="ct-title-danger">Command Bunker</span></h2>
            <p class="ct-subtitle">
              Active conference underway? Unexpected power interruption, key speaker cancellation, or urgent production failure? Our emergency crisis team deploys with a guaranteed 15-minute response SLA.
            </p>
          </div>

          <div class="ct-emergency-bunker-card framer-bunker-pulse">
            <!-- Left: High-Tech Control Room Visual -->
            <div class="ct-emergency-img-box">
              <img src="images/contact_emergency_support.jpg" alt="High-Tech Logistics and Emergency Operation Control Center" loading="lazy">
              <div class="ct-crisis-status-overlay">
                <span style="width: 10px; height: 10px; border-radius: 50%; background: #ef4444; box-shadow: 0 0 10px #ef4444; display: inline-block;"></span>
                COMMAND BUNKER STANDBY: 15-MIN SLA ACTIVE
              </div>
            </div>

            <!-- Right: Crisis Protocols & Rapid Line -->
            <div class="ct-emergency-content">
              <div>
                <span class="ct-badge ct-badge-danger"><i class="fas fa-bolt"></i> 24/7 Incident Dispatch</span>
                <h3 style="font-size: 1.6rem; font-weight: 800; color: var(--ct-text-main); margin-bottom: 0.75rem;">Immediate Conference Intervention</h3>
                <p style="font-size: 0.95rem; color: var(--ct-text-muted); line-height: 1.6;">
                  For on-site event directors experiencing critical live emergencies. We maintain hot-standby generator assets, redundant touring sound consoles, and satellite broadcast relays ready for immediate deployment.
                </p>
              </div>

              <div class="ct-crisis-protocols-list">
                <div class="ct-crisis-protocol-item">
                  <i class="fas fa-plug-circle-bolt"></i>
                  <div><strong>Sub-Second Power &amp; Signal Transfer:</strong> Immediate activation of dual-redundant Caterpillar 2MW mobile generators and UPS buffers.</div>
                </div>
                <div class="ct-crisis-protocol-item">
                  <i class="fas fa-satellite"></i>
                  <div><strong>Emergency Broadcast Reroute:</strong> Instant failover to bonded Starlink &amp; Teradek satellite uplinks within 90 seconds.</div>
                </div>
                <div class="ct-crisis-protocol-item">
                  <i class="fas fa-shield-virus"></i>
                  <div><strong>Force Majeure &amp; Medical Evacuation:</strong> Direct coordination with private trauma aviation and municipal security liaisons.</div>
                </div>
              </div>

              <!-- Prominent Emergency Hotline Banner -->
              <div class="ct-hotline-dial-banner">
                <div>
                  <div style="font-size: 0.75rem; text-transform: uppercase; font-weight: 800; color: #ef4444; letter-spacing: 0.05em;">24/7 CRISIS DISPATCH HOTLINE</div>
                  <a href="tel:+18889113836" style="font-size: 1.75rem; font-weight: 900; color: #dc2626; font-family: monospace; text-decoration: none; display: block; margin-top: 0.25rem;">+1 (888) 911-EVENT</a>
                </div>
                <button class="ct-btn ct-btn-danger" onclick="alert('CONNECTING TO 24/7 EMERGENCY CRISIS DISPATCH COMMANDER...');">
                  <i class="fas fa-phone-volume"></i> Priority Dispatch Call
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SUCCESS MODAL POPUP -->
      <div class="ct-modal-backdrop" id="contactSuccessModal">
        <div class="ct-modal-box">
          <div class="ct-modal-icon">
            <i class="fas fa-check"></i>
          </div>
          <h3 style="font-size: 1.65rem; font-weight: 800; color: var(--ct-text-main); margin-bottom: 0.5rem;">Communications Dossier Dispatched!</h3>
          <p style="font-size: 0.95rem; color: var(--ct-text-muted); line-height: 1.6; margin-bottom: 1.75rem;">
            Your inquiry has been encrypted and routed to our Senior Vice President of Production. Reference Tracking Code: <strong id="trackingRefCode" style="color: var(--ct-accent); font-family: monospace;">INQ-2026-7842</strong>. Our team will initiate dialogue within 2 business hours.
          </p>
          <button class="ct-btn ct-btn-primary" onclick="closeContactModal()" style="width: 100%;">
            <i class="fas fa-arrow-left"></i> Return to Directory
          </button>
        </div>
      </div>

    </main>
    """

    # Page Interactive Scripts
    contact_scripts = """
  <!-- =====================================================================
       INTERACTIVE CLIENT CONTROLS & FRAMER MOTION OBSERVERS
       ===================================================================== -->
  <script>
    // 1. Framer Motion Scroll Trigger Observers
    document.addEventListener('DOMContentLoaded', function () {
      var motionClasses = [
        '.framer-embassy-rise',
        '.framer-telephony-snap',
        '.framer-pgp-decrypt',
        '.framer-chronometer-spin',
        '.framer-wayfinding-zoom',
        '.framer-forge-expand',
        '.framer-bunker-pulse'
      ];

      var motionObserver = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('framer-in-view');
            var children = entry.target.querySelectorAll('.framer-embassy-rise, .framer-telephony-snap, .framer-pgp-decrypt, .framer-chronometer-spin, .framer-wayfinding-zoom, .framer-forge-expand, .framer-bunker-pulse');
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

    // 3. Hub Selector Interaction
    function selectHubLocation(cityName) {
      alert('Selected ' + cityName + ' Regional Hub. Dialing direct local liaison desk...');
    }

    // 4. Copy Email to Clipboard
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

    // 5. Dual-Track Form Switcher
    function switchFormMode(mode) {
      var tabConsult = document.getElementById('tabConsultation');
      var tabGen = document.getElementById('tabGeneral');
      var consultFields = document.getElementById('consultationFields');
      var msgLabel = document.getElementById('messageFieldLabel');

      if (mode === 'consultation') {
        if (tabConsult) tabConsult.classList.add('active');
        if (tabGen) tabGen.classList.remove('active');
        if (consultFields) consultFields.style.display = 'block';
        if (msgLabel) msgLabel.textContent = 'Project Scope & Strategic Objectives *';
      } else {
        if (tabGen) tabGen.classList.add('active');
        if (tabConsult) tabConsult.classList.remove('active');
        if (consultFields) consultFields.style.display = 'none';
        if (msgLabel) msgLabel.textContent = 'General Inquiry & Subject Details *';
      }
    }

    // 6. Form Submission & Modal Feedback
    function handleContactFormSubmit(e) {
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
      var form = document.getElementById('contactMainForm');
      if (form) form.reset();
    }
  </script>
"""

    # Assemble complete document
    final_html = (
        nav_head_up_to_style
        + contact_css
        + "\n  </style>"
        + nav_mid[len("</style>"):]
        + contact_html_content
        + footer_full
        + contact_scripts
        + closing_part
    )

    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print("Successfully built contact.html! Total length:", len(final_html))

if __name__ == '__main__':
    build_contact_html()
