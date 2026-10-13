import sys, re

sys.stdout.reconfigure(encoding='utf-8')

# Group 1: 10 Public Pages
PUBLIC_PAGES = [
    'index.html', 'home-2.html', 'about.html', 'services.html', 
    'portfolio.html', 'event-planning.html', 'vendors.html', 
    'resources.html', 'contact.html', 'navbar.html'
]

# Group 2: 2 Dashboard Pages
DASHBOARDS = ['admin-dashboard.html', 'user-dashboard.html']

# Group 3: 4 Auth & Error Pages
AUTH_PAGES = ['login.html', 'registeration.html', 'registration.html', '404.html']

CSS_PUBLIC_RESPONSIVE = """
    /* ==========================================================================
       MOBILE-FIRST RESPONSIVE SUITE (320px, 480px, 768px, 1024px)
       ========================================================================== */
    *, *::before, *::after {
      box-sizing: border-box !important;
    }

    html {
      overflow-x: hidden !important;
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box !important;
      -webkit-text-size-adjust: 100%;
    }

    body {
      overflow-x: hidden !important;
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box !important;
      margin: 0 !important;
      padding: 0 !important;
    }

    img, picture, video, canvas, svg, iframe {
      max-width: 100% !important;
      height: auto;
    }

    h1, h2, h3, h4, h5, h6, p, span, a, label, li, button, td, th {
      overflow-wrap: break-word !important;
      word-wrap: break-word !important;
      word-break: break-word;
    }

    .app-wrapper {
      width: 100% !important;
      max-width: 1440px !important;
      box-sizing: border-box !important;
      margin: 0 auto !important;
      padding-left: 1.5rem !important;
      padding-right: 1.5rem !important;
      overflow-x: hidden !important;
    }

    .content-section, section, [class*="-section"] {
      width: 100% !important;
      max-width: 1280px !important;
      box-sizing: border-box !important;
      margin-left: auto !important;
      margin-right: auto !important;
      padding-left: 1rem !important;
      padding-right: 1rem !important;
    }

    button, .btn, .btn-hero-primary, .btn-hero-secondary, .login-btn, [class*="btn-"] {
      max-width: 100% !important;
      box-sizing: border-box !important;
    }

    .glass-card, [class*="-card"], [class*="-glass-card"] {
      max-width: 100% !important;
      box-sizing: border-box !important;
    }

    /* --- BREAKPOINT: 1024px --- */
    @media (max-width: 1024px) {
      .app-wrapper {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
      }
      .content-section, section, [class*="-section"] {
        margin-top: 3.5rem !important;
        margin-bottom: 3.5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
      }
      .section-header {
        margin-bottom: 2.2rem !important;
        gap: 0.6rem !important;
      }
      h1, .hero-headline, [class*="-hero-title"], [class*="-headline"] {
        font-size: clamp(2.2rem, 5vw, 2.9rem) !important;
        line-height: 1.25 !important;
      }
      h2, .section-title, [class*="-section-title"] {
        font-size: clamp(1.75rem, 4vw, 2.2rem) !important;
      }
      h3, .card-title, [class*="-card-title"] {
        font-size: clamp(1.2rem, 3vw, 1.45rem) !important;
      }

      /* Navbar Collapse */
      .nav-links, .right-section .icon-btn, .right-section .login-btn {
        display: none !important;
      }
      .hamburger {
        display: flex !important;
      }
      .nav-container {
        padding: 0.5rem 1.25rem !important;
      }

      /* 2-Column Grids */
      .bento-grid, 
      .features-grid, 
      .services-grid, 
      .portfolio-grid, 
      .team-grid, 
      .testimonials-grid, 
      .pricing-grid,
      .gallery-masonry-grid,
      .stats-grid,
      .hero-highlights-grid,
      [class*="-grid"] {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 1.5rem !important;
      }

      .hero-container,
      .venues-split-grid,
      .success-industry-grid,
      .testimonials-rfp-grid,
      .process-details-card,
      [class*="-split-grid"] {
        grid-template-columns: 1fr !important;
        gap: 2.2rem !important;
      }

      .footer-container {
        padding: 2.5rem 2rem 1.8rem !important;
        border-radius: 36px !important;
        margin-top: 3.5rem !important;
      }
      .footer-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 2rem !important;
      }
      .footer-cta {
        padding: 1.8rem 1.5rem !important;
      }
    }

    /* --- BREAKPOINT: 768px --- */
    @media (max-width: 768px) {
      .content-section, section, [class*="-section"] {
        margin-top: 2.8rem !important;
        margin-bottom: 2.8rem !important;
        padding-left: 0.85rem !important;
        padding-right: 0.85rem !important;
      }

      h1, .hero-headline, [class*="-hero-title"], [class*="-headline"] {
        font-size: clamp(1.85rem, 5.5vw, 2.35rem) !important;
      }
      h2, .section-title, [class*="-section-title"] {
        font-size: clamp(1.45rem, 4.5vw, 1.85rem) !important;
      }
      h3, .card-title, [class*="-card-title"] {
        font-size: clamp(1.15rem, 3.5vw, 1.35rem) !important;
      }
      p, .hero-paragraph, .section-desc {
        font-size: 0.92rem !important;
        line-height: 1.6 !important;
      }

      /* Single-Column Stack */
      .bento-grid, 
      .features-grid, 
      .services-grid, 
      .portfolio-grid, 
      .team-grid, 
      .testimonials-grid, 
      .pricing-grid,
      .gallery-masonry-grid,
      .stepper-roadmap,
      .stepper-nav-bar,
      .success-industry-grid,
      .rfp-form-grid,
      .rfp-type-group,
      [class*="-grid"] {
        grid-template-columns: 1fr !important;
        gap: 1.25rem !important;
      }

      .gallery-card.span-2,
      .col-span-2,
      [class*="span-"] {
        grid-column: span 1 !important;
      }

      /* Stack Buttons */
      .hero-cta-group, .cta-group, .btn-row {
        flex-direction: column !important;
        width: 100% !important;
        gap: 0.75rem !important;
      }
      .btn-hero-primary, .btn-hero-secondary, .btn-primary, .btn-secondary, [class*="btn-hero-"] {
        width: 100% !important;
        justify-content: center !important;
        text-align: center !important;
        padding: 0.85rem 1.4rem !important;
      }

      .hero-metrics-bar {
        grid-template-columns: 1fr !important;
        flex-direction: column !important;
        gap: 0.85rem !important;
        width: 100% !important;
      }
      .roi-metrics-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 0.75rem !important;
      }

      .countdown-clock {
        grid-template-columns: repeat(4, 1fr) !important;
        padding: 0.6rem !important;
        gap: 0.4rem !important;
      }
      .time-num { font-size: 1.15rem !important; }
      .time-label { font-size: 0.65rem !important; }

      /* Footer */
      .footer-container {
        padding: 2.2rem 1.25rem 1.5rem !important;
        border-radius: 28px !important;
        margin-top: 2.8rem !important;
        gap: 2rem !important;
      }
      .footer-cta {
        flex-direction: column !important;
        align-items: stretch !important;
        padding: 1.6rem 1.25rem !important;
        gap: 1.25rem !important;
        border-radius: 22px !important;
      }
      .footer-cta-form-wrapper {
        min-width: 0 !important;
        width: 100% !important;
      }
      .footer-form {
        flex-direction: column !important;
        border-radius: 18px !important;
        padding: 0.5rem !important;
        gap: 0.5rem !important;
        width: 100% !important;
      }
      .footer-form input {
        width: 100% !important;
        border-radius: 12px !important;
        padding: 0.65rem 0.85rem !important;
      }
      .footer-form button {
        width: 100% !important;
        justify-content: center !important;
        border-radius: 12px !important;
        padding: 0.65rem 1rem !important;
      }
      .footer-grid {
        grid-template-columns: 1fr !important;
        gap: 1.8rem !important;
      }
      .footer-bottom {
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 1.2rem !important;
      }
      .footer-legal-links {
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 0.6rem !important;
      }

      .es-modal-dialog, .modal-dialog {
        width: 94% !important;
        max-width: 100% !important;
        padding: 1.5rem 1.25rem !important;
        margin: 1rem auto !important;
      }
    }

    /* --- BREAKPOINT: 480px --- */
    @media (max-width: 480px) {
      .content-section, section, [class*="-section"] {
        margin-top: 2.2rem !important;
        margin-bottom: 2.2rem !important;
        padding-left: 0.75rem !important;
        padding-right: 0.75rem !important;
      }

      .app-wrapper {
        padding-left: 0.6rem !important;
        padding-right: 0.6rem !important;
        padding-top: 0.8rem !important;
        padding-bottom: 1.5rem !important;
      }

      .nav-container {
        padding: 0.4rem 0.8rem !important;
        border-radius: 30px !important;
        top: 0.5rem !important;
      }
      .logo-text { font-size: 1.15rem !important; }
      .logo-3d { width: 19px !important; height: 19px !important; }
      .logo-face {
        width: 19px !important;
        height: 19px !important;
        font-size: 0.52rem !important;
        border-radius: 5px !important;
      }
      .hamburger {
        width: 36px !important;
        height: 36px !important;
        padding: 8px 6px !important;
      }

      .mobile-menu {
        border-radius: 20px !important;
        padding: 1.25rem 1rem !important;
      }
      .mobile-nav-links > li > a, 
      .mobile-dropdown-header > a {
        font-size: 0.95rem !important;
      }
      .mobile-actions {
        gap: 0.5rem !important;
      }
      .mobile-actions .login-btn {
        width: 100% !important;
        justify-content: center !important;
      }

      h1, .hero-headline, [class*="-hero-title"], [class*="-headline"] {
        font-size: clamp(1.5rem, 6.8vw, 1.85rem) !important;
      }
      h2, .section-title, [class*="-section-title"] {
        font-size: clamp(1.25rem, 5.5vw, 1.55rem) !important;
      }
      h3, .card-title, [class*="-card-title"] {
        font-size: 1.12rem !important;
      }
      .section-pill-badge {
        font-size: 0.72rem !important;
        padding: 0.3rem 0.75rem !important;
      }

      .glass-card, [class*="-card"], [class*="-glass-card"] {
        padding: 1.35rem 1rem !important;
        border-radius: 20px !important;
      }

      .roi-metrics-grid {
        grid-template-columns: 1fr !important;
        gap: 0.6rem !important;
      }
      .countdown-clock {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 0.5rem !important;
      }

      .footer-container {
        padding: 1.8rem 0.95rem 1.2rem !important;
        border-radius: 24px !important;
        margin-top: 2.2rem !important;
      }
      .footer-cta-title { font-size: 1.22rem !important; }
      .footer-cta-desc { font-size: 0.85rem !important; }
      .metric-pill {
        font-size: 0.72rem !important;
        padding: 0.35rem 0.7rem !important;
      }
    }

    /* --- BREAKPOINT: 320px --- */
    @media (max-width: 320px) {
      .content-section, section, [class*="-section"] {
        margin-top: 1.6rem !important;
        margin-bottom: 1.6rem !important;
        padding-left: 0.45rem !important;
        padding-right: 0.45rem !important;
      }

      .app-wrapper {
        padding-left: 0.35rem !important;
        padding-right: 0.35rem !important;
        padding-top: 0.5rem !important;
      }

      .nav-container {
        padding: 0.35rem 0.65rem !important;
        border-radius: 22px !important;
        top: 0.3rem !important;
      }
      .logo-text { font-size: 1.02rem !important; }
      .logo-3d { width: 17px !important; height: 17px !important; }
      .logo-face {
        width: 17px !important;
        height: 17px !important;
        font-size: 0.48rem !important;
        border-radius: 4px !important;
      }
      .hamburger {
        width: 32px !important;
        height: 32px !important;
        padding: 7px 5px !important;
      }

      h1, .hero-headline, [class*="-hero-title"], [class*="-headline"] {
        font-size: 1.38rem !important;
      }
      h2, .section-title, [class*="-section-title"] {
        font-size: 1.18rem !important;
      }
      h3, .card-title, [class*="-card-title"] {
        font-size: 1.02rem !important;
      }
      p, .hero-paragraph, .section-desc {
        font-size: 0.8rem !important;
      }
      .section-pill-badge {
        font-size: 0.66rem !important;
        padding: 0.25rem 0.55rem !important;
      }

      .glass-card, [class*="-card"], [class*="-glass-card"] {
        padding: 1.1rem 0.75rem !important;
        border-radius: 16px !important;
      }

      button, .btn, .btn-hero-primary, .btn-hero-secondary, .login-btn, [class*="btn-"] {
        font-size: 0.78rem !important;
        padding: 0.65rem 0.9rem !important;
      }

      .footer-container {
        padding: 1.5rem 0.75rem 1rem !important;
        border-radius: 18px !important;
      }
      .footer-cta {
        padding: 1.25rem 0.75rem !important;
        border-radius: 16px !important;
      }
      .footer-cta-title { font-size: 1.1rem !important; }
      .footer-cta-desc { font-size: 0.78rem !important; }
    }
"""

