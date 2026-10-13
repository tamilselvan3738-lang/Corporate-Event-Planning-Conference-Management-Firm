import os

def generate_resources():
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

    # CSS for the new resources.html layout
    new_res_css = """
    /* =====================================================================
       REDESIGNED RESOURCES ARCHITECTURE: KNOWLEDGE ARCHIVE & MISSION INTEL
       Supports Light Mode, Dark Mode (body.dark), and RTL (body.rtl)
       ===================================================================== */
    :root {
      --res-primary: #1e3a8a;
      --res-primary-dark: #0f172a;
      --res-accent: #d97706;
      --res-accent-light: #fbbf24;
      --res-accent-glow: rgba(217, 119, 6, 0.16);
      --res-teal: #0d9488;
      --res-teal-glow: rgba(13, 148, 136, 0.16);
      --res-emerald: #059669;
      --res-bg: #f8fafc;
      --res-surface: #ffffff;
      --res-surface-muted: #f1f5f9;
      --res-card-border: #e2e8f0;
      --res-text-main: #0f172a;
      --res-text-muted: #64748b;
      --res-text-light: #94a3b8;
      --res-gold-gradient: linear-gradient(135deg, #b45309 0%, #d97706 50%, #f59e0b 100%);
      --res-blue-gradient: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      --res-teal-gradient: linear-gradient(135deg, #0f766e 0%, #0d9488 100%);
      --res-shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --res-shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.07), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
      --res-shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      --res-shadow-glow: 0 0 25px rgba(217, 119, 6, 0.22);
    }

    body.dark {
      --res-bg: #070b14;
      --res-surface: #0f172a;
      --res-surface-muted: #131d33;
      --res-card-border: #1e293b;
      --res-text-main: #f8fafc;
      --res-text-muted: #94a3b8;
      --res-text-light: #64748b;
      --res-blue-gradient: linear-gradient(135deg, #070b14 0%, #172554 100%);
    }

    /* RTL Support */
    body.rtl .res-section-head { text-align: right; }
    body.rtl .res-badge i { margin-left: 0.5rem; margin-right: 0; }
    body.rtl .res-btn i { margin-right: 0.5rem; margin-left: 0; }

    /* Base Container */
    .res-page-wrap {
      background-color: var(--res-bg);
      color: var(--res-text-main);
      font-family: 'Inter', system-ui, sans-serif;
      overflow-x: hidden;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    .res-container {
      max-width: 1320px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }

    /* SECTION HEADER STYLING */
    .res-section-head {
      margin-bottom: 3.5rem;
      position: relative;
    }

    .res-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.45rem 1.1rem;
      border-radius: 9999px;
      background: var(--res-accent-glow);
      color: var(--res-accent);
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 1rem;
      border: 1px solid rgba(217, 119, 6, 0.3);
    }

    .res-title {
      font-size: 2.5rem;
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.025em;
      color: var(--res-text-main);
      margin-bottom: 1rem;
    }

    .res-title-gradient {
      background: var(--res-gold-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .res-subtitle {
      font-size: 1.1rem;
      color: var(--res-text-muted);
      max-width: 760px;
      line-height: 1.65;
    }

    /* BUTTONS */
    .res-btn {
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

    .res-btn-primary {
      background: var(--res-gold-gradient);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(217, 119, 6, 0.35);
    }

    .res-btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(217, 119, 6, 0.45);
      color: #ffffff;
    }

    .res-btn-outline {
      background: transparent;
      color: var(--res-text-main);
      border-color: var(--res-card-border);
    }

    .res-btn-outline:hover {
      border-color: var(--res-accent);
      color: var(--res-accent);
      background: var(--res-accent-glow);
    }

    /* =====================================================================
       FRAMER MOTION SPECIFIC CLASSES & KEYFRAMES (1 PER SECTION)
       ===================================================================== */
    
    /* 1. Planning Guides: .framer-codex-stack */
    .framer-codex-stack {
      opacity: 0;
      transform: translateY(35px) scale(0.97) rotateX(4deg);
      transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1),
                  transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .framer-codex-stack.framer-in-view {
      opacity: 1;
      transform: translateY(0) scale(1) rotateX(0deg);
    }

    /* 2. Conference Checklist: .framer-mission-gauge */
    .framer-mission-gauge {
      opacity: 0;
      transform: translateX(-35px) scale(0.98);
      transition: opacity 0.75s cubic-bezier(0.22, 1, 0.36, 1),
                  transform 0.75s cubic-bezier(0.22, 1, 0.36, 1);
    }
    .framer-mission-gauge.framer-in-view {
      opacity: 1;
      transform: translateX(0) scale(1);
    }

    /* 3. Budget Guide: .framer-ledger-cascade */
    .framer-ledger-cascade {
      opacity: 0;
      transform: translateY(40px) scale(0.96);
      transition: opacity 0.85s cubic-bezier(0.34, 1.56, 0.64, 1),
                  transform 0.85s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .framer-ledger-cascade.framer-in-view {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    /* 4. Venue Guide: .framer-spatial-radar */
    .framer-spatial-radar {
      opacity: 0;
      transform: scale(0.94) rotate(-1.5deg);
      transition: opacity 0.8s cubic-bezier(0.19, 1, 0.22, 1),
                  transform 0.8s cubic-bezier(0.19, 1, 0.22, 1);
    }
    .framer-spatial-radar.framer-in-view {
      opacity: 1;
      transform: scale(1) rotate(0deg);
    }

    /* 5. Hybrid Practices: .framer-telemetry-nexus */
    .framer-telemetry-nexus {
      opacity: 0;
      transform: translateY(30px) scale(0.97);
      filter: blur(4px);
      transition: opacity 0.85s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                  transform 0.85s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                  filter 0.85s ease;
    }
    .framer-telemetry-nexus.framer-in-view {
      opacity: 1;
      transform: translateY(0) scale(1);
      filter: blur(0px);
    }

    /* 6. Industry Insights: .framer-monograph-editorial */
    .framer-monograph-editorial {
      opacity: 0;
      transform: translateY(35px);
      transition: opacity 0.75s cubic-bezier(0.16, 1, 0.3, 1),
                  transform 0.75s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .framer-monograph-editorial.framer-in-view {
      opacity: 1;
      transform: translateY(0);
    }

    /* 7. FAQ Vault: .framer-vault-accordion */
    .framer-vault-accordion {
      opacity: 0;
      transform: translateY(30px) scale(0.98);
      transition: opacity 0.7s cubic-bezier(0.33, 1, 0.68, 1),
                  transform 0.7s cubic-bezier(0.33, 1, 0.68, 1);
    }
    .framer-vault-accordion.framer-in-view {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    /* =====================================================================
       SECTION 1: PLANNING GUIDES - CODEX STACK ARCHITECTURE
       ===================================================================== */
    .res-section-guides {
      padding: 6rem 0;
      position: relative;
    }

    /* Master Archive Status & Filter Ribbon */
    .res-archive-status-ribbon {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      padding: 1.25rem 2rem;
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1rem;
      box-shadow: var(--res-shadow-sm);
      margin-bottom: 2.5rem;
    }

    .res-archive-stats-strip {
      display: flex;
      align-items: center;
      gap: 2rem;
    }

    .res-astat-item {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .res-astat-icon {
      width: 2.75rem;
      height: 2.75rem;
      border-radius: 0.75rem;
      background: var(--res-accent-glow);
      color: var(--res-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
    }

    .res-astat-val {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--res-text-main);
      line-height: 1.2;
    }

    .res-astat-lbl {
      font-size: 0.8rem;
      color: var(--res-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .res-archive-filters {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }

    .res-arch-pill {
      padding: 0.5rem 1rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 600;
      border: 1px solid var(--res-card-border);
      background: var(--res-surface-muted);
      color: var(--res-text-muted);
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .res-arch-pill:hover,
    .res-arch-pill.active {
      background: var(--res-accent);
      color: #ffffff;
      border-color: var(--res-accent);
    }

    /* Master Codex Showcase Centerpiece */
    .res-codex-centerpiece {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.5rem;
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.5rem;
      padding: 2.5rem;
      box-shadow: var(--res-shadow-md);
      margin-bottom: 2.5rem;
      position: relative;
      overflow: hidden;
    }

    .res-codex-visual {
      position: relative;
      border-radius: 1.2rem;
      overflow: hidden;
      box-shadow: var(--res-shadow-md);
      min-height: 380px;
    }

    .res-codex-visual img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    .res-codex-visual:hover img {
      transform: scale(1.04);
    }

    .res-codex-visual-badge {
      position: absolute;
      top: 1.25rem;
      left: 1.25rem;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(8px);
      padding: 0.5rem 1rem;
      border-radius: 9999px;
      color: #fbbf24;
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      border: 1px solid rgba(251, 191, 36, 0.3);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .res-codex-info {
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .res-codex-edition-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--res-accent);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 0.75rem;
    }

    .res-codex-title {
      font-size: 1.85rem;
      font-weight: 800;
      color: var(--res-text-main);
      line-height: 1.25;
      margin-bottom: 1rem;
    }

    .res-codex-desc {
      font-size: 0.95rem;
      color: var(--res-text-muted);
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }

    .res-codex-chapter-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-bottom: 2rem;
    }

    .res-chip {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.35rem 0.8rem;
      border-radius: 0.5rem;
      background: var(--res-surface-muted);
      border: 1px solid var(--res-card-border);
      font-size: 0.8rem;
      color: var(--res-text-muted);
      font-weight: 500;
    }

    .res-codex-actions {
      display: flex;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
    }

    /* 4-Card Micro Codex Grid */
    .res-codex-micro-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.5rem;
    }

    .res-micro-card {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1rem;
      padding: 1.5rem;
      box-shadow: var(--res-shadow-sm);
      display: flex;
      flex-direction: column;
      transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
      position: relative;
    }

    .res-micro-card:hover {
      transform: translateY(-5px);
      box-shadow: var(--res-shadow-md);
      border-color: var(--res-accent);
    }

    .res-micro-num {
      width: 2.25rem;
      height: 2.25rem;
      border-radius: 0.6rem;
      background: var(--res-accent-glow);
      color: var(--res-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.9rem;
      margin-bottom: 1rem;
    }

    .res-micro-title {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--res-text-main);
      line-height: 1.35;
      margin-bottom: 0.75rem;
    }

    .res-micro-meta {
      display: flex;
      align-items: center;
      gap: 1rem;
      font-size: 0.8rem;
      color: var(--res-text-muted);
      margin-bottom: 1.25rem;
      margin-top: auto;
    }

    .res-micro-btn {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--res-accent);
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      text-decoration: none;
      cursor: pointer;
      transition: gap 0.2s ease;
    }

    .res-micro-btn:hover {
      gap: 0.65rem;
    }

    /* =====================================================================
       SECTION 2: CONFERENCE PREPARATION CHECKLIST - MISSION CONTROL GAUGE
       ===================================================================== */
    .res-section-checklist {
      padding: 6rem 0;
      background: var(--res-surface-muted);
      border-top: 1px solid var(--res-card-border);
      border-bottom: 1px solid var(--res-card-border);
    }

    /* Mission Control Header & Readiness Gauge */
    .res-mission-status-deck {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 2rem;
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.25rem;
      padding: 1.75rem 2.25rem;
      box-shadow: var(--res-shadow-sm);
      margin-bottom: 2.5rem;
    }

    .res-radial-gauge-box {
      display: flex;
      align-items: center;
      gap: 1.5rem;
    }

    .res-gauge-circle {
      position: relative;
      width: 80px;
      height: 80px;
    }

    .res-gauge-svg {
      transform: rotate(-90deg);
      width: 80px;
      height: 80px;
    }

    .res-gauge-track {
      fill: none;
      stroke: var(--res-card-border);
      stroke-width: 8;
    }

    .res-gauge-bar {
      fill: none;
      stroke: var(--res-accent);
      stroke-width: 8;
      stroke-linecap: round;
      stroke-dasharray: 226;
      stroke-dashoffset: 45; /* 80% */
      transition: stroke-dashoffset 0.6s ease;
    }

    .res-gauge-val {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--res-text-main);
    }

    .res-gauge-title {
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--res-text-main);
      margin-bottom: 0.25rem;
    }

    .res-gauge-desc {
      font-size: 0.85rem;
      color: var(--res-text-muted);
    }

    .res-phase-pill-selector {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }

    .res-phase-btn {
      padding: 0.6rem 1.1rem;
      border-radius: 0.6rem;
      border: 1px solid var(--res-card-border);
      background: var(--res-surface-muted);
      color: var(--res-text-muted);
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s ease;
    }

    .res-phase-btn.active,
    .res-phase-btn:hover {
      background: var(--res-accent);
      color: #ffffff;
      border-color: var(--res-accent);
    }

    /* 3-Column Mission Command Console */
    .res-mission-command-grid {
      display: grid;
      grid-template-columns: 300px 1fr 340px;
      gap: 2rem;
    }

    /* Col 1: Phase Selector & Milestones */
    .res-phase-deck {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .res-phase-card {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1rem;
      padding: 1.25rem;
      cursor: pointer;
      transition: all 0.25s ease;
      position: relative;
    }

    .res-phase-card.active {
      border-color: var(--res-accent);
      background: var(--res-surface);
      box-shadow: 0 4px 15px rgba(217, 119, 6, 0.15);
    }

    .res-phase-card.active::before {
      content: '';
      position: absolute;
      top: 0;
      bottom: 0;
      left: 0;
      width: 4px;
      background: var(--res-accent);
      border-radius: 1rem 0 0 1rem;
    }

    body.rtl .res-phase-card.active::before {
      left: auto;
      right: 0;
      border-radius: 0 1rem 1rem 0;
    }

    .res-phase-badge {
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--res-accent);
      margin-bottom: 0.35rem;
    }

    .res-phase-name {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--res-text-main);
      margin-bottom: 0.5rem;
    }

    .res-phase-sub {
      font-size: 0.8rem;
      color: var(--res-text-muted);
      display: flex;
      justify-content: space-between;
    }

    /* Col 2: Interactive Checkpoint Matrix */
    .res-task-matrix-card {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.25rem;
      padding: 2rem;
      box-shadow: var(--res-shadow-sm);
    }

    .res-task-matrix-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--res-card-border);
    }

    .res-task-active-title {
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--res-text-main);
    }

    .res-task-cleared-count {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--res-accent);
      background: var(--res-accent-glow);
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
    }

    .res-task-items-list {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .res-task-item {
      display: flex;
      align-items: flex-start;
      gap: 1rem;
      padding: 1rem;
      border-radius: 0.75rem;
      background: var(--res-surface-muted);
      border: 1px solid var(--res-card-border);
      transition: background 0.2s ease, border-color 0.2s ease;
      cursor: pointer;
    }

    .res-task-item:hover {
      border-color: var(--res-accent);
    }

    .res-task-item.completed {
      background: rgba(5, 150, 105, 0.08);
      border-color: rgba(5, 150, 105, 0.3);
    }

    .res-task-check {
      width: 1.25rem;
      height: 1.25rem;
      border-radius: 0.35rem;
      border: 2px solid var(--res-card-border);
      background: var(--res-surface);
      margin-top: 0.15rem;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      font-size: 0.75rem;
      flex-shrink: 0;
      transition: all 0.2s ease;
    }

    .res-task-item.completed .res-task-check {
      background: var(--res-emerald);
      border-color: var(--res-emerald);
    }

    .res-task-content {
      flex: 1;
    }

    .res-task-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--res-text-main);
      margin-bottom: 0.25rem;
    }

    .res-task-desc {
      font-size: 0.82rem;
      color: var(--res-text-muted);
      line-height: 1.45;
    }

    .res-task-tag {
      font-size: 0.75rem;
      font-weight: 600;
      padding: 0.2rem 0.55rem;
      border-radius: 0.35rem;
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      color: var(--res-text-light);
      margin-top: 0.5rem;
      display: inline-block;
    }

    /* Col 3: Readiness Monitor & Inspection Card */
    .res-audit-monitor-card {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.25rem;
      overflow: hidden;
      box-shadow: var(--res-shadow-sm);
      display: flex;
      flex-direction: column;
    }

    .res-audit-img-box {
      height: 200px;
      position: relative;
      overflow: hidden;
    }

    .res-audit-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .res-audit-img-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, transparent 40%, rgba(15, 23, 42, 0.85) 100%);
      display: flex;
      align-items: flex-end;
      padding: 1.25rem;
    }

    .res-audit-stamp {
      color: #fbbf24;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .res-audit-body {
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      flex: 1;
    }

    .res-audit-title {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--res-text-main);
      margin-bottom: 0.5rem;
    }

    .res-audit-desc {
      font-size: 0.85rem;
      color: var(--res-text-muted);
      line-height: 1.5;
      margin-bottom: 1.25rem;
    }

    .res-audit-spec-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      margin-bottom: 1.5rem;
    }

    .res-aspec-row {
      display: flex;
      justify-content: space-between;
      font-size: 0.82rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px dashed var(--res-card-border);
    }

    .res-aspec-lbl {
      color: var(--res-text-muted);
    }

    .res-aspec-val {
      font-weight: 700;
      color: var(--res-text-main);
    }

    .res-audit-cta-btn {
      width: 100%;
      margin-top: auto;
    }

    /* =====================================================================
       SECTION 3: BUDGET GUIDE - CAPEX ALLOCATOR & LEDGER CASCADE
       ===================================================================== */
    .res-section-budget {
      padding: 6rem 0;
      position: relative;
    }

    /* Fiscal Telemetry Strip */
    .res-fiscal-metric-strip {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.5rem;
      margin-bottom: 3rem;
    }

    .res-fiscal-metric-card {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1rem;
      padding: 1.5rem;
      box-shadow: var(--res-shadow-sm);
      text-align: center;
      position: relative;
      overflow: hidden;
    }

    .res-fiscal-metric-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: var(--res-gold-gradient);
    }

    .res-fmetric-val {
      font-size: 2rem;
      font-weight: 800;
      color: var(--res-text-main);
      line-height: 1.2;
      margin-bottom: 0.35rem;
    }

    .res-fmetric-lbl {
      font-size: 0.85rem;
      color: var(--res-text-muted);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    /* Asymmetric Dynamic Allocation Cockpit */
    .res-budget-cockpit-grid {
      display: grid;
      grid-template-columns: 420px 1fr;
      gap: 2.5rem;
      align-items: start;
    }

    .res-budget-media-card {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--res-shadow-md);
    }

    .res-budget-img-box {
      height: 240px;
      position: relative;
      overflow: hidden;
    }

    .res-budget-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .res-budget-img-tag {
      position: absolute;
      bottom: 1rem;
      left: 1rem;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(8px);
      padding: 0.4rem 0.9rem;
      border-radius: 9999px;
      color: #ffffff;
      font-size: 0.75rem;
      font-weight: 700;
      border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .res-budget-framework-body {
      padding: 2rem;
    }

    .res-budget-framework-title {
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--res-text-main);
      margin-bottom: 0.75rem;
    }

    .res-budget-framework-desc {
      font-size: 0.9rem;
      color: var(--res-text-muted);
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }

    .res-budget-checks-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      margin-bottom: 2rem;
    }

    .res-bcheck-row {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-size: 0.88rem;
      color: var(--res-text-main);
    }

    .res-bcheck-icon {
      color: var(--res-accent);
      font-size: 0.9rem;
    }

    /* Right Interactive Simulator Panel */
    .res-simulator-board {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.5rem;
      padding: 2.5rem;
      box-shadow: var(--res-shadow-md);
    }

    .res-sim-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2rem;
      padding-bottom: 1.25rem;
      border-bottom: 1px solid var(--res-card-border);
    }

    .res-sim-title {
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--res-text-main);
    }

    .res-sim-badge {
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--res-teal);
      background: var(--res-teal-glow);
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      border: 1px solid rgba(13, 148, 136, 0.3);
    }

    /* Budget Range Slider Control */
    .res-sim-slider-box {
      background: var(--res-surface-muted);
      border-radius: 1rem;
      padding: 1.5rem;
      margin-bottom: 2.25rem;
      border: 1px solid var(--res-card-border);
    }

    .res-slider-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
    }

    .res-slider-lbl {
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--res-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .res-slider-val {
      font-size: 1.75rem;
      font-weight: 800;
      color: var(--res-accent);
    }

    .res-budget-range {
      width: 100%;
      height: 8px;
      border-radius: 4px;
      background: var(--res-card-border);
      outline: none;
      -webkit-appearance: none;
      cursor: pointer;
    }

    .res-budget-range::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: var(--res-accent);
      cursor: pointer;
      box-shadow: 0 0 10px rgba(217, 119, 6, 0.5);
      border: 2px solid #ffffff;
    }

    .res-slider-ticks {
      display: flex;
      justify-content: space-between;
      margin-top: 0.6rem;
      font-size: 0.75rem;
      color: var(--res-text-light);
      font-weight: 600;
    }

    /* 4 Cost Centers */
    .res-cost-centers-stack {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      margin-bottom: 2.5rem;
    }

    .res-cost-item {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .res-cost-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.95rem;
    }

    .res-cost-title {
      font-weight: 700;
      color: var(--res-text-main);
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .res-cost-title i {
      color: var(--res-accent);
    }

    .res-cost-amounts {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .res-cost-pct {
      font-size: 0.8rem;
      color: var(--res-text-muted);
      font-weight: 600;
    }

    .res-cost-calc {
      font-weight: 800;
      color: var(--res-text-main);
    }

    .res-cost-bar-bg {
      height: 10px;
      border-radius: 9999px;
      background: var(--res-surface-muted);
      overflow: hidden;
      border: 1px solid var(--res-card-border);
    }

    .res-cost-bar-fill {
      height: 100%;
      border-radius: 9999px;
      background: var(--res-gold-gradient);
      transition: width 0.4s ease;
    }

    /* =====================================================================
       SECTION 4: VENUE GUIDE - SPATIAL RADAR & BLUEPRINT WORKBENCH
       ===================================================================== */
    .res-section-venue-guide {
      padding: 6rem 0;
      background: var(--res-surface-muted);
      border-top: 1px solid var(--res-card-border);
      border-bottom: 1px solid var(--res-card-border);
    }

    /* Dimension Selector Bar */
    .res-dimension-bar {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.75rem;
      margin-bottom: 2.5rem;
    }

    .res-dim-tab {
      padding: 0.65rem 1.4rem;
      border-radius: 9999px;
      border: 1px solid var(--res-card-border);
      background: var(--res-surface);
      color: var(--res-text-muted);
      font-size: 0.9rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      transition: all 0.25s ease;
      box-shadow: var(--res-shadow-sm);
    }

    .res-dim-tab.active,
    .res-dim-tab:hover {
      background: var(--res-accent);
      color: #ffffff;
      border-color: var(--res-accent);
    }

    /* Split-Level Architectural Workbench */
    .res-spatial-workbench {
      display: flex;
      flex-direction: column;
      gap: 2.5rem;
    }

    /* Upper Level Blueprint Showcase */
    .res-blueprint-card {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--res-shadow-md);
      position: relative;
    }

    .res-blueprint-img-wrap {
      position: relative;
      height: 440px;
      overflow: hidden;
    }

    .res-blueprint-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    /* Interactive Spatial Hotspots */
    .res-hotspot {
      position: absolute;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: rgba(217, 119, 6, 0.9);
      border: 3px solid #ffffff;
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.8rem;
      font-weight: 800;
      cursor: pointer;
      box-shadow: 0 0 18px rgba(217, 119, 6, 0.8);
      animation: resPulsePin 2s infinite;
      transition: transform 0.2s ease;
      z-index: 5;
    }

    .res-hotspot:hover {
      transform: scale(1.25);
    }

    @keyframes resPulsePin {
      0% { box-shadow: 0 0 0 0 rgba(217, 119, 6, 0.7); }
      70% { box-shadow: 0 0 0 15px rgba(217, 119, 6, 0); }
      100% { box-shadow: 0 0 0 0 rgba(217, 119, 6, 0); }
    }

    .res-hotspot-1 { top: 28%; left: 34%; }
    .res-hotspot-2 { top: 62%; left: 18%; }
    .res-hotspot-3 { top: 38%; left: 74%; }
    .res-hotspot-4 { top: 76%; left: 62%; }

    .res-hotspot-callout {
      position: absolute;
      bottom: 1.5rem;
      left: 1.5rem;
      right: 1.5rem;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 1rem;
      padding: 1.25rem 1.75rem;
      color: #ffffff;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1.5rem;
      z-index: 10;
    }

    .res-callout-info {
      flex: 1;
    }

    .res-callout-tag {
      font-size: 0.75rem;
      color: #fbbf24;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 0.25rem;
    }

    .res-callout-title {
      font-size: 1.15rem;
      font-weight: 700;
      margin-bottom: 0.25rem;
    }

    .res-callout-detail {
      font-size: 0.85rem;
      color: #cbd5e1;
    }

    /* Lower Level 3-Pillar Inspection Scorecards */
    .res-vetting-pillars-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 2rem;
    }

    .res-pillar-card {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.25rem;
      padding: 2rem;
      box-shadow: var(--res-shadow-sm);
      display: flex;
      flex-direction: column;
      transition: all 0.3s ease;
    }

    .res-pillar-card:hover {
      transform: translateY(-5px);
      box-shadow: var(--res-shadow-md);
      border-color: var(--res-accent);
    }

    .res-pillar-icon {
      width: 3.25rem;
      height: 3.25rem;
      border-radius: 0.85rem;
      background: var(--res-accent-glow);
      color: var(--res-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.35rem;
      margin-bottom: 1.25rem;
    }

    .res-pillar-title {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--res-text-main);
      margin-bottom: 0.75rem;
    }

    .res-pillar-desc {
      font-size: 0.88rem;
      color: var(--res-text-muted);
      line-height: 1.55;
      margin-bottom: 1.5rem;
    }

    .res-pillar-specs {
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      margin-top: auto;
    }

    .res-pspec-item {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-size: 0.82rem;
      color: var(--res-text-main);
    }

    .res-pspec-item i {
      color: var(--res-emerald);
      font-size: 0.85rem;
    }

    /* =====================================================================
       SECTION 5: HYBRID PRACTICES - DUAL-HEMISPHERE TELEMETRY NEXUS
       ===================================================================== */
    .res-section-hybrid {
      padding: 6rem 0;
      position: relative;
    }

    /* Telemetry Latency Banner */
    .res-telemetry-status-banner {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.5rem;
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.25rem;
      padding: 1.5rem 2rem;
      box-shadow: var(--res-shadow-sm);
      margin-bottom: 3.5rem;
    }

    .res-telemetry-chip {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .res-tchip-icon {
      width: 2.75rem;
      height: 2.75rem;
      border-radius: 0.75rem;
      background: var(--res-teal-glow);
      color: var(--res-teal);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
    }

    .res-tchip-val {
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--res-text-main);
      line-height: 1.2;
    }

    .res-tchip-lbl {
      font-size: 0.78rem;
      color: var(--res-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    /* Dual-Hemisphere Interlocking Display */
    .res-dual-hemisphere-grid {
      display: grid;
      grid-template-columns: 1fr 340px 1fr;
      gap: 2rem;
      align-items: center;
      margin-bottom: 3.5rem;
    }

    .res-hemisphere-panel {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.5rem;
      padding: 2.25rem;
      box-shadow: var(--res-shadow-md);
    }

    .res-hemi-tag {
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--res-accent);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .res-hemi-title {
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--res-text-main);
      margin-bottom: 1rem;
    }

    .res-hemi-desc {
      font-size: 0.9rem;
      color: var(--res-text-muted);
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }

    .res-hemi-features {
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }

    .res-hfeat-row {
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      font-size: 0.85rem;
      color: var(--res-text-main);
    }

    .res-hfeat-row i {
      color: var(--res-accent);
      margin-top: 0.2rem;
    }

    /* Center Nexus Sphere */
    .res-nexus-center {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
    }

    .res-nexus-lens {
      width: 260px;
      height: 260px;
      border-radius: 50%;
      position: relative;
      overflow: hidden;
      box-shadow: 0 0 35px rgba(217, 119, 6, 0.3);
      border: 4px solid var(--res-accent);
    }

    .res-nexus-lens img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .res-nexus-badge-floating {
      margin-top: 1.25rem;
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      padding: 0.5rem 1.25rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--res-accent);
      box-shadow: var(--res-shadow-sm);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    /* Interlocking Horizontal Timeline Protocols */
    .res-hybrid-protocols-row {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.5rem;
    }

    .res-protocol-card {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1rem;
      padding: 1.5rem;
      box-shadow: var(--res-shadow-sm);
    }

    .res-protocol-step-num {
      font-size: 0.8rem;
      font-weight: 800;
      color: var(--res-teal);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.5rem;
    }

    .res-protocol-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--res-text-main);
      margin-bottom: 0.5rem;
    }

    .res-protocol-desc {
      font-size: 0.82rem;
      color: var(--res-text-muted);
      line-height: 1.5;
    }

    /* =====================================================================
       SECTION 6: INDUSTRY INSIGHTS - EXECUTIVE MONOGRAPH EDITORIAL
       ===================================================================== */
    .res-section-insights {
      padding: 6rem 0;
      background: var(--res-surface-muted);
      border-top: 1px solid var(--res-card-border);
      border-bottom: 1px solid var(--res-card-border);
    }

    /* Taxonomy Filter Bar */
    .res-taxonomy-bar {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 1.5rem;
      margin-bottom: 3rem;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid var(--res-card-border);
    }

    .res-tax-filters {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }

    .res-tax-btn {
      padding: 0.5rem 1rem;
      border-radius: 0.5rem;
      font-size: 0.85rem;
      font-weight: 600;
      border: 1px solid var(--res-card-border);
      background: var(--res-surface);
      color: var(--res-text-muted);
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .res-tax-btn.active,
    .res-tax-btn:hover {
      background: var(--res-accent);
      color: #ffffff;
      border-color: var(--res-accent);
    }

    /* Asymmetric Monograph Grid */
    .res-editorial-deck-grid {
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 2.5rem;
      margin-bottom: 3rem;
    }

    /* Left Hero Monograph */
    .res-hero-monograph {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--res-shadow-md);
      display: flex;
      flex-direction: column;
    }

    .res-monograph-img-box {
      height: 320px;
      position: relative;
      overflow: hidden;
    }

    .res-monograph-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s ease;
    }

    .res-hero-monograph:hover .res-monograph-img-box img {
      transform: scale(1.04);
    }

    .res-monograph-meta-ribbon {
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
    }

    .res-monograph-content {
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      flex: 1;
    }

    .res-monograph-byline {
      display: flex;
      align-items: center;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--res-text-muted);
      margin-bottom: 0.75rem;
    }

    .res-monograph-title {
      font-size: 1.75rem;
      font-weight: 800;
      color: var(--res-text-main);
      line-height: 1.3;
      margin-bottom: 1rem;
    }

    .res-monograph-summary {
      font-size: 0.95rem;
      color: var(--res-text-muted);
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }

    .res-monograph-bullets {
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      margin-bottom: 2rem;
    }

    .res-mbullet-row {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      font-size: 0.88rem;
      color: var(--res-text-main);
    }

    .res-mbullet-row i {
      color: var(--res-accent);
      font-size: 0.8rem;
    }

    .res-monograph-actions {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: auto;
      padding-top: 1.5rem;
      border-top: 1px solid var(--res-card-border);
    }

    /* Right Stacked Research Briefs */
    .res-stacked-briefs {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    .res-brief-card {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.25rem;
      padding: 1.75rem;
      box-shadow: var(--res-shadow-sm);
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
    }

    .res-brief-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--res-shadow-md);
      border-color: var(--res-accent);
    }

    .res-brief-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.75rem;
    }

    .res-brief-cat {
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--res-teal);
      background: var(--res-teal-glow);
      padding: 0.25rem 0.65rem;
      border-radius: 0.35rem;
    }

    .res-brief-date {
      font-size: 0.8rem;
      color: var(--res-text-light);
    }

    .res-brief-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--res-text-main);
      line-height: 1.35;
      margin-bottom: 0.65rem;
    }

    .res-brief-excerpt {
      font-size: 0.85rem;
      color: var(--res-text-muted);
      line-height: 1.5;
      margin-bottom: 1.25rem;
    }

    .res-brief-bottom {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: auto;
      padding-top: 1rem;
      border-top: 1px dashed var(--res-card-border);
    }

    .res-brief-link {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--res-accent);
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      cursor: pointer;
    }

    /* Executive Newsletter Bar */
    .res-newsletter-vault-bar {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.25rem;
      padding: 1.75rem 2.5rem;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 2rem;
      box-shadow: var(--res-shadow-sm);
    }

    .res-news-info {
      max-width: 500px;
    }

    .res-news-title {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--res-text-main);
      margin-bottom: 0.25rem;
    }

    .res-news-desc {
      font-size: 0.85rem;
      color: var(--res-text-muted);
    }

    .res-news-form {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex: 1;
      max-width: 480px;
    }

    .res-news-input {
      flex: 1;
      padding: 0.75rem 1.25rem;
      border-radius: 0.6rem;
      border: 1px solid var(--res-card-border);
      background: var(--res-surface-muted);
      color: var(--res-text-main);
      outline: none;
      font-size: 0.9rem;
    }

    .res-news-input:focus {
      border-color: var(--res-accent);
    }

    /* =====================================================================
       SECTION 7: FAQ - INTELLIGENCE QUERY VAULT & CONCIERGE HELP MATRIX
       ===================================================================== */
    .res-section-faq {
      padding: 6rem 0;
      position: relative;
    }

    /* FAQ Search & Category Filter Header */
    .res-faq-query-hub {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.25rem;
      padding: 2rem 2.5rem;
      box-shadow: var(--res-shadow-sm);
      margin-bottom: 3rem;
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    .res-faq-search-box {
      position: relative;
      width: 100%;
    }

    .res-faq-search-icon {
      position: absolute;
      top: 50%;
      left: 1.25rem;
      transform: translateY(-50%);
      color: var(--res-text-muted);
      font-size: 1.1rem;
    }

    body.rtl .res-faq-search-icon {
      left: auto;
      right: 1.25rem;
    }

    .res-faq-search-input {
      width: 100%;
      padding: 1rem 1.25rem 1rem 3.25rem;
      border-radius: 0.75rem;
      border: 1px solid var(--res-card-border);
      background: var(--res-surface-muted);
      color: var(--res-text-main);
      font-size: 1rem;
      outline: none;
      transition: all 0.2s ease;
    }

    body.rtl .res-faq-search-input {
      padding: 1rem 3.25rem 1rem 1.25rem;
    }

    .res-faq-search-input:focus {
      border-color: var(--res-accent);
      box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.15);
      background: var(--res-surface);
    }

    .res-faq-tabs-row {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }

    .res-faq-cat-btn {
      padding: 0.5rem 1.1rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      border: 1px solid var(--res-card-border);
      background: var(--res-surface-muted);
      color: var(--res-text-muted);
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .res-faq-cat-btn.active,
    .res-faq-cat-btn:hover {
      background: var(--res-accent);
      color: #ffffff;
      border-color: var(--res-accent);
    }

    /* Asymmetric 2-Wing Architecture */
    .res-faq-matrix-grid {
      display: grid;
      grid-template-columns: 380px 1fr;
      gap: 2.5rem;
      align-items: start;
    }

    /* Left Concierge Pod */
    .res-faq-concierge-card {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: var(--res-shadow-md);
      position: sticky;
      top: 100px;
    }

    .res-concierge-img-box {
      height: 220px;
      position: relative;
      overflow: hidden;
    }

    .res-concierge-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .res-concierge-status-badge {
      position: absolute;
      bottom: 1rem;
      left: 1rem;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(8px);
      padding: 0.4rem 0.9rem;
      border-radius: 9999px;
      color: #34d399;
      font-size: 0.78rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.45rem;
      border: 1px solid rgba(52, 211, 153, 0.3);
    }

    .res-concierge-body {
      padding: 2rem;
    }

    .res-concierge-title {
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--res-text-main);
      margin-bottom: 0.5rem;
    }

    .res-concierge-desc {
      font-size: 0.88rem;
      color: var(--res-text-muted);
      line-height: 1.55;
      margin-bottom: 1.5rem;
    }

    .res-concierge-sla-box {
      background: var(--res-surface-muted);
      border-radius: 0.75rem;
      padding: 1rem;
      margin-bottom: 1.75rem;
      border: 1px solid var(--res-card-border);
    }

    .res-sla-item {
      display: flex;
      justify-content: space-between;
      font-size: 0.82rem;
      margin-bottom: 0.4rem;
    }

    .res-sla-item:last-child {
      margin-bottom: 0;
    }

    .res-sla-lbl {
      color: var(--res-text-muted);
    }

    .res-sla-val {
      font-weight: 700;
      color: var(--res-text-main);
    }

    .res-concierge-btn {
      width: 100%;
    }

    /* Right Accordion List */
    .res-faq-accordion-list {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    .res-faq-item {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.25rem;
      overflow: hidden;
      box-shadow: var(--res-shadow-sm);
      transition: border-color 0.25s ease, box-shadow 0.25s ease;
    }

    .res-faq-item.active {
      border-color: var(--res-accent);
      box-shadow: var(--res-shadow-md);
    }

    .res-faq-header {
      padding: 1.5rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      user-select: none;
      gap: 1rem;
    }

    .res-faq-header-left {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }

    .res-faq-cat-tag {
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--res-accent);
    }

    .res-faq-question {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--res-text-main);
      line-height: 1.35;
    }

    .res-faq-chevron {
      width: 2.25rem;
      height: 2.25rem;
      border-radius: 50%;
      background: var(--res-surface-muted);
      color: var(--res-text-muted);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.9rem;
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), background 0.2s ease, color 0.2s ease;
      flex-shrink: 0;
    }

    .res-faq-item.active .res-faq-chevron {
      transform: rotate(180deg);
      background: var(--res-accent);
      color: #ffffff;
    }

    .res-faq-body {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .res-faq-item.active .res-faq-body {
      max-height: 800px;
    }

    .res-faq-content {
      padding: 0 2rem 2rem 2rem;
      color: var(--res-text-muted);
      font-size: 0.95rem;
      line-height: 1.65;
      border-top: 1px dashed var(--res-card-border);
      padding-top: 1.5rem;
    }

    .res-faq-content ul {
      margin: 1rem 0;
      padding-left: 1.5rem;
    }

    body.rtl .res-faq-content ul {
      padding-left: 0;
      padding-right: 1.5rem;
    }

    .res-faq-content li {
      margin-bottom: 0.5rem;
    }

    .res-faq-feedback {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 1.5rem;
      padding-top: 1rem;
      border-top: 1px solid var(--res-card-border);
      font-size: 0.82rem;
      color: var(--res-text-light);
    }

    .res-feedback-btns {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .res-feedback-btn {
      padding: 0.3rem 0.75rem;
      border-radius: 0.4rem;
      border: 1px solid var(--res-card-border);
      background: var(--res-surface-muted);
      color: var(--res-text-muted);
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.2s ease;
    }

    .res-feedback-btn:hover {
      border-color: var(--res-accent);
      color: var(--res-accent);
    }

    /* Modal for Quick View & Downloads */
    .res-modal-overlay {
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

    .res-modal-card {
      background: var(--res-surface);
      border: 1px solid var(--res-card-border);
      border-radius: 1.5rem;
      max-width: 560px;
      width: 100%;
      padding: 2.5rem;
      box-shadow: var(--res-shadow-lg);
      position: relative;
      text-align: center;
    }

    .res-modal-close {
      position: absolute;
      top: 1.25rem;
      right: 1.25rem;
      background: transparent;
      border: none;
      color: var(--res-text-muted);
      font-size: 1.25rem;
      cursor: pointer;
    }

    body.rtl .res-modal-close {
      right: auto;
      left: 1.25rem;
    }

    .res-modal-icon {
      width: 4rem;
      height: 4rem;
      border-radius: 1rem;
      background: var(--res-teal-glow);
      color: var(--res-teal);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.85rem;
      margin: 0 auto 1.5rem auto;
    }

    .res-modal-title {
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--res-text-main);
      margin-bottom: 0.5rem;
    }

    .res-modal-desc {
      font-size: 0.95rem;
      color: var(--res-text-muted);
      line-height: 1.55;
      margin-bottom: 2rem;
    }

    /* Responsive Queries */
    @media (max-width: 1100px) {
      .res-codex-centerpiece { grid-template-columns: 1fr; }
      .res-codex-micro-grid { grid-template-columns: repeat(2, 1fr); }
      .res-mission-command-grid { grid-template-columns: 1fr; }
      .res-budget-cockpit-grid { grid-template-columns: 1fr; }
      .res-dual-hemisphere-grid { grid-template-columns: 1fr; }
      .res-editorial-deck-grid { grid-template-columns: 1fr; }
      .res-faq-matrix-grid { grid-template-columns: 1fr; }
      .res-nexus-center { margin: 2rem 0; }
    }

    @media (max-width: 768px) {
      .res-codex-micro-grid { grid-template-columns: 1fr; }
      .res-fiscal-metric-strip { grid-template-columns: repeat(2, 1fr); }
      .res-vetting-pillars-grid { grid-template-columns: 1fr; }
      .res-telemetry-status-banner { grid-template-columns: repeat(2, 1fr); }
      .res-hybrid-protocols-row { grid-template-columns: 1fr; }
      .res-title { font-size: 2rem; }
      .res-blueprint-img-wrap { height: 300px; }
    }
"""

    # HTML for the redesigned resources page
    new_res_content = """
  <!-- MAIN RESOURCES CONTENT WRAPPER -->
  <main class="res-page-wrap">

    <!-- =====================================================================
         SECTION 1: CORPORATE EVENT PLANNING GUIDES (CODEX STACK ARCHITECTURE)
         ===================================================================== -->
    <section id="planning-guides" class="res-section-guides">
      <div class="res-container">
        <!-- Section Header -->
        <div class="res-section-head framer-codex-stack">
          <div class="res-badge"><i class="fas fa-book-bookmark"></i> Executive Field Manuals</div>
          <h2 class="res-title">Corporate Event Planning <span class="res-title-gradient">Guides & Field Codex</span></h2>
          <p class="res-subtitle">Access proprietary standard operating procedures, architectural blueprints, and protocol frameworks battle-tested across Fortune 500 summits and global plenaries.</p>
        </div>

        <!-- Master Archive Status Ribbon -->
        <div class="res-archive-status-ribbon framer-codex-stack">
          <div class="res-archive-stats-strip">
            <div class="res-astat-item">
              <div class="res-astat-icon"><i class="fas fa-layer-group"></i></div>
              <div>
                <div class="res-astat-val">12 Volumes</div>
                <div class="res-astat-lbl">Verified Manuals</div>
              </div>
            </div>
            <div class="res-astat-item">
              <div class="res-astat-icon"><i class="fas fa-cloud-arrow-down"></i></div>
              <div>
                <div class="res-astat-val">14,200+</div>
                <div class="res-astat-lbl">Executive Downloads</div>
              </div>
            </div>
            <div class="res-astat-item">
              <div class="res-astat-icon"><i class="fas fa-shield-halved"></i></div>
              <div>
                <div class="res-astat-val">ISO-20121</div>
                <div class="res-astat-lbl">Certified Standards</div>
              </div>
            </div>
          </div>
          <div class="res-archive-filters">
            <button class="res-arch-pill active" onclick="filterGuides('all', this)"><i class="fas fa-globe"></i> All Guides</button>
            <button class="res-arch-pill" onclick="filterGuides('plenary', this)"><i class="fas fa-landmark"></i> Plenaries</button>
            <button class="res-arch-pill" onclick="filterGuides('governance', this)"><i class="fas fa-gavel"></i> Governance</button>
            <button class="res-arch-pill" onclick="filterGuides('crisis', this)"><i class="fas fa-shield-virus"></i> Risk & Crisis</button>
          </div>
        </div>

        <!-- Master Codex Showcase Centerpiece -->
        <div class="res-codex-centerpiece framer-codex-stack">
          <div class="res-codex-visual">
            <img src="images/resource_planning_guides.jpg" alt="Executive Event Planning Field Codex Manual">
            <div class="res-codex-visual-badge">
              <i class="fas fa-certificate"></i> Enterprise Master Edition 2026
            </div>
          </div>
          <div class="res-codex-info">
            <div class="res-codex-edition-tag">
              <i class="fas fa-star"></i> Featured Executive Compendium • Volume IV
            </div>
            <h3 class="res-codex-title">Enterprise Plenary Operations & Production Architecture</h3>
            <p class="res-codex-desc">A comprehensive 48-page operational bible engineered for Chief Marketing Officers, Heads of Corporate Communications, and Event Steering Committees executing tier-one multi-day summits.</p>
            <div class="res-codex-chapter-chips">
              <span class="res-chip"><i class="fas fa-check-circle"></i> Ch. 1: Critical Path Scheduling</span>
              <span class="res-chip"><i class="fas fa-check-circle"></i> Ch. 2: Technical Rider Structuring</span>
              <span class="res-chip"><i class="fas fa-check-circle"></i> Ch. 3: VIP Security Ring Geometry</span>
              <span class="res-chip"><i class="fas fa-check-circle"></i> Ch. 4: Multi-Track Acoustic Zoning</span>
            </div>
            <div class="res-codex-actions">
              <button class="res-btn res-btn-primary" onclick="openDownloadModal('Enterprise Plenary Operations Manual (PDF • 18.4 MB)')">
                <i class="fas fa-file-pdf"></i> Download Master Codex
              </button>
              <button class="res-btn res-btn-outline" onclick="openQuickView('Enterprise Plenary Operations Overview')">
                <i class="fas fa-eye"></i> Quick Preview
              </button>
            </div>
          </div>
        </div>

        <!-- 4-Card Micro Codex Grid -->
        <div class="res-codex-micro-grid">
          <!-- Card 1 -->
          <div class="res-micro-card framer-codex-stack" data-category="governance">
            <div class="res-micro-num">01</div>
            <h4 class="res-micro-title">Sponsorship Valuation & Partner Deck Blueprint</h4>
            <div class="res-micro-meta">
              <span><i class="fas fa-file-lines"></i> 24 Pages</span>
              <span><i class="fas fa-clock"></i> 10 min read</span>
            </div>
            <a class="res-micro-btn" onclick="openDownloadModal('Sponsorship Valuation Blueprint')">
              Download Guide <i class="fas fa-arrow-right"></i>
            </a>
          </div>

          <!-- Card 2 -->
          <div class="res-micro-card framer-codex-stack" data-category="plenary">
            <div class="res-micro-num">02</div>
            <h4 class="res-micro-title">Keynote Stage & Spatial Experience Protocols</h4>
            <div class="res-micro-meta">
              <span><i class="fas fa-file-lines"></i> 32 Pages</span>
              <span><i class="fas fa-clock"></i> 14 min read</span>
            </div>
            <a class="res-micro-btn" onclick="openDownloadModal('Keynote Stage Spatial Protocols')">
              Download Guide <i class="fas fa-arrow-right"></i>
            </a>
          </div>

          <!-- Card 3 -->
          <div class="res-micro-card framer-codex-stack" data-category="crisis">
            <div class="res-micro-num">03</div>
            <h4 class="res-micro-title">Crisis Mitigation & Contingency Response SOP</h4>
            <div class="res-micro-meta">
              <span><i class="fas fa-file-lines"></i> 28 Pages</span>
              <span><i class="fas fa-clock"></i> 12 min read</span>
            </div>
            <a class="res-micro-btn" onclick="openDownloadModal('Crisis Mitigation Response SOP')">
              Download Guide <i class="fas fa-arrow-right"></i>
            </a>
          </div>

          <!-- Card 4 -->
          <div class="res-micro-card framer-codex-stack" data-category="governance">
            <div class="res-micro-num">04</div>
            <h4 class="res-micro-title">VIP Dignitary & Executive Escort Protocol</h4>
            <div class="res-micro-meta">
              <span><i class="fas fa-file-lines"></i> 20 Pages</span>
              <span><i class="fas fa-clock"></i> 8 min read</span>
            </div>
            <a class="res-micro-btn" onclick="openDownloadModal('VIP Dignitary Escort Protocol')">
              Download Guide <i class="fas fa-arrow-right"></i>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 2: CONFERENCE PREPARATION CHECKLIST (MISSION CONTROL GAUGE)
         ===================================================================== -->
    <section id="preparation-checklist" class="res-section-checklist">
      <div class="res-container">
        <!-- Section Header -->
        <div class="res-section-head framer-mission-gauge">
          <div class="res-badge"><i class="fas fa-clipboard-check"></i> Flight-Check Readiness</div>
          <h2 class="res-title">Conference Preparation <span class="res-title-gradient">Checklist & Mission Matrix</span></h2>
          <p class="res-subtitle">Track operational readiness across every pre-summit milestone with an aerospace-grade checkpoint system designed to eliminate blind spots.</p>
        </div>

        <!-- Mission Control Header & Readiness Gauge -->
        <div class="res-mission-status-deck framer-mission-gauge">
          <div class="res-radial-gauge-box">
            <div class="res-gauge-circle">
              <svg class="res-gauge-svg" viewBox="0 0 80 80">
                <circle class="res-gauge-track" cx="40" cy="40" r="36"></circle>
                <circle id="radialGaugeBar" class="res-gauge-bar" cx="40" cy="40" r="36"></circle>
              </svg>
              <div id="radialGaugeText" class="res-gauge-val">80%</div>
            </div>
            <div>
              <div class="res-gauge-title">Pre-Flight Readiness Index</div>
              <div class="res-gauge-desc">Interactive live score calculated from cleared phase checkpoints</div>
            </div>
          </div>
          <div class="res-phase-pill-selector">
            <button class="res-phase-btn active" onclick="switchChecklistPhase(0, this)"><i class="fas fa-compass"></i> T-180 Days</button>
            <button class="res-phase-btn" onclick="switchChecklistPhase(1, this)"><i class="fas fa-box-archive"></i> T-90 Days</button>
            <button class="res-phase-btn" onclick="switchChecklistPhase(2, this)"><i class="fas fa-truck-ramp-box"></i> T-30 Days</button>
            <button class="res-phase-btn" onclick="switchChecklistPhase(3, this)"><i class="fas fa-flag-checkered"></i> T-0 Go-Live</button>
          </div>
        </div>

        <!-- 3-Column Mission Command Console -->
        <div class="res-mission-command-grid">
          <!-- Col 1: Phase Selector Cards -->
          <div class="res-phase-deck framer-mission-gauge">
            <div class="res-phase-card active" onclick="switchChecklistPhase(0, null, this)">
              <div class="res-phase-badge">Phase I • Strategic Foundation</div>
              <div class="res-phase-name">T-180 to T-120 Days</div>
              <div class="res-phase-sub">
                <span>Scope & Stakeholder Lock</span>
                <span><i class="fas fa-check text-success"></i> 5 Checks</span>
              </div>
            </div>
            <div class="res-phase-card" onclick="switchChecklistPhase(1, null, this)">
              <div class="res-phase-badge">Phase II • Production Matrix</div>
              <div class="res-phase-name">T-90 to T-60 Days</div>
              <div class="res-phase-sub">
                <span>RFP & Vendor Vetting</span>
                <span><i class="fas fa-check text-success"></i> 5 Checks</span>
              </div>
            </div>
            <div class="res-phase-card" onclick="switchChecklistPhase(2, null, this)">
              <div class="res-phase-badge">Phase III • Logistics & Staging</div>
              <div class="res-phase-name">T-30 to T-7 Days</div>
              <div class="res-phase-sub">
                <span>Freight, CAD & Rehearsal</span>
                <span><i class="fas fa-check text-success"></i> 5 Checks</span>
              </div>
            </div>
            <div class="res-phase-card" onclick="switchChecklistPhase(3, null, this)">
              <div class="res-phase-badge">Phase IV • Zero-Hour Execution</div>
              <div class="res-phase-name">T-24 Hours to Go-Live</div>
              <div class="res-phase-sub">
                <span>Radio Check & Plenary Launch</span>
                <span><i class="fas fa-check text-success"></i> 5 Checks</span>
              </div>
            </div>
          </div>

          <!-- Col 2: Interactive Checkpoint Matrix -->
          <div class="res-task-matrix-card framer-mission-gauge">
            <div class="res-task-matrix-head">
              <div id="activePhaseTitle" class="res-task-active-title">Phase I: Strategic Foundation Checkpoints</div>
              <div id="clearedCountBadge" class="res-task-cleared-count">4 of 5 Cleared</div>
            </div>
            <div id="taskItemsContainer" class="res-task-items-list">
              <!-- Dynamically populated tasks will render here -->
            </div>
          </div>

          <!-- Col 3: Readiness Monitor & Inspection Card -->
          <div class="res-audit-monitor-card framer-mission-gauge">
            <div class="res-audit-img-box">
              <img src="images/resource_conference_checklist.jpg" alt="Conference Preparation Flight Check">
              <div class="res-audit-img-overlay">
                <div class="res-audit-stamp"><i class="fas fa-stamp"></i> Production Auditor Verified</div>
              </div>
            </div>
            <div class="res-audit-body">
              <h4 class="res-audit-title">Quality Assurance & Audit Desk</h4>
              <p class="res-audit-desc">Every checklist is peer-audited by a senior production executive to ensure strict alignment with ISO-20121 safety and sustainability guidelines.</p>
              <div class="res-audit-spec-list">
                <div class="res-aspec-row">
                  <span class="res-aspec-lbl">Lead Verifier</span>
                  <span class="res-aspec-val">Marcus Vance, VP Ops</span>
                </div>
                <div class="res-aspec-row">
                  <span class="res-aspec-lbl">Audit Standard</span>
                  <span class="res-aspec-val">Apex Grade A-1</span>
                </div>
                <div class="res-aspec-row">
                  <span class="res-aspec-lbl">Contingency Redundancy</span>
                  <span class="res-aspec-val">N+1 Redundant</span>
                </div>
              </div>
              <button class="res-btn res-btn-primary res-audit-cta-btn" onclick="openDownloadModal('Verified Conference Preparation Checklist (.XLSX & .PDF)')">
                <i class="fas fa-file-arrow-down"></i> Export Full Checklist
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 3: EVENT BUDGET PLANNING GUIDE (CAPEX ALLOCATOR & LEDGER)
         ===================================================================== -->
    <section id="budget-guide" class="res-section-budget">
      <div class="res-container">
        <!-- Section Header -->
        <div class="res-section-head framer-ledger-cascade">
          <div class="res-badge"><i class="fas fa-coins"></i> Fiscal Governance</div>
          <h2 class="res-title">Event Budget Planning Guide <span class="res-title-gradient">& Capex Allocator</span></h2>
          <p class="res-subtitle">Maximize corporate return on objective (ROO) and capital efficiency with our institutional budgeting simulator and financial architecture model.</p>
        </div>

        <!-- Fiscal Telemetry Strip -->
        <div class="res-fiscal-metric-strip framer-ledger-cascade">
          <div class="res-fiscal-metric-card">
            <div class="res-fmetric-val">&lt; 1.8%</div>
            <div class="res-fmetric-lbl">Historical Variance</div>
          </div>
          <div class="res-fiscal-metric-card">
            <div class="res-fmetric-val">4.2x</div>
            <div class="res-fmetric-lbl">Target ROI Multiplier</div>
          </div>
          <div class="res-fiscal-metric-card">
            <div class="res-fmetric-val">12.5%</div>
            <div class="res-fmetric-lbl">Contingency Buffer</div>
          </div>
          <div class="res-fiscal-metric-card">
            <div class="res-fmetric-val">$45M+</div>
            <div class="res-fmetric-lbl">Managed In 2026</div>
          </div>
        </div>

        <!-- Asymmetric Dynamic Allocation Cockpit -->
        <div class="res-budget-cockpit-grid">
          <!-- Left Panel: Budget Media & Framework -->
          <div class="res-budget-media-card framer-ledger-cascade">
            <div class="res-budget-img-box">
              <img src="images/resource_budget_guide.jpg" alt="Event Budget Financial Ledger Framework">
              <div class="res-budget-img-tag"><i class="fas fa-calculator"></i> Institutional Financial Ledger</div>
            </div>
            <div class="res-budget-framework-body">
              <h4 class="res-budget-framework-title">The Apex Fiscal Governance Framework</h4>
              <p class="res-budget-framework-desc">We structure event expenditure through a rigorous Capex-to-Opex ledger, separating fixed venue infrastructure from variable delegate experience touchpoints.</p>
              <div class="res-budget-checks-list">
                <div class="res-bcheck-row">
                  <i class="fas fa-circle-check res-bcheck-icon"></i>
                  <span>Zero-base budgeting for third-party production contracts</span>
                </div>
                <div class="res-bcheck-row">
                  <i class="fas fa-circle-check res-bcheck-icon"></i>
                  <span>Guaranteed vendor volume rebates passed directly to client</span>
                </div>
                <div class="res-bcheck-row">
                  <i class="fas fa-circle-check res-bcheck-icon"></i>
                  <span>Real-time expenditure tracking with automated overage alerts</span>
                </div>
              </div>
              <button class="res-btn res-btn-primary" style="width: 100%;" onclick="openDownloadModal('Corporate Event Financial Model (.XLSX Template)')">
                <i class="fas fa-file-excel"></i> Download Excel Model Template
              </button>
            </div>
          </div>

          <!-- Right Panel: Interactive Simulator Board -->
          <div class="res-simulator-board framer-ledger-cascade">
            <div class="res-sim-head">
              <div class="res-sim-title">Interactive Capex Simulator</div>
              <div class="res-sim-badge"><i class="fas fa-sliders"></i> Dynamic Allocation Engine</div>
            </div>

            <!-- Budget Range Slider -->
            <div class="res-sim-slider-box">
              <div class="res-slider-top">
                <span class="res-slider-lbl">Total Planned Event Budget</span>
                <span id="sliderDisplayVal" class="res-slider-val">$500,000</span>
              </div>
              <input type="range" id="budgetRangeInput" class="res-budget-range" min="150000" max="2500000" step="50000" value="500000" oninput="updateBudgetSimulation(this.value)">
              <div class="res-slider-ticks">
                <span>$150,000 (Regional)</span>
                <span>$1,000,000 (Continental)</span>
                <span>$2,500,000 (Global Flagship)</span>
              </div>
            </div>

            <!-- 4 Cost Centers -->
            <div class="res-cost-centers-stack">
              <!-- Center 1: Venue & Staging (35%) -->
              <div class="res-cost-item">
                <div class="res-cost-header">
                  <span class="res-cost-title"><i class="fas fa-building-columns"></i> Venue Infrastructure & Staging</span>
                  <div class="res-cost-amounts">
                    <span class="res-cost-pct">35% Allocation</span>
                    <span id="costCenter1" class="res-cost-calc">$175,000</span>
                  </div>
                </div>
                <div class="res-cost-bar-bg">
                  <div class="res-cost-bar-fill" style="width: 35%;"></div>
                </div>
              </div>

              <!-- Center 2: AV, Rigging & Lighting (25%) -->
              <div class="res-cost-item">
                <div class="res-cost-header">
                  <span class="res-cost-title"><i class="fas fa-satellite-dish"></i> Audio-Visual & Holographic Tech</span>
                  <div class="res-cost-amounts">
                    <span class="res-cost-pct">25% Allocation</span>
                    <span id="costCenter2" class="res-cost-calc">$125,000</span>
                  </div>
                </div>
                <div class="res-cost-bar-bg">
                  <div class="res-cost-bar-fill" style="width: 25%;"></div>
                </div>
              </div>

              <!-- Center 3: Hospitality & VIP (20%) -->
              <div class="res-cost-item">
                <div class="res-cost-header">
                  <span class="res-cost-title"><i class="fas fa-champagne-glasses"></i> Curated Gastronomy & Hospitality</span>
                  <div class="res-cost-amounts">
                    <span class="res-cost-pct">20% Allocation</span>
                    <span id="costCenter3" class="res-cost-calc">$100,000</span>
                  </div>
                </div>
                <div class="res-cost-bar-bg">
                  <div class="res-cost-bar-fill" style="width: 20%;"></div>
                </div>
              </div>

              <!-- Center 4: Governance & Buffer (20%) -->
              <div class="res-cost-item">
                <div class="res-cost-header">
                  <span class="res-cost-title"><i class="fas fa-shield-heart"></i> Contingency Reserve & Risk Buffer</span>
                  <div class="res-cost-amounts">
                    <span class="res-cost-pct">20% Allocation</span>
                    <span id="costCenter4" class="res-cost-calc">$100,000</span>
                  </div>
                </div>
                <div class="res-cost-bar-bg">
                  <div class="res-cost-bar-fill" style="width: 20%;"></div>
                </div>
              </div>
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center; background: var(--res-surface-muted); padding: 1.25rem 1.75rem; border-radius: 1rem; border: 1px solid var(--res-card-border);">
              <div>
                <div style="font-size: 0.8rem; color: var(--res-text-muted); text-transform: uppercase; font-weight: 700;">Projected Pipeline Impact</div>
                <div id="projectedRoiVal" style="font-size: 1.25rem; font-weight: 800; color: var(--res-teal);">$2,100,000 Estimated Value</div>
              </div>
              <button class="res-btn res-btn-outline" onclick="openDownloadModal('Simulated Budget Breakdown PDF')">
                <i class="fas fa-print"></i> Export Breakdown
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 4: VENUE SELECTION GUIDE (SPATIAL RADAR & BLUEPRINT)
         ===================================================================== -->
    <section id="venue-guide" class="res-section-venue-guide">
      <div class="res-container">
        <!-- Section Header -->
        <div class="res-section-head framer-spatial-radar">
          <div class="res-badge"><i class="fas fa-compass-drafting"></i> Spatial Architecture</div>
          <h2 class="res-title">Venue Selection Guide <span class="res-title-gradient">& Architectural Vetting</span></h2>
          <p class="res-subtitle">Evaluate event real estate against structural load, acoustic zoning, delegate ingress, and electrical specifications before signing costly multi-year master service agreements.</p>
        </div>

        <!-- Dimension Selector Bar -->
        <div class="res-dimension-bar framer-spatial-radar">
          <button class="res-dim-tab active" onclick="switchVenueDimension('structural', this)"><i class="fas fa-ruler-combined"></i> Structural & Clear Height</button>
          <button class="res-dim-tab" onclick="switchVenueDimension('ingress', this)"><i class="fas fa-dolly"></i> Freight & Loading Ingress</button>
          <button class="res-dim-tab" onclick="switchVenueDimension('acoustics', this)"><i class="fas fa-wave-square"></i> Acoustic Isolation (STC 55)</button>
          <button class="res-dim-tab" onclick="switchVenueDimension('power', this)"><i class="fas fa-bolt"></i> 3-Phase 400A Power</button>
        </div>

        <!-- Split-Level Architectural Workbench -->
        <div class="res-spatial-workbench">
          <!-- Upper Level Blueprint Showcase with Interactive Hotspots -->
          <div class="res-blueprint-card framer-spatial-radar">
            <div class="res-blueprint-img-wrap">
              <img src="images/resource_venue_guide.jpg" alt="Architectural Venue Vetting Blueprint">
              
              <!-- Clickable Spatial Hotspots -->
              <div class="res-hotspot res-hotspot-1" onclick="activateHotspot(1, 'Truss Rigging & 28ft Clear Height', 'Structural roof supports certified for 45,000 lbs distributed AV payload and dynamic line arrays.')">
                1
              </div>
              <div class="res-hotspot res-hotspot-2" onclick="activateHotspot(2, 'Direct Freight Ingress Dock', 'Twin roll-up freight bays (16ft x 14ft) capable of receiving 53ft semitruck trailers directly onto plenary floor.')">
                2
              </div>
              <div class="res-hotspot res-hotspot-3" onclick="activateHotspot(3, 'VIP Green Room Isolation Zone', 'Soundproofed green room with private executive restroom, secure fiber optic feed, and discreet motorcade egress.')">
                3
              </div>
              <div class="res-hotspot res-hotspot-4" onclick="activateHotspot(4, 'Emergency Egress & Fire Marshal Matrix', 'Dual-redundant primary egress corridors exceeding municipal NFPA-101 crowd dispersion standards by 35%.')">
                4
              </div>

              <!-- Hotspot Active Callout Ribbon -->
              <div class="res-hotspot-callout">
                <div class="res-callout-info">
                  <div id="hotspotTag" class="res-callout-tag">Hotspot 1 Selected</div>
                  <div id="hotspotTitle" class="res-callout-title">Truss Rigging & 28ft Clear Height</div>
                  <div id="hotspotDetail" class="res-callout-detail">Structural roof supports certified for 45,000 lbs distributed AV payload and dynamic line arrays.</div>
                </div>
                <button class="res-btn res-btn-outline" style="color: #ffffff; border-color: rgba(255,255,255,0.3);" onclick="openDownloadModal('Venue Architectural Vetting Checklist')">
                  <i class="fas fa-file-pdf"></i> Download Vetting Matrix
                </button>
              </div>
            </div>
          </div>

          <!-- Lower Level 3-Pillar Inspection Scorecards -->
          <div class="res-vetting-pillars-grid">
            <!-- Pillar 1 -->
            <div class="res-pillar-card framer-spatial-radar">
              <div class="res-pillar-icon"><i class="fas fa-microchip"></i></div>
              <h4 class="res-pillar-title">Technical & Electrical Vetting</h4>
              <p class="res-pillar-desc">Verifying that venue facilities supply dedicated transformer power without voltage drop during heavy stage lighting and LED volume spikes.</p>
              <div class="res-pillar-specs">
                <div class="res-pspec-item"><i class="fas fa-check"></i> 400A 3-Phase Camlock Company Switches</div>
                <div class="res-pspec-item"><i class="fas fa-check"></i> Dedicated Dark Fiber 10Gbps Symmetric Uplink</div>
                <div class="res-pspec-item"><i class="fas fa-check"></i> Uninterruptible Power Supply (UPS) for Broadcast</div>
              </div>
            </div>

            <!-- Pillar 2 -->
            <div class="res-pillar-card framer-spatial-radar">
              <div class="res-pillar-icon"><i class="fas fa-users-viewfinder"></i></div>
              <h4 class="res-pillar-title">Circulation & Capacity Ratios</h4>
              <p class="res-pillar-desc">Ensuring delegate flow between keynote plenaries, partner expos, and breakout sessions prevents choke points during peak intermissions.</p>
              <div class="res-pillar-specs">
                <div class="res-pspec-item"><i class="fas fa-check"></i> 18 sqft Minimum Per Seated Delegate</div>
                <div class="res-pspec-item"><i class="fas fa-check"></i> 1:25 Restroom Ratio for Executive Summits</div>
                <div class="res-pspec-item"><i class="fas fa-check"></i> 4,500 sqft Dedicated Registration Pre-Function</div>
              </div>
            </div>

            <!-- Pillar 3 -->
            <div class="res-pillar-card framer-spatial-radar">
              <div class="res-pillar-icon"><i class="fas fa-file-contract"></i></div>
              <h4 class="res-pillar-title">Contractual & Union Labour Riders</h4>
              <p class="res-pillar-desc">Auditing union jurisdiction boundaries (IATSE, Teamsters, Culinary) to prevent unbudgeted double-time and holiday labour escalation clauses.</p>
              <div class="res-pillar-specs">
                <div class="res-pspec-item"><i class="fas fa-check"></i> Load-In Curfew Waiver Clauses</div>
                <div class="res-pspec-item"><i class="fas fa-check"></i> Preferred AV Exclusivity Buyout Terms</div>
                <div class="res-pspec-item"><i class="fas fa-check"></i> Force Majeure Pandemic & Weather Rider</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 5: HYBRID PRACTICES (DUAL-HEMISPHERE TELEMETRY NEXUS)
         ===================================================================== -->
    <section id="hybrid-practices" class="res-section-hybrid">
      <div class="res-container">
        <!-- Section Header -->
        <div class="res-section-head framer-telemetry-nexus">
          <div class="res-badge"><i class="fas fa-tower-broadcast"></i> Dual-Hemisphere Broadcast</div>
          <h2 class="res-title">Hybrid Event Best Practices <span class="res-title-gradient">& Streaming Architecture</span></h2>
          <p class="res-subtitle">Unify in-person sensory engagement with global digital broadcast precision, synchronizing remote and on-premise delegates with zero perceived latency.</p>
        </div>

        <!-- Telemetry Status Ribbon -->
        <div class="res-telemetry-status-banner framer-telemetry-nexus">
          <div class="res-telemetry-chip">
            <div class="res-tchip-icon"><i class="fas fa-gauge-high"></i></div>
            <div>
              <div class="res-tchip-val">&lt; 45ms</div>
              <div class="res-tchip-lbl">Glass-to-Glass Latency</div>
            </div>
          </div>
          <div class="res-telemetry-chip">
            <div class="res-tchip-icon"><i class="fas fa-video"></i></div>
            <div>
              <div class="res-tchip-val">Dual 4K60</div>
              <div class="res-tchip-lbl">Redundant SRT Ingest</div>
            </div>
          </div>
          <div class="res-telemetry-chip">
            <div class="res-tchip-icon"><i class="fas fa-network-wired"></i></div>
            <div>
              <div class="res-tchip-val">99.999%</div>
              <div class="res-tchip-lbl">Uptime SLA Guarantee</div>
            </div>
          </div>
          <div class="res-telemetry-chip">
            <div class="res-tchip-icon"><i class="fas fa-language"></i></div>
            <div>
              <div class="res-tchip-val">18 Languages</div>
              <div class="res-tchip-lbl">Real-Time AI Subtitling</div>
            </div>
          </div>
        </div>

        <!-- Dual-Hemisphere Interlocking Display -->
        <div class="res-dual-hemisphere-grid">
          <!-- Left Hemisphere: Physical Plenary -->
          <div class="res-hemisphere-panel framer-telemetry-nexus">
            <div class="res-hemi-tag"><i class="fas fa-location-dot"></i> Hemisphere Alpha • In-Person Experience</div>
            <h3 class="res-hemi-title">Physical Stage & Sensory Impact</h3>
            <p class="res-hemi-desc">Designing live keynotes that command the physical room through dynamic lighting, spatial audio, and high-contrast LED volumes.</p>
            <div class="res-hemi-features">
              <div class="res-hfeat-row">
                <i class="fas fa-check-circle"></i>
                <span><strong>Confidence Monitors:</strong> Dual 65" teleprompters displaying speaker notes and live remote Q&A stream.</span>
              </div>
              <div class="res-hfeat-row">
                <i class="fas fa-check-circle"></i>
                <span><strong>Line-of-Sight Geometry:</strong> Tiered seating arranged to optimize unobstructed sightlines to primary visual focal points.</span>
              </div>
              <div class="res-hfeat-row">
                <i class="fas fa-check-circle"></i>
                <span><strong>Wireless Mic Coordination:</strong> Intermodulation-free frequency plan managed with real-time RF spectrum analyzers.</span>
              </div>
            </div>
          </div>

          <!-- Center Nexus Sphere -->
          <div class="res-nexus-center framer-telemetry-nexus">
            <div class="res-nexus-lens">
              <img src="images/resource_hybrid_practices.jpg" alt="Hybrid Event Broadcast Control Center">
            </div>
            <div class="res-nexus-badge-floating">
              <i class="fas fa-satellite"></i> Sync Hub Active
            </div>
          </div>

          <!-- Right Hemisphere: Virtual Cloud -->
          <div class="res-hemisphere-panel framer-telemetry-nexus">
            <div class="res-hemi-tag"><i class="fas fa-cloud"></i> Hemisphere Beta • Virtual Broadcast</div>
            <h3 class="res-hemi-title">Cloud CDN & Interactive Metaverse</h3>
            <p class="res-hemi-desc">Transforming the passive video stream into an active digital exchange with synchronized interactive polling and networking breakout suites.</p>
            <div class="res-hemi-features">
              <div class="res-hfeat-row">
                <i class="fas fa-check-circle"></i>
                <span><strong>Multi-Bitrate Transcoding:</strong> Adaptive streaming serving optimal resolution from 720p mobile to 4K executive displays.</span>
              </div>
              <div class="res-hfeat-row">
                <i class="fas fa-check-circle"></i>
                <span><strong>Digital Green Room:</strong> Remote VIP keynote speakers staged and briefed via isolated intercom and latency checks.</span>
              </div>
              <div class="res-hfeat-row">
                <i class="fas fa-check-circle"></i>
                <span><strong>Attendee Engagement Telemetry:</strong> Live sentiment scoring, heatmaps of session retention, and automated attendance logging.</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Interlocking Horizontal Timeline Protocols -->
        <div class="res-hybrid-protocols-row">
          <div class="res-protocol-card framer-telemetry-nexus">
            <div class="res-protocol-step-num">Protocol 01</div>
            <h4 class="res-protocol-title">Pre-Show Digital Sync</h4>
            <p class="res-protocol-desc">Simultaneous 60-minute technical dry run verifying audio packet buffering, switcher cut cues, and remote speaker links.</p>
          </div>
          <div class="res-protocol-card framer-telemetry-nexus">
            <div class="res-protocol-step-num">Protocol 02</div>
            <h4 class="res-protocol-title">Speaker Green Room Isolation</h4>
            <p class="res-protocol-desc">Dedicated video engineers manage remote contributor lighting, bandwidth stability, and teleprompter synchronicity.</p>
          </div>
          <div class="res-protocol-card framer-telemetry-nexus">
            <div class="res-protocol-step-num">Protocol 03</div>
            <h4 class="res-protocol-title">Bimodal Q&A Bridging</h4>
            <p class="res-protocol-desc">In-room mic runners and virtual upvoted questions alternated dynamically by the session moderator via tablet feed.</p>
          </div>
          <div class="res-protocol-card framer-telemetry-nexus">
            <div class="res-protocol-step-num">Protocol 04</div>
            <h4 class="res-protocol-title">Automated VOD Archival</h4>
            <p class="res-protocol-desc">Keynote sessions clipped, closed-captioned, and uploaded to the corporate digital learning portal within 90 minutes of wrap.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 6: INDUSTRY INSIGHTS (EXECUTIVE MONOGRAPH EDITORIAL)
         ===================================================================== -->
    <section id="industry-insights" class="res-section-insights">
      <div class="res-container">
        <!-- Section Header -->
        <div class="res-section-head framer-monograph-editorial">
          <div class="res-badge"><i class="fas fa-newspaper"></i> Executive Research</div>
          <h2 class="res-title">Industry Insights <span class="res-title-gradient">& Special Monographs</span></h2>
          <p class="res-subtitle">In-depth whitepapers, empirical market reports, and strategic briefings authored by our senior event management architects.</p>
        </div>

        <!-- Taxonomy Filter Bar -->
        <div class="res-taxonomy-bar framer-monograph-editorial">
          <div class="res-tax-filters">
            <button class="res-tax-btn active" onclick="filterArticles('all', this)">All Research</button>
            <button class="res-tax-btn" onclick="filterArticles('trends', this)">Macro Trends</button>
            <button class="res-tax-btn" onclick="filterArticles('tech', this)">AV & Emerging Tech</button>
            <button class="res-tax-btn" onclick="filterArticles('sustainability', this)">Net-Zero & ESG</button>
            <button class="res-tax-btn" onclick="filterArticles('strategy', this)">Executive Retention</button>
          </div>
          <div style="font-size: 0.85rem; color: var(--res-text-muted); font-weight: 600;">
            <i class="fas fa-check-double text-warning"></i> Updated Weekly with Peer-Reviewed Insights
          </div>
        </div>

        <!-- Asymmetric Monograph Grid -->
        <div class="res-editorial-deck-grid">
          <!-- Left Feature Hero Monograph -->
          <div class="res-hero-monograph framer-monograph-editorial">
            <div class="res-monograph-img-box">
              <img src="images/resource_industry_insights.jpg" alt="Executive Event Industry Monograph Report">
              <div class="res-monograph-meta-ribbon">
                <i class="fas fa-bookmark"></i> Q4 2026 Special Whitepaper
              </div>
            </div>
            <div class="res-monograph-content">
              <div class="res-monograph-byline">
                <span><i class="fas fa-user-tie"></i> By Dr. Victoria Chen, Lead Strategist</span>
                <span><i class="fas fa-clock"></i> 14 Min Read</span>
                <span><i class="fas fa-calendar-day"></i> October 2026</span>
              </div>
              <h3 class="res-monograph-title">The Death of Traditional PowerPoints: Generative Real-Time Visuals in B2B Keynotes</h3>
              <p class="res-monograph-summary">Why Fortune 100 summits are abandoning static bullet-point slides in favor of live-rendered 3D holographic models, generative data visualization canvasses, and interactive audience-driven storytelling.</p>
              <div class="res-monograph-bullets">
                <div class="res-mbullet-row"><i class="fas fa-arrow-right"></i> Measurable 42% lift in post-keynote recall among C-suite executives.</div>
                <div class="res-mbullet-row"><i class="fas fa-arrow-right"></i> Low-latency Unreal Engine integration for real-time stage background synthesis.</div>
                <div class="res-mbullet-row"><i class="fas fa-arrow-right"></i> Budget allocation shift from post-production animation to real-time visual operators.</div>
              </div>
              <div class="res-monograph-actions">
                <button class="res-btn res-btn-primary" onclick="openDownloadModal('Complete Whitepaper: Generative Visuals in B2B Keynotes (PDF)')">
                  <i class="fas fa-file-pdf"></i> Read Full Monograph
                </button>
                <div style="font-size: 0.85rem; color: var(--res-text-muted); font-weight: 600;">
                  <i class="fas fa-download"></i> 3,840 Downloads
                </div>
              </div>
            </div>
          </div>

          <!-- Right Stacked Research Briefs -->
          <div class="res-stacked-briefs">
            <!-- Brief 1 -->
            <div class="res-brief-card framer-monograph-editorial" data-category="sustainability">
              <div class="res-brief-top">
                <span class="res-brief-cat">Net-Zero & ESG</span>
                <span class="res-brief-date">September 2026</span>
              </div>
              <h4 class="res-brief-title">Decarbonizing 5,000-Attendee Summits: Scope 1-3 Carbon Accounting</h4>
              <p class="res-brief-excerpt">A tactical framework for reducing food-mile emissions, replacing diesel generators with hydrogen fuel cells, and measuring delegate transport impacts.</p>
              <div class="res-brief-bottom">
                <span style="font-size: 0.8rem; color: var(--res-text-muted);"><i class="fas fa-clock"></i> 9 Min Read</span>
                <a class="res-brief-link" onclick="openDownloadModal('Net-Zero Conference Blueprint (PDF)')">Download Brief <i class="fas fa-arrow-right"></i></a>
              </div>
            </div>

            <!-- Brief 2 -->
            <div class="res-brief-card framer-monograph-editorial" data-category="strategy">
              <div class="res-brief-top">
                <span class="res-brief-cat">Executive Retention</span>
                <span class="res-brief-date">August 2026</span>
              </div>
              <h4 class="res-brief-title">Neuroscience-Backed Agenda Design: Eliminating Executive Summit Fatigue</h4>
              <p class="res-brief-excerpt">Structuring 18-minute TED-style keynote modules separated by active networking interludes to maximize neurological attention and deal flow.</p>
              <div class="res-brief-bottom">
                <span style="font-size: 0.8rem; color: var(--res-text-muted);"><i class="fas fa-clock"></i> 11 Min Read</span>
                <a class="res-brief-link" onclick="openDownloadModal('Neuroscience Agenda Design Report (PDF)')">Download Brief <i class="fas fa-arrow-right"></i></a>
              </div>
            </div>

            <!-- Brief 3 -->
            <div class="res-brief-card framer-monograph-editorial" data-category="tech">
              <div class="res-brief-top">
                <span class="res-brief-cat">AV & Emerging Tech</span>
                <span class="res-brief-date">July 2026</span>
              </div>
              <h4 class="res-brief-title">The Rise of Spatial Audio in Exhibition Halls: Micro-Zoned Soundscapes</h4>
              <p class="res-brief-excerpt">How directional acoustic beamforming isolates 50 concurrent sponsor presentations in an open trade show floor without noise bleed.</p>
              <div class="res-brief-bottom">
                <span style="font-size: 0.8rem; color: var(--res-text-muted);"><i class="fas fa-clock"></i> 8 Min Read</span>
                <a class="res-brief-link" onclick="openDownloadModal('Spatial Audio Vetting Report (PDF)')">Download Brief <i class="fas fa-arrow-right"></i></a>
              </div>
            </div>
          </div>
        </div>

        <!-- Executive Newsletter Bar -->
        <div class="res-newsletter-vault-bar framer-monograph-editorial">
          <div class="res-news-info">
            <h4 class="res-news-title">Receive Quarterly Strategic Intelligence Briefings</h4>
            <p class="res-news-desc">Curated executive summaries delivered directly to corporate event leads and agency partners. Zero spam.</p>
          </div>
          <form class="res-news-form" onsubmit="handleNewsletterSubmit(event)">
            <input type="email" required placeholder="Enter corporate email address..." class="res-news-input">
            <button type="submit" class="res-btn res-btn-primary">
              <i class="fas fa-paper-plane"></i> Subscribe
            </button>
          </form>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         SECTION 7: FREQUENTLY ASKED QUESTIONS (INTELLIGENCE QUERY VAULT)
         ===================================================================== -->
    <section id="faq" class="res-section-faq">
      <div class="res-container">
        <!-- Section Header -->
        <div class="res-section-head framer-vault-accordion">
          <div class="res-badge"><i class="fas fa-circle-question"></i> Knowledge Repository</div>
          <h2 class="res-title">Frequently Asked Questions <span class="res-title-gradient">& Executive Knowledge Vault</span></h2>
          <p class="res-subtitle">Clear, authoritative answers to common inquiries regarding lead times, budget structures, technical riders, and crisis management protocols.</p>
        </div>

        <!-- FAQ Search & Category Filter Hub -->
        <div class="res-faq-query-hub framer-vault-accordion">
          <div class="res-faq-search-box">
            <i class="fas fa-magnifying-glass res-faq-search-icon"></i>
            <input type="text" id="faqSearchInput" class="res-faq-search-input" placeholder="Search keywords across all FAQs (e.g. lead time, budget, streaming, cancellation)..." oninput="filterFaqLive(this.value)">
          </div>
          <div class="res-faq-tabs-row">
            <button class="res-faq-cat-btn active" onclick="filterFaqCategory('all', this)">All Categories</button>
            <button class="res-faq-cat-btn" onclick="filterFaqCategory('planning', this)">Planning & Timelines</button>
            <button class="res-faq-cat-btn" onclick="filterFaqCategory('budget', this)">Budget & Billing</button>
            <button class="res-faq-cat-btn" onclick="filterFaqCategory('production', this)">Production & AV</button>
            <button class="res-faq-cat-btn" onclick="filterFaqCategory('security', this)">Risk & Safety</button>
          </div>
        </div>

        <!-- Asymmetric 2-Wing Architecture -->
        <div class="res-faq-matrix-grid">
          <!-- Left Wing: Concierge Assistance Pod -->
          <div class="res-faq-concierge-card framer-vault-accordion">
            <div class="res-concierge-img-box">
              <img src="images/resource_faq_desk.jpg" alt="Executive Concierge Support Desk">
              <div class="res-concierge-status-badge">
                <i class="fas fa-circle text-success" style="font-size: 0.6rem;"></i> Concierge Desk Active
              </div>
            </div>
            <div class="res-concierge-body">
              <h4 class="res-concierge-title">Need Bespoke Guidance?</h4>
              <p class="res-concierge-desc">Our senior consultation team is available for real-time scoping sessions and custom RFP technical reviews.</p>
              <div class="res-concierge-sla-box">
                <div class="res-sla-item">
                  <span class="res-sla-lbl">Direct Response Time</span>
                  <span class="res-sla-val">&lt; 18 Minutes</span>
                </div>
                <div class="res-sla-item">
                  <span class="res-sla-lbl">Direct Support Hotline</span>
                  <span class="res-sla-val">+1 (800) 456-APEX</span>
                </div>
                <div class="res-sla-item">
                  <span class="res-sla-lbl">Confidentiality</span>
                  <span class="res-sla-val">Mutual NDA Ready</span>
                </div>
              </div>
              <a href="contact.html" class="res-btn res-btn-primary res-concierge-btn">
                <i class="fas fa-headset"></i> Contact Advisory Desk
              </a>
            </div>
          </div>

          <!-- Right Wing: Interactive Smart Accordion List -->
          <div class="res-faq-accordion-list">
            <!-- FAQ 1 -->
            <div class="res-faq-item framer-vault-accordion active" data-category="planning">
              <div class="res-faq-header" onclick="toggleFaqItem(this)">
                <div class="res-faq-header-left">
                  <span class="res-faq-cat-tag">Planning & Timelines</span>
                  <h4 class="res-faq-question">What is the recommended planning runway for an enterprise corporate summit?</h4>
                </div>
                <div class="res-faq-chevron"><i class="fas fa-chevron-down"></i></div>
              </div>
              <div class="res-faq-body">
                <div class="res-faq-content">
                  <p>For flagship corporate conferences (1,000+ delegates) or multi-day leadership summits, we recommend a minimum planning runway of <strong>6 to 9 months</strong>. This allows for prime venue acquisition, keynote speaker lock-in, and custom scenic stage fabrication.</p>
                  <ul>
                    <li><strong>T-180 Days:</strong> Venue contract execution and primary production scope lock.</li>
                    <li><strong>T-90 Days:</strong> Keynote narrative development, registration launch, and sponsor onboarding.</li>
                    <li><strong>T-30 Days:</strong> Final run-of-show synchronization, catering count lock, and freight dispatch.</li>
                  </ul>
                  <p>For urgent executive summits or crisis symposiums, our rapid-response production division can deploy fully operational turn-key environments within <strong>21 to 30 business days</strong>.</p>
                  <div class="res-faq-feedback">
                    <span>Was this response informative?</span>
                    <div class="res-feedback-btns">
                      <button class="res-feedback-btn" onclick="rateFaq(this, true)"><i class="fas fa-thumbs-up"></i> Yes (142)</button>
                      <button class="res-feedback-btn" onclick="rateFaq(this, false)"><i class="fas fa-thumbs-down"></i> No (2)</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- FAQ 2 -->
            <div class="res-faq-item framer-vault-accordion" data-category="budget">
              <div class="res-faq-header" onclick="toggleFaqItem(this)">
                <div class="res-faq-header-left">
                  <span class="res-faq-cat-tag">Budget & Billing</span>
                  <h4 class="res-faq-question">How does Apex manage unexpected cost overages and change orders?</h4>
                </div>
                <div class="res-faq-chevron"><i class="fas fa-chevron-down"></i></div>
              </div>
              <div class="res-faq-body">
                <div class="res-faq-content">
                  <p>We operate under an open-book transparent ledger model. Our contracts feature a strict <strong>Guaranteed Maximum Price (GMP)</strong> clause for management and production staging. Any requested scope change requires a formal written Change Order with itemized cost justification.</p>
                  <p>Furthermore, we establish an explicit <strong>10% to 12% contingency reserve</strong> within every approved budget to absorb unforeseen site fees or technical rider additions without impacting executive authorization limits.</p>
                  <div class="res-faq-feedback">
                    <span>Was this response informative?</span>
                    <div class="res-feedback-btns">
                      <button class="res-feedback-btn" onclick="rateFaq(this, true)"><i class="fas fa-thumbs-up"></i> Yes (98)</button>
                      <button class="res-feedback-btn" onclick="rateFaq(this, false)"><i class="fas fa-thumbs-down"></i> No (1)</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- FAQ 3 -->
            <div class="res-faq-item framer-vault-accordion" data-category="production">
              <div class="res-faq-header" onclick="toggleFaqItem(this)">
                <div class="res-faq-header-left">
                  <span class="res-faq-cat-tag">Production & AV</span>
                  <h4 class="res-faq-question">What failsafe redundancies are deployed during live global plenary broadcasts?</h4>
                </div>
                <div class="res-faq-chevron"><i class="fas fa-chevron-down"></i></div>
              </div>
              <div class="res-faq-body">
                <div class="res-faq-content">
                  <p>Apex enforces an <strong>N+1 and N+2 hardware redundancy standard</strong> across all mission-critical audio-visual nodes:</p>
                  <ul>
                    <li><strong>Dual Main & Backup Vision Switchers:</strong> Mirroring every cut seamlessly; if Primary fails, Backup takes control in &lt; 2 frames.</li>
                    <li><strong>Bonded Cellular & Satellite Uplink:</strong> Commercial dark fiber backed by dual bonded Starlink and 5G cellular arrays.</li>
                    <li><strong>Isolated Generator Feeds:</strong> High-efficiency whisper generators operating concurrently with municipal house feeds through automatic transfer switches.</li>
                  </ul>
                  <div class="res-faq-feedback">
                    <span>Was this response informative?</span>
                    <div class="res-feedback-btns">
                      <button class="res-feedback-btn" onclick="rateFaq(this, true)"><i class="fas fa-thumbs-up"></i> Yes (164)</button>
                      <button class="res-feedback-btn" onclick="rateFaq(this, false)"><i class="fas fa-thumbs-down"></i> No (0)</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- FAQ 4 -->
            <div class="res-faq-item framer-vault-accordion" data-category="security">
              <div class="res-faq-header" onclick="toggleFaqItem(this)">
                <div class="res-faq-header-left">
                  <span class="res-faq-cat-tag">Risk & Safety</span>
                  <h4 class="res-faq-question">How are VIP dignitary protocols and secure perimeter zones handled?</h4>
                </div>
                <div class="res-faq-chevron"><i class="fas fa-chevron-down"></i></div>
              </div>
              <div class="res-faq-body">
                <div class="res-faq-content">
                  <p>Our executive protection liaison coordinates directly with secret service detachments, municipal police, and corporate security teams. We design <strong>three concentric rings of security clearance</strong>:</p>
                  <ul>
                    <li><strong>Outer Perimeter:</strong> Vehicle screening, badge verification checkpoints, and discreet bomb-sniffing K9 sweeps.</li>
                    <li><strong>Intermediate Concourse:</strong> RFID/NFC attendee validation and biometric access lanes.</li>
                    <li><strong>Inner Green Room Sanctum:</strong> Soundproofed, isolated executive suites with private emergency ingress/egress.</li>
                  </ul>
                  <div class="res-faq-feedback">
                    <span>Was this response informative?</span>
                    <div class="res-feedback-btns">
                      <button class="res-feedback-btn" onclick="rateFaq(this, true)"><i class="fas fa-thumbs-up"></i> Yes (87)</button>
                      <button class="res-feedback-btn" onclick="rateFaq(this, false)"><i class="fas fa-thumbs-down"></i> No (3)</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- FAQ 5 -->
            <div class="res-faq-item framer-vault-accordion" data-category="planning">
              <div class="res-faq-header" onclick="toggleFaqItem(this)">
                <div class="res-faq-header-left">
                  <span class="res-faq-cat-tag">Planning & Timelines</span>
                  <h4 class="res-faq-question">Can Apex handle international multi-city roadshows across diverse jurisdictions?</h4>
                </div>
                <div class="res-faq-chevron"><i class="fas fa-chevron-down"></i></div>
              </div>
              <div class="res-faq-body">
                <div class="res-faq-content">
                  <p>Yes. We operate global operational hubs in New York, London, Singapore, and Dubai. Our ATA Carnet logistics specialists manage cross-border customs clearance for stage equipment, staging hardware, and promotional collateral without import tariffs or shipping impounds.</p>
                  <p>We provide localized bilingual site coordinators, local union liaison leads, and regional compliance experts for all major international conference capitals.</p>
                  <div class="res-faq-feedback">
                    <span>Was this response informative?</span>
                    <div class="res-feedback-btns">
                      <button class="res-feedback-btn" onclick="rateFaq(this, true)"><i class="fas fa-thumbs-up"></i> Yes (115)</button>
                      <button class="res-feedback-btn" onclick="rateFaq(this, false)"><i class="fas fa-thumbs-down"></i> No (1)</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- FAQ 6 -->
            <div class="res-faq-item framer-vault-accordion" data-category="production">
              <div class="res-faq-header" onclick="toggleFaqItem(this)">
                <div class="res-faq-header-left">
                  <span class="res-faq-cat-tag">Production & AV</span>
                  <h4 class="res-faq-question">What sustainability and waste reduction standards are enforced on-site?</h4>
                </div>
                <div class="res-faq-chevron"><i class="fas fa-chevron-down"></i></div>
              </div>
              <div class="res-faq-body">
                <div class="res-faq-content">
                  <p>All Apex-managed events adhere to <strong>ISO-20121 Sustainable Event Management systems</strong>. We mandate 100% LED lighting fixtures, reusable aluminum scenic truss systems, zero single-use plastics, digital credentialing, and post-event donation of excess prepared food to verified local charities.</p>
                  <p>At the conclusion of each summit, we provide clients with an audited Carbon Footprint & Waste Diversion Report suitable for annual corporate ESG filings.</p>
                  <div class="res-faq-feedback">
                    <span>Was this response informative?</span>
                    <div class="res-feedback-btns">
                      <button class="res-feedback-btn" onclick="rateFaq(this, true)"><i class="fas fa-thumbs-up"></i> Yes (130)</button>
                      <button class="res-feedback-btn" onclick="rateFaq(this, false)"><i class="fas fa-thumbs-down"></i> No (2)</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Interactive Quick View / Download Modal -->
  <div id="resDownloadModal" class="res-modal-overlay">
    <div class="res-modal-card">
      <button class="res-modal-close" onclick="closeResModal()">&times;</button>
      <div class="res-modal-icon"><i class="fas fa-file-circle-check"></i></div>
      <h3 id="resModalTitle" class="res-modal-title">Resource Download Ready</h3>
      <p id="resModalDesc" class="res-modal-desc">Your requested executive resource document has been queued for immediate access. Enter your email to receive direct link & updates.</p>
      <div style="display: flex; gap: 0.75rem; justify-content: center;">
        <button class="res-btn res-btn-primary" onclick="confirmDownload()">
          <i class="fas fa-download"></i> Begin Download (.PDF)
        </button>
        <button class="res-btn res-btn-outline" onclick="closeResModal()">Close</button>
      </div>
    </div>
  </div>
"""

    # Page Interactive Scripts
    new_res_scripts = """
  <!-- =====================================================================
       INTERACTIVE RESOURCES PAGE CONTROLLER SCRIPT
       ===================================================================== -->
  <script>
    // 1. Intersection Observer for Bespoke Framer Motion Animations
    document.addEventListener('DOMContentLoaded', function() {
      var framerElements = document.querySelectorAll(
        '.framer-codex-stack, ' +
        '.framer-mission-gauge, ' +
        '.framer-ledger-cascade, ' +
        '.framer-spatial-radar, ' +
        '.framer-telemetry-nexus, ' +
        '.framer-monograph-editorial, ' +
        '.framer-vault-accordion'
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

      // Initialize Checklist Task Matrix
      renderChecklistPhase(0);
    });

    // 2. Guide Category Filter
    function filterGuides(category, btn) {
      var pills = document.querySelectorAll('.res-arch-pill');
      pills.forEach(function(p) { p.classList.remove('active'); });
      if (btn) btn.classList.add('active');

      var cards = document.querySelectorAll('.res-micro-card');
      cards.forEach(function(card) {
        if (category === 'all' || card.getAttribute('data-category') === category) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    }

    // 3. Conference Preparation Checklist State & Phase Matrix
    var checklistData = [
      {
        phase: 'Phase I: Strategic Foundation Checkpoints (T-180 Days)',
        tasks: [
          { title: 'Executive Charter & Objectives Sign-off', desc: 'Secure alignment on key deliverables and attendee demographics.', tag: 'Governance', done: true },
          { title: 'Prime Venue Sourcing & RFP Shortlisting', desc: 'Distribute spatial criteria to verified convention centers.', tag: 'Procurement', done: true },
          { title: 'Keynote Speaker & Luminary Hold Dates', desc: 'Confirm availability and draft initial appearance agreements.', tag: 'Talent', done: true },
          { title: 'Preliminary Budget Allocation Model Lock', desc: 'Establish approved Capex and contingency variance thresholds.', tag: 'Finance', done: true },
          { title: 'Steering Committee Bi-Weekly Cadence', desc: 'Assign workstream leaders across marketing, AV, and VIP liaison.', tag: 'Operations', done: false }
        ]
      },
      {
        phase: 'Phase II: Production Matrix & RFP Vetting (T-90 Days)',
        tasks: [
          { title: 'Audiovisual & Stage Fabricator Contracting', desc: 'Review 3D CAD renders, rigging calculations, and LED volume specs.', tag: 'Technical', done: true },
          { title: 'Sponsorship Packages & Exhibitor Portal Launch', desc: 'Publish booth tiers and distribute technical electrical riders.', tag: 'Revenue', done: true },
          { title: 'Hospitality & VIP Menu Tasting Protocols', desc: 'Verify dietary certifications, banquet staffing, and cocktail logistics.', tag: 'Catering', done: true },
          { title: 'Emergency Management & Municipal Permit Filings', desc: 'Submit fire marshal plans and medical emergency egress maps.', tag: 'Safety', done: false },
          { title: 'Branding & Scenic Collateral Production Run', desc: 'Sign off high-resolution vector print assets and lanyard runs.', tag: 'Creative', done: false }
        ]
      },
      {
        phase: 'Phase III: Logistics & Rehearsals (T-30 Days)',
        tasks: [
          { title: 'Complete Minute-by-Minute Run-of-Show Lock', desc: 'Synchronize stage cues, presenter walk-ups, and audio stings.', tag: 'Show Calling', done: true },
          { title: 'Freight Dispatch & Custom Carnet Clearance', desc: 'Track transit trucks carrying proprietary lighting rigs and AV servers.', tag: 'Logistics', done: true },
          { title: 'Mobile App & Digital Credential Deployment', desc: 'Test barcode badge scanning and personalized delegate agendas.', tag: 'Digital', done: false },
          { title: 'VIP Motorcade Ingress & Green Room Walkthrough', desc: 'Dry-run dignitary arrival routes with municipal security escorts.', tag: 'Security', done: false },
          { title: 'Presenter Slide Deck Review & 16:9 Formatting', desc: 'Conduct technical rehearsals and check embedded video audio codecs.', tag: 'Content', done: false }
        ]
      },
      {
        phase: 'Phase IV: Zero-Hour Execution (T-24 Hours to Go-Live)',
        tasks: [
          { title: 'Complete Intercom & Radio Channel Sweep', desc: 'Verify clear comms between Show Caller, Audio Engineer, and Stage Manager.', tag: 'Comms', done: true },
          { title: 'Primary & Backup Generator Load Test', desc: 'Simulate municipal power failure and measure transfer switch response.', tag: 'Redundancy', done: true },
          { title: 'Confidence Monitor & Teleprompter Dry Run', desc: 'Ensure keynote scripts and downstage timer clocks are synchronized.', tag: 'Staging', done: true },
          { title: 'Catering Line Health & Sanitation Audit', desc: 'Inspect back-of-house culinary prep areas and refrigeration logs.', tag: 'Hospitality', done: true },
          { title: 'Doors Open Final Radio Clearance', desc: 'Authorize registration concourse opening and delegate badge flow.', tag: 'Launch', done: true }
        ]
      }
    ];

    var currentPhaseIdx = 0;

    function renderChecklistPhase(phaseIdx) {
      currentPhaseIdx = phaseIdx;
      var data = checklistData[phaseIdx];
      var titleEl = document.getElementById('activePhaseTitle');
      if (titleEl) titleEl.textContent = data.phase;

      var container = document.getElementById('taskItemsContainer');
      if (!container) return;

      container.innerHTML = '';
      var cleared = 0;

      data.tasks.forEach(function(task, idx) {
        if (task.done) cleared++;
        var item = document.createElement('div');
        item.className = 'res-task-item' + (task.done ? ' completed' : '');
        item.onclick = function() {
          task.done = !task.done;
          renderChecklistPhase(currentPhaseIdx);
        };

        var checkIcon = task.done ? '<i class="fas fa-check"></i>' : '';
        item.innerHTML = 
          '<div class="res-task-check">' + checkIcon + '</div>' +
          '<div class="res-task-content">' +
            '<div class="res-task-title">' + task.title + '</div>' +
            '<div class="res-task-desc">' + task.desc + '</div>' +
            '<span class="res-task-tag">' + task.tag + '</span>' +
          '</div>';
        container.appendChild(item);
      });

      var badgeEl = document.getElementById('clearedCountBadge');
      if (badgeEl) badgeEl.textContent = cleared + ' of ' + data.tasks.length + ' Cleared';

      // Update Radial Gauge across all phases
      updateOverallGauge();
    }

    function updateOverallGauge() {
      var total = 0;
      var done = 0;
      checklistData.forEach(function(phase) {
        phase.tasks.forEach(function(t) {
          total++;
          if (t.done) done++;
        });
      });

      var pct = Math.round((done / total) * 100);
      var textEl = document.getElementById('radialGaugeText');
      if (textEl) textEl.textContent = pct + '%';

      var bar = document.getElementById('radialGaugeBar');
      if (bar) {
        // circumference for r=36 is ~226
        var offset = 226 - (226 * (pct / 100));
        bar.style.strokeDashoffset = offset;
      }
    }

    function switchChecklistPhase(idx, btn, card) {
      if (btn) {
        var btns = document.querySelectorAll('.res-phase-btn');
        btns.forEach(function(b) { b.classList.remove('active'); });
        btn.classList.add('active');
      }

      var cards = document.querySelectorAll('.res-phase-card');
      cards.forEach(function(c, cIdx) {
        if (cIdx === idx) c.classList.add('active');
        else c.classList.remove('active');
      });

      renderChecklistPhase(idx);
    }

    // 4. Budget Planning Slider & Dynamic Allocation
    function updateBudgetSimulation(val) {
      val = parseInt(val, 10);
      var display = document.getElementById('sliderDisplayVal');
      if (display) display.textContent = '$' + val.toLocaleString();

      // Allocations
      var c1 = Math.round(val * 0.35); // 35% Venue & Staging
      var c2 = Math.round(val * 0.25); // 25% AV & Tech
      var c3 = Math.round(val * 0.20); // 20% Hospitality
      var c4 = Math.round(val * 0.20); // 20% Contingency

      var el1 = document.getElementById('costCenter1');
      var el2 = document.getElementById('costCenter2');
      var el3 = document.getElementById('costCenter3');
      var el4 = document.getElementById('costCenter4');

      if (el1) el1.textContent = '$' + c1.toLocaleString();
      if (el2) el2.textContent = '$' + c2.toLocaleString();
      if (el3) el3.textContent = '$' + c3.toLocaleString();
      if (el4) el4.textContent = '$' + c4.toLocaleString();

      // Estimated ROI (4.2x multiplier)
      var roiVal = document.getElementById('projectedRoiVal');
      if (roiVal) roiVal.textContent = '$' + Math.round(val * 4.2).toLocaleString() + ' Estimated Value';
    }

    // 5. Venue Guide Hotspots & Dimension Switcher
    function switchVenueDimension(dim, btn) {
      var tabs = document.querySelectorAll('.res-dim-tab');
      tabs.forEach(function(t) { t.classList.remove('active'); });
      if (btn) btn.classList.add('active');

      if (dim === 'structural') {
        activateHotspot(1, 'Truss Rigging & 28ft Clear Height', 'Structural roof supports certified for 45,000 lbs distributed AV payload and dynamic line arrays.');
      } else if (dim === 'ingress') {
        activateHotspot(2, 'Direct Freight Ingress Dock', 'Twin roll-up freight bays (16ft x 14ft) capable of receiving 53ft semitruck trailers directly onto plenary floor.');
      } else if (dim === 'acoustics') {
        activateHotspot(3, 'VIP Green Room Isolation Zone', 'Soundproofed green room with private executive restroom, secure fiber optic feed, and discreet motorcade egress.');
      } else if (dim === 'power') {
        activateHotspot(4, 'Emergency Egress & Fire Marshal Matrix', 'Dual-redundant primary egress corridors exceeding municipal NFPA-101 crowd dispersion standards by 35%.');
      }
    }

    function activateHotspot(num, title, detail) {
      var tagEl = document.getElementById('hotspotTag');
      var titleEl = document.getElementById('hotspotTitle');
      var detailEl = document.getElementById('hotspotDetail');

      if (tagEl) tagEl.textContent = 'Hotspot ' + num + ' Selected';
      if (titleEl) titleEl.textContent = title;
      if (detailEl) detailEl.textContent = detail;
    }

    // 6. Article Taxonomy Filter
    function filterArticles(cat, btn) {
      var btns = document.querySelectorAll('.res-tax-btn');
      btns.forEach(function(b) { b.classList.remove('active'); });
      if (btn) btn.classList.add('active');

      var briefs = document.querySelectorAll('.res-brief-card');
      briefs.forEach(function(b) {
        if (cat === 'all' || b.getAttribute('data-category') === cat) {
          b.style.display = 'flex';
        } else {
          b.style.display = 'none';
        }
      });
    }

    // 7. FAQ Smart Accordion & Live Search
    function toggleFaqItem(header) {
      var item = header.closest('.res-faq-item');
      if (!item) return;
      var isActive = item.classList.contains('active');

      // Optional: keep single open or accordion
      var allItems = document.querySelectorAll('.res-faq-item');
      allItems.forEach(function(i) { i.classList.remove('active'); });

      if (!isActive) {
        item.classList.add('active');
      }
    }

    function filterFaqLive(query) {
      query = query.toLowerCase().trim();
      var items = document.querySelectorAll('.res-faq-item');
      items.forEach(function(item) {
        var text = item.textContent.toLowerCase();
        if (query === '' || text.indexOf(query) !== -1) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    }

    function filterFaqCategory(cat, btn) {
      var btns = document.querySelectorAll('.res-faq-cat-btn');
      btns.forEach(function(b) { b.classList.remove('active'); });
      if (btn) btn.classList.add('active');

      var searchInput = document.getElementById('faqSearchInput');
      if (searchInput) searchInput.value = '';

      var items = document.querySelectorAll('.res-faq-item');
      items.forEach(function(item) {
        if (cat === 'all' || item.getAttribute('data-category') === cat) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    }

    function rateFaq(btn, isPositive) {
      btn.style.background = isPositive ? 'rgba(5, 150, 105, 0.2)' : 'rgba(220, 38, 38, 0.2)';
      btn.style.borderColor = isPositive ? '#059669' : '#dc2626';
      btn.innerHTML = '<i class="fas fa-check"></i> Feedback Recorded';
      btn.disabled = true;
    }

    // 8. Download / Quick View Modals
    function openDownloadModal(docName) {
      var modal = document.getElementById('resDownloadModal');
      var title = document.getElementById('resModalTitle');
      var desc = document.getElementById('resModalDesc');

      if (title) title.textContent = 'Resource Download Ready';
      if (desc) desc.textContent = 'You are downloading "' + docName + '". This certified document includes full ISO-20121 templates and implementation worksheets.';
      if (modal) modal.style.display = 'flex';
    }

    function openQuickView(docName) {
      var modal = document.getElementById('resDownloadModal');
      var title = document.getElementById('resModalTitle');
      var desc = document.getElementById('resModalDesc');

      if (title) title.textContent = 'Executive Preview Mode';
      if (desc) desc.textContent = 'Previewing: ' + docName + '. All proprietary production rubrics and spatial guidelines have been initialized for client review.';
      if (modal) modal.style.display = 'flex';
    }

    function closeResModal() {
      var modal = document.getElementById('resDownloadModal');
      if (modal) modal.style.display = 'none';
    }

    function confirmDownload() {
      alert('Your document download has commenced! Thank you for accessing the Apex Knowledge Repository.');
      closeResModal();
    }

    function handleNewsletterSubmit(e) {
      e.preventDefault();
      alert('Thank you! You have been successfully subscribed to our Quarterly Strategic Intelligence Briefings.');
      e.target.reset();
    }
  </script>
"""

    # Assemble complete document
    final_html = (
        nav_head_up_to_style
        + new_res_css
        + "\n  </style>"
        + nav_mid[len("</style>"):]
        + new_res_content
        + footer_full
        + new_res_scripts
        + closing_part
    )

    with open('resources.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print("Successfully built redesigned resources.html! Total length:", len(final_html))

if __name__ == '__main__':
    generate_resources()
