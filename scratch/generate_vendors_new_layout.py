import os

def generate_vendors():
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

    # CSS for the new vendors.html layout
    new_vnd_css = """
    /* =====================================================================
       REDESIGNED VENDORS ARCHITECTURE: GLOBAL GUILD & SUPPLY CHAIN ALLIANCE
       Supports Light Mode, Dark Mode (body.dark), and RTL (body.rtl)
       ===================================================================== */
    :root {
      --vnd-primary: #1e3a8a;
      --vnd-primary-dark: #0f172a;
      --vnd-accent: #d97706;
      --vnd-accent-light: #fbbf24;
      --vnd-accent-glow: rgba(217, 119, 6, 0.16);
      --vnd-cyan: #0891b2;
      --vnd-cyan-glow: rgba(8, 145, 178, 0.16);
      --vnd-emerald: #059669;
      --vnd-emerald-glow: rgba(5, 150, 105, 0.16);
      --vnd-bg: #f8fafc;
      --vnd-surface: #ffffff;
      --vnd-surface-muted: #f1f5f9;
      --vnd-card-border: #e2e8f0;
      --vnd-text-main: #0f172a;
      --vnd-text-muted: #64748b;
      --vnd-text-light: #94a3b8;
      --vnd-gold-gradient: linear-gradient(135deg, #b45309 0%, #d97706 50%, #f59e0b 100%);
      --vnd-blue-gradient: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      --vnd-cyan-gradient: linear-gradient(135deg, #0e7490 0%, #0891b2 100%);
      --vnd-shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --vnd-shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.07), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
      --vnd-shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      --vnd-shadow-glow: 0 0 25px rgba(217, 119, 6, 0.22);
    }

    body.dark {
      --vnd-bg: #070b14;
      --vnd-surface: #0f172a;
      --vnd-surface-muted: #131d33;
      --vnd-card-border: #1e293b;
      --vnd-text-main: #f8fafc;
      --vnd-text-muted: #94a3b8;
      --vnd-text-light: #64748b;
      --vnd-blue-gradient: linear-gradient(135deg, #070b14 0%, #172554 100%);
    }

    /* RTL Support */
    body.rtl .vnd-section-head { text-align: right; }
    body.rtl .vnd-badge i { margin-left: 0.5rem; margin-right: 0; }
    body.rtl .vnd-btn i { margin-right: 0.5rem; margin-left: 0; }

    /* Base Container */
    .vnd-page-wrap {
      background-color: var(--vnd-bg);
      color: var(--vnd-text-main);
      font-family: 'Inter', system-ui, sans-serif;
      overflow-x: hidden;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    .vnd-container {
      max-width: 1320px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }

    /* SECTION HEADER STYLING */
    .vnd-section-head {
      margin-bottom: 3.5rem;
      position: relative;
    }

    .vnd-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.45rem 1.1rem;
      border-radius: 9999px;
      background: var(--vnd-accent-glow);
      color: var(--vnd-accent);
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 1rem;
      border: 1px solid rgba(217, 119, 6, 0.3);
    }

    .vnd-title {
      font-size: 2.5rem;
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.025em;
      color: var(--vnd-text-main);
      margin-bottom: 1rem;
    }

    .vnd-title-gradient {
      background: var(--vnd-gold-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .vnd-subtitle {
      font-size: 1.1rem;
      color: var(--vnd-text-muted);
      max-width: 760px;
      line-height: 1.65;
    }

    /* BUTTONS */
    .vnd-btn {
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

    .vnd-btn-primary {
      background: var(--vnd-gold-gradient);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(217, 119, 6, 0.35);
    }

    .vnd-btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(217, 119, 6, 0.45);
      color: #ffffff;
    }

    .vnd-btn-outline {
      background: transparent;
      color: var(--vnd-text-main);
      border-color: var(--vnd-card-border);
    }

    .vnd-btn-outline:hover {
      border-color: var(--vnd-accent);
      color: var(--vnd-accent);
      background: var(--vnd-accent-glow);
    }

    /* =====================================================================
       FRAMER MOTION SPECIFIC CLASSES & KEYFRAMES (1 PER SECTION)
       ===================================================================== */

    /* 1. Venue Partners: .framer-atrium-unfold */
    .framer-atrium-unfold {
      opacity: 0;
      transform: translateY(35px) perspective(1000px) rotateX(3deg);
      transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1),
                  transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .framer-atrium-unfold.framer-in-view {
      opacity: 1;
      transform: translateY(0) perspective(1000px) rotateX(0deg);
    }

    /* 2. Audio-Visual Suppliers: .framer-rack-mount */
    .framer-rack-mount {
      opacity: 0;
      transform: scale(0.95) translateY(30px);
      transition: opacity 0.75s cubic-bezier(0.34, 1.56, 0.64, 1),
                  transform 0.75s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .framer-rack-mount.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    /* 3. Catering Partners: .framer-gastronomy-float */
    .framer-gastronomy-float {
      opacity: 0;
      transform: translateY(40px) scale(0.97);
      transition: opacity 0.85s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                  transform 0.85s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    .framer-gastronomy-float.framer-in-view {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    /* 4. Decoration & Production Teams: .framer-scenic-forge */
    .framer-scenic-forge {
      opacity: 0;
      transform: translateX(-35px) scale(0.98);
      transition: opacity 0.8s cubic-bezier(0.19, 1, 0.22, 1),
                  transform 0.8s cubic-bezier(0.19, 1, 0.22, 1);
    }
    .framer-scenic-forge.framer-in-view {
      opacity: 1;
      transform: translateX(0) scale(1);
    }

    /* 5. Transport Providers: .framer-fleet-manifest */
    .framer-fleet-manifest {
      opacity: 0;
      transform: translateY(35px);
      filter: blur(3px);
      transition: opacity 0.8s cubic-bezier(0.22, 1, 0.36, 1),
                  transform 0.8s cubic-bezier(0.22, 1, 0.36, 1),
                  filter 0.8s ease;
    }
    .framer-fleet-manifest.framer-in-view {
      opacity: 1;
      transform: translateY(0);
      filter: blur(0px);
    }

    /* 6. Vendor Partnership Enquiry: .framer-procurement-gate */
    .framer-procurement-gate {
      opacity: 0;
      transform: scale(0.94) translateY(25px);
      transition: opacity 0.75s cubic-bezier(0.68, -0.55, 0.265, 1.55),
                  transform 0.75s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    }
    .framer-procurement-gate.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    /* 7. Vendor Registration: .framer-terminal-onboard */
    .framer-terminal-onboard {
      opacity: 0;
      transform: translateY(30px) scale(0.98);
      transition: opacity 0.7s cubic-bezier(0.33, 1, 0.68, 1),
                  transform 0.7s cubic-bezier(0.33, 1, 0.68, 1);
    }
    .framer-terminal-onboard.framer-in-view {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    /* =====================================================================
       SECTION 1: VENUE PARTNERS - ATRIUM BENTO & ALLIANCE GALLERY
       ===================================================================== */
    .vnd-section-venues {
      padding: 6rem 0;
      position: relative;
    }

    /* Accreditation & Network Ticker */
    .vnd-venue-ticker-ribbon {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 1.5rem;
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem 2rem;
      box-shadow: var(--vnd-shadow-sm);
      margin-bottom: 2.5rem;
    }

    .vnd-ticker-metrics {
      display: flex;
      align-items: center;
      gap: 2rem;
    }

    .vnd-tmetric-item {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .vnd-tmetric-icon {
      width: 2.5rem;
      height: 2.5rem;
      border-radius: 0.6rem;
      background: var(--vnd-accent-glow);
      color: var(--vnd-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
    }

    .vnd-tmetric-val {
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--vnd-text-main);
      line-height: 1.2;
    }

    .vnd-tmetric-lbl {
      font-size: 0.78rem;
      color: var(--vnd-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .vnd-cluster-filters {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }

    .vnd-cluster-btn {
      padding: 0.5rem 1rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 600;
      border: 1px solid var(--vnd-card-border);
      background: var(--vnd-surface-muted);
      color: var(--vnd-text-muted);
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .vnd-cluster-btn.active,
    .vnd-cluster-btn:hover {
      background: var(--vnd-accent);
      color: #ffffff;
      border-color: var(--vnd-accent);
    }

    /* Asymmetric 4-Tier Bento Architectural Gallery */
    .vnd-venue-bento-grid {
      display: grid;
      grid-template-columns: 1.25fr 1fr;
      gap: 2.5rem;
      align-items: start;
    }

    .vnd-venue-hero-pavilion {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--vnd-shadow-md);
      position: relative;
    }

    .vnd-pavilion-img-wrap {
      height: 380px;
      position: relative;
      overflow: hidden;
    }

    .vnd-pavilion-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s ease;
    }

    .vnd-venue-hero-pavilion:hover .vnd-pavilion-img-wrap img {
      transform: scale(1.04);
    }

    .vnd-pavilion-status-chip {
      position: absolute;
      top: 1.25rem;
      left: 1.25rem;
      background: rgba(15, 23, 42, 0.85);
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

    .vnd-pavilion-body {
      padding: 2.25rem;
    }

    .vnd-pavilion-title {
      font-size: 1.75rem;
      font-weight: 800;
      color: var(--vnd-text-main);
      line-height: 1.3;
      margin-bottom: 0.75rem;
    }

    .vnd-pavilion-desc {
      font-size: 0.95rem;
      color: var(--vnd-text-muted);
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }

    .vnd-pavilion-specs-strip {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
      padding: 1.25rem;
      background: var(--vnd-surface-muted);
      border-radius: 1rem;
      margin-bottom: 2rem;
      border: 1px solid var(--vnd-card-border);
    }

    .vnd-pspec-item {
      text-align: center;
    }

    .vnd-pspec-val {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--vnd-text-main);
    }

    .vnd-pspec-lbl {
      font-size: 0.75rem;
      color: var(--vnd-text-muted);
      text-transform: uppercase;
      font-weight: 600;
      margin-top: 0.25rem;
    }

    /* Right Staggered Tier Spec Deck */
    .vnd-staggered-tiers-col {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    .vnd-tier-card {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.25rem;
      padding: 1.75rem;
      box-shadow: var(--vnd-shadow-sm);
      transition: all 0.25s ease;
      cursor: pointer;
    }

    .vnd-tier-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--vnd-shadow-md);
      border-color: var(--vnd-accent);
    }

    .vnd-tier-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.75rem;
    }

    .vnd-tier-tag {
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--vnd-accent);
      background: var(--vnd-accent-glow);
      padding: 0.25rem 0.65rem;
      border-radius: 0.35rem;
    }

    .vnd-tier-cap {
      font-size: 0.82rem;
      color: var(--vnd-text-muted);
      font-weight: 600;
    }

    .vnd-tier-title {
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--vnd-text-main);
      margin-bottom: 0.5rem;
    }

    .vnd-tier-features {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-top: 0.75rem;
    }

    .vnd-feat-chip {
      font-size: 0.78rem;
      padding: 0.25rem 0.6rem;
      border-radius: 0.4rem;
      background: var(--vnd-surface-muted);
      border: 1px solid var(--vnd-card-border);
      color: var(--vnd-text-muted);
    }

    /* =====================================================================
       SECTION 2: AUDIO-VISUAL SUPPLIERS - HARDWARE SYNTHESIS & RACK-MOUNT
       ===================================================================== */
    .vnd-section-audiovisual {
      padding: 6rem 0;
      background: var(--vnd-surface-muted);
      border-top: 1px solid var(--vnd-card-border);
      border-bottom: 1px solid var(--vnd-card-border);
    }

    /* Hardware Telemetry Strip */
    .vnd-av-telemetry-strip {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.5rem;
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem 2rem;
      box-shadow: var(--vnd-shadow-sm);
      margin-bottom: 3rem;
    }

    .vnd-av-chip {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .vnd-av-icon {
      width: 2.75rem;
      height: 2.75rem;
      border-radius: 0.75rem;
      background: var(--vnd-cyan-glow);
      color: var(--vnd-cyan);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
    }

    .vnd-av-val {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--vnd-text-main);
      line-height: 1.2;
    }

    .vnd-av-lbl {
      font-size: 0.75rem;
      color: var(--vnd-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    /* Multi-Panel Broadcast Switcher Interface */
    .vnd-av-console-grid {
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 2.5rem;
      align-items: start;
    }

    /* Master Video Monitor Frame */
    .vnd-av-monitor-card {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--vnd-shadow-md);
      position: relative;
    }

    .vnd-monitor-header {
      padding: 1rem 1.5rem;
      background: rgba(15, 23, 42, 0.95);
      color: #ffffff;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .vnd-monitor-tally {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.75rem;
      font-weight: 800;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: #ef4444;
    }

    .vnd-tally-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #ef4444;
      box-shadow: 0 0 10px #ef4444;
      animation: resPulsePin 1.5s infinite;
    }

    .vnd-monitor-screen {
      height: 340px;
      position: relative;
      overflow: hidden;
    }

    .vnd-monitor-screen img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .vnd-monitor-controls {
      padding: 1.75rem;
      background: var(--vnd-surface);
      border-top: 1px solid var(--vnd-card-border);
    }

    .vnd-vu-meters-row {
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-bottom: 1.25rem;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--vnd-text-muted);
    }

    .vnd-vu-bar {
      flex: 1;
      height: 8px;
      background: var(--vnd-surface-muted);
      border-radius: 4px;
      overflow: hidden;
      border: 1px solid var(--vnd-card-border);
    }

    .vnd-vu-fill {
      height: 100%;
      width: 82%;
      background: linear-gradient(90deg, #10b981 60%, #f59e0b 85%, #ef4444 100%);
    }

    /* Right Modular Rack Units */
    .vnd-rack-mount-stack {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    .vnd-rack-unit-card {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.25rem;
      padding: 1.75rem;
      box-shadow: var(--vnd-shadow-sm);
      position: relative;
      overflow: hidden;
      transition: all 0.25s ease;
    }

    .vnd-rack-unit-card:hover {
      border-color: var(--vnd-cyan);
      transform: translateX(4px);
    }

    body.rtl .vnd-rack-unit-card:hover {
      transform: translateX(-4px);
    }

    .vnd-rack-unit-card::before {
      content: '';
      position: absolute;
      top: 0;
      bottom: 0;
      left: 0;
      width: 4px;
      background: var(--vnd-cyan);
    }

    body.rtl .vnd-rack-unit-card::before {
      left: auto;
      right: 0;
    }

    .vnd-rack-unit-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.75rem;
    }

    .vnd-rack-id {
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--vnd-cyan);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .vnd-rack-title {
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--vnd-text-main);
      margin-bottom: 0.5rem;
    }

    .vnd-rack-desc {
      font-size: 0.88rem;
      color: var(--vnd-text-muted);
      line-height: 1.55;
      margin-bottom: 1rem;
    }

    .vnd-rack-specs {
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
      font-size: 0.8rem;
      color: var(--vnd-text-main);
    }

    .vnd-rack-specs i {
      color: var(--vnd-cyan);
      margin-right: 0.4rem;
    }

    body.rtl .vnd-rack-specs i {
      margin-right: 0;
      margin-left: 0.4rem;
    }

    /* =====================================================================
       SECTION 3: CATERING PARTNERS - CULINARY GUILD & TASTING ATELIER
       ===================================================================== */
    .vnd-section-catering {
      padding: 6rem 0;
      position: relative;
    }

    /* Culinary Philosophy & Accreditation Bar */
    .vnd-culinary-badge-bar {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 1rem;
      margin-bottom: 3.5rem;
    }

    .vnd-cbadge-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.6rem 1.25rem;
      border-radius: 9999px;
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      color: var(--vnd-text-main);
      font-size: 0.85rem;
      font-weight: 700;
      box-shadow: var(--vnd-shadow-sm);
    }

    .vnd-cbadge-pill i {
      color: var(--vnd-accent);
    }

    /* 3-Column Asymmetric Atelier */
    .vnd-gastronomy-atelier-grid {
      display: grid;
      grid-template-columns: 1fr 1.2fr 1fr;
      gap: 2rem;
      align-items: center;
    }

    /* Col 1: Curated Tasting Menu */
    .vnd-tasting-menu-card {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.5rem;
      padding: 2rem;
      box-shadow: var(--vnd-shadow-sm);
    }

    .vnd-menu-title {
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--vnd-text-main);
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--vnd-card-border);
    }

    .vnd-course-item {
      margin-bottom: 1.5rem;
    }

    .vnd-course-num {
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--vnd-accent);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.25rem;
    }

    .vnd-course-name {
      font-size: 1rem;
      font-weight: 700;
      color: var(--vnd-text-main);
      margin-bottom: 0.25rem;
    }

    .vnd-course-tags {
      font-size: 0.75rem;
      color: var(--vnd-text-muted);
    }

    /* Col 2: Center Featured Gastronomic Visual Frame */
    .vnd-culinary-center-frame {
      background: var(--vnd-surface);
      border: 2px solid var(--vnd-accent);
      border-radius: 2rem;
      overflow: hidden;
      box-shadow: 0 0 35px rgba(217, 119, 6, 0.25);
      position: relative;
    }

    .vnd-culinary-img-box {
      height: 420px;
      position: relative;
      overflow: hidden;
    }

    .vnd-culinary-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s ease;
    }

    .vnd-culinary-center-frame:hover .vnd-culinary-img-box img {
      transform: scale(1.05);
    }

    .vnd-chef-stamp {
      position: absolute;
      bottom: 1.5rem;
      left: 1.5rem;
      right: 1.5rem;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(8px);
      padding: 1rem 1.5rem;
      border-radius: 1rem;
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.2);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    /* Col 3: Banquet Velocity & Metrics */
    .vnd-banquet-metrics-card {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.5rem;
      padding: 2rem;
      box-shadow: var(--vnd-shadow-sm);
    }

    .vnd-bmetric-row {
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px dashed var(--vnd-card-border);
    }

    .vnd-bmetric-row:last-child {
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }

    .vnd-bval {
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--vnd-text-main);
    }

    .vnd-blbl {
      font-size: 0.82rem;
      color: var(--vnd-text-muted);
      margin-top: 0.25rem;
    }

    /* =====================================================================
       SECTION 4: DECORATION & PRODUCTION TEAMS - SCENIC FORGE & MATERIAL SWATCH
       ===================================================================== */
    .vnd-section-production {
      padding: 6rem 0;
      background: var(--vnd-surface-muted);
      border-top: 1px solid var(--vnd-card-border);
      border-bottom: 1px solid var(--vnd-card-border);
    }

    .vnd-production-forge-grid {
      display: grid;
      grid-template-columns: 1fr 1.25fr;
      gap: 2.5rem;
      align-items: center;
    }

    .vnd-forge-visual-card {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--vnd-shadow-md);
    }

    .vnd-forge-img-wrap {
      height: 380px;
      position: relative;
      overflow: hidden;
    }

    .vnd-forge-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .vnd-forge-footer {
      padding: 1.75rem;
      background: var(--vnd-surface);
      border-top: 1px solid var(--vnd-card-border);
    }

    /* Right 4-Quadrant Swatchboard */
    .vnd-swatchboard-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.5rem;
    }

    .vnd-swatch-box {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.25rem;
      padding: 1.75rem;
      box-shadow: var(--vnd-shadow-sm);
      cursor: pointer;
      transition: all 0.25s ease;
      position: relative;
    }

    .vnd-swatch-box:hover,
    .vnd-swatch-box.active {
      border-color: var(--vnd-accent);
      transform: translateY(-4px);
      box-shadow: var(--vnd-shadow-md);
    }

    .vnd-swatch-icon {
      width: 2.75rem;
      height: 2.75rem;
      border-radius: 0.75rem;
      background: var(--vnd-accent-glow);
      color: var(--vnd-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
      margin-bottom: 1rem;
    }

    .vnd-swatch-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--vnd-text-main);
      margin-bottom: 0.5rem;
    }

    .vnd-swatch-desc {
      font-size: 0.85rem;
      color: var(--vnd-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 5: TRANSPORT PROVIDERS - VIP LOGISTICS & MOTORCADE MANIFEST
       ===================================================================== */
    .vnd-section-transport {
      padding: 6rem 0;
      position: relative;
    }

    .vnd-transport-telemetry-banner {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.5rem;
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem 2rem;
      box-shadow: var(--vnd-shadow-sm);
      margin-bottom: 3rem;
    }

    .vnd-tarmac-chip {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .vnd-tarmac-icon {
      width: 2.75rem;
      height: 2.75rem;
      border-radius: 0.75rem;
      background: var(--vnd-cyan-glow);
      color: var(--vnd-cyan);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
    }

    .vnd-tarmac-val {
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--vnd-text-main);
      line-height: 1.2;
    }

    .vnd-tarmac-lbl {
      font-size: 0.78rem;
      color: var(--vnd-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .vnd-fleet-split-grid {
      display: grid;
      grid-template-columns: 1.1fr 1fr;
      gap: 2.5rem;
      align-items: start;
    }

    .vnd-fleet-visual-card {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--vnd-shadow-md);
    }

    .vnd-fleet-img-box {
      height: 380px;
      position: relative;
      overflow: hidden;
    }

    .vnd-fleet-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .vnd-fleet-manifest-col {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    .vnd-fleet-item-card {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.25rem;
      padding: 1.75rem;
      box-shadow: var(--vnd-shadow-sm);
      transition: all 0.25s ease;
    }

    .vnd-fleet-item-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--vnd-shadow-md);
      border-color: var(--vnd-cyan);
    }

    .vnd-fitem-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.5rem;
    }

    .vnd-fitem-class {
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--vnd-cyan);
    }

    .vnd-fitem-cap {
      font-size: 0.8rem;
      color: var(--vnd-text-muted);
      font-weight: 600;
    }

    .vnd-fitem-title {
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--vnd-text-main);
      margin-bottom: 0.5rem;
    }

    .vnd-fitem-desc {
      font-size: 0.88rem;
      color: var(--vnd-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 6: VENDOR PARTNERSHIP ENQUIRY - SUPPLY CHAIN GATEWAY
       ===================================================================== */
    .vnd-section-enquiry {
      padding: 6rem 0;
      background: var(--vnd-surface-muted);
      border-top: 1px solid var(--vnd-card-border);
      border-bottom: 1px solid var(--vnd-card-border);
    }

    .vnd-enquiry-crucible-grid {
      display: grid;
      grid-template-columns: 420px 1fr;
      gap: 2.5rem;
      align-items: start;
    }

    .vnd-dossier-card {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--vnd-shadow-md);
    }

    .vnd-dossier-img-box {
      height: 240px;
      position: relative;
      overflow: hidden;
    }

    .vnd-dossier-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .vnd-dossier-body {
      padding: 2rem;
    }

    .vnd-dossier-title {
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--vnd-text-main);
      margin-bottom: 0.75rem;
    }

    .vnd-dossier-desc {
      font-size: 0.9rem;
      color: var(--vnd-text-muted);
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }

    .vnd-dossier-perks {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .vnd-perk-row {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-size: 0.88rem;
      color: var(--vnd-text-main);
    }

    .vnd-perk-row i {
      color: var(--vnd-emerald);
    }

    /* Form Card */
    .vnd-enquiry-form-card {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.5rem;
      padding: 2.5rem;
      box-shadow: var(--vnd-shadow-md);
    }

    .vnd-form-grid-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.25rem;
      margin-bottom: 1.25rem;
    }

    .vnd-field-group {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      margin-bottom: 1.25rem;
    }

    .vnd-label {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--vnd-text-main);
    }

    .vnd-input,
    .vnd-select,
    .vnd-textarea {
      padding: 0.8rem 1.1rem;
      border-radius: 0.6rem;
      border: 1px solid var(--vnd-card-border);
      background: var(--vnd-surface-muted);
      color: var(--vnd-text-main);
      font-size: 0.95rem;
      outline: none;
      transition: all 0.2s ease;
      font-family: inherit;
    }

    .vnd-input:focus,
    .vnd-select:focus,
    .vnd-textarea:focus {
      border-color: var(--vnd-accent);
      background: var(--vnd-surface);
      box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.15);
    }

    /* =====================================================================
       SECTION 7: VENDOR REGISTRATION - ONBOARDING TERMINAL & COMPLIANCE VAULT
       ===================================================================== */
    .vnd-section-registration {
      padding: 6rem 0;
      position: relative;
    }

    /* 3-Step Progress Stepper */
    .vnd-onboard-stepper {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
      margin-bottom: 3rem;
    }

    .vnd-step-pod {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1rem;
      padding: 1.25rem 1.5rem;
      display: flex;
      align-items: center;
      gap: 1rem;
      box-shadow: var(--vnd-shadow-sm);
    }

    .vnd-step-pod.active {
      border-color: var(--vnd-accent);
      background: var(--vnd-surface);
    }

    .vnd-step-num {
      width: 2.25rem;
      height: 2.25rem;
      border-radius: 50%;
      background: var(--vnd-surface-muted);
      color: var(--vnd-text-muted);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.9rem;
    }

    .vnd-step-pod.active .vnd-step-num {
      background: var(--vnd-accent);
      color: #ffffff;
    }

    .vnd-step-text-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--vnd-text-main);
    }

    .vnd-step-text-sub {
      font-size: 0.78rem;
      color: var(--vnd-text-muted);
    }

    /* Registration Terminal Layout */
    .vnd-terminal-grid {
      display: grid;
      grid-template-columns: 380px 1fr;
      gap: 2.5rem;
      align-items: start;
    }

    .vnd-terminal-shield-card {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--vnd-shadow-md);
      position: sticky;
      top: 100px;
    }

    .vnd-shield-img-box {
      height: 220px;
      position: relative;
      overflow: hidden;
    }

    .vnd-shield-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .vnd-shield-body {
      padding: 2rem;
    }

    .vnd-shield-title {
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--vnd-text-main);
      margin-bottom: 0.5rem;
    }

    .vnd-shield-desc {
      font-size: 0.88rem;
      color: var(--vnd-text-muted);
      line-height: 1.55;
      margin-bottom: 1.5rem;
    }

    .vnd-reg-terminal-card {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.5rem;
      padding: 2.5rem;
      box-shadow: var(--vnd-shadow-md);
    }

    .vnd-dropzone-box {
      border: 2px dashed var(--vnd-card-border);
      border-radius: 0.75rem;
      padding: 2rem;
      text-align: center;
      background: var(--vnd-surface-muted);
      margin-bottom: 1.75rem;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .vnd-dropzone-box:hover {
      border-color: var(--vnd-accent);
      background: var(--vnd-accent-glow);
    }

    .vnd-drop-icon {
      font-size: 2rem;
      color: var(--vnd-accent);
      margin-bottom: 0.75rem;
    }

    /* Modal for Submission Feedback */
    .vnd-modal-overlay {
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

    .vnd-modal-card {
      background: var(--vnd-surface);
      border: 1px solid var(--vnd-card-border);
      border-radius: 1.5rem;
      max-width: 540px;
      width: 100%;
      padding: 2.5rem;
      box-shadow: var(--vnd-shadow-lg);
      text-align: center;
      position: relative;
    }

    .vnd-modal-close {
      position: absolute;
      top: 1.25rem;
      right: 1.25rem;
      background: transparent;
      border: none;
      color: var(--vnd-text-muted);
      font-size: 1.25rem;
      cursor: pointer;
    }

    body.rtl .vnd-modal-close {
      right: auto;
      left: 1.25rem;
    }

    /* Responsive Queries */
    @media (max-width: 1100px) {
      .vnd-venue-bento-grid { grid-template-columns: 1fr; }
      .vnd-av-console-grid { grid-template-columns: 1fr; }
      .vnd-gastronomy-atelier-grid { grid-template-columns: 1fr; }
      .vnd-production-forge-grid { grid-template-columns: 1fr; }
      .vnd-fleet-split-grid { grid-template-columns: 1fr; }
      .vnd-enquiry-crucible-grid { grid-template-columns: 1fr; }
      .vnd-terminal-grid { grid-template-columns: 1fr; }
    }

    @media (max-width: 768px) {
      .vnd-ticker-metrics { flex-direction: column; align-items: flex-start; }
      .vnd-av-telemetry-strip { grid-template-columns: repeat(2, 1fr); }
      .vnd-transport-telemetry-banner { grid-template-columns: repeat(2, 1fr); }
      .vnd-onboard-stepper { grid-template-columns: 1fr; }
      .vnd-form-grid-2 { grid-template-columns: 1fr; }
      .vnd-title { font-size: 2rem; }
      .vnd-pavilion-specs-strip { grid-template-columns: 1fr; }
      .vnd-swatchboard-grid { grid-template-columns: 1fr; }
    }
"""

    # HTML for the redesigned vendors page
    new_vnd_content = """
  <!-- MAIN VENDORS CONTENT WRAPPER -->
  <main class="vnd-page-wrap">

    <!-- =====================================================================
         SECTION 1: VENUE PARTNERS (ATRIUM BENTO & ALLIANCE GALLERY)
         ===================================================================== -->
    <section id="venue-partners" class="vnd-section-venues">
      <div class="vnd-container">
        <!-- Section Header -->
        <div class="vnd-section-head framer-atrium-unfold">
          <div class="vnd-badge"><i class="fas fa-building-flag"></i> Sovereign Venue Alliance</div>
          <h2 class="vnd-title">Venue Partners & <span class="vnd-title-gradient">Sovereign Atriums</span></h2>
          <p class="vnd-subtitle">Access pre-negotiated master service agreements across premier convention centers, luxury glass atriums, and private historical pavilions with zero client attrition liability.</p>
        </div>

        <!-- Accreditation & Network Ticker -->
        <div class="vnd-venue-ticker-ribbon framer-atrium-unfold">
          <div class="vnd-ticker-metrics">
            <div class="vnd-tmetric-item">
              <div class="vnd-tmetric-icon"><i class="fas fa-landmark"></i></div>
              <div>
                <div class="vnd-tmetric-val">140+ Venues</div>
                <div class="vnd-tmetric-lbl">Pre-Vetted Network</div>
              </div>
            </div>
            <div class="vnd-tmetric-item">
              <div class="vnd-tmetric-icon"><i class="fas fa-chart-area"></i></div>
              <div>
                <div class="vnd-tmetric-val">4.8M Sqft</div>
                <div class="vnd-tmetric-lbl">Certified Plenary Space</div>
              </div>
            </div>
            <div class="vnd-tmetric-item">
              <div class="vnd-tmetric-icon"><i class="fas fa-shield-halved"></i></div>
              <div>
                <div class="vnd-tmetric-val">98.6% MSA</div>
                <div class="vnd-tmetric-lbl">Compliance Rate</div>
              </div>
            </div>
          </div>
          <div class="vnd-cluster-filters">
            <button class="vnd-cluster-btn active" onclick="filterVenueCluster('all', this)"><i class="fas fa-earth-americas"></i> All Locations</button>
            <button class="vnd-cluster-btn" onclick="filterVenueCluster('atrium', this)"><i class="fas fa-gem"></i> Flagship Atriums</button>
            <button class="vnd-cluster-btn" onclick="filterVenueCluster('waterfront', this)"><i class="fas fa-water"></i> Waterfront</button>
            <button class="vnd-cluster-btn" onclick="filterVenueCluster('heritage', this)"><i class="fas fa-monument"></i> Historic Guildhalls</button>
          </div>
        </div>

        <!-- Asymmetric 4-Tier Bento Architectural Gallery -->
        <div class="vnd-venue-bento-grid">
          <!-- Featured Panoramic Grand Pavilion -->
          <div class="vnd-venue-hero-pavilion framer-atrium-unfold">
            <div class="vnd-pavilion-img-wrap">
              <img src="images/vendor_venues.jpg" alt="Grand Sovereign Convention Center Atrium">
              <div class="vnd-pavilion-status-chip">
                <i class="fas fa-certificate"></i> Apex Premier Sovereign Hub
              </div>
            </div>
            <div class="vnd-pavilion-body">
              <h3 class="vnd-pavilion-title">The Grand Meridian Glass Atrium & Convention Center</h3>
              <p class="vnd-pavilion-desc">A certified Tier-1 plenary campus engineered for Fortune 100 global summits, featuring 32ft clear ceiling heights, integrated sub-floor cable trenches, and acoustic STC 58 rating.</p>
              <div class="vnd-pavilion-specs-strip">
                <div class="vnd-pspec-item">
                  <div class="vnd-pspec-val">4,500 Max</div>
                  <div class="vnd-pspec-lbl">Seated Delegates</div>
                </div>
                <div class="vnd-pspec-item">
                  <div class="vnd-pspec-val">32 Ft</div>
                  <div class="vnd-pspec-lbl">Truss Clearance</div>
                </div>
                <div class="vnd-pspec-item">
                  <div class="vnd-pspec-val">45,000 Sqft</div>
                  <div class="vnd-pspec-lbl">Pillarless Hall</div>
                </div>
              </div>
              <button class="vnd-btn vnd-btn-primary" onclick="openVendorModal('The Grand Meridian Atrium Technical Rider')">
                <i class="fas fa-file-contract"></i> Request Venue Technical Rider
              </button>
            </div>
          </div>

          <!-- Staggered Tier Spec Deck -->
          <div class="vnd-staggered-tiers-col">
            <!-- Tier 1 -->
            <div class="vnd-tier-card framer-atrium-unfold" data-cluster="waterfront" onclick="highlightVenue('Waterfront Plenary Pavilion')">
              <div class="vnd-tier-top">
                <span class="vnd-tier-tag">Waterfront Pavilion</span>
                <span class="vnd-tier-cap"><i class="fas fa-users"></i> 2,200 Capacity</span>
              </div>
              <h4 class="vnd-tier-title">The Geodesic Waterfront Plenary Campus</h4>
              <p style="font-size: 0.88rem; color: var(--vnd-text-muted); line-height: 1.5;">Clear-span architectural dome with direct deep-water yacht docking for VIP dignitaries and floor-to-ceiling panoramic harbor vistas.</p>
              <div class="vnd-tier-features">
                <span class="vnd-feat-chip"><i class="fas fa-check"></i> Private Yacht Ingress</span>
                <span class="vnd-feat-chip"><i class="fas fa-check"></i> LEED Platinum</span>
                <span class="vnd-feat-chip"><i class="fas fa-check"></i> Dark Fiber 10Gbps</span>
              </div>
            </div>

            <!-- Tier 2 -->
            <div class="vnd-tier-card framer-atrium-unfold" data-cluster="heritage" onclick="highlightVenue('Imperial Financial Guildhall')">
              <div class="vnd-tier-top">
                <span class="vnd-tier-tag">Historic Guildhall</span>
                <span class="vnd-tier-cap"><i class="fas fa-users"></i> 1,400 Capacity</span>
              </div>
              <h4 class="vnd-tier-title">The Imperial Financial Guildhall & Heritage Ballroom</h4>
              <p style="font-size: 0.88rem; color: var(--vnd-text-muted); line-height: 1.5;">Neoclassical architectural icon outfitted with discreet modern motorized trussing and subterranean VIP holding vaults.</p>
              <div class="vnd-tier-features">
                <span class="vnd-feat-chip"><i class="fas fa-check"></i> Vaulted Ceilings</span>
                <span class="vnd-feat-chip"><i class="fas fa-check"></i> Acoustic Timber</span>
                <span class="vnd-feat-chip"><i class="fas fa-check"></i> Secret Service Cleared</span>
              </div>
            </div>

            <!-- Tier 3 -->
            <div class="vnd-tier-card framer-atrium-unfold" data-cluster="atrium" onclick="highlightVenue('Alpine High-Altitude Lodge')">
              <div class="vnd-tier-top">
                <span class="vnd-tier-tag">Alpine Summit Campus</span>
                <span class="vnd-tier-cap"><i class="fas fa-users"></i> 850 Capacity</span>
              </div>
              <h4 class="vnd-tier-title">The High-Altitude Alpine Executive Retreat Center</h4>
              <p style="font-size: 0.88rem; color: var(--vnd-text-muted); line-height: 1.5;">Ultra-exclusive mountain sanctuary designed for sovereign wealth funds, bilateral negotiations, and private board retreats.</p>
              <div class="vnd-tier-features">
                <span class="vnd-feat-chip"><i class="fas fa-check"></i> Heli-Ingress Only</span>
                <span class="vnd-feat-chip"><i class="fas fa-check"></i> SCIF Audio Isolation</span>
                <span class="vnd-feat-chip"><i class="fas fa-check"></i> 5-Star Concierge</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 2: AUDIO-VISUAL SUPPLIERS (HARDWARE SYNTHESIS & RACK-MOUNT)
         ===================================================================== -->
    <section id="audiovisual-suppliers" class="vnd-section-audiovisual">
      <div class="vnd-container">
        <!-- Section Header -->
        <div class="vnd-section-head framer-rack-mount">
          <div class="vnd-badge"><i class="fas fa-sliders"></i> Broadcast Engineering</div>
          <h2 class="vnd-title">Audio-Visual Suppliers & <span class="vnd-title-gradient">Hardware Synthesis</span></h2>
          <p class="vnd-subtitle">Institutional broadcast partnerships delivering 4K120 SMPTE ST 2110 IP video switching, Dante digital audio networks, and high-density microLED canvas architecture.</p>
        </div>

        <!-- Hardware Telemetry Strip -->
        <div class="vnd-av-telemetry-strip framer-rack-mount">
          <div class="vnd-av-chip">
            <div class="vnd-av-icon"><i class="fas fa-tv"></i></div>
            <div>
              <div class="vnd-av-val">0.9mm Pixel</div>
              <div class="vnd-av-lbl">MicroLED Canvas Pitch</div>
            </div>
          </div>
          <div class="vnd-av-chip">
            <div class="vnd-av-icon"><i class="fas fa-network-wired"></i></div>
            <div>
              <div class="vnd-av-val">SMPTE 2110</div>
              <div class="vnd-av-lbl">Uncompressed IP Routing</div>
            </div>
          </div>
          <div class="vnd-av-chip">
            <div class="vnd-av-icon"><i class="fas fa-headphones"></i></div>
            <div>
              <div class="vnd-av-val">384 Channels</div>
              <div class="vnd-av-lbl">Dante Digital Audio</div>
            </div>
          </div>
          <div class="vnd-av-chip">
            <div class="vnd-av-icon"><i class="fas fa-server"></i></div>
            <div>
              <div class="vnd-av-val">N+2 Hot-Swap</div>
              <div class="vnd-av-lbl">Encore3 Presentation Grid</div>
            </div>
          </div>
        </div>

        <!-- Multi-Panel Broadcast Switcher Interface -->
        <div class="vnd-av-console-grid">
          <!-- Master Video Monitor Frame -->
          <div class="vnd-av-monitor-card framer-rack-mount">
            <div class="vnd-monitor-header">
              <span style="font-size: 0.85rem; font-weight: 700;"><i class="fas fa-satellite-dish text-primary"></i> LIVE BROADCAST CONSOLE • FEED 01</span>
              <div class="vnd-monitor-tally">
                <span class="vnd-tally-dot"></span> LIVE ON-AIR
              </div>
            </div>
            <div class="vnd-monitor-screen">
              <img src="images/vendor_audiovisual.jpg" alt="Broadcast Hardware Engineering Control Console">
            </div>
            <div class="vnd-monitor-controls">
              <div class="vnd-vu-meters-row">
                <span>MASTER STEREO BUS</span>
                <div class="vnd-vu-bar"><div class="vnd-vu-fill"></div></div>
                <span>-6.2 dBFS</span>
              </div>
              <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; color: var(--vnd-text-muted);">
                <span>Colorimetry: Rec.2020 12-Bit HDR</span>
                <button class="vnd-btn vnd-btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;" onclick="openVendorModal('Broadcast Technical Specs')">
                  <i class="fas fa-code-branch"></i> Inquire AV Inventory
                </button>
              </div>
            </div>
          </div>

          <!-- Right Modular Rack Units -->
          <div class="vnd-rack-mount-stack">
            <!-- Rack 1 -->
            <div class="vnd-rack-unit-card framer-rack-mount">
              <div class="vnd-rack-unit-head">
                <span class="vnd-rack-id">Rack Unit 01 • Video Engine</span>
                <span style="font-size: 0.8rem; font-weight: 700; color: var(--vnd-cyan);"><i class="fas fa-microchip"></i> 4K Native</span>
              </div>
              <h4 class="vnd-rack-title">Barco Encore3 & Disguise vx4+ Media Servers</h4>
              <p class="vnd-rack-desc">Ultra-low latency real-time generative visual synthesis and pixel-perfect LED mapping capable of handling 32x 4K60 video outputs concurrently.</p>
              <div class="vnd-rack-specs">
                <div><i class="fas fa-angle-right"></i> True 12-bit 4:4:4 processing pipeline</div>
                <div><i class="fas fa-angle-right"></i> Sub-frame frame synchronization across multi-screen canvases</div>
              </div>
            </div>

            <!-- Rack 2 -->
            <div class="vnd-rack-unit-card framer-rack-mount">
              <div class="vnd-rack-unit-head">
                <span class="vnd-rack-id">Rack Unit 02 • Acoustic Grid</span>
                <span style="font-size: 0.8rem; font-weight: 700; color: var(--vnd-cyan);"><i class="fas fa-volume-high"></i> Spatial Audio</span>
              </div>
              <h4 class="vnd-rack-title">L-Acoustics K2 & Shure Axient Digital Array</h4>
              <p class="vnd-rack-desc">Stadia-grade line array acoustic reinforcement with steerable beamforming technology to eliminate room slap and deliver pristine vocal intelligibility.</p>
              <div class="vnd-rack-specs">
                <div><i class="fas fa-angle-right"></i> Quadversity antenna frequency diversity protection</div>
                <div><i class="fas fa-angle-right"></i> Real-time RF spectrum analysis preventing microphonic interference</div>
              </div>
            </div>

            <!-- Rack 3 -->
            <div class="vnd-rack-unit-card framer-rack-mount">
              <div class="vnd-rack-unit-head">
                <span class="vnd-rack-id">Rack Unit 03 • Kinetic Automation</span>
                <span style="font-size: 0.8rem; font-weight: 700; color: var(--vnd-cyan);"><i class="fas fa-arrows-spin"></i> grandMA3</span>
              </div>
              <h4 class="vnd-rack-title">grandMA3 Full-Size & Kinetic Rigging Hoists</h4>
              <p class="vnd-rack-desc">SIL-3 certified variable-speed computerized chain hoists controlling dynamic stage elements, kinetic chandelier rings, and automated moving fixtures.</p>
              <div class="vnd-rack-specs">
                <div><i class="fas fa-angle-right"></i> 100,000 parameters per lighting network session</div>
                <div><i class="fas fa-angle-right"></i> Millimeter-accurate positional load cell feedback telemetry</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 3: CATERING PARTNERS (CULINARY GUILD & TASTING ATELIER)
         ===================================================================== -->
    <section id="catering-partners" class="vnd-section-catering">
      <div class="vnd-container">
        <!-- Section Header -->
        <div class="vnd-section-head framer-gastronomy-float">
          <div class="vnd-badge"><i class="fas fa-utensils"></i> Michelin-Caliber Gastronomy</div>
          <h2 class="vnd-title">Catering Partners & <span class="vnd-title-gradient">Culinary Guild</span></h2>
          <p class="vnd-subtitle">Elevate executive summit hospitality with farm-to-table culinary ateliers, certified master sommeliers, and synchronized banquet services engineered for zero downtime.</p>
        </div>

        <!-- Culinary Accreditation Pill Bar -->
        <div class="vnd-culinary-badge-bar framer-gastronomy-float">
          <div class="vnd-cbadge-pill"><i class="fas fa-leaf"></i> 100% Farm-To-Summit Sourcing</div>
          <div class="vnd-cbadge-pill"><i class="fas fa-award"></i> Michelin Star Mentored Chefs</div>
          <div class="vnd-cbadge-pill"><i class="fas fa-shield-virus"></i> ISO-22000 Food Safety</div>
          <div class="vnd-cbadge-pill"><i class="fas fa-recycle"></i> Zero-Food-Waste Donation Certified</div>
        </div>

        <!-- 3-Column Asymmetric Atelier -->
        <div class="vnd-gastronomy-atelier-grid">
          <!-- Col 1: Curated Tasting Menu -->
          <div class="vnd-tasting-menu-card framer-gastronomy-float">
            <h4 class="vnd-menu-title">Executive Gala Flight</h4>
            <div class="vnd-course-item">
              <div class="vnd-course-num">Course 01 • Cold Harvest</div>
              <div class="vnd-course-name">Botanical Heirloom Tartare</div>
              <div class="vnd-course-tags">Truffle Emulsion • Micro Herbs • GF / Vegan</div>
            </div>
            <div class="vnd-course-item">
              <div class="vnd-course-num">Course 02 • Plenary Main</div>
              <div class="vnd-course-name">Wild-Caught Chilean Sea Bass</div>
              <div class="vnd-course-tags">Saffron Beurre Blanc • Romanesco • Halal</div>
            </div>
            <div class="vnd-course-item">
              <div class="vnd-course-num">Course 03 • Grand Finale</div>
              <div class="vnd-course-name">Deconstructed Valrhona Ganache</div>
              <div class="vnd-course-tags">Smoked Sea Salt • Gold Leaf • Organic</div>
            </div>
            <button class="vnd-btn vnd-btn-outline" style="width: 100%; margin-top: 1rem;" onclick="openVendorModal('Full Culinary Flight Menu')">
              <i class="fas fa-file-pdf"></i> Download Dietary Guide
            </button>
          </div>

          <!-- Col 2: Center Featured Gastronomic Visual Frame -->
          <div class="vnd-culinary-center-frame framer-gastronomy-float">
            <div class="vnd-culinary-img-box">
              <img src="images/vendor_catering.jpg" alt="Culinary Gastronomic Artistry">
            </div>
            <div class="vnd-chef-stamp">
              <div>
                <div style="font-size: 0.8rem; color: #fbbf24; font-weight: 700; text-transform: uppercase;">Culinary Director</div>
                <div style="font-weight: 800; font-size: 1.1rem;">Chef Laurent Moreaux</div>
              </div>
              <i class="fas fa-medal text-warning" style="font-size: 1.75rem;"></i>
            </div>
          </div>

          <!-- Col 3: Banquet Velocity & Metrics -->
          <div class="vnd-banquet-metrics-card framer-gastronomy-float">
            <h4 class="vnd-menu-title">Banquet Telemetry</h4>
            <div class="vnd-bmetric-row">
              <div class="vnd-bval">2,500 Guests</div>
              <div class="vnd-blbl">Synchronized Plated Gala Serving in &lt; 14 Mins</div>
            </div>
            <div class="vnd-bmetric-row">
              <div class="vnd-bval">100% Isolated</div>
              <div class="vnd-blbl">Dedicated Allergen-Safe Clean-Air Kitchen Lines</div>
            </div>
            <div class="vnd-bmetric-row">
              <div class="vnd-bval">1:8 Ratio</div>
              <div class="vnd-blbl">Trained Butler-to-Table Service for VIP Delegates</div>
            </div>
            <div class="vnd-bmetric-row">
              <div class="vnd-bval">Zero Landfill</div>
              <div class="vnd-blbl">100% Compostable Packaging & Excess Donation</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 4: DECORATION & PRODUCTION TEAMS (SCENIC FORGE & MATERIAL SWATCH)
         ===================================================================== -->
    <section id="production-teams" class="vnd-section-production">
      <div class="vnd-container">
        <!-- Section Header -->
        <div class="vnd-section-head framer-scenic-forge">
          <div class="vnd-badge"><i class="fas fa-hammer"></i> Master Stagecraft Atelier</div>
          <h2 class="vnd-title">Decoration & Production <span class="vnd-title-gradient">Teams & Scenic Forge</span></h2>
          <p class="vnd-subtitle">From custom sculptural keynotes to architectural stage engineering, our fabrication facilities translate 3D CAD blueprints into awe-inspiring physical realities.</p>
        </div>

        <div class="vnd-production-forge-grid">
          <!-- Left Visual Card -->
          <div class="vnd-forge-visual-card framer-scenic-forge">
            <div class="vnd-forge-img-wrap">
              <img src="images/vendor_production.jpg" alt="Master Scenic Fabrication Workshop">
            </div>
            <div class="vnd-forge-footer">
              <h4 style="font-size: 1.25rem; font-weight: 800; color: var(--vnd-text-main); margin-bottom: 0.5rem;">CNC Scenic Milling & Structural Fabrication Facility</h4>
              <p style="font-size: 0.88rem; color: var(--vnd-text-muted); line-height: 1.5; margin-bottom: 1rem;">Operating 3 shifts 24/7 during pre-summit build weeks, producing fire-rated stage sets, custom speaker rostrums, and immersive sponsor activations.</p>
              <div style="display: flex; gap: 1rem; align-items: center; font-size: 0.8rem; font-weight: 700; color: var(--vnd-accent);">
                <span><i class="fas fa-shield"></i> NFPA 701 Fire Code Certified</span>
                <span><i class="fas fa-check-double"></i> 48-Hour Rapid Fabrication</span>
              </div>
            </div>
          </div>

          <!-- Right 4-Quadrant Swatchboard -->
          <div class="vnd-swatchboard-grid">
            <div class="vnd-swatch-box active framer-scenic-forge" onclick="selectSwatch(this, 'Structural Trussing')">
              <div class="vnd-swatch-icon"><i class="fas fa-cubes-stacked"></i></div>
              <h4 class="vnd-swatch-title">Structural Aluminum Box Trussing</h4>
              <p class="vnd-swatch-desc">TUV-certified 6082-T6 aircraft-grade alloy supporting up to 3,500 kg per node for expansive overhead kinetic canopies.</p>
            </div>
            <div class="vnd-swatch-box framer-scenic-forge" onclick="selectSwatch(this, 'Acoustic Woodcraft')">
              <div class="vnd-swatch-icon"><i class="fas fa-tree"></i></div>
              <h4 class="vnd-swatch-title">Architectural Acoustic Woodcraft</h4>
              <p class="vnd-swatch-desc">Sustainably harvested fluted American walnut paneling engineered with hidden micro-perforations to dampen auditorium reverberation.</p>
            </div>
            <div class="vnd-swatch-box framer-scenic-forge" onclick="selectSwatch(this, 'Curved LED Volumes')">
              <div class="vnd-swatch-icon"><i class="fas fa-display"></i></div>
              <h4 class="vnd-swatch-title">Curved Bezel-Free Stage Fascia</h4>
              <p class="vnd-swatch-desc">Custom concave framing holding seamless video walls, creating an infinite immersive horizon behind plenary speakers.</p>
            </div>
            <div class="vnd-swatch-box framer-scenic-forge" onclick="selectSwatch(this, 'IFR Eco-Draping')">
              <div class="vnd-swatch-icon"><i class="fas fa-scroll"></i></div>
              <h4 class="vnd-swatch-title">IFR Velour & Acoustic Draping</h4>
              <p class="vnd-swatch-desc">Inherently flame-retardant heavyweight black masking drape eliminating light bleed and ambient backstage noise.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 5: TRANSPORT PROVIDERS (VIP LOGISTICS & MOTORCADE MANIFEST)
         ===================================================================== -->
    <section id="transport-providers" class="vnd-section-transport">
      <div class="vnd-container">
        <!-- Section Header -->
        <div class="vnd-section-head framer-fleet-manifest">
          <div class="vnd-badge"><i class="fas fa-car-rear"></i> Executive Mobility</div>
          <h2 class="vnd-title">Transport Providers & <span class="vnd-title-gradient">VIP Motorcade Logistics</span></h2>
          <p class="vnd-subtitle">Flawless dignitary movement across municipal corridors, dedicated executive airport tarmac transfers, and helicopter charters operating under real-time telematics.</p>
        </div>

        <!-- Mobility Operations Telemetry Strip -->
        <div class="vnd-transport-telemetry-banner framer-fleet-manifest">
          <div class="vnd-tarmac-chip">
            <div class="vnd-tarmac-icon"><i class="fas fa-shield-halved"></i></div>
            <div>
              <div class="vnd-tarmac-val">B6 Armored</div>
              <div class="vnd-tarmac-lbl">Ballistic Rating Available</div>
            </div>
          </div>
          <div class="vnd-tarmac-chip">
            <div class="vnd-tarmac-icon"><i class="fas fa-van-shuttle"></i></div>
            <div>
              <div class="vnd-tarmac-val">250+ Vehicles</div>
              <div class="vnd-tarmac-lbl">Dedicated Fleet Roster</div>
            </div>
          </div>
          <div class="vnd-tarmac-chip">
            <div class="vnd-tarmac-icon"><i class="fas fa-helicopter"></i></div>
            <div>
              <div class="vnd-tarmac-val">&lt; 8 Mins</div>
              <div class="vnd-tarmac-lbl">Airport-to-Rooftop Heli</div>
            </div>
          </div>
          <div class="vnd-tarmac-chip">
            <div class="vnd-tarmac-icon"><i class="fas fa-route"></i></div>
            <div>
              <div class="vnd-tarmac-val">100% Real-Time</div>
              <div class="vnd-tarmac-lbl">GPS Telematics & Escort</div>
            </div>
          </div>
        </div>

        <div class="vnd-fleet-split-grid">
          <!-- Left Visual Card -->
          <div class="vnd-fleet-visual-card framer-fleet-manifest">
            <div class="vnd-fleet-img-box">
              <img src="images/vendor_transport.jpg" alt="Executive Tarmac Motorcade Dispatch">
            </div>
            <div style="padding: 1.75rem; background: var(--vnd-surface);">
              <h4 style="font-size: 1.25rem; font-weight: 800; color: var(--vnd-text-main); margin-bottom: 0.5rem;">Dedicated Aviation Tarmac Interlinks</h4>
              <p style="font-size: 0.88rem; color: var(--vnd-text-muted); line-height: 1.5;">Direct airside tarmac greeting for private corporate aircraft with discreet baggage escorts, municipal motorcade staging, and automated diplomatic clearances.</p>
            </div>
          </div>

          <!-- Right Fleet Fleet Manifest -->
          <div class="vnd-fleet-manifest-col">
            <!-- Class 1 -->
            <div class="vnd-fleet-item-card framer-fleet-manifest">
              <div class="vnd-fitem-head">
                <span class="vnd-fitem-class">Category Alpha • Dignitary Fleet</span>
                <span class="vnd-fitem-cap">Up to 3 Passengers</span>
              </div>
              <h4 class="vnd-fitem-title">Mercedes-Maybach S680 & Armored Suburbans</h4>
              <p class="vnd-fitem-desc">Chauffeured by law-enforcement trained executive protection drivers with privacy partition, secure Wi-Fi, and active route clearance.</p>
            </div>

            <!-- Class 2 -->
            <div class="vnd-fleet-item-card framer-fleet-manifest">
              <div class="vnd-fitem-head">
                <span class="vnd-fitem-class">Category Beta • Executive Shuttles</span>
                <span class="vnd-fitem-cap">14 to 20 Delegates</span>
              </div>
              <h4 class="vnd-fitem-title">Mercedes-Benz Sprinter Executive Luxury Coaches</h4>
              <p class="vnd-fitem-desc">Individual reclining Italian leather captain chairs, conference tables, multi-screen presentations, and premium charging consoles.</p>
            </div>

            <!-- Class 3 -->
            <div class="vnd-fleet-item-card framer-fleet-manifest">
              <div class="vnd-fitem-head">
                <span class="vnd-fitem-class">Category Gamma • Aviation Charters</span>
                <span class="vnd-fitem-cap">6 to 8 VIPs</span>
              </div>
              <h4 class="vnd-fitem-title">Twin-Engine Sikorsky S-76 & Airbus H145 Helicopters</h4>
              <p class="vnd-fitem-desc">Point-to-point executive rooftop transfers bypassing metropolitan traffic jams during high-stakes summit arrivals.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 6: VENDOR PARTNERSHIP ENQUIRY (SUPPLY CHAIN GATEWAY)
         ===================================================================== -->
    <section id="partnership-enquiry" class="vnd-section-enquiry">
      <div class="vnd-container">
        <!-- Section Header -->
        <div class="vnd-section-head framer-procurement-gate">
          <div class="vnd-badge"><i class="fas fa-handshake"></i> Procurement Alliance</div>
          <h2 class="vnd-title">Vendor Partnership <span class="vnd-title-gradient">Enquiry Gateway</span></h2>
          <p class="vnd-subtitle">Join our preferred global tier-one supply chain. We offer prompt Net-15 payment terms, high-volume recurring conference master contracts, and collaborative growth.</p>
        </div>

        <div class="vnd-enquiry-crucible-grid">
          <!-- Left Dossier Card -->
          <div class="vnd-dossier-card framer-procurement-gate">
            <div class="vnd-dossier-img-box">
              <img src="images/vendor_partnership.jpg" alt="Corporate Vendor Partnership Agreement">
            </div>
            <div class="vnd-dossier-body">
              <h4 class="vnd-dossier-title">The Apex Supplier Covenant</h4>
              <p class="vnd-dossier-desc">We view our vendors as co-architects of extraordinary human experiences. Our partners enjoy institutional stability and prompt compensation.</p>
              <div class="vnd-dossier-perks">
                <div class="vnd-perk-row"><i class="fas fa-circle-check"></i> Guaranteed Net-15 Day Invoicing Settlement</div>
                <div class="vnd-perk-row"><i class="fas fa-circle-check"></i> Multi-Year Master Service Agreements</div>
                <div class="vnd-perk-row"><i class="fas fa-circle-check"></i> Shared Production CAD Workspaces</div>
                <div class="vnd-perk-row"><i class="fas fa-circle-check"></i> Mutual Non-Disclosure & IP Protection</div>
              </div>
            </div>
          </div>

          <!-- Right Form Card -->
          <div class="vnd-enquiry-form-card framer-procurement-gate">
            <h4 style="font-size: 1.4rem; font-weight: 800; color: var(--vnd-text-main); margin-bottom: 1.5rem;">Supplier Partnership Inquiry</h4>
            <form onsubmit="handlePartnershipSubmit(event)">
              <div class="vnd-form-grid-2">
                <div class="vnd-field-group">
                  <label class="vnd-label">Company / Enterprise Name *</label>
                  <input type="text" required class="vnd-input" placeholder="e.g. Apex Staging & Audio Ltd">
                </div>
                <div class="vnd-field-group">
                  <label class="vnd-label">Supplier Category *</label>
                  <select required class="vnd-select">
                    <option value="">Select Primary Domain...</option>
                    <option value="venues">Venue & Convention Facility</option>
                    <option value="av">Audio-Visual & Lighting Tech</option>
                    <option value="catering">Gastronomy & Banquet Catering</option>
                    <option value="scenic">Scenic Decoration & Fabrication</option>
                    <option value="transport">VIP Motorcade & Mobility</option>
                    <option value="specialized">Other Specialized Production</option>
                  </select>
                </div>
              </div>
              <div class="vnd-form-grid-2">
                <div class="vnd-field-group">
                  <label class="vnd-label">Primary Business Email *</label>
                  <input type="email" required class="vnd-input" placeholder="procurement@company.com">
                </div>
                <div class="vnd-field-group">
                  <label class="vnd-label">Direct Phone / Hotline *</label>
                  <input type="tel" required class="vnd-input" placeholder="+1 (555) 000-0000">
                </div>
              </div>
              <div class="vnd-form-grid-2">
                <div class="vnd-field-group">
                  <label class="vnd-label">Annual Production Volume</label>
                  <select class="vnd-select">
                    <option>$1,000,000 - $5,000,000</option>
                    <option>$5,000,000 - $15,000,000</option>
                    <option>$15,000,000+</option>
                  </select>
                </div>
                <div class="vnd-field-group">
                  <label class="vnd-label">Geographic Coverage</label>
                  <input type="text" class="vnd-input" placeholder="e.g. North America & Western Europe">
                </div>
              </div>
              <div class="vnd-field-group">
                <label class="vnd-label">Capability Summary & Technical Distinctions *</label>
                <textarea rows="4" required class="vnd-textarea" placeholder="Describe equipment inventory, staff certifications, insurance ratings, and notable corporate references..."></textarea>
              </div>
              <button type="submit" class="vnd-btn vnd-btn-primary" style="width: 100%;">
                <i class="fas fa-paper-plane"></i> Submit Supplier Partnership Application
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 7: VENDOR REGISTRATION (ONBOARDING TERMINAL & COMPLIANCE VAULT)
         ===================================================================== -->
    <section id="vendor-registration" class="vnd-section-registration">
      <div class="vnd-container">
        <!-- Section Header -->
        <div class="vnd-section-head framer-terminal-onboard">
          <div class="vnd-badge"><i class="fas fa-shield-check"></i> Official Onboarding</div>
          <h2 class="vnd-title">Vendor Registration & <span class="vnd-title-gradient">Compliance Terminal</span></h2>
          <p class="vnd-subtitle">Formalize legal credentialing, upload certificates of insurance (COI), and counter-sign standard operating procedures to activate production vendor dispatch.</p>
        </div>

        <!-- 3-Step Progress Stepper -->
        <div class="vnd-onboard-stepper framer-terminal-onboard">
          <div class="vnd-step-pod active">
            <div class="vnd-step-num">1</div>
            <div>
              <div class="vnd-step-text-title">Entity Verification</div>
              <div class="vnd-step-text-sub">Tax ID, DUNS & Legal Entity</div>
            </div>
          </div>
          <div class="vnd-step-pod">
            <div class="vnd-step-num">2</div>
            <div>
              <div class="vnd-step-text-title">Insurance & Policy</div>
              <div class="vnd-step-text-sub">$10M General Liability COI</div>
            </div>
          </div>
          <div class="vnd-step-pod">
            <div class="vnd-step-num">3</div>
            <div>
              <div class="vnd-step-text-title">MSA Activation</div>
              <div class="vnd-step-text-sub">Digital Signature & Dispatch ID</div>
            </div>
          </div>
        </div>

        <!-- Registration Terminal Layout -->
        <div class="vnd-terminal-grid">
          <!-- Left Shield Card -->
          <div class="vnd-terminal-shield-card framer-terminal-onboard">
            <div class="vnd-shield-img-box">
              <img src="images/vendor_registration.jpg" alt="Certified Vendor Onboarding Digital Terminal">
            </div>
            <div class="vnd-shield-body">
              <h4 class="vnd-shield-title">Compliance Escrow Portal</h4>
              <p class="vnd-shield-desc">All submitted financial records, W-9 declarations, and liability certificates are encrypted with AES-256 standard and stored in isolated escrow.</p>
              <div style="background: var(--vnd-surface-muted); padding: 1rem; border-radius: 0.75rem; border: 1px solid var(--vnd-card-border); font-size: 0.8rem; color: var(--vnd-text-muted);">
                <div><strong>Compliance Desk:</strong> 24/7 Fast-Track</div>
                <div><strong>Standard Turnaround:</strong> &lt; 24 Hours</div>
                <div><strong>Assistance:</strong> vendor-support@apexevents.com</div>
              </div>
            </div>
          </div>

          <!-- Right Form Console -->
          <div class="vnd-reg-terminal-card framer-terminal-onboard">
            <h4 style="font-size: 1.4rem; font-weight: 800; color: var(--vnd-text-main); margin-bottom: 1.5rem;">Corporate Entity Credentialing Terminal</h4>
            <form onsubmit="handleRegistrationSubmit(event)">
              <div class="vnd-form-grid-2">
                <div class="vnd-field-group">
                  <label class="vnd-label">Legal Entity Name (As Registered) *</label>
                  <input type="text" required class="vnd-input" placeholder="Legal registered corporate entity">
                </div>
                <div class="vnd-field-group">
                  <label class="vnd-label">Federal Tax ID / EIN / VAT *</label>
                  <input type="text" required class="vnd-input" placeholder="XX-XXXXXXX">
                </div>
              </div>
              <div class="vnd-form-grid-2">
                <div class="vnd-field-group">
                  <label class="vnd-label">DUNS Number (If Applicable)</label>
                  <input type="text" class="vnd-input" placeholder="9-digit DUNS number">
                </div>
                <div class="vnd-field-group">
                  <label class="vnd-label">Insurance Carrier Name *</label>
                  <input type="text" required class="vnd-input" placeholder="e.g. Travelers, Chubb, Zurich">
                </div>
              </div>

              <!-- Interactive Document Dropzone -->
              <div class="vnd-field-group">
                <label class="vnd-label">Upload Certificate of Insurance & W-9 (PDF) *</label>
                <div class="vnd-dropzone-box" onclick="simulateFileUpload()">
                  <div class="vnd-drop-icon"><i class="fas fa-cloud-arrow-up"></i></div>
                  <div id="dropzoneText" style="font-weight: 700; color: var(--vnd-text-main);">Drag & Drop COI, W-9, or Click to Browse</div>
                  <div style="font-size: 0.8rem; color: var(--vnd-text-muted); margin-top: 0.25rem;">Supported formats: PDF, DOCX, ZIP (Max 25MB)</div>
                </div>
              </div>

              <div class="vnd-field-group">
                <label style="display: flex; align-items: flex-start; gap: 0.75rem; font-size: 0.85rem; color: var(--vnd-text-muted); cursor: pointer;">
                  <input type="checkbox" required style="margin-top: 0.25rem;">
                  <span>I certify that all supplied entity information, insurance riders, and banking designations are accurate and compliant with ISO-20121 supply chain standards.</span>
                </label>
              </div>

              <button type="submit" class="vnd-btn vnd-btn-primary" style="width: 100%;">
                <i class="fas fa-shield-halved"></i> Verify & Finalize Vendor Registration
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Interactive Feedback Modal -->
  <div id="vndFeedbackModal" class="vnd-modal-overlay">
    <div class="vnd-modal-card">
      <button class="vnd-modal-close" onclick="closeVndModal()">&times;</button>
      <div style="width: 4rem; height: 4rem; border-radius: 1rem; background: var(--vnd-emerald-glow); color: var(--vnd-emerald); display: flex; align-items: center; justify-content: center; font-size: 1.85rem; margin: 0 auto 1.5rem auto;">
        <i class="fas fa-circle-check"></i>
      </div>
      <h3 id="vndModalTitle" style="font-size: 1.5rem; font-weight: 800; color: var(--vnd-text-main); margin-bottom: 0.5rem;">Application Transmitted</h3>
      <p id="vndModalDesc" style="font-size: 0.95rem; color: var(--vnd-text-muted); line-height: 1.55; margin-bottom: 2rem;">Your credentials have been securely routed to the Apex Procurement Desk. A Vendor Success Manager will reach out within 24 business hours.</p>
      <button class="vnd-btn vnd-btn-primary" onclick="closeVndModal()">Return to Portal</button>
    </div>
  </div>
"""

    # Page Interactive Scripts
    new_vnd_scripts = """
  <!-- =====================================================================
       INTERACTIVE VENDORS PAGE CONTROLLER SCRIPT
       ===================================================================== -->
  <script>
    // 1. Intersection Observer for Unique Framer Motion Animations
    document.addEventListener('DOMContentLoaded', function() {
      var framerElements = document.querySelectorAll(
        '.framer-atrium-unfold, ' +
        '.framer-rack-mount, ' +
        '.framer-gastronomy-float, ' +
        '.framer-scenic-forge, ' +
        '.framer-fleet-manifest, ' +
        '.framer-procurement-gate, ' +
        '.framer-terminal-onboard'
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

    // 2. Venue Cluster Filter
    function filterVenueCluster(cluster, btn) {
      var btns = document.querySelectorAll('.vnd-cluster-btn');
      btns.forEach(function(b) { b.classList.remove('active'); });
      if (btn) btn.classList.add('active');

      var cards = document.querySelectorAll('.vnd-tier-card');
      cards.forEach(function(card) {
        if (cluster === 'all' || card.getAttribute('data-cluster') === cluster) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    }

    function highlightVenue(name) {
      alert('Selected Venue Campus: ' + name + '\\nPreparing technical spatial dimensions and floorplan dossier.');
    }

    // 3. Scenic Forge Swatch Selector
    function selectSwatch(card, name) {
      var boxes = document.querySelectorAll('.vnd-swatch-box');
      boxes.forEach(function(b) { b.classList.remove('active'); });
      card.classList.add('active');
    }

    // 4. Dropzone Simulator
    function simulateFileUpload() {
      var textEl = document.getElementById('dropzoneText');
      if (textEl) {
        textEl.innerHTML = '<i class="fas fa-check text-success"></i> COI_Apex_2026_Certified.pdf (4.8 MB) Attached';
        textEl.style.color = '#059669';
      }
    }

    // 5. Form Submissions & Feedback Modals
    function handlePartnershipSubmit(e) {
      e.preventDefault();
      var modal = document.getElementById('vndFeedbackModal');
      var title = document.getElementById('vndModalTitle');
      var desc = document.getElementById('vndModalDesc');
      if (title) title.textContent = 'Partnership Application Transmitted';
      if (desc) desc.textContent = 'Your company portfolio and capability profile have been assigned tracking code APX-VND-' + Math.floor(1000 + Math.random() * 9000) + '. Our procurement director will review within 24 hours.';
      if (modal) modal.style.display = 'flex';
      e.target.reset();
    }

    function handleRegistrationSubmit(e) {
      e.preventDefault();
      var modal = document.getElementById('vndFeedbackModal');
      var title = document.getElementById('vndModalTitle');
      var desc = document.getElementById('vndModalDesc');
      if (title) title.textContent = 'Vendor Credentials Registered';
      if (desc) desc.textContent = 'Your entity tax documentation, COI certificates, and compliance declarations have been cryptographically secured in escrow under Dispatch ID #VP-' + Math.floor(10000 + Math.random() * 90000) + '.';
      if (modal) modal.style.display = 'flex';
      e.target.reset();
      var drop = document.getElementById('dropzoneText');
      if (drop) {
        drop.textContent = 'Drag & Drop COI, W-9, or Click to Browse';
        drop.style.color = '';
      }
    }

    function openVendorModal(itemName) {
      var modal = document.getElementById('vndFeedbackModal');
      var title = document.getElementById('vndModalTitle');
      var desc = document.getElementById('vndModalDesc');
      if (title) title.textContent = 'Documentation Queued';
      if (desc) desc.textContent = 'Technical specifications and procurement riders for "' + itemName + '" are ready for transmission. Please check your corporate inbox.';
      if (modal) modal.style.display = 'flex';
    }

    function closeVndModal() {
      var modal = document.getElementById('vndFeedbackModal');
      if (modal) modal.style.display = 'none';
    }
  </script>
"""

    # Assemble complete document
    final_html = (
        nav_head_up_to_style
        + new_vnd_css
        + "\n  </style>"
        + nav_mid[len("</style>"):]
        + new_vnd_content
        + footer_full
        + new_vnd_scripts
        + closing_part
    )

    with open('vendors.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print("Successfully built redesigned vendors.html! Total length:", len(final_html))

if __name__ == '__main__':
    generate_vendors()