CSS_DASHBOARD_RESPONSIVE = """
    /* ==========================================================================
       DASHBOARD MOBILE-FIRST RESPONSIVE SUITE (320px, 480px, 768px, 1024px)
       ========================================================================== */
    *, *::before, *::after {
      box-sizing: border-box !important;
    }

    html, body {
      overflow-x: hidden !important;
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box !important;
    }

    img, canvas, svg {
      max-width: 100% !important;
      height: auto;
    }

    h1, h2, h3, h4, h5, h6, p, span, a, label, li, button, td, th {
      overflow-wrap: break-word !important;
      word-wrap: break-word !important;
    }

    .table-responsive, .data-table-container, .table-wrapper, .table-container, [class*="table"] {
      max-width: 100% !important;
      overflow-x: auto !important;
      -webkit-overflow-scrolling: touch !important;
    }

    /* --- BREAKPOINT: 1024px --- */
    @media (max-width: 1024px) {
      .dashboard-layout {
        flex-direction: column !important;
      }
      .admin-sidebar {
        display: none !important;
      }
      .hamburger-btn {
        display: flex !important;
      }
      .admin-main {
        padding: 1.25rem 1rem !important;
        width: 100% !important;
        max-width: 100% !important;
      }
      .metrics-telemetry-grid, .stats-grid, [class*="metrics-grid"] {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 1rem !important;
      }
    }

    /* --- BREAKPOINT: 768px --- */
    @media (max-width: 768px) {
      .admin-topbar {
        padding: 0.5rem 1rem !important;
        height: auto !important;
        min-height: 58px !important;
      }
      .topbar-right .topbar-btn {
        display: none !important;
      }
      .metrics-telemetry-grid, .stats-grid, .panel-grid, [class*="grid"] {
        grid-template-columns: 1fr !important;
        gap: 1rem !important;
      }
      .module-header-row, .action-bar, .filter-bar {
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 0.75rem !important;
      }
      .module-header-row button, .action-bar button {
        width: 100% !important;
        justify-content: center !important;
      }
      .telemetry-card, .panel-card {
        padding: 1.25rem 1rem !important;
        border-radius: 18px !important;
      }
      .mobile-drawer {
        width: 86vw !important;
        max-width: 320px !important;
      }
    }

    /* --- BREAKPOINT: 480px --- */
    @media (max-width: 480px) {
      .admin-topbar {
        padding: 0.4rem 0.75rem !important;
      }
      .console-pill {
        display: none !important;
      }
      .logo-text { font-size: 1.08rem !important; }
      .logo-3d { width: 19px !important; height: 19px !important; }
      .logo-face {
        width: 19px !important;
        height: 19px !important;
        font-size: 0.52rem !important;
      }
      .admin-main {
        padding: 1rem 0.6rem !important;
      }
      .telemetry-card, .panel-card {
        padding: 1rem 0.75rem !important;
        border-radius: 14px !important;
      }
      .node-status-title { font-size: 0.85rem !important; }
      .metric-value { font-size: 1.45rem !important; }
      .modal-dialog {
        width: 95% !important;
        padding: 1.25rem 1rem !important;
      }
    }

    /* --- BREAKPOINT: 320px --- */
    @media (max-width: 320px) {
      .admin-topbar {
        padding: 0.35rem 0.55rem !important;
      }
      .logo-text { font-size: 0.98rem !important; }
      .admin-main {
        padding: 0.75rem 0.4rem !important;
      }
      .telemetry-card, .panel-card {
        padding: 0.85rem 0.65rem !important;
        border-radius: 12px !important;
      }
      .mobile-drawer {
        width: 92vw !important;
        max-width: 290px !important;
        padding: 1rem 0.75rem !important;
      }
      button, .drawer-action-btn {
        font-size: 0.75rem !important;
      }
    }
"""

