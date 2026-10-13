# -*- coding: utf-8 -*-
"""
generate_home2_page.py
Generates home-2.html with 6 distinct sections between navbar and footer.
Guarantees 100% preservation of navbar and footer from navbar.html.
"""

import os, re

def build_home2():
    with open('navbar.html', 'r', encoding='utf-8') as f:
        nav = f.read()

    head_idx = nav.find('</style>')
    footer_start = nav.find('<!-- FOOTER -->')
    footer_end = nav.rfind('</body>')

    head_before = nav[:head_idx]
    nav_middle = nav[head_idx:footer_start]
    footer_body = nav[footer_start:footer_end]
    closing_html = nav[footer_end:]

    # CSS for home-2.html
    page_css = """
    /* ==========================================================================
       HOME-2 SOVEREIGN SUMMIT ARCHITECTURE STYLES
       ========================================================================== */
    :root {
      --h2-navy-deep: #070c18;
      --h2-navy-card: #0f182c;
      --h2-navy-card-border: rgba(59, 130, 246, 0.18);
      --h2-gold-accent: #f59e0b;
      --h2-sapphire-accent: #3b82f6;
      --h2-cyan-accent: #06b6d4;
      --h2-emerald-accent: #10b981;
      --h2-text-light-title: #0f172a;
      --h2-text-light-body: #334155;
      --h2-bg-light-sec: #f8fafc;
      --h2-card-light-bg: #ffffff;
      --h2-card-light-border: #e2e8f0;
    }

    body.dark {
      --h2-navy-deep: #050811;
      --h2-navy-card: #0b1325;
      --h2-navy-card-border: rgba(59, 130, 246, 0.25);
      --h2-text-light-title: #f8fafc;
      --h2-text-light-body: #94a3b8;
      --h2-bg-light-sec: #070d1a;
      --h2-card-light-bg: #0d162a;
      --h2-card-light-border: rgba(255, 255, 255, 0.08);
    }

    /* Common Section Wrapper */
    .h2-section {
      position: relative;
      padding: 6.5rem 1.5rem;
      background-color: var(--h2-bg-light-sec);
      color: var(--h2-text-light-body);
      overflow: hidden;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    .h2-container {
      max-width: 1280px;
      margin: 0 auto;
      position: relative;
      z-index: 10;
    }

    .h2-section-header {
      text-align: center;
      max-width: 820px;
      margin: 0 auto 4rem auto;
    }

    .h2-supertitle {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      padding: 0.35rem 1rem;
      border-radius: 9999px;
      background: rgba(59, 130, 246, 0.1);
      color: var(--h2-sapphire-accent);
      border: 1px solid rgba(59, 130, 246, 0.25);
      margin-bottom: 1rem;
    }

    body.dark .h2-supertitle {
      background: rgba(59, 130, 246, 0.15);
      border-color: rgba(59, 130, 246, 0.35);
      color: #60a5fa;
    }

    .h2-title {
      font-size: 2.5rem;
      font-weight: 800;
      line-height: 1.2;
      color: var(--h2-text-light-title);
      margin-bottom: 1.25rem;
      letter-spacing: -0.02em;
    }

    @media (min-width: 768px) {
      .h2-title {
        font-size: 3.25rem;
      }
    }

    .h2-desc {
      font-size: 1.125rem;
      line-height: 1.7;
      color: var(--h2-text-light-body);
    }

    /* Ambient Glow Effects */
    .h2-ambient-glow {
      position: absolute;
      width: 500px;
      height: 500px;
      border-radius: 50%;
      pointer-events: none;
      filter: blur(120px);
      opacity: 0.15;
      z-index: 1;
    }

    body.dark .h2-ambient-glow {
      opacity: 0.25;
    }

    /* ==========================================================================
       FRAMER MOTION SPECIFIC CLASSES & KEYFRAMES (6 NOVEL EASINGS)
       ========================================================================== */

    /* 1. framer-cinema-hero */
    .framer-cinema-hero {
      opacity: 0;
      transform: translateY(45px) scale(0.97);
      transition: opacity 0.95s cubic-bezier(0.16, 1, 0.3, 1), transform 0.95s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform, opacity;
    }
    .framer-cinema-hero.framer-in-view {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    /* 2. framer-chamber-matrix */
    .framer-chamber-matrix {
      opacity: 0;
      transform: scale(0.93) translateY(35px);
      filter: blur(8px);
      transition: opacity 0.85s cubic-bezier(0.22, 1, 0.36, 1), transform 0.85s cubic-bezier(0.22, 1, 0.36, 1), filter 0.85s cubic-bezier(0.22, 1, 0.36, 1);
      will-change: transform, opacity, filter;
    }
    .framer-chamber-matrix.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
      filter: blur(0);
    }

    /* 3. framer-neuro-lab */
    .framer-neuro-lab {
      opacity: 0;
      transform: translateX(-35px) translateY(30px);
      transition: opacity 0.9s cubic-bezier(0.19, 1, 0.22, 1), transform 0.9s cubic-bezier(0.19, 1, 0.22, 1);
      will-change: transform, opacity;
    }
    .framer-neuro-lab.framer-in-view {
      opacity: 1;
      transform: translateX(0) translateY(0);
    }

    /* 4. framer-footprint-grid */
    .framer-footprint-grid {
      opacity: 0;
      transform: scale(0.9) translateY(40px);
      transition: opacity 0.85s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.85s cubic-bezier(0.34, 1.56, 0.64, 1);
      will-change: transform, opacity;
    }
    .framer-footprint-grid.framer-in-view {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    /* 5. framer-impact-dossier */
    .framer-impact-dossier {
      opacity: 0;
      clip-path: inset(8% 0 8% 0);
      transform: translateY(25px);
      transition: opacity 0.9s cubic-bezier(0.25, 0.46, 0.45, 0.94), clip-path 0.9s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.9s cubic-bezier(0.25, 0.46, 0.45, 0.94);
      will-change: clip-path, opacity, transform;
    }
    .framer-impact-dossier.framer-in-view {
      opacity: 1;
      clip-path: inset(0 0 0 0);
      transform: translateY(0);
    }

    /* 6. framer-feasibility-gateway */
    .framer-feasibility-gateway {
      opacity: 0;
      transform: translateY(45px) rotateX(3deg);
      transition: opacity 0.8s cubic-bezier(0.33, 1, 0.68, 1), transform 0.8s cubic-bezier(0.33, 1, 0.68, 1);
      will-change: transform, opacity;
    }
    .framer-feasibility-gateway.framer-in-view {
      opacity: 1;
      transform: translateY(0) rotateX(0deg);
    }

    /* Stagger Delays for child elements */
    .framer-delay-1 { transition-delay: 0.12s; }
    .framer-delay-2 { transition-delay: 0.24s; }
    .framer-delay-3 { transition-delay: 0.36s; }
    .framer-delay-4 { transition-delay: 0.48s; }

    /* ==========================================================================
       SECTION 1: HERO CINEMA & TELEMETRY COCKPIT
       ========================================================================== */
    #hero-cinema {
      padding-top: 8rem;
      padding-bottom: 6rem;
      background: radial-gradient(circle at 75% 20%, rgba(37, 99, 235, 0.08) 0%, transparent 60%),
                  radial-gradient(circle at 10% 80%, rgba(245, 158, 11, 0.05) 0%, transparent 50%),
                  var(--h2-bg-light-sec);
    }

    body.dark #hero-cinema {
      background: radial-gradient(circle at 75% 20%, rgba(37, 99, 235, 0.18) 0%, transparent 60%),
                  radial-gradient(circle at 10% 80%, rgba(245, 158, 11, 0.08) 0%, transparent 50%),
                  #070d18;
    }

    .hero-split-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 3.5rem;
      align-items: center;
    }

    @media (min-width: 1024px) {
      .hero-split-grid {
        grid-template-columns: 1.15fr 1fr;
        gap: 4rem;
      }
    }

    .hero-kicker {
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      padding: 0.4rem 1.1rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.12), rgba(245, 158, 11, 0.12));
      border: 1px solid rgba(37, 99, 235, 0.25);
      color: #1d4ed8;
      margin-bottom: 1.5rem;
    }

    body.dark .hero-kicker {
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.25), rgba(245, 158, 11, 0.2));
      border-color: rgba(96, 165, 250, 0.35);
      color: #93c5fd;
    }

    .pulse-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 10px #10b981;
      animation: pulseAnim 2s infinite;
    }

    @keyframes pulseAnim {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(1.3); }
    }

    .hero-headline {
      font-size: 2.85rem;
      font-weight: 900;
      line-height: 1.12;
      color: var(--h2-text-light-title);
      margin-bottom: 1.5rem;
      letter-spacing: -0.03em;
    }

    @media (min-width: 768px) {
      .hero-headline {
        font-size: 3.85rem;
      }
    }

    .hero-headline .gradient-accent {
      background: linear-gradient(135deg, #2563eb, #06b6d4, #f59e0b);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    body.dark .hero-headline .gradient-accent {
      background: linear-gradient(135deg, #60a5fa, #38bdf8, #fbbf24);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-lead {
      font-size: 1.2rem;
      line-height: 1.7;
      color: var(--h2-text-light-body);
      margin-bottom: 2.25rem;
      max-width: 620px;
    }

    .hero-cta-group {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 1.25rem;
      margin-bottom: 3rem;
    }

    .btn-sovereign-primary {
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.95rem 2rem;
      border-radius: 0.75rem;
      background: linear-gradient(135deg, #1e40af, #2563eb);
      color: #ffffff;
      font-weight: 700;
      font-size: 1rem;
      text-decoration: none;
      box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.4);
      transition: all 0.3s ease;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }

    .btn-sovereign-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 15px 30px -5px rgba(37, 99, 235, 0.55);
      background: linear-gradient(135deg, #1d4ed8, #3b82f6);
      color: #ffffff;
    }

    .btn-sovereign-ghost {
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.95rem 1.85rem;
      border-radius: 0.75rem;
      background: var(--h2-card-light-bg);
      color: var(--h2-text-light-title);
      font-weight: 700;
      font-size: 1rem;
      text-decoration: none;
      border: 1px solid var(--h2-card-light-border);
      transition: all 0.3s ease;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }

    .btn-sovereign-ghost:hover {
      background: rgba(37, 99, 235, 0.06);
      border-color: #2563eb;
      transform: translateY(-2px);
    }

    body.dark .btn-sovereign-ghost:hover {
      background: rgba(37, 99, 235, 0.15);
    }

    /* Live Telemetry Ticker Ribbon */
    .hero-telemetry-ribbon {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.5rem;
      padding-top: 1.5rem;
      border-top: 1px solid var(--h2-card-light-border);
    }

    @media (min-width: 640px) {
      .hero-telemetry-ribbon {
        grid-template-columns: repeat(4, 1fr);
      }
    }

    .telemetry-node {
      display: flex;
      flex-direction: column;
    }

    .telemetry-val {
      font-size: 1.85rem;
      font-weight: 900;
      color: var(--h2-text-light-title);
      line-height: 1.1;
      letter-spacing: -0.02em;
    }

    .telemetry-lbl {
      font-size: 0.78rem;
      color: var(--h2-text-light-body);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-top: 0.3rem;
    }

    /* Right Cinematic Viewport Frame */
    .hero-cinema-viewport {
      position: relative;
      border-radius: 1.5rem;
      padding: 0.75rem;
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.3), rgba(245, 158, 11, 0.2));
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.25);
    }

    body.dark .hero-cinema-viewport {
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.4), rgba(6, 182, 212, 0.25), rgba(245, 158, 11, 0.2));
      box-shadow: 0 30px 70px -15px rgba(0, 0, 0, 0.6);
    }

    .hero-cinema-card {
      position: relative;
      border-radius: 1.15rem;
      overflow: hidden;
      background: #0b1325;
    }

    .hero-cinema-img {
      width: 100%;
      height: 480px;
      object-fit: cover;
      display: block;
      transition: transform 0.7s ease;
    }

    .hero-cinema-card:hover .hero-cinema-img {
      transform: scale(1.03);
    }

    /* Floating HUD Chips */
    .hud-chip {
      position: absolute;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      padding: 0.55rem 1.1rem;
      border-radius: 0.75rem;
      font-size: 0.8rem;
      font-weight: 700;
      background: rgba(11, 19, 37, 0.88);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      color: #f8fafc;
      border: 1px solid rgba(255, 255, 255, 0.15);
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.35);
      z-index: 10;
      transition: all 0.3s ease;
    }

    .hud-chip:hover {
      transform: translateY(-2px);
      border-color: #38bdf8;
    }

    .hud-chip-top-left {
      top: 1.5rem;
      left: 1.5rem;
    }

    .hud-chip-bottom-right {
      bottom: 1.5rem;
      right: 1.5rem;
    }

    .hud-chip-mid-left {
      bottom: 5.5rem;
      left: 1.5rem;
    }

    /* ==========================================================================
       SECTION 2: 4-DIMENSIONAL SUMMIT MATRIX & CHAMBER CAROUSEL
       ========================================================================== */
    #summit-dimensions {
      background: var(--h2-card-light-bg);
      border-top: 1px solid var(--h2-card-light-border);
      border-bottom: 1px solid var(--h2-card-light-border);
    }

    body.dark #summit-dimensions {
      background: #090e1c;
      border-color: rgba(255, 255, 255, 0.06);
    }

    .matrix-tab-bar {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.75rem;
      margin-bottom: 3rem;
    }

    .matrix-tab-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      padding: 0.8rem 1.6rem;
      border-radius: 0.75rem;
      font-size: 0.92rem;
      font-weight: 700;
      cursor: pointer;
      background: var(--h2-bg-light-sec);
      border: 1px solid var(--h2-card-light-border);
      color: var(--h2-text-light-body);
      transition: all 0.3s ease;
    }

    .matrix-tab-btn.active, .matrix-tab-btn:hover {
      background: #1e40af;
      color: #ffffff;
      border-color: #2563eb;
      box-shadow: 0 8px 20px -4px rgba(37, 99, 235, 0.35);
    }

    body.dark .matrix-tab-btn {
      background: #0f182c;
      border-color: rgba(255, 255, 255, 0.08);
      color: #cbd5e1;
    }

    body.dark .matrix-tab-btn.active {
      background: #2563eb;
      color: #ffffff;
    }

    .matrix-display-card {
      display: grid;
      grid-template-columns: 1fr;
      gap: 2.5rem;
      padding: 2.5rem;
      border-radius: 1.5rem;
      background: var(--h2-bg-light-sec);
      border: 1px solid var(--h2-card-light-border);
      box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.05);
    }

    body.dark .matrix-display-card {
      background: #0c1428;
      border-color: rgba(59, 130, 246, 0.2);
      box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.4);
    }

    @media (min-width: 1024px) {
      .matrix-display-card {
        grid-template-columns: 1.1fr 1fr;
        padding: 3rem;
      }
    }

    .matrix-img-wrap {
      position: relative;
      border-radius: 1.25rem;
      overflow: hidden;
      border: 1px solid var(--h2-card-light-border);
    }

    body.dark .matrix-img-wrap {
      border-color: rgba(255, 255, 255, 0.1);
    }

    .matrix-img-wrap img {
      width: 100%;
      height: 420px;
      object-fit: cover;
      display: block;
    }

    .matrix-specs-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.25rem;
      margin-top: 2rem;
    }

    .matrix-spec-box {
      padding: 1.2rem;
      border-radius: 0.85rem;
      background: var(--h2-card-light-bg);
      border: 1px solid var(--h2-card-light-border);
    }

    body.dark .matrix-spec-box {
      background: #111c34;
      border-color: rgba(255, 255, 255, 0.06);
    }

    .spec-box-lbl {
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--h2-sapphire-accent);
      margin-bottom: 0.35rem;
    }

    .spec-box-val {
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--h2-text-light-title);
    }

    /* Capacity Range Slider inside Section 2 */
    .capacity-interactive-bar {
      margin-top: 2rem;
      padding: 1.5rem;
      border-radius: 1rem;
      background: var(--h2-card-light-bg);
      border: 1px solid var(--h2-card-light-border);
    }

    body.dark .capacity-interactive-bar {
      background: #111c34;
      border-color: rgba(59, 130, 246, 0.2);
    }

    .slider-range-input {
      width: 100%;
      margin: 1rem 0 0.5rem 0;
      accent-color: #2563eb;
      cursor: pointer;
    }

    /* ==========================================================================
       SECTION 3: NEURODESIGN & SPATIAL ENGINEERING LABORATORY
       ========================================================================== */
    #spatial-technologies {
      background: var(--h2-bg-light-sec);
    }

    body.dark #spatial-technologies {
      background: #070d18;
    }

    .neuro-split {
      display: grid;
      grid-template-columns: 1fr;
      gap: 3.5rem;
      align-items: center;
    }

    @media (min-width: 1024px) {
      .neuro-split {
        grid-template-columns: 1.15fr 1fr;
      }
    }

    .neuro-cards-stack {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    .neuro-tech-card {
      display: flex;
      align-items: flex-start;
      gap: 1.25rem;
      padding: 1.5rem;
      border-radius: 1rem;
      background: var(--h2-card-light-bg);
      border: 1px solid var(--h2-card-light-border);
      transition: all 0.3s ease;
    }

    .neuro-tech-card:hover {
      transform: translateX(6px);
      border-color: #2563eb;
      box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.15);
    }

    body.dark .neuro-tech-card {
      background: #0e172e;
      border-color: rgba(255, 255, 255, 0.07);
    }

    body.dark .neuro-tech-card:hover {
      border-color: rgba(59, 130, 246, 0.4);
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    }

    .neuro-icon-wrapper {
      width: 52px;
      height: 52px;
      border-radius: 0.75rem;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.35rem;
      flex-shrink: 0;
      background: rgba(37, 99, 235, 0.1);
      color: #2563eb;
    }

    body.dark .neuro-icon-wrapper {
      background: rgba(59, 130, 246, 0.18);
      color: #60a5fa;
    }

    .neuro-card-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--h2-text-light-title);
      margin-bottom: 0.35rem;
    }

    .neuro-card-text {
      font-size: 0.95rem;
      line-height: 1.6;
      color: var(--h2-text-light-body);
    }

    /* Right Interactive Neuro Viewport */
    .neuro-viewport-container {
      position: relative;
      border-radius: 1.5rem;
      overflow: hidden;
      border: 1px solid var(--h2-card-light-border);
      box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.15);
      background: #0b1325;
    }

    body.dark .neuro-viewport-container {
      border-color: rgba(59, 130, 246, 0.3);
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.6);
    }

    .neuro-viewport-img {
      width: 100%;
      height: 480px;
      object-fit: cover;
      display: block;
    }

    .neuro-simulation-overlay {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 1.75rem;
      background: linear-gradient(to top, rgba(7, 12, 24, 0.95), rgba(7, 12, 24, 0.7) 60%, transparent);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      color: #ffffff;
    }

    .neuro-toggle-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1rem;
    }

    .neuro-metric-bars {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
    }

    .neuro-stat-pill {
      background: rgba(255, 255, 255, 0.1);
      padding: 0.6rem 0.8rem;
      border-radius: 0.6rem;
      text-align: center;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }

    .neuro-stat-pill strong {
      display: block;
      font-size: 1.25rem;
      color: #38bdf8;
    }

    .neuro-stat-pill span {
      font-size: 0.72rem;
      color: #cbd5e1;
      text-transform: uppercase;
    }

    /* ==========================================================================
       SECTION 4: SOVEREIGN OPERATIONS GRID & GLOBAL CITY HUBS
       ========================================================================== */
    #global-footprint {
      background: var(--h2-card-light-bg);
      border-top: 1px solid var(--h2-card-light-border);
      border-bottom: 1px solid var(--h2-card-light-border);
    }

    body.dark #global-footprint {
      background: #090e1c;
      border-color: rgba(255, 255, 255, 0.06);
    }

    .footprint-split {
      display: grid;
      grid-template-columns: 1fr;
      gap: 3.5rem;
      align-items: center;
    }

    @media (min-width: 1024px) {
      .footprint-split {
        grid-template-columns: 1.15fr 1fr;
      }
    }

    .footprint-map-wrapper {
      position: relative;
      border-radius: 1.5rem;
      overflow: hidden;
      border: 1px solid var(--h2-card-light-border);
      background: #060a14;
    }

    body.dark .footprint-map-wrapper {
      border-color: rgba(59, 130, 246, 0.25);
    }

    .footprint-map-img {
      width: 100%;
      height: 520px;
      object-fit: cover;
      display: block;
      filter: saturate(1.1) brightness(0.95);
    }

    /* Radar scan effect overlay */
    .radar-sweep-beam {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: conic-gradient(from 0deg at 50% 50%, rgba(59, 130, 246, 0.25) 0deg, transparent 60deg, transparent 360deg);
      border-radius: 50%;
      pointer-events: none;
      animation: radarScan 10s linear infinite;
    }

    @keyframes radarScan {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    .city-hubs-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.25rem;
    }

    @media (min-width: 640px) {
      .city-hubs-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    .city-hub-card {
      padding: 1.4rem;
      border-radius: 1rem;
      background: var(--h2-bg-light-sec);
      border: 1px solid var(--h2-card-light-border);
      cursor: pointer;
      transition: all 0.3s ease;
    }

    .city-hub-card:hover, .city-hub-card.active {
      background: rgba(37, 99, 235, 0.08);
      border-color: #2563eb;
      transform: translateY(-3px);
      box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.2);
    }

    body.dark .city-hub-card {
      background: #0f182c;
      border-color: rgba(255, 255, 255, 0.06);
    }

    body.dark .city-hub-card:hover, body.dark .city-hub-card.active {
      background: #14223f;
      border-color: #3b82f6;
    }

    .city-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.6rem;
    }

    .city-name {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--h2-text-light-title);
    }

    .city-badge {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      background: rgba(16, 185, 129, 0.15);
      color: #10b981;
    }

    .city-meta {
      font-size: 0.85rem;
      color: var(--h2-text-light-body);
      line-height: 1.5;
    }

    /* ==========================================================================
       SECTION 5: EXECUTIVE IMPACT DOSSIER & TRANSFORMATION CASEBOOK
       ========================================================================== */
    #resonance-casebook {
      background: var(--h2-bg-light-sec);
    }

    body.dark #resonance-casebook {
      background: #070d18;
    }

    .casebook-layout {
      display: grid;
      grid-template-columns: 1fr;
      gap: 3.5rem;
      align-items: center;
    }

    @media (min-width: 1024px) {
      .casebook-layout {
        grid-template-columns: 1.15fr 1fr;
      }
    }

    .case-nav-tabs {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 1.75rem;
    }

    .case-tab-chip {
      padding: 0.5rem 1.1rem;
      border-radius: 0.6rem;
      font-size: 0.82rem;
      font-weight: 700;
      background: var(--h2-card-light-bg);
      border: 1px solid var(--h2-card-light-border);
      color: var(--h2-text-light-body);
      cursor: pointer;
      transition: all 0.25s ease;
    }

    .case-tab-chip.active, .case-tab-chip:hover {
      background: #1e40af;
      color: #ffffff;
      border-color: #2563eb;
    }

    body.dark .case-tab-chip {
      background: #0f182c;
      border-color: rgba(255, 255, 255, 0.08);
    }

    body.dark .case-tab-chip.active {
      background: #2563eb;
      color: #ffffff;
    }

    .casebook-dossier-card {
      padding: 2.25rem;
      border-radius: 1.25rem;
      background: var(--h2-card-light-bg);
      border: 1px solid var(--h2-card-light-border);
      box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.06);
    }

    body.dark .casebook-dossier-card {
      background: #0c1428;
      border-color: rgba(59, 130, 246, 0.2);
      box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.4);
    }

    .dossier-kpi-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
      margin: 1.75rem 0;
      padding: 1.25rem;
      border-radius: 0.85rem;
      background: var(--h2-bg-light-sec);
      border: 1px solid var(--h2-card-light-border);
    }

    body.dark .dossier-kpi-grid {
      background: #111c34;
      border-color: rgba(255, 255, 255, 0.06);
    }

    .dossier-kpi-item strong {
      display: block;
      font-size: 1.6rem;
      font-weight: 900;
      color: #2563eb;
      line-height: 1.1;
    }

    body.dark .dossier-kpi-item strong {
      color: #60a5fa;
    }

    .dossier-kpi-item span {
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--h2-text-light-body);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .dossier-quote-block {
      border-left: 3px solid #f59e0b;
      padding-left: 1.25rem;
      margin-top: 1.5rem;
      font-style: italic;
      font-size: 1.05rem;
      line-height: 1.6;
      color: var(--h2-text-light-title);
    }

    .casebook-image-frame {
      position: relative;
      border-radius: 1.5rem;
      overflow: hidden;
      border: 1px solid var(--h2-card-light-border);
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.2);
    }

    body.dark .casebook-image-frame {
      border-color: rgba(245, 158, 11, 0.3);
      box-shadow: 0 30px 70px -15px rgba(0, 0, 0, 0.6);
    }

    .casebook-img {
      width: 100%;
      height: 520px;
      object-fit: cover;
      display: block;
    }

    .dossier-seal-badge {
      position: absolute;
      top: 1.5rem;
      right: 1.5rem;
      padding: 0.5rem 1rem;
      border-radius: 9999px;
      background: rgba(15, 23, 42, 0.9);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1px solid rgba(245, 158, 11, 0.5);
      color: #fbbf24;
      font-size: 0.8rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    /* ==========================================================================
       SECTION 6: STRATEGIC SCOPING GATEWAY & FEASIBILITY ENGINE
       ========================================================================== */
    #executive-engagement {
      background: var(--h2-card-light-bg);
      border-top: 1px solid var(--h2-card-light-border);
    }

    body.dark #executive-engagement {
      background: #090e1c;
      border-color: rgba(255, 255, 255, 0.06);
    }

    .feasibility-engine-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 3.5rem;
    }

    @media (min-width: 1024px) {
      .feasibility-engine-grid {
        grid-template-columns: 1.1fr 1fr;
      }
    }

    .engine-calculator-panel {
      padding: 2.5rem;
      border-radius: 1.5rem;
      background: var(--h2-bg-light-sec);
      border: 1px solid var(--h2-card-light-border);
    }

    body.dark .engine-calculator-panel {
      background: #0c1428;
      border-color: rgba(59, 130, 246, 0.2);
    }

    .calc-field-group {
      margin-bottom: 1.5rem;
    }

    .calc-field-label {
      display: block;
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--h2-text-light-title);
      margin-bottom: 0.6rem;
    }

    .calc-select, .calc-input {
      width: 100%;
      padding: 0.85rem 1.1rem;
      border-radius: 0.75rem;
      font-size: 0.95rem;
      background: var(--h2-card-light-bg);
      border: 1px solid var(--h2-card-light-border);
      color: var(--h2-text-light-title);
      outline: none;
      transition: border-color 0.25s ease;
    }

    body.dark .calc-select, body.dark .calc-input {
      background: #111c34;
      border-color: rgba(255, 255, 255, 0.1);
      color: #f8fafc;
    }

    .calc-select:focus, .calc-input:focus {
      border-color: #2563eb;
    }

    /* Live Output Telemetry Box */
    .calc-live-telemetry {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1rem;
      margin: 2rem 0;
      padding: 1.5rem;
      border-radius: 1rem;
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.1), rgba(6, 182, 212, 0.08));
      border: 1px solid rgba(37, 99, 235, 0.25);
    }

    body.dark .calc-live-telemetry {
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.2), rgba(6, 182, 212, 0.15));
      border-color: rgba(59, 130, 246, 0.35);
    }

    .telemetry-stat-tile strong {
      display: block;
      font-size: 1.45rem;
      font-weight: 900;
      color: var(--h2-text-light-title);
    }

    .telemetry-stat-tile span {
      font-size: 0.75rem;
      font-weight: 600;
      text-transform: uppercase;
      color: var(--h2-sapphire-accent);
    }

    /* Right Form & Image Card */
    .consultation-form-card {
      display: flex;
      flex-direction: column;
      gap: 1.75rem;
    }

    .gateway-img-preview {
      border-radius: 1.25rem;
      overflow: hidden;
      border: 1px solid var(--h2-card-light-border);
      box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.1);
    }

    body.dark .gateway-img-preview {
      border-color: rgba(59, 130, 246, 0.25);
    }

    .gateway-img-preview img {
      width: 100%;
      height: 240px;
      object-fit: cover;
      display: block;
    }

    .booking-fields-wrap {
      padding: 2.25rem;
      border-radius: 1.25rem;
      background: var(--h2-bg-light-sec);
      border: 1px solid var(--h2-card-light-border);
    }

    body.dark .booking-fields-wrap {
      background: #0c1428;
      border-color: rgba(59, 130, 246, 0.2);
    }

    .form-btn-submit {
      width: 100%;
      padding: 1rem 1.5rem;
      border-radius: 0.75rem;
      background: linear-gradient(135deg, #1e40af, #2563eb);
      color: #ffffff;
      font-weight: 800;
      font-size: 1.05rem;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.75rem;
      box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.4);
      transition: all 0.3s ease;
      margin-top: 1.25rem;
    }

    .form-btn-submit:hover {
      background: linear-gradient(135deg, #1d4ed8, #3b82f6);
      transform: translateY(-2px);
      box-shadow: 0 15px 30px -5px rgba(37, 99, 235, 0.55);
    }

    /* RTL Support */
    body.rtl {
      direction: rtl;
      text-align: right;
    }

    body.rtl .neuro-tech-card:hover {
      transform: translateX(-6px);
    }

    body.rtl .dossier-quote-block {
      border-left: none;
      border-right: 3px solid #f59e0b;
      padding-left: 0;
      padding-right: 1.25rem;
    }

    body.rtl .hud-chip-top-left {
      left: auto;
      right: 1.5rem;
    }

    body.rtl .hud-chip-bottom-right {
      right: auto;
      left: 1.5rem;
    }

    body.rtl .dossier-seal-badge {
      right: auto;
      left: 1.5rem;
    }
    """

    # HTML Content for the 6 sections
    page_html = """
    <!-- ==========================================================================
         SECTION 1: THE CINEMATIC SOVEREIGN HERO & LIVE TELEMETRY COCKPIT
         ========================================================================== -->
    <section id="hero-cinema" class="h2-section framer-cinema-hero">
      <div class="h2-ambient-glow" style="top: -100px; right: -100px; background: #3b82f6;"></div>
      <div class="h2-container">
        <div class="hero-split-grid">
          <!-- Left Column: Copy & Command Telemetry -->
          <div class="hero-content-col">
            <div class="hero-kicker">
              <span class="pulse-dot"></span>
              <span>SOVEREIGN CORPORATE SUMMIT ARCHITECTURE</span>
            </div>

            <h1 class="hero-headline">
              Engineering <span class="gradient-accent">High-Stakes Summits</span> Where Global Destiny Is Decided
            </h1>

            <p class="hero-lead">
              EventSphere Sovereign orchestrates the world's most critical corporate plenaries, bilateral trade summits, and institutional assemblies with military-grade precision, immersive spatial acoustics, and zero-latency global telepresence.
            </p>

            <div class="hero-cta-group">
              <a href="#executive-engagement" class="btn-sovereign-primary">
                <i class="fas fa-microchip"></i>
                <span>Launch Feasibility Engine</span>
                <i class="fas fa-arrow-right"></i>
              </a>
              <a href="#summit-dimensions" class="btn-sovereign-ghost">
                <i class="fas fa-cube"></i>
                <span>Explore 4D Chambers</span>
              </a>
            </div>

            <!-- Live Telemetry Ribbon -->
            <div class="hero-telemetry-ribbon">
              <div class="telemetry-node">
                <span class="telemetry-val">450+</span>
                <span class="telemetry-lbl">G7 & Global Summits</span>
              </div>
              <div class="telemetry-node">
                <span class="telemetry-val">$18.4B</span>
                <span class="telemetry-lbl">Liquidity Facilitated</span>
              </div>
              <div class="telemetry-node">
                <span class="telemetry-val">99.98%</span>
                <span class="telemetry-lbl">Broadcast Uptime</span>
              </div>
              <div class="telemetry-node">
                <span class="telemetry-val">64</span>
                <span class="telemetry-lbl">Free-Trade Hubs</span>
              </div>
            </div>
          </div>

          <!-- Right Column: Cinematic Telemetry Viewport -->
          <div class="hero-visual-col">
            <div class="hero-cinema-viewport">
              <div class="hero-cinema-card">
                <img src="images/home2_hero_command.jpg" alt="Sovereign Conference Command Centre" class="hero-cinema-img">
                
                <!-- Floating HUD Overlays -->
                <div class="hud-chip hud-chip-top-left">
                  <i class="fas fa-satellite-dish" style="color: #38bdf8;"></i>
                  <span>Encrypted 8K Uplink: OPTIMAL</span>
                </div>

                <div class="hud-chip hud-chip-mid-left">
                  <i class="fas fa-users" style="color: #fbbf24;"></i>
                  <span>8,420 Active Executive Nodes</span>
                </div>

                <div class="hud-chip hud-chip-bottom-right">
                  <i class="fas fa-wave-square" style="color: #34d399;"></i>
                  <span>Harmonic 432Hz Spatial Sync</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         SECTION 2: THE 4-DIMENSIONAL SUMMIT MATRIX & CHAMBER CAROUSEL
         ========================================================================== -->
    <section id="summit-dimensions" class="h2-section framer-chamber-matrix">
      <div class="h2-container">
        <div class="h2-section-header">
          <span class="h2-supertitle"><i class="fas fa-cubes"></i> DIMENSIONAL SPATIAL TYPOLOGIES</span>
          <h2 class="h2-title">The 4-Dimensional Summit Matrix</h2>
          <p class="h2-desc">
            Every high-stakes corporate assembly demands specialized architectural physics. From 10,000-delegate plenary amphitheaters to biometric closed-door treaty chambers, our spatial layouts maximize executive focus and operational command.
          </p>
        </div>

        <!-- Matrix Tabs -->
        <div class="matrix-tab-bar" id="matrixTabBar">
          <button class="matrix-tab-btn active" data-typology="plenary">
            <i class="fas fa-landmark"></i> Giga-Plenary Amphitheatre
          </button>
          <button class="matrix-tab-btn" data-typology="roundtable">
            <i class="fas fa-shield-alt"></i> Sovereign G7 / B20 Roundtables
          </button>
          <button class="matrix-tab-btn" data-typology="expo">
            <i class="fas fa-project-diagram"></i> Frontier Tech & Innovation Expos
          </button>
          <button class="matrix-tab-btn" data-typology="telepresence">
            <i class="fas fa-globe-americas"></i> Multi-City Synchronous Nodes
          </button>
        </div>

        <!-- Matrix Showcase Card -->
        <div class="matrix-display-card">
          <div class="matrix-info-wrap">
            <span class="h2-supertitle" id="matrixBadge">CAPACITY: 1,000 - 10,000+ DELEGATES</span>
            <h3 class="h2-title" style="font-size: 2.2rem; margin-top: 0.5rem;" id="matrixTitle">
              Giga-Plenary Amphitheatre Architecture
            </h3>
            <p class="h2-desc" id="matrixDesc">
              Engineered for Fortune 50 annual shareholders' meetings, global economic plenaries, and presidential addresses. Features 360-degree curved panoramic microLED backdrops, multi-tier raked amphitheater sightlines, and calibrated spatial acoustic dispersion.
            </p>

            <div class="matrix-specs-grid">
              <div class="matrix-spec-box">
                <div class="spec-box-lbl">Ceiling Clearance</div>
                <div class="spec-box-val" id="specCeiling">18.5 Meters</div>
              </div>
              <div class="matrix-spec-box">
                <div class="spec-box-lbl">Acoustic Attenuation</div>
                <div class="spec-box-val" id="specAcoustics">-48 dB Isolation</div>
              </div>
              <div class="matrix-spec-box">
                <div class="spec-box-lbl">Sightline Geometry</div>
                <div class="spec-box-val" id="specSightline">100% Zero-Obstruction</div>
              </div>
              <div class="matrix-spec-box">
                <div class="spec-box-lbl">Security Classification</div>
                <div class="spec-box-val" id="specSecurity">Tier-1 Diplomatic</div>
              </div>
            </div>

            <!-- Dynamic Capacity Visualizer -->
            <div class="capacity-interactive-bar">
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 700; font-size: 0.9rem; color: var(--h2-text-light-title);">
                  <i class="fas fa-sliders-h" style="color: #2563eb;"></i> Delegate Volume Scale:
                </span>
                <span id="sliderValueDisplay" style="font-weight: 800; color: #2563eb; font-size: 1.1rem;">
                  3,500 Attendees
                </span>
              </div>
              <input type="range" min="500" max="10000" step="250" value="3500" class="slider-range-input" id="matrixCapacitySlider">
              <div style="display: flex; justify-content: space-between; font-size: 0.75rem; color: var(--h2-text-light-body);">
                <span>500 PAX</span>
                <span>Recommended Hall Footprint: <strong id="footprintCalc" style="color: var(--h2-text-light-title);">70,000 sq ft</strong></span>
                <span>10,000+ PAX</span>
              </div>
            </div>
          </div>

          <div class="matrix-img-wrap">
            <img src="images/home2_summit_matrix.jpg" alt="The 4-Dimensional Summit Matrix and Executive Chambers" id="matrixDynamicImage">
            <div class="hud-chip" style="bottom: 1.5rem; left: 1.5rem; right: 1.5rem; justify-content: space-between;">
              <span><i class="fas fa-broadcast-tower" style="color: #38bdf8;"></i> Multi-Track Translation: 16 Booths Active</span>
              <span style="color: #34d399;"><i class="fas fa-check-circle"></i> Calibrated</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         SECTION 3: THE NEURODESIGN & SPATIAL ENGINEERING LABORATORY
         ========================================================================== -->
    <section id="spatial-technologies" class="h2-section framer-neuro-lab">
      <div class="h2-ambient-glow" style="bottom: -150px; left: -100px; background: #06b6d4;"></div>
      <div class="h2-container">
        <div class="h2-section-header">
          <span class="h2-supertitle"><i class="fas fa-brain"></i> COGNITIVE SCIENCE & BIOPHILIC PHYSICS</span>
          <h2 class="h2-title">The Neurodesign & Spatial Engineering Laboratory</h2>
          <p class="h2-desc">
            High-stakes executive negotiation requires sustained cognitive sharpness. We engineer conference environments using clinical psychoacoustics, dynamic circadian light curves, and pure-air microclimates to banish mental fatigue.
          </p>
        </div>

        <div class="neuro-split">
          <!-- Left: 4 Scientific Pillars -->
          <div class="neuro-cards-stack">
            <div class="neuro-tech-card">
              <div class="neuro-icon-wrapper">
                <i class="fas fa-wave-square"></i>
              </div>
              <div>
                <h3 class="neuro-card-title">Harmonic 432Hz Psychoacoustic Tuning</h3>
                <p class="neuro-card-text">
                  Algorithmic acoustic baffling cancels flutter echoes and delivers natural harmonic frequencies, reducing attendee cortisol levels by 34% and sustaining focus over 8-hour plenary sessions.
                </p>
              </div>
            </div>

            <div class="neuro-tech-card">
              <div class="neuro-icon-wrapper">
                <i class="fas fa-sun"></i>
              </div>
              <div>
                <h3 class="neuro-card-title">Circadian Lux Chrono-Shifting</h3>
                <p class="neuro-card-text">
                  Full-spectrum LED choreography shifts naturally from 5,500K morning alertness lighting during keynote addresses to 3,000K warm tone during strategic executive debate, keeping alertness optimal.
                </p>
              </div>
            </div>

            <div class="neuro-tech-card">
              <div class="neuro-icon-wrapper">
                <i class="fas fa-vr-cardboard"></i>
              </div>
              <div>
                <h3 class="neuro-card-title">Sub-Second Volumetric Telepresence</h3>
                <p class="neuro-card-text">
                  Photorealistic 3D holographic projection connects overseas ministers and CEOs onto the stage with sub-18ms transcontinental latency and lifelike eye-contact geometry.
                </p>
              </div>
            </div>

            <div class="neuro-tech-card">
              <div class="neuro-icon-wrapper">
                <i class="fas fa-wind"></i>
              </div>
              <div>
                <h3 class="neuro-card-title">Hyper-Purified Cognitive Oxygenation</h3>
                <p class="neuro-card-text">
                  Microclimate displacement ventilation maintains CO2 levels strictly below 550ppm with medical HEPA-H14 filtration, ensuring maximum executive brain oxygenation and decision clarity.
                </p>
              </div>
            </div>
          </div>

          <!-- Right: Visual Simulation Cockpit -->
          <div class="neuro-visual-wrapper">
            <div class="neuro-viewport-container">
              <img src="images/home2_spatial_neuro.jpg" alt="Neurodesign and Spatial Engineering Laboratory" class="neuro-viewport-img">
              
              <!-- Simulation Overlay -->
              <div class="neuro-simulation-overlay">
                <div class="neuro-toggle-row">
                  <div>
                    <span style="font-size: 0.8rem; text-transform: uppercase; font-weight: 700; color: #38bdf8;">
                      <i class="fas fa-microscope"></i> LIVE TELEMETRY SIMULATOR
                    </span>
                    <h4 style="font-size: 1.15rem; font-weight: 800; margin: 0.2rem 0 0 0;" id="neuroModeTitle">
                      EventSphere Neuro-Engineered Mode
                    </h4>
                  </div>
                  <button id="neuroToggleBtn" style="padding: 0.5rem 1rem; border-radius: 9999px; background: #2563eb; color: #fff; font-size: 0.78rem; font-weight: 700; border: none; cursor: pointer;">
                    Switch to Standard
                  </button>
                </div>

                <div class="neuro-metric-bars">
                  <div class="neuro-stat-pill">
                    <strong id="statCortisol">-34%</strong>
                    <span>Cortisol Stress</span>
                  </div>
                  <div class="neuro-stat-pill">
                    <strong id="statRetention">8.5 Hrs</strong>
                    <span>Peak Alertness</span>
                  </div>
                  <div class="neuro-stat-pill">
                    <strong id="statAcoustic">99.4%</strong>
                    <span>Speech Intelligibility</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         SECTION 4: THE SOVEREIGN OPERATIONS GRID & GLOBAL CITY HUBS
         ========================================================================== -->
    <section id="global-footprint" class="h2-section framer-footprint-grid">
      <div class="h2-container">
        <div class="h2-section-header">
          <span class="h2-supertitle"><i class="fas fa-network-wired"></i> GLOBAL CONVENE COMMAND</span>
          <h2 class="h2-title">The Sovereign Operations Grid</h2>
          <p class="h2-desc">
            Unified conference delivery across the world's primary financial, political, and technological capitals. Wherever your enterprise convenes, our permanent local command teams and bonded venue networks ensure zero execution friction.
          </p>
        </div>

        <div class="footprint-split">
          <!-- Left: Tactical Radar Map Viewport -->
          <div class="footprint-map-wrapper">
            <img src="images/home2_global_grid.jpg" alt="Sovereign Operations Grid & Global Hubs" class="footprint-map-img">
            <div class="radar-sweep-beam"></div>

            <div class="hud-chip" style="top: 1.5rem; left: 1.5rem;">
              <i class="fas fa-radar" style="color: #38bdf8;"></i>
              <span id="activeCityLabel">Active Hub: ZURICH & GENEVA COMMAND</span>
            </div>

            <div class="hud-chip" style="bottom: 1.5rem; right: 1.5rem;">
              <i class="fas fa-shield-alt" style="color: #10b981;"></i>
              <span>Customs & AV Clearance: EXEMPT</span>
            </div>
          </div>

          <!-- Right: Interactive City Hub Matrix -->
          <div class="footprint-details-col">
            <div class="city-hubs-grid" id="cityHubsGrid">
              <!-- City 1 -->
              <div class="city-hub-card active" data-city="zurich">
                <div class="city-head">
                  <span class="city-name"><i class="fas fa-mountain"></i> Zurich & Geneva</span>
                  <span class="city-badge">TIER-1 HUB</span>
                </div>
                <p class="city-meta">
                  Private Banking & Sovereign Treaties. 48 Diplomatic Venue Alliances, Swiss Air Fleet Logistics.
                </p>
              </div>

              <!-- City 2 -->
              <div class="city-hub-card" data-city="london">
                <div class="city-head">
                  <span class="city-name"><i class="fas fa-crown"></i> London Mayfair</span>
                  <span class="city-badge">TIER-1 HUB</span>
                </div>
                <p class="city-meta">
                  Cross-Border M&A & Institutional FinTech. 62 Heritage & Modern Plenaries, Royal Protocol Escorts.
                </p>
              </div>

              <!-- City 3 -->
              <div class="city-hub-card" data-city="newyork">
                <div class="city-head">
                  <span class="city-name"><i class="fas fa-city"></i> New York Manhattan</span>
                  <span class="city-badge">TIER-1 HUB</span>
                </div>
                <p class="city-meta">
                  Wall Street Investor Plenaries & Tech Summits. 55 High-Capacity Arenas, 24/7 Redundant Telemetry.
                </p>
              </div>

              <!-- City 4 -->
              <div class="city-hub-card" data-city="singapore">
                <div class="city-head">
                  <span class="city-name"><i class="fas fa-ship"></i> Singapore Marina</span>
                  <span class="city-badge">TIER-1 HUB</span>
                </div>
                <p class="city-meta">
                  Pan-Asian Bilateral Summits & Frontier Expos. 42 Smart Convention Complexes, Multi-Language Hub.
                </p>
              </div>

              <!-- City 5 -->
              <div class="city-hub-card" data-city="dubai">
                <div class="city-head">
                  <span class="city-name"><i class="fas fa-sun"></i> Dubai DIFC</span>
                  <span class="city-badge">TIER-1 HUB</span>
                </div>
                <p class="city-meta">
                  Sovereign Wealth & Future Energy Summits. 38 Luxury Convention Palaces, VIP Armored Motorcades.
                </p>
              </div>

              <!-- City 6 -->
              <div class="city-hub-card" data-city="tokyo">
                <div class="city-head">
                  <span class="city-name"><i class="fas fa-torii-gate"></i> Tokyo Marunouchi</span>
                  <span class="city-badge">TIER-1 HUB</span>
                </div>
                <p class="city-meta">
                  Industrial Robotics & Clean Mobility Assemblies. 35 Ultra-High-Speed Nodes, Zero-Jitter Pacific Mesh.
                </p>
              </div>
            </div>

            <!-- City Live Status Bar -->
            <div style="margin-top: 1.5rem; padding: 1.25rem; border-radius: 1rem; background: var(--h2-bg-light-sec); border: 1px solid var(--h2-card-light-border); display: flex; align-items: center; justify-content: space-between;">
              <span style="font-size: 0.88rem; font-weight: 700; color: var(--h2-text-light-title);">
                <i class="fas fa-satellite text-sky-500"></i> Synchronous Multi-City Link:
              </span>
              <span style="font-size: 0.85rem; font-weight: 800; color: #10b981;">
                ALL 6 HUBS SYNCHRONIZED &bull; 0.00ms JITTER
              </span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         SECTION 5: THE EXECUTIVE IMPACT DOSSIER & TRANSFORMATION CASEBOOK
         ========================================================================== -->
    <section id="resonance-casebook" class="h2-section framer-impact-dossier">
      <div class="h2-container">
        <div class="h2-section-header">
          <span class="h2-supertitle"><i class="fas fa-file-contract"></i> AUDITED VALUE DELIVERY</span>
          <h2 class="h2-title">The Executive Impact Dossier & Transformation Casebook</h2>
          <p class="h2-desc">
            Conferences are not merely events—they are strategic balance-sheet accelerators. Review audited operational dossiers from our most consequential multinational convenings.
          </p>
        </div>

        <div class="casebook-layout">
          <!-- Left: Dossier Editorial Details -->
          <div class="casebook-content-col">
            <!-- Case Study Selector Chips -->
            <div class="case-nav-tabs" id="caseNavTabs">
              <button class="case-tab-chip active" data-case="fintech">
                <i class="fas fa-coins"></i> World FinTech 2025
              </button>
              <button class="case-tab-chip" data-case="climate">
                <i class="fas fa-leaf"></i> Decarbonization Accord
              </button>
              <button class="case-tab-chip" data-case="ai">
                <i class="fas fa-microchip"></i> Frontier AI Conclave
              </button>
            </div>

            <div class="casebook-dossier-card">
              <span class="h2-supertitle" id="caseBadge">JURISDICTION: GENEVA, SWITZERLAND</span>
              <h3 class="h2-title" style="font-size: 2.1rem; margin-top: 0.4rem;" id="caseTitle">
                World FinTech Sovereign Summit 2025
              </h3>
              <p class="h2-desc" id="caseSummary">
                Convened 5,800 institutional finance leaders, central bank governors, and fintech founders across 42 countries. Delivered triple-redundant satellite feeds, bilateral treaty lounges, and biometric voting telemetry with zero latency.
              </p>

              <!-- Audited KPI Grid -->
              <div class="dossier-kpi-grid">
                <div class="dossier-kpi-item">
                  <strong id="kpiValue1">$4.2B+</strong>
                  <span id="kpiLabel1">M&A Liquidity Closed</span>
                </div>
                <div class="dossier-kpi-item">
                  <strong id="kpiValue2">0.00%</strong>
                  <span id="kpiLabel2">Stream Downtime</span>
                </div>
                <div class="dossier-kpi-item">
                  <strong id="kpiValue3">99.1%</strong>
                  <span id="kpiLabel3">Net Promoter Score</span>
                </div>
              </div>

              <!-- Quote Block -->
              <div class="dossier-quote-block" id="caseQuote">
                "EventSphere Sovereign executed our 3-day ministerial assembly with flawless precision. Their neuro-acoustic zoning kept our delegates focused through 14 hours of contentious treaty negotiations."
              </div>
              <div style="margin-top: 0.75rem; font-size: 0.85rem; font-weight: 700; color: var(--h2-sapphire-accent);" id="caseAuthor">
                &mdash; Lord Alistair Vance, Secretary General, International Banking Forum
              </div>
            </div>
          </div>

          <!-- Right: Visual Editorial Frame -->
          <div class="casebook-image-col">
            <div class="casebook-image-frame">
              <img src="images/home2_resonance_dossier.jpg" alt="Executive Impact Dossier and Transformation Casebook" class="casebook-img">
              <div class="dossier-seal-badge">
                <i class="fas fa-stamp"></i> AUDITED KPMG VERIFIED
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         SECTION 6: THE STRATEGIC SCOPING GATEWAY & FAST-TRACK FEASIBILITY ENGINE
         ========================================================================== -->
    <section id="executive-engagement" class="h2-section framer-feasibility-gateway">
      <div class="h2-container">
        <div class="h2-section-header">
          <span class="h2-supertitle"><i class="fas fa-calculator"></i> REAL-TIME SUMMIT MODELING</span>
          <h2 class="h2-title">The Strategic Scoping Gateway & Feasibility Engine</h2>
          <p class="h2-desc">
            Model your upcoming plenary, conference, or executive retreat in real time. Adjust delegate volume, AV tiers, and protocol requirements to receive immediate spatial calculations and reserve a confidential partner scoping briefing.
          </p>
        </div>

        <div class="feasibility-engine-grid">
          <!-- Left: The Interactive Engine Calculator -->
          <div class="engine-calculator-panel">
            <h3 style="font-size: 1.45rem; font-weight: 800; color: var(--h2-text-light-title); margin-bottom: 1.5rem;">
              <i class="fas fa-cogs" style="color: #2563eb;"></i> Summit Parameter Architecture
            </h3>

            <!-- Select 1: Typology -->
            <div class="calc-field-group">
              <label class="calc-field-label">1. Assembly Archetype</label>
              <select class="calc-select" id="calcTypology">
                <option value="giga">Giga-Plenary Amphitheatre (1,000 - 10,000+ PAX)</option>
                <option value="roundtable">Sovereign G7 / B20 High-Table Roundtable (20 - 100 VIPs)</option>
                <option value="expo">Frontier Tech & Innovation Brand Pavilion (500 - 5,000 PAX)</option>
                <option value="hybrid">Multi-City Synchronous Telepresence Pods (4+ Continents)</option>
              </select>
            </div>

            <!-- Select 2: Delegate Volume Slider -->
            <div class="calc-field-group">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                <label class="calc-field-label" style="margin-bottom: 0;">2. Targeted In-Person Delegate Count</label>
                <strong id="calcDelegateDisplay" style="color: #2563eb; font-size: 1.05rem;">2,500 Delegates</strong>
              </div>
              <input type="range" min="100" max="10000" step="100" value="2500" class="slider-range-input" id="calcDelegateRange">
            </div>

            <!-- Select 3: AV & Spatial Production Tier -->
            <div class="calc-field-group">
              <label class="calc-field-label">3. Production & Telepresence Tier</label>
              <select class="calc-select" id="calcTier">
                <option value="sovereign">Sovereign 8K Holographic + 360° Panoramic LED Mesh</option>
                <option value="executive">Executive Dual-Stage Curved LED + Neuro-Acoustic Suite</option>
                <option value="standard">Essential Broadcast Studio + High-Definition Plenary Stage</option>
              </select>
            </div>

            <!-- Select 4: Protocol & Security Classification -->
            <div class="calc-field-group">
              <label class="calc-field-label">4. Security & Protocol Classification</label>
              <select class="calc-select" id="calcProtocol">
                <option value="diplomatic">Tier-1 Diplomatic Protocol & Biometric Security</option>
                <option value="csuite">Fortune 50 C-Suite Non-Disclosure Standard</option>
                <option value="open">Public Corporate Conclave & Enterprise Press Access</option>
              </select>
            </div>

            <!-- Calculated Live Telemetry -->
            <div class="calc-live-telemetry">
              <div class="telemetry-stat-tile">
                <span id="calcFootprintLbl">Spatial Footprint</span>
                <strong id="calcFootprint">55,000 sq ft</strong>
              </div>
              <div class="telemetry-stat-tile">
                <span id="calcCrewLbl">Production Crew</span>
                <strong id="calcCrew">48 Specialists</strong>
              </div>
              <div class="telemetry-stat-tile">
                <span id="calcWindowLbl">Lead Time Window</span>
                <strong id="calcWindow">10 - 12 Weeks</strong>
              </div>
              <div class="telemetry-stat-tile">
                <span id="calcFeasibilityLbl">Feasibility Score</span>
                <strong id="calcFeasibility" style="color: #10b981;">99.8% VERIFIED</strong>
              </div>
            </div>
          </div>

          <!-- Right: Consultation Reservation Gateway -->
          <div class="consultation-form-card">
            <div class="gateway-img-preview">
              <img src="images/home2_feasibility_gateway.jpg" alt="Strategic Feasibility Gateway and Summit Configurator">
            </div>

            <div class="booking-fields-wrap">
              <h3 style="font-size: 1.35rem; font-weight: 800; color: var(--h2-text-light-title); margin-bottom: 0.5rem;">
                <i class="fas fa-lock" style="color: #10b981;"></i> Lock Confidential Partner Scoping Session
              </h3>
              <p style="font-size: 0.9rem; color: var(--h2-text-light-body); margin-bottom: 1.5rem;">
                All consultations are protected under mutual diplomatic NDA. Our Principal Partners respond within 3 business hours.
              </p>

              <form id="scopingConsultForm" onsubmit="handleScopingSubmit(event)">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
                  <div>
                    <label class="calc-field-label">Executive Name *</label>
                    <input type="text" required placeholder="Lord Julian Sterling" class="calc-input" id="scopeName">
                  </div>
                  <div>
                    <label class="calc-field-label">Corporate Title *</label>
                    <input type="text" required placeholder="Chief Strategy Officer" class="calc-input" id="scopeTitle">
                  </div>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
                  <div>
                    <label class="calc-field-label">Institutional Email *</label>
                    <input type="email" required placeholder="j.sterling@sterling-holdings.com" class="calc-input" id="scopeEmail">
                  </div>
                  <div>
                    <label class="calc-field-label">Primary Destination</label>
                    <select class="calc-select" id="scopeDestination">
                      <option>Zurich / Geneva</option>
                      <option>London Mayfair</option>
                      <option>New York Manhattan</option>
                      <option>Singapore Marina</option>
                      <option>Dubai DIFC</option>
                      <option>Tokyo Marunouchi</option>
                    </select>
                  </div>
                </div>

                <button type="submit" class="form-btn-submit">
                  <i class="fas fa-shield-check"></i>
                  <span>Transmit Scoping Dossier & Lock Session</span>
                  <i class="fas fa-arrow-right"></i>
                </button>
              </form>

              <div id="scopingSuccessMsg" style="display: none; margin-top: 1.25rem; padding: 1.2rem; border-radius: 0.75rem; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.35); color: #10b981; font-weight: 700; font-size: 0.92rem;">
                <i class="fas fa-check-circle"></i> Feasibility Dossier Transmitted! Verification Code: <span style="font-family: monospace; color: #fff; background: #065f46; padding: 0.2rem 0.5rem; border-radius: 0.3rem;">ESP-FEAS-2026-9812</span>. A Senior Managing Partner has been dispatched.
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    """

    # Interactive JavaScript for home-2.html
    page_js = """
  <!-- HOME-2 INTERACTIVE SCRIPTS & FRAMER MOTION OBSERVERS -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      // 1. Framer Motion Scroll Trigger using IntersectionObserver
      const framerSections = document.querySelectorAll(
        '.framer-cinema-hero, .framer-chamber-matrix, .framer-neuro-lab, .framer-footprint-grid, .framer-impact-dossier, .framer-feasibility-gateway'
      );

      const observerOptions = {
        root: null,
        rootMargin: '0px 0px -100px 0px',
        threshold: 0.15
      };

      const framerObserver = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('framer-in-view');
          }
        });
      }, observerOptions);

      framerSections.forEach(sec => framerObserver.observe(sec));

      // Trigger first section immediately
      const hero = document.getElementById('hero-cinema');
      if (hero) {
        setTimeout(() => hero.classList.add('framer-in-view'), 100);
      }

      // 2. Section 2: Chamber Matrix Typology Switcher
      const matrixTabs = document.querySelectorAll('#matrixTabBar .matrix-tab-btn');
      const matrixBadge = document.getElementById('matrixBadge');
      const matrixTitle = document.getElementById('matrixTitle');
      const matrixDesc = document.getElementById('matrixDesc');
      const specCeiling = document.getElementById('specCeiling');
      const specAcoustics = document.getElementById('specAcoustics');
      const specSightline = document.getElementById('specSightline');
      const specSecurity = document.getElementById('specSecurity');

      const typologyData = {
        plenary: {
          badge: 'CAPACITY: 1,000 - 10,000+ DELEGATES',
          title: 'Giga-Plenary Amphitheatre Architecture',
          desc: "Engineered for Fortune 50 annual shareholders' meetings, global economic plenaries, and presidential addresses. Features 360-degree curved panoramic microLED backdrops, multi-tier raked amphitheater sightlines, and calibrated spatial acoustic dispersion.",
          ceiling: '18.5 Meters',
          acoustics: '-48 dB Isolation',
          sightline: '100% Zero-Obstruction',
          security: 'Tier-1 Diplomatic'
        },
        roundtable: {
          badge: 'CAPACITY: 20 - 80 C-SUITE LEADERS',
          title: 'Sovereign G7 / B20 Closed-Door Roundtables',
          desc: 'High-security diplomatic sanctuary designed for inter-governmental treaty negotiations and Fortune 10 boardroom conclaves. Equipped with RF/microwave eavesdropping countermeasures, biometric airlocks, and discrete transcription pods.',
          ceiling: '7.5 Meters',
          acoustics: '-62 dB Eavesdrop Shield',
          sightline: 'Circular Equidistant',
          security: 'Diplomatic Secret Compartment'
        },
        expo: {
          badge: 'CAPACITY: 500 - 5,000 ATTENDEES',
          title: 'Frontier Tech & Innovation Brand Pavilions',
          desc: 'Immersive experiential exhibition halls built for radical technological unveilings and sovereign investor demos. Modular kinetic trusses, high-density fiber routing, and holographic demonstration stages.',
          ceiling: '12.0 Meters',
          acoustics: 'Zoned Directional Sound',
          sightline: 'Dynamic Multi-Angle',
          security: 'Enterprise NDA Enforced'
        },
        telepresence: {
          badge: 'CAPACITY: GLOBAL SYNCHRONOUS NODES',
          title: 'Multi-City Synchronous Telepresence Pods',
          desc: 'Synchronizes executive gatherings across Zurich, New York, Tokyo, and Singapore into a single unified broadcast environment. Sub-18ms transatlantic fiber routing with zero perceived conversational delay.',
          ceiling: '9.0 Meters',
          acoustics: 'Harmonic 432Hz Matched',
          sightline: 'Bilateral Eye-Contact Camera',
          security: 'Quantum-Encrypted Uplink'
        }
      };

      matrixTabs.forEach(btn => {
        btn.addEventListener('click', function() {
          matrixTabs.forEach(b => b.classList.remove('active'));
          this.classList.add('active');
          const type = this.getAttribute('data-typology');
          const data = typologyData[type];
          if (data) {
            matrixBadge.textContent = data.badge;
            matrixTitle.textContent = data.title;
            matrixDesc.textContent = data.desc;
            specCeiling.textContent = data.ceiling;
            specAcoustics.textContent = data.acoustics;
            specSightline.textContent = data.sightline;
            specSecurity.textContent = data.security;
          }
        });
      });

      // Section 2: Capacity Slider Math
      const capSlider = document.getElementById('matrixCapacitySlider');
      const valDisplay = document.getElementById('sliderValueDisplay');
      const footprintCalc = document.getElementById('footprintCalc');
      if (capSlider) {
        capSlider.addEventListener('input', function() {
          const val = parseInt(this.value);
          valDisplay.textContent = Number(val).toLocaleString() + ' Attendees';
          const sqft = Math.round(val * 20);
          footprintCalc.textContent = Number(sqft).toLocaleString() + ' sq ft';
        });
      }

      // 3. Section 3: Neuro-Simulator Toggle
      const neuroToggleBtn = document.getElementById('neuroToggleBtn');
      const neuroModeTitle = document.getElementById('neuroModeTitle');
      const statCortisol = document.getElementById('statCortisol');
      const statRetention = document.getElementById('statRetention');
      const statAcoustic = document.getElementById('statAcoustic');
      let isNeuroOptimized = true;

      if (neuroToggleBtn) {
        neuroToggleBtn.addEventListener('click', function() {
          isNeuroOptimized = !isNeuroOptimized;
          if (isNeuroOptimized) {
            neuroModeTitle.textContent = 'EventSphere Neuro-Engineered Mode';
            neuroToggleBtn.textContent = 'Switch to Standard';
            neuroToggleBtn.style.background = '#2563eb';
            statCortisol.textContent = '-34%';
            statCortisol.style.color = '#38bdf8';
            statRetention.textContent = '8.5 Hrs';
            statRetention.style.color = '#38bdf8';
            statAcoustic.textContent = '99.4%';
            statAcoustic.style.color = '#38bdf8';
          } else {
            neuroModeTitle.textContent = 'Standard Commercial Hotel Ballroom';
            neuroToggleBtn.textContent = 'Re-engage Neuro-Lab';
            neuroToggleBtn.style.background = '#e11d48';
            statCortisol.textContent = '+42%';
            statCortisol.style.color = '#f87171';
            statRetention.textContent = '3.2 Hrs';
            statRetention.style.color = '#f87171';
            statAcoustic.textContent = '64.2%';
            statAcoustic.style.color = '#f87171';
          }
        });
      }

      // 4. Section 4: Global City Node Selector
      const cityCards = document.querySelectorAll('#cityHubsGrid .city-hub-card');
      const activeCityLabel = document.getElementById('activeCityLabel');
      const cityLabels = {
        zurich: 'Active Hub: ZURICH & GENEVA COMMAND',
        london: 'Active Hub: LONDON MAYFAIR SOVEREIGN',
        newyork: 'Active Hub: NEW YORK MANHATTAN CONVENE',
        singapore: 'Active Hub: SINGAPORE MARINA OPERATIONS',
        dubai: 'Active Hub: DUBAI DIFC SOVEREIGN PALACE',
        tokyo: 'Active Hub: TOKYO MARUNOUCHI CLEAN GRID'
      };

      cityCards.forEach(card => {
        card.addEventListener('click', function() {
          cityCards.forEach(c => c.classList.remove('active'));
          this.classList.add('active');
          const cityKey = this.getAttribute('data-city');
          if (cityLabels[cityKey] && activeCityLabel) {
            activeCityLabel.textContent = cityLabels[cityKey];
          }
        });
      });

      // 5. Section 5: Casebook Dossier Switcher
      const caseChips = document.querySelectorAll('#caseNavTabs .case-tab-chip');
      const caseBadge = document.getElementById('caseBadge');
      const caseTitle = document.getElementById('caseTitle');
      const caseSummary = document.getElementById('caseSummary');
      const kpiVal1 = document.getElementById('kpiValue1');
      const kpiLbl1 = document.getElementById('kpiLabel1');
      const kpiVal2 = document.getElementById('kpiValue2');
      const kpiLbl2 = document.getElementById('kpiLabel2');
      const kpiVal3 = document.getElementById('kpiValue3');
      const kpiLbl3 = document.getElementById('kpiLabel3');
      const caseQuote = document.getElementById('caseQuote');
      const caseAuthor = document.getElementById('caseAuthor');

      const casebookData = {
        fintech: {
          badge: 'JURISDICTION: GENEVA, SWITZERLAND',
          title: 'World FinTech Sovereign Summit 2025',
          summary: 'Convened 5,800 institutional finance leaders, central bank governors, and fintech founders across 42 countries. Delivered triple-redundant satellite feeds, bilateral treaty lounges, and biometric voting telemetry with zero latency.',
          kpis: ['$4.2B+', 'M&A Liquidity Closed', '0.00%', 'Stream Downtime', '99.1%', 'Net Promoter Score'],
          quote: '"EventSphere Sovereign executed our 3-day ministerial assembly with flawless precision. Their neuro-acoustic zoning kept our delegates focused through 14 hours of contentious treaty negotiations."',
          author: '— Lord Alistair Vance, Secretary General, International Banking Forum'
        },
        climate: {
          badge: 'JURISDICTION: ZURICH ALPINE PAVILION',
          title: 'Global Decarbonization Leadership Plenary',
          summary: '1,400 ministerial and Fortune 100 executives convened to execute cross-border green accords. Certified ISO-20121 carbon-neutral execution with live blockchain carbon offset telemetry on a 60m panoramic LED screen.',
          kpis: ['100%', 'Zero-Waste Certified', '1,400', 'Cabinet Leaders Present', '18.4k', 'Tons CO2 Offset'],
          quote: '"The spatial elegance and zero-emission delivery established an entirely new global benchmark for sustainable sovereign assemblies."',
          author: '— Dr. Elena Rostova, High Commissioner for Clean Infrastructure'
        },
        ai: {
          badge: 'JURISDICTION: NEW YORK & SINGAPORE DUAL-NODE',
          title: 'Frontier AI Enterprise Architecture Conclave',
          summary: 'Synchronous transcontinental summit linking 3,200 senior engineers and enterprise CEOs. Live interactive code compilations broadcast across 12 timezones with sub-18ms ping and facial biometric check-in.',
          kpis: ['18ms', 'Trans-Pacific Latency', '3,200', 'Enterprise Architects', '100%', 'Biometric Precision'],
          quote: '"The dual-stage holographic telepresence felt as if the Singapore keynote speaker was standing physically on our Manhattan plenary stage."',
          author: '— Marcus Chen, Chief Technology Officer, NexGen Cloud Holdings'
        }
      };

      caseChips.forEach(chip => {
        chip.addEventListener('click', function() {
          caseChips.forEach(c => c.classList.remove('active'));
          this.classList.add('active');
          const key = this.getAttribute('data-case');
          const d = casebookData[key];
          if (d) {
            caseBadge.textContent = d.badge;
            caseTitle.textContent = d.title;
            caseSummary.textContent = d.summary;
            kpiVal1.textContent = d.kpis[0];
            kpiLbl1.textContent = d.kpis[1];
            kpiVal2.textContent = d.kpis[2];
            kpiLbl2.textContent = d.kpis[3];
            kpiVal3.textContent = d.kpis[4];
            kpiLbl3.textContent = d.kpis[5];
            caseQuote.textContent = d.quote;
            caseAuthor.innerHTML = d.author;
          }
        });
      });

      // 6. Section 6: Feasibility Engine Live Calculations
      const calcDelegateRange = document.getElementById('calcDelegateRange');
      const calcDelegateDisplay = document.getElementById('calcDelegateDisplay');
      const calcFootprint = document.getElementById('calcFootprint');
      const calcCrew = document.getElementById('calcCrew');
      const calcWindow = document.getElementById('calcWindow');
      const calcTier = document.getElementById('calcTier');
      const calcTypology = document.getElementById('calcTypology');

      function updateFeasibilityMath() {
        if (!calcDelegateRange) return;
        const pax = parseInt(calcDelegateRange.value);
        calcDelegateDisplay.textContent = Number(pax).toLocaleString() + ' Delegates';

        // Calculation algorithms
        let sqftPerPerson = 22;
        if (calcTypology.value === 'roundtable') sqftPerPerson = 45;
        if (calcTypology.value === 'expo') sqftPerPerson = 35;
        const totalSqft = Math.round(pax * sqftPerPerson);
        calcFootprint.textContent = Number(totalSqft).toLocaleString() + ' sq ft';

        // Crew
        let crewScale = Math.round(14 + (pax / 75));
        if (calcTier.value === 'sovereign') crewScale += 18;
        calcCrew.textContent = crewScale + ' Specialists';

        // Lead time
        let weeks = '8 - 10 Weeks';
        if (pax > 2000) weeks = '12 - 16 Weeks';
        if (pax > 5000) weeks = '20 - 24 Weeks';
        calcWindow.textContent = weeks;
      }

      if (calcDelegateRange) {
        calcDelegateRange.addEventListener('input', updateFeasibilityMath);
      }
      if (calcTier) {
        calcTier.addEventListener('change', updateFeasibilityMath);
      }
      if (calcTypology) {
        calcTypology.addEventListener('change', updateFeasibilityMath);
      }
      updateFeasibilityMath();
    });

    // Form submission handler
    function handleScopingSubmit(e) {
      e.preventDefault();
      const form = document.getElementById('scopingConsultForm');
      const successMsg = document.getElementById('scopingSuccessMsg');
      if (form && successMsg) {
        form.style.display = 'none';
        successMsg.style.display = 'block';
      }
    }
  </script>
    """

    # Assemble home-2.html
    # 1. Insert CSS right before </style>
    final_head = head_before + page_css + '\n  '

    # 2. Middle navbar part + 6 sections
    final_body = nav_middle + '\n    ' + page_html + '\n'

    # 3. Footer part + script right before </body>
    final_footer = footer_body + '\n' + page_js + '\n' + closing_html

    full_page = final_head + final_body + final_footer

    with open('home-2.html', 'w', encoding='utf-8') as f:
        f.write(full_page)

    print("Successfully built home-2.html!")
    print(f"Total size: {len(full_page)} characters")

if __name__ == '__main__':
    build_home2()
