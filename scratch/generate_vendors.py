import os

def build_vendors_html():
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

    script_close = nav_text.rfind('  </script>')
    if script_close == -1:
        raise Exception("Could not find </script> in navbar.html")

    footer_part = nav_text[footer_pos:script_close]
    closing_part = nav_text[script_close:]

    # CSS for vendors.html
    vendors_css = """
    /* =====================================================================
       VENDORS & SUPPLIERS DIRECTORY - CUSTOM PAGE STYLES
       Supports Light Mode, Dark Mode (body.dark), and RTL (body.rtl)
       ===================================================================== */
    :root {
      --vn-primary: #1e3a8a;
      --vn-primary-dark: #0f172a;
      --vn-accent: #d97706;
      --vn-accent-light: #fbbf24;
      --vn-accent-glow: rgba(217, 119, 6, 0.18);
      --vn-bg: #f8fafc;
      --vn-surface: #ffffff;
      --vn-surface-muted: #f1f5f9;
      --vn-card-border: #e2e8f0;
      --vn-text-main: #0f172a;
      --vn-text-muted: #64748b;
      --vn-text-light: #94a3b8;
      --vn-gold-gradient: linear-gradient(135deg, #b45309 0%, #d97706 50%, #f59e0b 100%);
      --vn-blue-gradient: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      --vn-shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --vn-shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.07), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
      --vn-shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      --vn-shadow-glow: 0 0 25px rgba(217, 119, 6, 0.25);
    }

    body.dark {
      --vn-bg: #070b14;
      --vn-surface: #0f172a;
      --vn-surface-muted: #131d33;
      --vn-card-border: #1e293b;
      --vn-text-main: #f8fafc;
      --vn-text-muted: #94a3b8;
      --vn-text-light: #64748b;
      --vn-blue-gradient: linear-gradient(135deg, #070b14 0%, #172554 100%);
    }

    /* RTL Support */
    body.rtl .vn-section-head { text-align: right; }
    body.rtl .vn-badge i { margin-left: 0.5rem; margin-right: 0; }
    body.rtl .vn-btn i { margin-right: 0.5rem; margin-left: 0; }

    /* Base Reset for Vendors Container */
    .vn-page-wrap {
      background-color: var(--vn-bg);
      color: var(--vn-text-main);
      font-family: 'Inter', system-ui, sans-serif;
      overflow-x: hidden;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    .vn-container {
      max-width: 1320px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }

    /* SECTION HEADER STYLING */
    .vn-section-head {
      margin-bottom: 3.5rem;
      position: relative;
    }

    .vn-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.45rem 1.1rem;
      border-radius: 9999px;
      background: var(--vn-accent-glow);
      border: 1px solid rgba(217, 119, 6, 0.35);
      color: var(--vn-accent);
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      margin-bottom: 1rem;
    }

    .vn-title {
      font-size: clamp(2rem, 3.5vw, 2.75rem);
      font-weight: 800;
      line-height: 1.18;
      color: var(--vn-text-main);
      letter-spacing: -0.025em;
      margin-bottom: 1rem;
    }

    .vn-title-gradient {
      background: var(--vn-gold-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .vn-subtitle {
      font-size: 1.1rem;
      color: var(--vn-text-muted);
      line-height: 1.65;
      max-width: 760px;
    }

    /* HERO JUMP NAV STRIP */
    .vn-hero-strip {
      background: var(--vn-surface);
      border-bottom: 1px solid var(--vn-card-border);
      padding: 2.5rem 0 2rem;
      position: relative;
    }
    .vn-hero-content {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 1.25rem;
    }
    .vn-hero-title {
      font-size: clamp(2.2rem, 4vw, 3.25rem);
      font-weight: 900;
      color: var(--vn-text-main);
      letter-spacing: -0.03em;
    }
    .vn-hero-desc {
      font-size: 1.15rem;
      color: var(--vn-text-muted);
      max-width: 820px;
      line-height: 1.65;
    }
    .vn-nav-pills {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.65rem;
      margin-top: 1rem;
    }
    .vn-nav-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.55rem 1.15rem;
      border-radius: 9999px;
      background: var(--vn-surface-muted);
      border: 1px solid var(--vn-card-border);
      color: var(--vn-text-main);
      font-size: 0.88rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
    }
    .vn-nav-pill:hover {
      background: var(--vn-accent);
      color: #ffffff;
      border-color: var(--vn-accent);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(217, 119, 6, 0.25);
    }
    .vn-nav-pill i {
      color: var(--vn-accent);
      transition: color 0.3s ease;
    }
    .vn-nav-pill:hover i {
      color: #ffffff;
    }

    /* GLOBAL BUTTONS */
    .vn-btn {
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
    .vn-btn-primary {
      background: var(--vn-gold-gradient);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(217, 119, 6, 0.3);
    }
    .vn-btn-primary:hover {
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 8px 24px rgba(217, 119, 6, 0.45);
      color: #ffffff;
    }
    .vn-btn-outline {
      background: transparent;
      color: var(--vn-text-main);
      border: 1.5px solid var(--vn-card-border);
    }
    .vn-btn-outline:hover {
      background: var(--vn-surface-muted);
      border-color: var(--vn-accent);
      color: var(--vn-accent);
      transform: translateY(-2px);
    }

    /* =====================================================================
       FRAMER MOTION OBSERVER SYSTEM (7 DISTINCT SECTION ANIMATIONS)
       ===================================================================== */
    /* Section 1: Colonnade 3D Perspective Reveal */
    .framer-colonnade-reveal {
      opacity: 0;
      transform: perspective(1200px) rotateX(12deg) translateY(45px);
      transition: opacity 0.85s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1);
      will-change: transform, opacity;
    }
    .framer-colonnade-reveal.framer-in-view {
      opacity: 1;
      transform: perspective(1200px) rotateX(0deg) translateY(0);
    }

    /* Section 2: Hardware Dial Lateral Elastic Snap */
    .framer-hardware-dial {
      opacity: 0;
      transform: skewX(-3deg) translateX(-50px);
      transition: opacity 0.75s cubic-bezier(0.175, 0.885, 0.32, 1.275), transform 0.75s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      will-change: transform, opacity;
    }
    .framer-hardware-dial.framer-in-view {
      opacity: 1;
      transform: skewX(0deg) translateX(0);
    }

    /* Section 3: Culinary Pendulum Soft Float */
    .framer-culinary-float {
      opacity: 0;
      transform: rotate(-3deg) translateY(40px) scale(0.96);
      transition: opacity 0.9s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.9s cubic-bezier(0.34, 1.56, 0.64, 1);
      will-change: transform, opacity;
    }
    .framer-culinary-float.framer-in-view {
      opacity: 1;
      transform: rotate(0deg) translateY(0) scale(1);
    }

    /* Section 4: Scenic Assemble Construct */
    .framer-scenic-construct {
      opacity: 0;
      transform: translate(35px, 35px) rotate(2deg);
      transition: opacity 0.8s cubic-bezier(0.25, 1, 0.5, 1), transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);
      will-change: transform, opacity;
    }
    .framer-scenic-construct.framer-in-view {
      opacity: 1;
      transform: translate(0, 0) rotate(0deg);
    }

    /* Section 5: Transit Aerodynamic Velocity Glide */
    .framer-transit-glide {
      opacity: 0;
      transform: translateX(65px);
      filter: blur(5px);
      transition: opacity 0.75s cubic-bezier(0.25, 1, 0.5, 1), transform 0.75s cubic-bezier(0.25, 1, 0.5, 1), filter 0.75s ease;
      will-change: transform, opacity, filter;
    }
    .framer-transit-glide.framer-in-view {
      opacity: 1;
      transform: translateX(0);
      filter: blur(0);
    }

    /* Section 6: Compliance Stamp-Down Effect */
    .framer-compliance-stamp {
      opacity: 0;
      transform: scale(1.08) translateY(-30px);
      transition: opacity 0.65s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.65s cubic-bezier(0.34, 1.56, 0.64, 1);
      will-change: transform, opacity;
    }
    .framer-compliance-stamp.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    /* Section 7: Portal Shutter Unlock Expansion */
    .framer-portal-unlock {
      opacity: 0;
      transform: scale(0.92) translateY(35px);
      transition: opacity 0.85s cubic-bezier(0.16, 1, 0.3, 1), transform 0.85s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform, opacity;
    }
    .framer-portal-unlock.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    /* =====================================================================
       SECTION 1: VENUE PARTNERS - DUAL-TIER COLONNADE & CAPACITY MATRIX
       ===================================================================== */
    .vn-section-venues {
      padding: 6.5rem 0;
      position: relative;
    }
    .vn-colonnade-layout {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 2.5rem;
      align-items: stretch;
    }
    .vn-venue-spotlight {
      background: var(--vn-surface);
      border: 1px solid var(--vn-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--vn-shadow-lg);
      transition: transform 0.4s ease, border-color 0.4s ease;
    }
    .vn-venue-spotlight:hover {
      border-color: rgba(217, 119, 6, 0.5);
      transform: translateY(-4px);
    }
    .vn-spotlight-visual {
      position: relative;
      height: 380px;
      overflow: hidden;
    }
    .vn-spotlight-visual img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.7s cubic-bezier(0.2, 0.8, 0.2, 1);
    }
    .vn-venue-spotlight:hover .vn-spotlight-visual img {
      transform: scale(1.04);
    }
    .vn-visual-overlay-tag {
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
      letter-spacing: 0.04em;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    body.rtl .vn-visual-overlay-tag {
      left: auto;
      right: 1.25rem;
    }
    .vn-visual-overlay-tag span.live-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 8px #10b981;
      display: inline-block;
    }
    .vn-spotlight-details {
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
      justify-content: space-between;
    }
    .vn-venue-specs-row {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
      padding: 1.25rem 0;
      margin: 1.25rem 0;
      border-top: 1px solid var(--vn-card-border);
      border-bottom: 1px solid var(--vn-card-border);
    }
    .vn-spec-item {
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }
    .vn-spec-label {
      font-size: 0.78rem;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--vn-text-light);
      letter-spacing: 0.05em;
    }
    .vn-spec-val {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--vn-text-main);
    }

    /* Right Colonnade Cards */
    .vn-colonnade-cards {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      justify-content: space-between;
    }
    .vn-colonnade-pod {
      background: var(--vn-surface);
      border: 1px solid var(--vn-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      box-shadow: var(--vn-shadow-sm);
      cursor: pointer;
      position: relative;
      transition: all 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
    }
    .vn-colonnade-pod.active,
    .vn-colonnade-pod:hover {
      border-color: var(--vn-accent);
      background: var(--vn-surface-muted);
      transform: translateX(6px);
      box-shadow: var(--vn-shadow-md);
    }
    body.rtl .vn-colonnade-pod.active,
    body.rtl .vn-colonnade-pod:hover {
      transform: translateX(-6px);
    }
    .vn-pod-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .vn-pod-icon-title {
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }
    .vn-pod-icon {
      width: 42px;
      height: 42px;
      border-radius: 0.75rem;
      background: var(--vn-accent-glow);
      color: var(--vn-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
    }
    .vn-pod-title {
      font-size: 1.08rem;
      font-weight: 800;
      color: var(--vn-text-main);
    }
    .vn-pod-badge {
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.3rem 0.75rem;
      border-radius: 9999px;
      background: var(--vn-card-border);
      color: var(--vn-text-muted);
    }
    .vn-pod-bar-wrap {
      margin-top: 0.25rem;
    }
    .vn-pod-bar-bg {
      height: 6px;
      background: var(--vn-card-border);
      border-radius: 3px;
      overflow: hidden;
    }
    .vn-pod-bar-fill {
      height: 100%;
      background: var(--vn-gold-gradient);
      border-radius: 3px;
      transition: width 0.8s ease;
    }

    /* =====================================================================
       SECTION 2: AUDIO-VISUAL SUPPLIERS - RACKMOUNT CONSOLE & CTS DIALS
       ===================================================================== */
    .vn-section-audiovisual {
      padding: 6.5rem 0;
      background: var(--vn-surface-muted);
      border-top: 1px solid var(--vn-card-border);
      border-bottom: 1px solid var(--vn-card-border);
      position: relative;
    }
    .vn-hardware-console {
      background: var(--vn-surface);
      border: 1px solid var(--vn-card-border);
      border-radius: 1.75rem;
      padding: 2.5rem;
      box-shadow: var(--vn-shadow-lg);
    }
    .vn-console-top-strip {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1.5rem;
      padding-bottom: 2rem;
      border-bottom: 1px solid var(--vn-card-border);
      margin-bottom: 2.25rem;
    }
    .vn-switch-group {
      display: flex;
      gap: 0.5rem;
      background: var(--vn-surface-muted);
      padding: 0.35rem;
      border-radius: 0.85rem;
      border: 1px solid var(--vn-card-border);
    }
    .vn-switch-btn {
      padding: 0.6rem 1.25rem;
      border-radius: 0.6rem;
      font-size: 0.88rem;
      font-weight: 700;
      border: none;
      cursor: pointer;
      background: transparent;
      color: var(--vn-text-muted);
      transition: all 0.3s ease;
    }
    .vn-switch-btn.active {
      background: var(--vn-surface);
      color: var(--vn-accent);
      box-shadow: var(--vn-shadow-sm);
    }
    .vn-console-body-grid {
      display: grid;
      grid-template-columns: 1fr 1.1fr;
      gap: 2.5rem;
      align-items: center;
    }
    .vn-console-feed-card {
      position: relative;
      border-radius: 1.25rem;
      overflow: hidden;
      border: 1px solid var(--vn-card-border);
      height: 420px;
    }
    .vn-console-feed-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .vn-feed-telemetry-hud {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(0deg, rgba(7, 11, 20, 0.95) 0%, rgba(7, 11, 20, 0.4) 70%, transparent 100%);
      padding: 1.5rem;
      color: #ffffff;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.75rem;
    }
    .vn-telemetry-item {
      display: flex;
      flex-direction: column;
    }
    .vn-telemetry-num {
      font-family: monospace;
      font-size: 1.25rem;
      font-weight: 800;
      color: #38bdf8;
    }
    .vn-telemetry-title {
      font-size: 0.72rem;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .vn-rack-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.25rem;
    }
    .vn-rack-slot {
      background: var(--vn-surface-muted);
      border: 1px solid var(--vn-card-border);
      border-radius: 1rem;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .vn-rack-slot:hover {
      border-color: var(--vn-accent);
      transform: translateY(-3px);
    }
    .vn-slot-badge {
      font-size: 0.72rem;
      font-weight: 800;
      padding: 0.2rem 0.6rem;
      border-radius: 0.4rem;
      background: var(--vn-surface);
      color: var(--vn-text-muted);
      align-self: flex-start;
      border: 1px solid var(--vn-card-border);
    }
    .vn-slot-title {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--vn-text-main);
    }
    .vn-slot-desc {
      font-size: 0.88rem;
      color: var(--vn-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 3: CATERING PARTNERS - MICHELIN GOURMET TASTING PAVILION
       ===================================================================== */
    .vn-section-catering {
      padding: 6.5rem 0;
      position: relative;
    }
    .vn-catering-split {
      display: grid;
      grid-template-columns: 1fr 1.2fr;
      gap: 3rem;
      align-items: center;
    }
    .vn-culinary-hero-card {
      position: relative;
      border-radius: 1.75rem;
      overflow: hidden;
      border: 1px solid var(--vn-card-border);
      box-shadow: var(--vn-shadow-lg);
      height: 480px;
    }
    .vn-culinary-hero-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .vn-chef-badge-floating {
      position: absolute;
      top: 1.5rem;
      right: 1.5rem;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(12px);
      padding: 0.75rem 1.25rem;
      border-radius: 1rem;
      border: 1px solid rgba(217, 119, 6, 0.4);
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    body.rtl .vn-chef-badge-floating {
      right: auto;
      left: 1.5rem;
    }
    .vn-chef-badge-floating i {
      color: var(--vn-accent);
      font-size: 1.2rem;
    }
    .vn-throughput-ticker {
      position: absolute;
      bottom: 1.5rem;
      left: 1.5rem;
      right: 1.5rem;
      background: rgba(15, 23, 42, 0.92);
      backdrop-filter: blur(10px);
      border-radius: 1rem;
      padding: 1.25rem 1.5rem;
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .vn-flight-cards {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }
    .vn-flight-pod {
      background: var(--vn-surface);
      border: 1px solid var(--vn-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      gap: 1.25rem;
      align-items: flex-start;
      box-shadow: var(--vn-shadow-sm);
      transition: all 0.3s ease;
    }
    .vn-flight-pod:hover {
      border-color: var(--vn-accent);
      transform: translateY(-3px);
      box-shadow: var(--vn-shadow-md);
    }
    .vn-flight-emblem {
      width: 48px;
      height: 48px;
      border-radius: 1rem;
      background: var(--vn-gold-gradient);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.25rem;
      flex-shrink: 0;
      box-shadow: 0 4px 10px rgba(217, 119, 6, 0.3);
    }
    .vn-flight-info {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }
    .vn-flight-title {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--vn-text-main);
    }
    .vn-flight-menu {
      font-size: 0.9rem;
      color: var(--vn-text-muted);
      line-height: 1.5;
    }
    .vn-dietary-strip {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-top: 0.75rem;
    }
    .vn-dietary-tag {
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      background: var(--vn-surface-muted);
      border: 1px solid var(--vn-card-border);
      color: var(--vn-accent);
    }

    /* =====================================================================
       SECTION 4: PRODUCTION TEAMS - KINETIC SCENIC TRUSS & MATERIAL ATELIER
       ===================================================================== */
    .vn-section-production {
      padding: 6.5rem 0;
      background: var(--vn-surface-muted);
      border-top: 1px solid var(--vn-card-border);
      border-bottom: 1px solid var(--vn-card-border);
      position: relative;
    }
    .vn-production-pillars-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.75rem;
      margin-bottom: 3.5rem;
    }
    .vn-pillar-card {
      background: var(--vn-surface);
      border: 1px solid var(--vn-card-border);
      border-radius: 1.5rem;
      padding: 2rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      box-shadow: var(--vn-shadow-sm);
      transition: all 0.35s ease;
    }
    .vn-pillar-card:hover {
      border-color: var(--vn-accent);
      transform: translateY(-5px);
      box-shadow: var(--vn-shadow-lg);
    }
    .vn-pillar-icon {
      width: 52px;
      height: 52px;
      border-radius: 1.15rem;
      background: var(--vn-accent-glow);
      color: var(--vn-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.35rem;
    }
    .vn-pillar-title {
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--vn-text-main);
    }
    .vn-pillar-desc {
      font-size: 0.92rem;
      color: var(--vn-text-muted);
      line-height: 1.6;
    }
    .vn-production-swatch-split {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.5rem;
      align-items: center;
      background: var(--vn-surface);
      border: 1px solid var(--vn-card-border);
      border-radius: 1.75rem;
      padding: 2.5rem;
      box-shadow: var(--vn-shadow-md);
    }
    .vn-atelier-img-box {
      border-radius: 1.25rem;
      overflow: hidden;
      height: 380px;
      position: relative;
      border: 1px solid var(--vn-card-border);
    }
    .vn-atelier-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .vn-swatch-picker-box {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }
    .vn-swatch-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1rem;
    }
    .vn-swatch-card {
      background: var(--vn-surface-muted);
      border: 1px solid var(--vn-card-border);
      border-radius: 1rem;
      padding: 1.25rem;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      transition: all 0.3s ease;
    }
    .vn-swatch-card.active,
    .vn-swatch-card:hover {
      border-color: var(--vn-accent);
      background: var(--vn-surface);
      box-shadow: var(--vn-shadow-sm);
    }
    .vn-swatch-bullet {
      width: 14px;
      height: 14px;
      border-radius: 50%;
      display: inline-block;
      margin-right: 0.5rem;
    }
    body.rtl .vn-swatch-bullet {
      margin-right: 0;
      margin-left: 0.5rem;
    }
    .vn-swatch-name {
      font-size: 0.95rem;
      font-weight: 800;
      color: var(--vn-text-main);
      display: flex;
      align-items: center;
    }
    .vn-swatch-detail {
      font-size: 0.82rem;
      color: var(--vn-text-muted);
      line-height: 1.4;
    }

    /* =====================================================================
       SECTION 5: TRANSPORT PROVIDERS - VIP FLEET INGRESS & MANIFEST GRID
       ===================================================================== */
    .vn-section-transport {
      padding: 6.5rem 0;
      position: relative;
    }
    .vn-transport-filter-strip {
      display: flex;
      gap: 0.65rem;
      flex-wrap: wrap;
      margin-bottom: 2.5rem;
    }
    .vn-transport-filter-btn {
      padding: 0.55rem 1.25rem;
      border-radius: 9999px;
      border: 1.5px solid var(--vn-card-border);
      background: var(--vn-surface);
      color: var(--vn-text-muted);
      font-size: 0.88rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.3s ease;
    }
    .vn-transport-filter-btn.active,
    .vn-transport-filter-btn:hover {
      background: var(--vn-primary);
      border-color: var(--vn-primary);
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(30, 58, 138, 0.25);
    }
    .vn-fleet-manifest-layout {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 2.5rem;
      align-items: stretch;
    }
    .vn-fleet-hero-deck {
      position: relative;
      border-radius: 1.75rem;
      overflow: hidden;
      border: 1px solid var(--vn-card-border);
      box-shadow: var(--vn-shadow-lg);
      min-height: 440px;
    }
    .vn-fleet-hero-deck img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .vn-tarmac-manifest-overlay {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(0deg, rgba(15, 23, 42, 0.95) 0%, rgba(15, 23, 42, 0.4) 65%, transparent 100%);
      padding: 2rem;
      color: #ffffff;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    .vn-tarmac-metrics-row {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
      border-top: 1px solid rgba(255, 255, 255, 0.15);
      padding-top: 1rem;
    }
    .vn-fleet-cards-col {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      justify-content: space-between;
    }
    .vn-fleet-pod {
      background: var(--vn-surface);
      border: 1px solid var(--vn-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      box-shadow: var(--vn-shadow-sm);
      transition: all 0.3s ease;
    }
    .vn-fleet-pod:hover {
      border-color: var(--vn-accent);
      transform: translateX(-4px);
      box-shadow: var(--vn-shadow-md);
    }
    body.rtl .vn-fleet-pod:hover {
      transform: translateX(4px);
    }
    .vn-fleet-pod-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .vn-fleet-pod-title {
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--vn-text-main);
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }
    .vn-fleet-pod-title i {
      color: var(--vn-accent);
    }
    .vn-fleet-badge {
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      background: var(--vn-surface-muted);
      color: var(--vn-text-muted);
      border: 1px solid var(--vn-card-border);
    }
    .vn-fleet-desc {
      font-size: 0.88rem;
      color: var(--vn-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 6: VENDOR PARTNERSHIP ENQUIRY - 140-POINT STANDARDS GATE
       ===================================================================== */
    .vn-section-enquiry {
      padding: 6.5rem 0;
      background: var(--vn-surface-muted);
      border-top: 1px solid var(--vn-card-border);
      border-bottom: 1px solid var(--vn-card-border);
      position: relative;
    }
    .vn-enquiry-layout {
      display: grid;
      grid-template-columns: 1fr 1.15fr;
      gap: 3rem;
      align-items: stretch;
    }
    .vn-enquiry-card-dossier {
      background: var(--vn-surface);
      border: 1px solid var(--vn-card-border);
      border-radius: 1.75rem;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--vn-shadow-lg);
    }
    .vn-enquiry-visual {
      position: relative;
      height: 280px;
    }
    .vn-enquiry-visual img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .vn-enquiry-body {
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      flex-grow: 1;
      justify-content: space-between;
    }
    .vn-tier-pill-list {
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }
    .vn-tier-pill-item {
      display: flex;
      align-items: flex-start;
      gap: 0.85rem;
      background: var(--vn-surface-muted);
      padding: 1rem;
      border-radius: 0.85rem;
      border: 1px solid var(--vn-card-border);
    }
    .vn-tier-icon {
      font-size: 1.1rem;
      color: var(--vn-accent);
      margin-top: 0.2rem;
    }

    /* Interactive Auditor Gate Tool */
    .vn-auditor-gate-panel {
      background: var(--vn-surface);
      border: 1px solid var(--vn-card-border);
      border-radius: 1.75rem;
      padding: 2.5rem;
      box-shadow: var(--vn-shadow-lg);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .vn-score-dial-wrap {
      background: var(--vn-surface-muted);
      border: 1px solid var(--vn-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem;
      margin-bottom: 1.75rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .vn-score-readout {
      display: flex;
      align-items: baseline;
      gap: 0.35rem;
    }
    .vn-score-number {
      font-size: 2.75rem;
      font-weight: 900;
      color: var(--vn-accent);
      line-height: 1;
    }
    .vn-score-max {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--vn-text-light);
    }
    .vn-score-status-badge {
      padding: 0.4rem 1rem;
      border-radius: 9999px;
      background: #10b981;
      color: #ffffff;
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }
    .vn-checklist-group {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin-bottom: 2rem;
    }
    .vn-check-item {
      display: flex;
      align-items: center;
      gap: 0.85rem;
      cursor: pointer;
      user-select: none;
    }
    .vn-check-item input[type="checkbox"] {
      width: 20px;
      height: 20px;
      accent-color: var(--vn-accent);
      cursor: pointer;
    }
    .vn-check-label {
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--vn-text-main);
    }

    /* =====================================================================
       SECTION 7: VENDOR REGISTRATION - SUPPLIER TERMINAL & DOCUMENT VAULT
       ===================================================================== */
    .vn-section-registration {
      padding: 6.5rem 0 8rem;
      position: relative;
    }
    .vn-reg-portal-grid {
      display: grid;
      grid-template-columns: 0.9fr 1.1fr;
      gap: 3rem;
      align-items: stretch;
    }
    .vn-portal-info-card {
      background: var(--vn-surface);
      border: 1px solid var(--vn-card-border);
      border-radius: 1.75rem;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--vn-shadow-lg);
    }
    .vn-portal-hero-img {
      position: relative;
      height: 290px;
    }
    .vn-portal-hero-img img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .vn-portal-steps-box {
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      flex-grow: 1;
      justify-content: space-between;
    }
    .vn-process-stepper {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }
    .vn-stepper-row {
      display: flex;
      align-items: flex-start;
      gap: 1rem;
    }
    .vn-stepper-num {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: var(--vn-gold-gradient);
      color: #ffffff;
      font-weight: 800;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .vn-stepper-content {
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
    }
    .vn-stepper-title {
      font-size: 0.98rem;
      font-weight: 700;
      color: var(--vn-text-main);
    }
    .vn-stepper-desc {
      font-size: 0.85rem;
      color: var(--vn-text-muted);
      line-height: 1.45;
    }

    /* Terminal Form */
    .vn-reg-form-card {
      background: var(--vn-surface);
      border: 1px solid var(--vn-card-border);
      border-radius: 1.75rem;
      padding: 2.5rem;
      box-shadow: var(--vn-shadow-lg);
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }
    .vn-form-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
    }
    .vn-form-group {
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
    }
    .vn-form-label {
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--vn-text-main);
    }
    .vn-form-input,
    .vn-form-select,
    .vn-form-textarea {
      width: 100%;
      padding: 0.85rem 1.15rem;
      border-radius: 0.75rem;
      border: 1px solid var(--vn-card-border);
      background: var(--vn-surface-muted);
      color: var(--vn-text-main);
      font-family: inherit;
      font-size: 0.95rem;
      outline: none;
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .vn-form-input:focus,
    .vn-form-select:focus,
    .vn-form-textarea:focus {
      border-color: var(--vn-accent);
      box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.15);
      background: var(--vn-surface);
    }
    .vn-vault-dropzone {
      border: 2px dashed var(--vn-card-border);
      border-radius: 1rem;
      padding: 2rem 1.5rem;
      text-align: center;
      background: var(--vn-surface-muted);
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.65rem;
      transition: all 0.3s ease;
    }
    .vn-vault-dropzone:hover,
    .vn-vault-dropzone.drag-over {
      border-color: var(--vn-accent);
      background: var(--vn-surface);
      box-shadow: var(--vn-shadow-sm);
    }
    .vn-vault-dropzone i {
      font-size: 2rem;
      color: var(--vn-accent);
    }

    /* SUBMISSION MODAL FEEDBACK */
    .vn-modal-backdrop {
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
    .vn-modal-box {
      background: var(--vn-surface);
      border: 1px solid var(--vn-card-border);
      border-radius: 1.75rem;
      max-width: 540px;
      width: 100%;
      padding: 2.75rem 2.25rem;
      text-align: center;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.35);
      position: relative;
      animation: vnModalPop 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    @keyframes vnModalPop {
      0% { transform: scale(0.85); opacity: 0; }
      100% { transform: scale(1); opacity: 1; }
    }
    .vn-modal-icon {
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
      .vn-colonnade-layout,
      .vn-console-body-grid,
      .vn-catering-split,
      .vn-production-swatch-split,
      .vn-fleet-manifest-layout,
      .vn-enquiry-layout,
      .vn-reg-portal-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
      }
      .vn-production-pillars-grid {
        grid-template-columns: 1fr;
      }
      .vn-spotlight-visual,
      .vn-console-feed-card,
      .vn-culinary-hero-card,
      .vn-fleet-hero-deck {
        height: 320px;
      }
    }
    @media (max-width: 640px) {
      .vn-form-row {
        grid-template-columns: 1fr;
      }
      .vn-rack-grid,
      .vn-swatch-grid {
        grid-template-columns: 1fr;
      }
      .vn-venue-specs-row,
      .vn-feed-telemetry-hud,
      .vn-tarmac-metrics-row {
        grid-template-columns: 1fr;
        gap: 0.5rem;
      }
    }
    """

    # HTML Body Content for the 7 Sections
    vendors_html_content = """
    <!-- =====================================================================
         MAIN CONTENT: 7 UNIQUE VENDOR & SUPPLIER SECTIONS
         ===================================================================== -->
    <main class="vn-page-wrap">

      <!-- SUB-HERO / STRATEGIC ECOSYSTEM HEADER STRIP -->
      <section class="vn-hero-strip">
        <div class="vn-container">
          <div class="vn-hero-content">
            <span class="vn-badge"><i class="fas fa-handshake"></i> Verified Supplier Network</span>
            <h1 class="vn-hero-title">Premier Global Event Vendor Directory</h1>
            <p class="vn-hero-desc">
              Direct master service agreements with world-class venue owners, touring-grade audiovisual engineers, Michelin culinary guilds, scenic fabrication ateliers, and sovereign VIP mobility providers.
            </p>
            <div class="vn-nav-pills">
              <a href="#venue-partners" class="vn-nav-pill"><i class="fas fa-hotel"></i> Venue Partners</a>
              <a href="#audiovisual-suppliers" class="vn-nav-pill"><i class="fas fa-tv"></i> Audio-Visual</a>
              <a href="#catering-partners" class="vn-nav-pill"><i class="fas fa-utensils"></i> Haute Catering</a>
              <a href="#production-teams" class="vn-nav-pill"><i class="fas fa-hammer"></i> Production & Staging</a>
              <a href="#transport-providers" class="vn-nav-pill"><i class="fas fa-car"></i> VIP Transport</a>
              <a href="#partnership-enquiry" class="vn-nav-pill"><i class="fas fa-clipboard-check"></i> Standards Audit</a>
              <a href="#vendor-registration" class="vn-nav-pill"><i class="fas fa-id-card"></i> Vendor Registration</a>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 1: VENUE PARTNERS -->
      <section id="venue-partners" class="vn-section-venues">
        <div class="vn-container">
          <div class="vn-section-head framer-colonnade-reveal">
            <span class="vn-badge"><i class="fas fa-hotel"></i> Destination & Estate Infrastructure</span>
            <h2 class="vn-title">Architectural Colonnade &amp; <span class="vn-title-gradient">Capacity Band Matrix</span></h2>
            <p class="vn-subtitle">
              Sovereign partnerships with leading global convention palaces, waterfront amphitheaters, and private summit estates with pre-negotiated tier-1 load-in windows and fiber redundancy.
            </p>
          </div>

          <div class="vn-colonnade-layout">
            <!-- Left Col: Primary Spotlight Showcase -->
            <div class="vn-venue-spotlight framer-colonnade-reveal">
              <div class="vn-spotlight-visual">
                <img src="images/vendor_venues.jpg" alt="Premier Architectural Convention Palace and Venue Partner" loading="lazy">
                <div class="vn-visual-overlay-tag">
                  <span class="live-dot"></span> Tier-1 Global Convention Hub
                </div>
              </div>
              <div class="vn-spotlight-details">
                <div>
                  <h3 id="currentVenueTitle" style="font-size: 1.5rem; font-weight: 800; color: var(--vn-text-main); margin-bottom: 0.5rem;">The Grand Plenary Palace &amp; Exposition Atrium</h3>
                  <p id="currentVenueDesc" style="font-size: 0.95rem; color: var(--vn-text-muted); line-height: 1.6;">
                    Featuring clear-span columnless architecture, acoustic wall baffle treatments, and automated rigging trusses capable of hosting up to 12,500 delegates in full plenary configuration.
                  </p>
                </div>

                <div class="vn-venue-specs-row">
                  <div class="vn-spec-item">
                    <span class="vn-spec-label">Capacity Ceiling</span>
                    <span id="venueCapStat" class="vn-spec-val">12,500 Delegates</span>
                  </div>
                  <div class="vn-spec-item">
                    <span class="vn-spec-label">Acoustic Rating</span>
                    <span id="venueSoundStat" class="vn-spec-val">54 dB STC</span>
                  </div>
                  <div class="vn-spec-item">
                    <span class="vn-spec-label">Rigging Ceiling</span>
                    <span id="venueRigStat" class="vn-spec-val">120 Metric Tons</span>
                  </div>
                </div>

                <div style="display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;">
                  <button class="vn-btn vn-btn-primary" onclick="window.location.href='#vendor-registration'"><i class="fas fa-calendar-check"></i> Reserve Venue Date</button>
                  <button class="vn-btn vn-btn-outline" onclick="alert('Downloading 2026 Global Venue Floorplan Index (PDF)...');"><i class="fas fa-file-pdf"></i> Technical Tech Specs</button>
                </div>
              </div>
            </div>

            <!-- Right Col: Colonnade Tier Selector Cards -->
            <div class="vn-colonnade-cards">
              <div class="vn-colonnade-pod active framer-colonnade-reveal" onclick="selectVenueTier(0)">
                <div class="vn-pod-header">
                  <div class="vn-pod-icon-title">
                    <div class="vn-pod-icon"><i class="fas fa-city"></i></div>
                    <div>
                      <div class="vn-pod-title">Metropolitan Convention Palaces</div>
                      <div style="font-size: 0.82rem; color: var(--vn-text-muted);">Keynote plenaries &amp; international trade pavilions</div>
                    </div>
                  </div>
                  <span class="vn-pod-badge">5,000 – 15,000 Pax</span>
                </div>
                <div class="vn-pod-bar-wrap">
                  <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:var(--vn-text-muted); margin-bottom:0.25rem;">
                    <span>Floor Area Utilization</span>
                    <span>94% Available</span>
                  </div>
                  <div class="vn-pod-bar-bg"><div class="vn-pod-bar-fill" style="width: 94%;"></div></div>
                </div>
              </div>

              <div class="vn-colonnade-pod framer-colonnade-reveal" onclick="selectVenueTier(1)">
                <div class="vn-pod-header">
                  <div class="vn-pod-icon-title">
                    <div class="vn-pod-icon"><i class="fas fa-water"></i></div>
                    <div>
                      <div class="vn-pod-title">Waterfront Amphitheaters &amp; Atriums</div>
                      <div style="font-size: 0.82rem; color: var(--vn-text-muted);">Curved acoustic shells &amp; harbor terraces</div>
                    </div>
                  </div>
                  <span class="vn-pod-badge">1,500 – 4,500 Pax</span>
                </div>
                <div class="vn-pod-bar-wrap">
                  <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:var(--vn-text-muted); margin-bottom:0.25rem;">
                    <span>Panoramic Horizon Vistas</span>
                    <span>82% Available</span>
                  </div>
                  <div class="vn-pod-bar-bg"><div class="vn-pod-bar-fill" style="width: 82%;"></div></div>
                </div>
              </div>

              <div class="vn-colonnade-pod framer-colonnade-reveal" onclick="selectVenueTier(2)">
                <div class="vn-pod-header">
                  <div class="vn-pod-icon-title">
                    <div class="vn-pod-icon"><i class="fas fa-chess-rook"></i></div>
                    <div>
                      <div class="vn-pod-title">Heritage Palaces &amp; Mountain Retreats</div>
                      <div style="font-size: 0.82rem; color: var(--vn-text-muted);">Gilded sovereign ballrooms &amp; alpine sanctuaries</div>
                    </div>
                  </div>
                  <span class="vn-pod-badge">300 – 1,200 Pax</span>
                </div>
                <div class="vn-pod-bar-wrap">
                  <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:var(--vn-text-muted); margin-bottom:0.25rem;">
                    <span>Sovereign Security Perimeter</span>
                    <span>100% Certified</span>
                  </div>
                  <div class="vn-pod-bar-bg"><div class="vn-pod-bar-fill" style="width: 100%;"></div></div>
                </div>
              </div>

              <!-- Venue Partner Verification Strip -->
              <div style="background: var(--vn-surface); border: 1px dashed var(--vn-accent); border-radius: 1rem; padding: 1.15rem; display: flex; align-items: center; gap: 0.85rem;" class="framer-colonnade-reveal">
                <i class="fas fa-shield-alt" style="color: var(--vn-accent); font-size: 1.35rem;"></i>
                <div style="font-size: 0.84rem; color: var(--vn-text-muted); line-height: 1.45;">
                  <strong style="color: var(--vn-text-main);">Venue Partner Assurance:</strong> Every listed property maintains ISO 14001 green event credentials and 24/7 dedicated freight marshaling docks.
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 2: AUDIO-VISUAL SUPPLIERS -->
      <section id="audiovisual-suppliers" class="vn-section-audiovisual">
        <div class="vn-container">
          <div class="vn-section-head framer-hardware-dial">
            <span class="vn-badge"><i class="fas fa-tv"></i> Broadcast Engineering &amp; Acoustics</span>
            <h2 class="vn-title">Rackmount Hardware Console &amp; <span class="vn-title-gradient">CTS Telemetry Dials</span></h2>
            <p class="vn-subtitle">
              Touring-grade broadcast media servers, 0.9mm MicroLED displays, spatial beam-steered line arrays, and dual-redundant optical distribution nodes.
            </p>
          </div>

          <div class="vn-hardware-console framer-hardware-dial">
            <div class="vn-console-top-strip">
              <div style="display: flex; align-items: center; gap: 1rem;">
                <div style="width: 12px; height: 12px; border-radius: 50%; background: #10b981; box-shadow: 0 0 10px #10b981;"></div>
                <span style="font-size: 0.9rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; color: var(--vn-text-main);">CTS-D Network Active: 48 Channels Sync</span>
              </div>
              <div class="vn-switch-group">
                <button class="vn-switch-btn active" onclick="switchAVPreset(0, this)">Keynote Arena Rig</button>
                <button class="vn-switch-btn" onclick="switchAVPreset(1, this)">Distributed Exhibition</button>
                <button class="vn-switch-btn" onclick="switchAVPreset(2, this)">Live Global Simulcast</button>
              </div>
            </div>

            <div class="vn-console-body-grid">
              <!-- AV Hardware Visual Deck -->
              <div class="vn-console-feed-card">
                <img src="images/vendor_audiovisual.jpg" alt="Audiovisual Production Staging Console and LED Arrays" loading="lazy">
                <div class="vn-feed-telemetry-hud">
                  <div class="vn-telemetry-item">
                    <span id="avLatencyVal" class="vn-telemetry-num">1.2 ms</span>
                    <span class="vn-telemetry-title">Glass-to-Glass Latency</span>
                  </div>
                  <div class="vn-telemetry-item">
                    <span id="avRefreshVal" class="vn-telemetry-num">7,680 Hz</span>
                    <span class="vn-telemetry-title">LED Panel Refresh Rate</span>
                  </div>
                  <div class="vn-telemetry-item">
                    <span id="avUptimeVal" class="vn-telemetry-num">99.999%</span>
                    <span class="vn-telemetry-title">Signal Redundancy</span>
                  </div>
                </div>
              </div>

              <!-- 4 Modular Rack Pods -->
              <div class="vn-rack-grid">
                <div class="vn-rack-slot">
                  <span class="vn-slot-badge"><i class="fas fa-layer-group"></i> VIDEO DISPLAY</span>
                  <div class="vn-slot-title">8K Curved MicroLED Arrays</div>
                  <div class="vn-slot-desc">ROE Visual &amp; Unilumin Black Marble tiles, 0.9mm pixel pitch, HDR10+, 1,800 nits daylight luminance rating.</div>
                </div>

                <div class="vn-rack-slot">
                  <span class="vn-slot-badge"><i class="fas fa-headphones"></i> ACOUSTICS</span>
                  <div class="vn-slot-title">Meyer Sound PANTHER Arrays</div>
                  <div class="vn-slot-desc">Linear sound reinforcement with Dante digital backbone, laser-calibrated room acoustic equalization.</div>
                </div>

                <div class="vn-rack-slot">
                  <span class="vn-slot-badge"><i class="fas fa-server"></i> MEDIA SERVER</span>
                  <div class="vn-slot-title">disguise gx 3 &amp; d3 Servers</div>
                  <div class="vn-slot-desc">Real-time Unreal Engine 5.4 camera tracking, genlocked uncompressed 4K 60fps canvas outputs.</div>
                </div>

                <div class="vn-rack-slot">
                  <span class="vn-slot-badge"><i class="fas fa-network-wired"></i> POWER &amp; FIBER</span>
                  <div class="vn-slot-title">Optical LemO Tactical Rings</div>
                  <div class="vn-slot-desc">Redundant multi-core fiber run with dual 400A 3-phase camlok distribution and UPS battery bank buffers.</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 3: CATERING PARTNERS -->
      <section id="catering-partners" class="vn-section-catering">
        <div class="vn-container">
          <div class="vn-section-head framer-culinary-float">
            <span class="vn-badge"><i class="fas fa-utensils"></i> Haute Cuisine &amp; Sustainable Gastronomy</span>
            <h2 class="vn-title">Michelin Gastronomy Pavilion &amp; <span class="vn-title-gradient">Palette Carousel</span></h2>
            <p class="vn-subtitle">
              Precision banquet operations capable of plating 4,500 covers in 42 minutes with Michelin-starred craft, organic farm-to-table traceability, and zero food waste redistribution.
            </p>
          </div>

          <div class="vn-catering-split">
            <!-- Left: Hero Culinary Craft Visual -->
            <div class="vn-culinary-hero-card framer-culinary-float">
              <img src="images/vendor_catering.jpg" alt="Michelin Executive Chefs Plating Banquet Gastronomy" loading="lazy">
              <div class="vn-chef-badge-floating">
                <i class="fas fa-award"></i>
                <div>
                  <div style="font-weight: 800; font-size: 0.95rem;">Chef-Led Catering Guild</div>
                  <div style="font-size: 0.75rem; color: #cbd5e1;">Michelin &amp; James Beard Alumni</div>
                </div>
              </div>
              <div class="vn-throughput-ticker">
                <div>
                  <div style="font-size: 1.25rem; font-weight: 900; color: #fbbf24;">4,500 Plates / 42 Min</div>
                  <div style="font-size: 0.75rem; color: #94a3b8;">Simultaneous synchronized gala table service</div>
                </div>
                <div style="display: flex; gap: 0.5rem;">
                  <span style="background: rgba(16, 185, 129, 0.2); color: #10b981; font-size: 0.75rem; font-weight: 800; padding: 0.35rem 0.75rem; border-radius: 9999px;">0% Food Waste</span>
                </div>
              </div>
            </div>

            <!-- Right: Interactive Tasting Flights -->
            <div class="vn-flight-cards framer-culinary-float">
              <div class="vn-flight-pod">
                <div class="vn-flight-emblem"><i class="fas fa-wine-glass"></i></div>
                <div class="vn-flight-info">
                  <div class="vn-flight-title">Executive Plated Gala Dinner</div>
                  <div class="vn-flight-menu">
                    Pan-roasted Chilean sea bass with saffron emulsion, heirloom cauliflower velouté, gold leaf Valrhona chocolate dome with salted caramel pearls.
                  </div>
                  <div class="vn-dietary-strip">
                    <span class="vn-dietary-tag"><i class="fas fa-check"></i> Halal Certified</span>
                    <span class="vn-dietary-tag"><i class="fas fa-check"></i> Gluten-Free Atelier</span>
                    <span class="vn-dietary-tag"><i class="fas fa-check"></i> Sommelier Curated</span>
                  </div>
                </div>
              </div>

              <div class="vn-flight-pod">
                <div class="vn-flight-emblem"><i class="fas fa-cocktail"></i></div>
                <div class="vn-flight-info">
                  <div class="vn-flight-title">Cocktail &amp; Canapé Networking Atelier</div>
                  <div class="vn-flight-menu">
                    A5 Wagyu tataki crisp with yuzu kosho, nitro passionfruit spheres, hand-rolled blue lobster corncob tartlets, and botanical cold-brew aperitifs.
                  </div>
                  <div class="vn-dietary-strip">
                    <span class="vn-dietary-tag"><i class="fas fa-check"></i> Bite-Sized Precision</span>
                    <span class="vn-dietary-tag"><i class="fas fa-check"></i> Molecular Bar Station</span>
                  </div>
                </div>
              </div>

              <div class="vn-flight-pod">
                <div class="vn-flight-emblem"><i class="fas fa-seedling"></i></div>
                <div class="vn-flight-info">
                  <div class="vn-flight-title">Summit Day Nourishment &amp; Clean Energy</div>
                  <div class="vn-flight-menu">
                    Cold-pressed regenerative botanicals, micro-roasted single-origin espresso bars, adaptogenic brain-fuel smoothie bowls, and gluten-free pastries.
                  </div>
                  <div class="vn-dietary-strip">
                    <span class="vn-dietary-tag"><i class="fas fa-check"></i> 100% Plant-Based Options</span>
                    <span class="vn-dietary-tag"><i class="fas fa-check"></i> Carbon-Neutral Sourced</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 4: DECORATION & PRODUCTION TEAMS -->
      <section id="production-teams" class="vn-section-production">
        <div class="vn-container">
          <div class="vn-section-head framer-scenic-construct">
            <span class="vn-badge"><i class="fas fa-hammer"></i> Architectural Staging &amp; Custom Fabrication</span>
            <h2 class="vn-title">Kinetic Scenic Truss &amp; <span class="vn-title-gradient">Material Swatchboard</span></h2>
            <p class="vn-subtitle">
              From high-capacity automated motion hoists and curved architectural millwork to fire-rated tactile acoustic finishes engineered for live broadcast.
            </p>
          </div>

          <!-- Top 3 Competency Pillars -->
          <div class="vn-production-pillars-grid framer-scenic-construct">
            <div class="vn-pillar-card">
              <div class="vn-pillar-icon"><i class="fas fa-cubes"></i></div>
              <div class="vn-pillar-title">Structural Steel &amp; Kinetic Hoists</div>
              <div class="vn-pillar-desc">
                Computerized automated Kinesys chain hoists certified for 120 metric tons of load with real-time wireless load cell telemetry monitoring.
              </div>
            </div>

            <div class="vn-pillar-card">
              <div class="vn-pillar-icon"><i class="fas fa-drafting-compass"></i></div>
              <div class="vn-pillar-title">Custom Scenic Millwork</div>
              <div class="vn-pillar-desc">
                5-Axis CNC machined geometric timber stages, fire-retardant Class B1 architectural fabrics, and bespoke acoustic presenter lecterns.
              </div>
            </div>

            <div class="vn-pillar-card">
              <div class="vn-pillar-icon"><i class="fas fa-lightbulb"></i></div>
              <div class="vn-pillar-title">Volumetric Atmospheric Lighting</div>
              <div class="vn-pillar-desc">
                Martin MAC Ultra Performance moving heads, Ayrton Domino IP65 weather-rated profiles, and GrandMA3 lighting console choreography.
              </div>
            </div>
          </div>

          <!-- Bottom: Staging Atelier Visual & Material Swatch Selector -->
          <div class="vn-production-swatch-split framer-scenic-construct">
            <div class="vn-atelier-img-box">
              <img src="images/vendor_production.jpg" alt="Scenic Production Atelier and Kinetic Stage Truss Rigging" loading="lazy">
              <div style="position: absolute; top: 1.25rem; left: 1.25rem; background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(8px); padding: 0.5rem 1rem; border-radius: 0.75rem; color: #ffffff; font-size: 0.82rem; font-weight: 700; border: 1px solid rgba(255, 255, 255, 0.15);">
                <i class="fas fa-certificate" style="color: var(--vn-accent);"></i> Certified B1 Fire-Retardant Atelier
              </div>
            </div>

            <div class="vn-swatch-picker-box">
              <div>
                <span class="vn-badge"><i class="fas fa-palette"></i> Tactile Surface Library</span>
                <h3 style="font-size: 1.35rem; font-weight: 800; color: var(--vn-text-main); margin-bottom: 0.5rem;">Broadcast-Grade Finishes</h3>
                <p style="font-size: 0.9rem; color: var(--vn-text-muted); line-height: 1.5;">
                  Select material samples engineered to prevent camera moiré patterns and control acoustic slap-back reflections in cavernous halls:
                </p>
              </div>

              <div class="vn-swatch-grid">
                <div class="vn-swatch-card active" onclick="activateSwatch(this, 'Anti-Reflective Brushed Titanium: Zero glare under 2000W stage floodlights.')">
                  <div class="vn-swatch-name">
                    <span class="vn-swatch-bullet" style="background: #94a3b8;"></span> Brushed Titanium
                  </div>
                  <div class="vn-swatch-detail">Anti-reflective camera-grade satin metal</div>
                </div>

                <div class="vn-swatch-card" onclick="activateSwatch(this, 'Heritage Fluted Walnut: Sustainably grown FSC certified timber with acoustic fluting.')">
                  <div class="vn-swatch-name">
                    <span class="vn-swatch-bullet" style="background: #78350f;"></span> Fluted Walnut
                  </div>
                  <div class="vn-swatch-detail">Acoustic diffusion FSC certified timber</div>
                </div>

                <div class="vn-swatch-card" onclick="activateSwatch(this, 'Holographic Frosted Acrylic: High diffusion edge-lit stage archways.')">
                  <div class="vn-swatch-name">
                    <span class="vn-swatch-bullet" style="background: #38bdf8;"></span> Frosted Acrylic
                  </div>
                  <div class="vn-swatch-detail">Edge-lit volumetric light diffusion panels</div>
                </div>

                <div class="vn-swatch-card" onclick="activateSwatch(this, 'Acoustic Velvet Drape: 0.85 NRC noise reduction rating for crystal audio.')">
                  <div class="vn-swatch-name">
                    <span class="vn-swatch-bullet" style="background: #0f172a;"></span> Acoustic Velvet
                  </div>
                  <div class="vn-swatch-detail">0.85 NRC absorption heavy stage drape</div>
                </div>
              </div>

              <div id="swatchNote" style="background: var(--vn-surface-muted); padding: 0.85rem 1.15rem; border-radius: 0.75rem; border-left: 3px solid var(--vn-accent); font-size: 0.85rem; color: var(--vn-text-muted);">
                Anti-Reflective Brushed Titanium: Zero glare under 2000W stage floodlights.
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 5: TRANSPORT PROVIDERS -->
      <section id="transport-providers" class="vn-section-transport">
        <div class="vn-container">
          <div class="vn-section-head framer-transit-glide">
            <span class="vn-badge"><i class="fas fa-car"></i> Executive Mobility &amp; Aviation Logistics</span>
            <h2 class="vn-title">Executive VIP Fleet Ingress &amp; <span class="vn-title-gradient">Tarmac Manifest Grid</span></h2>
            <p class="vn-subtitle">
              Sovereign motorcade coordination, zero-emission luxury electric sedans, armored security escorts, and airside tarmac helicopter shuttles.
            </p>
          </div>

          <!-- Category Filter Bar -->
          <div class="vn-transport-filter-strip framer-transit-glide">
            <button class="vn-transport-filter-btn active" onclick="filterFleet('all', this)">All Fleet Categories</button>
            <button class="vn-transport-filter-btn" onclick="filterFleet('electric', this)">Zero-Emission Sedans</button>
            <button class="vn-transport-filter-btn" onclick="filterFleet('armored', this)">Armored Motorcades</button>
            <button class="vn-transport-filter-btn" onclick="filterFleet('coaches', this)">Executive Sprinters</button>
            <button class="vn-transport-filter-btn" onclick="filterFleet('aviation', this)">Airside Rotary Charter</button>
          </div>

          <div class="vn-fleet-manifest-layout">
            <!-- Left: Hero Fleet Image Deck -->
            <div class="vn-fleet-hero-deck framer-transit-glide">
              <img src="images/vendor_transport.jpg" alt="Executive VIP Chauffeur Fleet and Airport Tarmac Mobility" loading="lazy">
              <div class="vn-tarmac-manifest-overlay">
                <div>
                  <span style="font-size: 0.8rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em; color: #fbbf24;">Live Dispatch Protocol</span>
                  <div style="font-size: 1.45rem; font-weight: 900; margin-top: 0.25rem;">Airport Fast-Track &amp; VIP Green Lane Corridors</div>
                </div>

                <div class="vn-tarmac-metrics-row">
                  <div>
                    <div style="font-family: monospace; font-size: 1.25rem; font-weight: 800; color: #38bdf8;">100% Zero-Carbon</div>
                    <div style="font-size: 0.72rem; color: #cbd5e1; text-transform: uppercase;">Electric &amp; SAF Offsets</div>
                  </div>
                  <div>
                    <div style="font-family: monospace; font-size: 1.25rem; font-weight: 800; color: #10b981;">Sub-3 Min</div>
                    <div style="font-size: 0.72rem; color: #cbd5e1; text-transform: uppercase;">Tarmac Gate Ingress</div>
                  </div>
                  <div>
                    <div style="font-family: monospace; font-size: 1.25rem; font-weight: 800; color: #fbbf24;">24/7 Telemetry</div>
                    <div style="font-size: 0.72rem; color: #cbd5e1; text-transform: uppercase;">Satellite Vehicle Mesh</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Right: 4 Fleet Manifest Pods -->
            <div class="vn-fleet-cards-col framer-transit-glide">
              <div class="vn-fleet-pod" data-fleet="electric">
                <div class="vn-fleet-pod-head">
                  <div class="vn-fleet-pod-title"><i class="fas fa-bolt"></i> Lucid Air &amp; Maybach EQS</div>
                  <span class="vn-fleet-badge">Ultra-Luxury EV</span>
                </div>
                <div class="vn-fleet-desc">
                  Whisper-quiet electric drive, executive rear console with encrypted Wi-Fi 6E, ventilated reclining massage seating.
                </div>
              </div>

              <div class="vn-fleet-pod" data-fleet="armored">
                <div class="vn-fleet-pod-head">
                  <div class="vn-fleet-pod-title"><i class="fas fa-shield-alt"></i> B6/B7 Ballistic Motorcades</div>
                  <span class="vn-fleet-badge">Diplomatic Grade</span>
                </div>
                <div class="vn-fleet-desc">
                  Certified armor protection with law-enforcement liaison, defensive tactical driving teams, and satellite radio integration.
                </div>
              </div>

              <div class="vn-fleet-pod" data-fleet="coaches">
                <div class="vn-fleet-pod-head">
                  <div class="vn-fleet-pod-title"><i class="fas fa-van-shuttle"></i> Executive Sprinter Pods</div>
                  <span class="vn-fleet-badge">12–24 Delegates</span>
                </div>
                <div class="vn-fleet-desc">
                  First-class captain chairs, onboard boardroom displays, dedicated luggage transport vans, and continuous hydration service.
                </div>
              </div>

              <div class="vn-fleet-pod" data-fleet="aviation">
                <div class="vn-fleet-pod-head">
                  <div class="vn-fleet-pod-title"><i class="fas fa-helicopter"></i> Airside Runway &amp; Helipad</div>
                  <span class="vn-fleet-badge">Direct Tarmac</span>
                </div>
                <div class="vn-fleet-desc">
                  Direct plane-side ramp clearance, twin-engine turbine helicopter transfers from private FBO hangars to venue rooftop helipads.
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 6: VENDOR PARTNERSHIP ENQUIRY -->
      <section id="partnership-enquiry" class="vn-section-enquiry">
        <div class="vn-container">
          <div class="vn-section-head framer-compliance-stamp">
            <span class="vn-badge"><i class="fas fa-scale-balanced"></i> Enterprise Standards &amp; Accreditation</span>
            <h2 class="vn-title">140-Point Standards Compliance &amp; <span class="vn-title-gradient">Tier Evaluator</span></h2>
            <p class="vn-subtitle">
              We uphold uncompromising service level agreements. Check your organization's readiness for master supplier accreditation with our interactive qualification auditor.
            </p>
          </div>

          <div class="vn-enquiry-layout">
            <!-- Left: Tier Dossier Visual & Specs -->
            <div class="vn-enquiry-card-dossier framer-compliance-stamp">
              <div class="vn-enquiry-visual">
                <img src="images/vendor_partnership.jpg" alt="Corporate Vendor Procurement Review and Compliance Meeting" loading="lazy">
                <div style="position: absolute; bottom: 1.25rem; left: 1.25rem; background: rgba(15, 23, 42, 0.88); backdrop-filter: blur(8px); padding: 0.5rem 1rem; border-radius: 0.75rem; color: #ffffff; font-size: 0.82rem; font-weight: 700;">
                  <i class="fas fa-handshake" style="color: var(--vn-accent);"></i> Strategic Alliance Master MSA
                </div>
              </div>

              <div class="vn-enquiry-body">
                <div>
                  <h3 style="font-size: 1.35rem; font-weight: 800; color: var(--vn-text-main); margin-bottom: 0.5rem;">Partner Accreditation Levels</h3>
                  <p style="font-size: 0.9rem; color: var(--vn-text-muted); line-height: 1.5;">
                    Accredited partners gain exclusive direct routing into multi-million dollar annual conference procurement pipelines.
                  </p>
                </div>

                <div class="vn-tier-pill-list">
                  <div class="vn-tier-pill-item">
                    <i class="fas fa-award vn-tier-icon"></i>
                    <div>
                      <strong style="color: var(--vn-text-main); font-size: 0.95rem;">Tier-1 Global Strategic Partner:</strong>
                      <div style="font-size: 0.82rem; color: var(--vn-text-muted);">Multi-year preferred contract, co-marketing at global summits, Net-15 settlement.</div>
                    </div>
                  </div>

                  <div class="vn-tier-pill-item">
                    <i class="fas fa-check-circle vn-tier-icon"></i>
                    <div>
                      <strong style="color: var(--vn-text-main); font-size: 0.95rem;">Tier-2 Regional Preferred Vendor:</strong>
                      <div style="font-size: 0.82rem; color: var(--vn-text-muted);">Pre-qualified RFP bidding queue across North America, EMEA, and APAC events.</div>
                    </div>
                  </div>

                  <div class="vn-tier-pill-item">
                    <i class="fas fa-gem vn-tier-icon"></i>
                    <div>
                      <strong style="color: var(--vn-text-main); font-size: 0.95rem;">Specialist Boutique Guild:</strong>
                      <div style="font-size: 0.82rem; color: var(--vn-text-muted);">Curated craft fabrication, bespoke culinary, and rare specialized experiential staging.</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Right: Interactive Auditor Tool -->
            <div class="vn-auditor-gate-panel framer-compliance-stamp">
              <div>
                <span class="vn-badge"><i class="fas fa-calculator"></i> Self-Assessment Calculator</span>
                <h3 style="font-size: 1.5rem; font-weight: 800; color: var(--vn-text-main); margin-bottom: 0.5rem;">Check Accreditation Readiness</h3>
                <p style="font-size: 0.9rem; color: var(--vn-text-muted); line-height: 1.5; margin-bottom: 1.5rem;">
                  Toggle your operational compliance qualifications below to calculate your supplier readiness tier score:
                </p>

                <div class="vn-score-dial-wrap">
                  <div>
                    <span style="font-size: 0.78rem; text-transform: uppercase; font-weight: 700; color: var(--vn-text-light); letter-spacing: 0.05em;">Compliance Index</span>
                    <div class="vn-score-readout">
                      <span id="complianceScoreNum" class="vn-score-number">100</span>
                      <span class="vn-score-max">/ 100%</span>
                    </div>
                  </div>
                  <span id="complianceScoreBadge" class="vn-score-status-badge">Tier-1 Qualified</span>
                </div>

                <div class="vn-checklist-group">
                  <label class="vn-check-item">
                    <input type="checkbox" checked onchange="updateComplianceScore(this, 25)">
                    <span class="vn-check-label">$10M+ Commercial General Liability Insurance Coverage</span>
                  </label>

                  <label class="vn-check-item">
                    <input type="checkbox" checked onchange="updateComplianceScore(this, 25)">
                    <span class="vn-check-label">ISO 20121 Sustainable Event Management or Green Sourcing</span>
                  </label>

                  <label class="vn-check-item">
                    <input type="checkbox" checked onchange="updateComplianceScore(this, 20)">
                    <span class="vn-check-label">Certified Rigging / CTS-D Engineering or Food Safety Certs</span>
                  </label>

                  <label class="vn-check-item">
                    <input type="checkbox" checked onchange="updateComplianceScore(this, 15)">
                    <span class="vn-check-label">Documented Redundancy Fail-Safe &amp; Emergency Contingency Fleet</span>
                  </label>

                  <label class="vn-check-item">
                    <input type="checkbox" checked onchange="updateComplianceScore(this, 15)">
                    <span class="vn-check-label">Verified Fortune 500 Enterprise Past Performance Portfolio</span>
                  </label>
                </div>
              </div>

              <div>
                <a href="#vendor-registration" class="vn-btn vn-btn-primary" style="width: 100%;">
                  <i class="fas fa-file-contract"></i> Proceed to Master Registration Form
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 7: VENDOR REGISTRATION -->
      <section id="vendor-registration" class="vn-section-registration">
        <div class="vn-container">
          <div class="vn-section-head framer-portal-unlock">
            <span class="vn-badge"><i class="fas fa-id-card"></i> Formal Onboarding Terminal</span>
            <h2 class="vn-title">Accredited Supplier Terminal &amp; <span class="vn-title-gradient">Document Vault</span></h2>
            <p class="vn-subtitle">
              Complete your company dossier and deposit official insurance certificates and capability manifests into our secure procurement vault.
            </p>
          </div>

          <div class="vn-reg-portal-grid">
            <!-- Left Col: Portal Guidelines & Support -->
            <div class="vn-portal-info-card framer-portal-unlock">
              <div class="vn-portal-hero-img">
                <img src="images/vendor_registration.jpg" alt="Official Supplier Accreditation Paperwork and Smart Cards" loading="lazy">
                <div style="position: absolute; top: 1.25rem; left: 1.25rem; background: rgba(15, 23, 42, 0.88); backdrop-filter: blur(8px); padding: 0.5rem 1rem; border-radius: 0.75rem; color: #ffffff; font-size: 0.82rem; font-weight: 700; border: 1px solid rgba(255, 255, 255, 0.15);">
                  <i class="fas fa-lock" style="color: #10b981;"></i> 256-Bit Encrypted Procurement Vault
                </div>
              </div>

              <div class="vn-portal-steps-box">
                <div>
                  <h3 style="font-size: 1.35rem; font-weight: 800; color: var(--vn-text-main); margin-bottom: 0.5rem;">Onboarding Protocol</h3>
                  <p style="font-size: 0.88rem; color: var(--vn-text-muted); line-height: 1.5; margin-bottom: 1.25rem;">
                    What happens after you submit your registration dossier:
                  </p>

                  <div class="vn-process-stepper">
                    <div class="vn-stepper-row">
                      <div class="vn-stepper-num">1</div>
                      <div class="vn-stepper-content">
                        <div class="vn-stepper-title">Automated Compliance Intake</div>
                        <div class="vn-stepper-desc">COI policy verification and active legal standing check within 48 business hours.</div>
                      </div>
                    </div>

                    <div class="vn-stepper-row">
                      <div class="vn-stepper-num">2</div>
                      <div class="vn-stepper-content">
                        <div class="vn-stepper-title">Technical Inspection &amp; Audit</div>
                        <div class="vn-stepper-desc">Virtual or on-site hardware inspection or kitchen culinary tasting audit.</div>
                      </div>
                    </div>

                    <div class="vn-stepper-row">
                      <div class="vn-stepper-num">3</div>
                      <div class="vn-stepper-content">
                        <div class="vn-stepper-title">Master Vendor Agreement (MSA)</div>
                        <div class="vn-stepper-desc">Execution of standard master agreement and assignment of dedicated procurement key.</div>
                      </div>
                    </div>
                  </div>
                </div>

                <div style="background: var(--vn-surface-muted); padding: 1.25rem; border-radius: 1rem; border: 1px solid var(--vn-card-border); font-size: 0.85rem; color: var(--vn-text-muted); line-height: 1.5;">
                  <strong style="color: var(--vn-text-main); display: block; margin-bottom: 0.25rem;"><i class="fas fa-headset" style="color: var(--vn-accent);"></i> Supplier Procurement Desk</strong>
                  Direct inquiries: <code>procurement@corporateevents.com</code> | Toll-free: <code>+1 (800) 555-EVENT</code>
                </div>
              </div>
            </div>

            <!-- Right Col: Interactive Application Form -->
            <div class="vn-reg-form-card framer-portal-unlock">
              <div>
                <span class="vn-badge"><i class="fas fa-file-pen"></i> Direct Supplier Registration</span>
                <h3 style="font-size: 1.5rem; font-weight: 800; color: var(--vn-text-main); margin-bottom: 0.5rem;">Corporate Supplier Application</h3>
                <p style="font-size: 0.88rem; color: var(--vn-text-muted);">
                  Please complete all fields with verified corporate records.
                </p>
              </div>

              <form id="vendorRegForm" onsubmit="handleVendorSubmit(event)">
                <div class="vn-form-row">
                  <div class="vn-form-group">
                    <label class="vn-form-label">Company Legal Name *</label>
                    <input type="text" class="vn-form-input" placeholder="e.g. Apex Audio Visual Systems Inc." required>
                  </div>
                  <div class="vn-form-group">
                    <label class="vn-form-label">Primary Vendor Category *</label>
                    <select class="vn-form-select" required>
                      <option value="">Select Primary Specialty...</option>
                      <option value="venues">Venue &amp; Convention Center</option>
                      <option value="av">Audiovisual &amp; Broadcast Lighting</option>
                      <option value="catering">Catering &amp; Executive Hospitality</option>
                      <option value="staging">Scenic Fabrication &amp; Staging</option>
                      <option value="transport">VIP Mobility &amp; Aviation Fleet</option>
                      <option value="other">Specialized Event Artisan</option>
                    </select>
                  </div>
                </div>

                <div class="vn-form-row" style="margin-top: 1.25rem;">
                  <div class="vn-form-group">
                    <label class="vn-form-label">Executive Contact Name *</label>
                    <input type="text" class="vn-form-input" placeholder="e.g. Eleanor Vance" required>
                  </div>
                  <div class="vn-form-group">
                    <label class="vn-form-label">Corporate Email Address *</label>
                    <input type="email" class="vn-form-input" placeholder="e.g. evance@apex-av.com" required>
                  </div>
                </div>

                <div class="vn-form-row" style="margin-top: 1.25rem;">
                  <div class="vn-form-group">
                    <label class="vn-form-label">Direct Phone Number *</label>
                    <input type="tel" class="vn-form-input" placeholder="+1 (555) 019-2834" required>
                  </div>
                  <div class="vn-form-group">
                    <label class="vn-form-label">Annual Gross Volume ($ USD)</label>
                    <select class="vn-form-select">
                      <option value="1-5M">$1,000,000 – $5,000,000</option>
                      <option value="5-20M" selected>$5,000,000 – $20,000,000</option>
                      <option value="20M+">$20,000,000+</option>
                    </select>
                  </div>
                </div>

                <div class="vn-form-group" style="margin-top: 1.25rem;">
                  <label class="vn-form-label">Operational Capacity &amp; Geographic Footprint</label>
                  <textarea class="vn-form-textarea" rows="3" placeholder="Detail your warehouse locations, full-time technician headcount, and inventory overview..."></textarea>
                </div>

                <!-- Vault File Upload Dropzone -->
                <div class="vn-form-group" style="margin-top: 1.25rem;">
                  <label class="vn-form-label">Upload Certificate of Insurance (COI) &amp; Manifest (PDF / ZIP)</label>
                  <div class="vn-vault-dropzone" id="vaultDropzone" onclick="triggerFileUpload()">
                    <i class="fas fa-cloud-arrow-up"></i>
                    <div>
                      <strong id="dropzoneText" style="color: var(--vn-text-main); font-size: 0.95rem;">Drag &amp; Drop COI or Click to Browse Files</strong>
                      <div style="font-size: 0.8rem; color: var(--vn-text-muted); margin-top: 0.2rem;">Accepts PDF, DOCX, ZIP up to 50MB</div>
                    </div>
                    <input type="file" id="hiddenFileInput" style="display: none;" onchange="handleFileSelected(this)">
                  </div>
                </div>

                <div style="margin-top: 1.75rem;">
                  <button type="submit" class="vn-btn vn-btn-primary" style="width: 100%; font-size: 1.05rem; padding: 1rem 2rem;">
                    <i class="fas fa-paper-plane"></i> Submit Official Supplier Accreditation Dossier
                  </button>
                  <div style="text-align: center; font-size: 0.78rem; color: var(--vn-text-muted); margin-top: 0.75rem;">
                    <i class="fas fa-shield-halved" style="color: #10b981;"></i> All information is held in strict non-disclosure compliance under our mutual NDA terms.
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </section>

      <!-- SUCCESS MODAL POPUP -->
      <div class="vn-modal-backdrop" id="vendorSuccessModal">
        <div class="vn-modal-box">
          <div class="vn-modal-icon">
            <i class="fas fa-check"></i>
          </div>
          <h3 style="font-size: 1.65rem; font-weight: 800; color: var(--vn-text-main); margin-bottom: 0.5rem;">Dossier Received Successfully!</h3>
          <p style="font-size: 0.95rem; color: var(--vn-text-muted); line-height: 1.6; margin-bottom: 1.75rem;">
            Your vendor registration package has been entered into the procurement evaluation queue. Tracking reference: <strong id="trackingRefCode" style="color: var(--vn-accent); font-family: monospace;">VR-2026-9842</strong>. Our director of procurement will reach out within 48 business hours.
          </p>
          <button class="vn-btn vn-btn-primary" onclick="closeVendorModal()" style="width: 100%;">
            <i class="fas fa-arrow-left"></i> Return to Directory
          </button>
        </div>
      </div>

    </main>
    """

    # Page Interactive Scripts
    vendors_scripts = """
    <!-- =====================================================================
         INTERACTIVE CLIENT CONTROLS & FRAMER MOTION OBSERVERS
         ===================================================================== -->
    <script>
    // 1. Framer Motion Scroll Trigger Observers
    document.addEventListener('DOMContentLoaded', () => {
      const motionClasses = [
        '.framer-colonnade-reveal',
        '.framer-hardware-dial',
        '.framer-culinary-float',
        '.framer-scenic-construct',
        '.framer-transit-glide',
        '.framer-compliance-stamp',
        '.framer-portal-unlock'
      ];

      const motionObserver = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('framer-in-view');
            // Stagger child elements if any
            const children = entry.target.querySelectorAll('.framer-colonnade-reveal, .framer-hardware-dial, .framer-culinary-float, .framer-scenic-construct, .framer-transit-glide, .framer-compliance-stamp, .framer-portal-unlock');
            children.forEach((c, idx) => {
              setTimeout(() => c.classList.add('framer-in-view'), idx * 80);
            });
            obs.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
      });

      motionClasses.forEach(selector => {
        document.querySelectorAll(selector).forEach(el => motionObserver.observe(el));
      });
    });

    // 2. Section 1: Venue Tier Selector
    const venueTiersData = [
      {
        title: "The Grand Plenary Palace & Exposition Atrium",
        desc: "Featuring clear-span columnless architecture, acoustic wall baffle treatments, and automated rigging trusses capable of hosting up to 12,500 delegates in full plenary configuration.",
        cap: "12,500 Delegates",
        sound: "54 dB STC",
        rig: "120 Metric Tons"
      },
      {
        title: "Marina Waterfront Amphitheater & Glasshouse",
        desc: "Acoustically tuned curved shells overlooking the bay with adjacent floor-to-ceiling glass pavilions, direct boat dock ingress, and sunset networking terraces.",
        cap: "4,500 Delegates",
        sound: "48 dB STC",
        rig: "75 Metric Tons"
      },
      {
        title: "Alpine Heritage Castle & Sovereign Sovereign Estate",
        desc: "Private 18th-century baroque architecture retrofitted with secure satellite fiber uplinks, sovereign VIP security perimeter, and private helicopter landing pads.",
        cap: "1,200 Delegates",
        sound: "50 dB STC",
        rig: "40 Metric Tons"
      }
    ];

    function selectVenueTier(index) {
      const pods = document.querySelectorAll('.vn-colonnade-pod');
      pods.forEach((p, idx) => {
        if (idx === index) p.classList.add('active');
        else p.classList.remove('active');
      });

      const data = venueTiersData[index];
      const titleEl = document.getElementById('currentVenueTitle');
      const descEl = document.getElementById('currentVenueDesc');
      const capEl = document.getElementById('venueCapStat');
      const soundEl = document.getElementById('venueSoundStat');
      const rigEl = document.getElementById('venueRigStat');

      if (titleEl) {
        titleEl.style.opacity = '0';
        setTimeout(() => {
          titleEl.textContent = data.title;
          if (descEl) descEl.textContent = data.desc;
          if (capEl) capEl.textContent = data.cap;
          if (soundEl) soundEl.textContent = data.sound;
          if (rigEl) rigEl.textContent = data.rig;
          titleEl.style.opacity = '1';
        }, 180);
      }
    }

    // 3. Section 2: AV Hardware Mode Switcher
    const avPresets = [
      { latency: '1.2 ms', refresh: '7,680 Hz', uptime: '99.999%' },
      { latency: '2.8 ms', refresh: '3,840 Hz', uptime: '99.995%' },
      { latency: '0.8 ms', refresh: '7,680 Hz', uptime: '100.00%' }
    ];

    function switchAVPreset(index, btn) {
      document.querySelectorAll('.vn-switch-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const data = avPresets[index];
      const latEl = document.getElementById('avLatencyVal');
      const refEl = document.getElementById('avRefreshVal');
      const upEl = document.getElementById('avUptimeVal');

      if (latEl) latEl.textContent = data.latency;
      if (refEl) refEl.textContent = data.refresh;
      if (upEl) upEl.textContent = data.uptime;
    }

    // 4. Section 4: Production Material Swatch Selector
    function activateSwatch(card, description) {
      document.querySelectorAll('.vn-swatch-card').forEach(c => c.classList.remove('active'));
      card.classList.add('active');
      const noteEl = document.getElementById('swatchNote');
      if (noteEl) noteEl.textContent = description;
    }

    // 5. Section 5: VIP Fleet Category Filter
    function filterFleet(category, btn) {
      document.querySelectorAll('.vn-transport-filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const pods = document.querySelectorAll('.vn-fleet-pod');
      pods.forEach(pod => {
        const podFleet = pod.getAttribute('data-fleet');
        if (category === 'all' || podFleet === category) {
          pod.style.display = 'flex';
          pod.style.opacity = '1';
        } else {
          pod.style.display = 'none';
        }
      });
    }

    // 6. Section 6: Compliance Auditor Tool
    let currentComplianceScore = 100;
    function updateComplianceScore(checkbox, weight) {
      if (checkbox.checked) {
        currentComplianceScore += weight;
      } else {
        currentComplianceScore -= weight;
      }
      currentComplianceScore = Math.max(0, Math.min(100, currentComplianceScore));

      const numEl = document.getElementById('complianceScoreNum');
      const badgeEl = document.getElementById('complianceScoreBadge');

      if (numEl) numEl.textContent = currentComplianceScore;
      if (badgeEl) {
        if (currentComplianceScore >= 85) {
          badgeEl.textContent = 'Tier-1 Qualified';
          badgeEl.style.background = '#10b981';
        } else if (currentComplianceScore >= 60) {
          badgeEl.textContent = 'Tier-2 Preferred';
          badgeEl.style.background = '#f59e0b';
        } else {
          badgeEl.textContent = 'Needs Review';
          badgeEl.style.background = '#ef4444';
        }
      }
    }

    // 7. Section 7: File Upload & Registration Submission
    function triggerFileUpload() {
      const input = document.getElementById('hiddenFileInput');
      if (input) input.click();
    }

    function handleFileSelected(input) {
      if (input.files && input.files.length > 0) {
        const fileName = input.files[0].name;
        const textEl = document.getElementById('dropzoneText');
        if (textEl) {
          textEl.innerHTML = `<span style="color:#10b981;"><i class="fas fa-check-circle"></i> File Attached: ${fileName}</span>`;
        }
      }
    }

    function handleVendorSubmit(e) {
      e.preventDefault();
      const code = 'VR-2026-' + Math.floor(1000 + Math.random() * 9000);
      const codeEl = document.getElementById('trackingRefCode');
      if (codeEl) codeEl.textContent = code;

      const modal = document.getElementById('vendorSuccessModal');
      if (modal) modal.style.display = 'flex';
    }

    function closeVendorModal() {
      const modal = document.getElementById('vendorSuccessModal');
      if (modal) modal.style.display = 'none';
      const form = document.getElementById('vendorRegForm');
      if (form) form.reset();
      const textEl = document.getElementById('dropzoneText');
      if (textEl) textEl.textContent = 'Drag & Drop COI or Click to Browse Files';
    }
    </script>
    """

    # Assemble complete document
    final_html = (
        nav_head_up_to_style
        + vendors_css
        + "\n  </style>"
        + nav_mid[len("</style>"):]
        + vendors_html_content
        + footer_part
        + vendors_scripts
        + closing_part
    )

    with open('vendors.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print("Successfully built vendors.html! Total length:", len(final_html))

if __name__ == '__main__':
    build_vendors_html()