CSS_AUTH_RESPONSIVE = """
    /* ==========================================================================
       AUTH & 404 MOBILE-FIRST RESPONSIVE SUITE (320px, 480px, 768px, 1024px)
       ========================================================================== */
    *, *::before, *::after {
      box-sizing: border-box !important;
    }

    html, body {
      overflow-x: hidden !important;
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box !important;
    }

    h1, h2, h3, h4, h5, h6, p, span, a, label, li, button {
      overflow-wrap: break-word !important;
      word-wrap: break-word !important;
    }

    .auth-page-wrapper, .error-container, .card-wrapper {
      width: 100% !important;
      max-width: 440px !important;
      box-sizing: border-box !important;
      padding: 1rem !important;
      margin: auto !important;
    }

    .auth-card, .error-card {
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box !important;
    }

    /* --- BREAKPOINT: 1024px --- */
    @media (max-width: 1024px) {
      .auth-page-wrapper {
        padding: 1.5rem 1rem !important;
      }
    }

    /* --- BREAKPOINT: 768px --- */
    @media (max-width: 768px) {
      .auth-page-wrapper {
        max-width: 420px !important;
        padding: 1rem !important;
      }
      .auth-card {
        padding: 1.85rem 1.5rem !important;
      }
      .error-code-glow {
        font-size: 5rem !important;
      }
    }

    /* --- BREAKPOINT: 480px --- */
    @media (max-width: 480px) {
      .auth-page-wrapper {
        padding: 0.75rem 0.6rem !important;
      }
      .auth-card {
        padding: 1.4rem 1rem !important;
        border-radius: 1rem !important;
      }
      .floating-top-actions {
        top: 0.65rem !important;
        right: 0.65rem !important;
        gap: 0.4rem !important;
      }
      body.rtl .floating-top-actions {
        right: auto !important;
        left: 0.65rem !important;
      }
      .btn-3d-switch {
        width: 34px !important;
        height: 34px !important;
        font-size: 0.8rem !important;
      }
      .logo-text { font-size: 1.15rem !important; }
      .sso-grid {
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 0.4rem !important;
      }
      .sso-btn {
        height: 36px !important;
        font-size: 0.75rem !important;
        padding: 0 0.4rem !important;
      }
      .error-code-glow {
        font-size: 3.8rem !important;
      }
      .quick-destinations-row {
        flex-wrap: wrap !important;
        gap: 0.45rem !important;
        justify-content: center !important;
      }
      .actions-row {
        flex-direction: column !important;
        width: 100% !important;
      }
      .actions-row button, .actions-row a {
        width: 100% !important;
        justify-content: center !important;
      }
      .modal-dialog {
        width: 95% !important;
        padding: 1.35rem 1rem !important;
      }
    }

    /* --- BREAKPOINT: 320px --- */
    @media (max-width: 320px) {
      .auth-page-wrapper {
        padding: 0.4rem 0.3rem !important;
      }
      .auth-card {
        padding: 1.1rem 0.75rem !important;
        border-radius: 0.85rem !important;
      }
      .floating-top-actions {
        top: 0.4rem !important;
        right: 0.4rem !important;
        gap: 0.3rem !important;
      }
      body.rtl .floating-top-actions {
        right: auto !important;
        left: 0.4rem !important;
      }
      .btn-3d-switch {
        width: 30px !important;
        height: 30px !important;
        font-size: 0.72rem !important;
      }
      .logo-text { font-size: 1rem !important; }
      .logo-3d { width: 20px !important; height: 20px !important; }
      .logo-face {
        width: 20px !important;
        height: 20px !important;
        font-size: 0.55rem !important;
      }
      .sso-grid {
        grid-template-columns: 1fr !important;
        gap: 0.4rem !important;
      }
      .sso-btn {
        height: 34px !important;
        width: 100% !important;
        justify-content: center !important;
      }
      .btn-login-submit, .btn-create-account {
        height: 38px !important;
        font-size: 0.8rem !important;
      }
      .error-code-glow {
        font-size: 3rem !important;
      }
      .error-title {
        font-size: 1.15rem !important;
      }
      .error-desc {
        font-size: 0.8rem !important;
      }
    }
"""

def inject_responsive_css(filename, css_block, marker_id):
    with open(filename, 'r', encoding='utf-8') as f:
        c = f.read()

    # Check if marker already injected
    if marker_id in c:
        # replace existing marker block
        pattern = re.escape(marker_id) + r'.*?/\* END ' + re.escape(marker_id) + r' \*/'
        replacement = marker_id + css_block + f"\n    /* END {marker_id} */"
        c, count = re.subn(pattern, replacement, c, flags=re.DOTALL)
        if count == 0:
            print(f"  [{filename}] Could not replace existing block, reinjecting")
            c = c.replace('</style>', f"\n    {marker_id}{css_block}\n    /* END {marker_id} */\n  </style>", 1)
        else:
            print(f"  [{filename}] Updated existing responsive block")
    else:
        # inject before </style>
        if '</style>' in c:
            c = c.replace('</style>', f"\n    /* {marker_id} */{css_block}\n    /* END {marker_id} */\n  </style>", 1)
            print(f"  [{filename}] Injected responsive master suite")
        else:
            print(f"  [{filename}] ERROR: </style> not found")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(c)

print("Applying Responsive Master Suite to 10 Public Pages...")
for p in PUBLIC_PAGES:
    inject_responsive_css(p, CSS_PUBLIC_RESPONSIVE, "RESPONSIVE_PUBLIC_MASTER")

print("\nApplying Responsive Master Suite to 2 Dashboard Pages...")
for p in DASHBOARDS:
    inject_responsive_css(p, CSS_DASHBOARD_RESPONSIVE, "RESPONSIVE_DASHBOARD_MASTER")

print("\nApplying Responsive Master Suite to 4 Auth & Error Pages...")
for p in AUTH_PAGES:
    inject_responsive_css(p, CSS_AUTH_RESPONSIVE, "RESPONSIVE_AUTH_MASTER")

print("\nAll 16 pages updated with Mobile-First Responsive Master Suite!")
