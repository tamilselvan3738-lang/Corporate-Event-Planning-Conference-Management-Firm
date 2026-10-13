# -*- coding: utf-8 -*-
"""
update_alignment.py
Fixes alignment issues in admin-dashboard.html:
1. Sidebar navigation items:
   - Sidebar width set to 320px
   - white-space: nowrap on items and labels (no multi-line wrapping)
   - Fixed 20x20px icon wrapper and vertical centering
   - Fixed height 42px per row for uniform vertical rhythm
   - Ellipsis fallback for ultra-narrow widths
   - flex-shrink: 0 on counter badges
2. Topbar controls:
   - white-space: nowrap and flex-shrink: 0 on all buttons, badges, and user profile
   - Uniform height 38px on buttons, 42px on user profile
   - Search bar scaled gracefully (width: 220px, min-width: 150px)
   - User profile info text: single line for "Marcus Vance, COO" and single line for "Head Producer • Super Admin"
3. Strict Mobile & Tablet layout:
   - Breakpoint set to 1120px so ALL mobile and tablet viewports (including 1024px) show ONLY logo on left and hamburger on right
"""

with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace root variables
html = html.replace('--sidebar-width: 290px;', '--sidebar-width: 320px;')
html = html.replace('--topbar-height: 72px;', '--topbar-height: 68px;')

# Replace CSS for Topbar items
old_topbar_css = """    .admin-topbar {
      height: var(--topbar-height);
      background: var(--adm-surface);
      border-bottom: 1px solid var(--adm-border);
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.5rem;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    }

    .topbar-left {
      display: flex;
      align-items: center;
      gap: 1.5rem;
    }

    .topbar-search {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      padding: 0.45rem 1rem;
      border-radius: 0.65rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      width: 280px;
      transition: all 0.25s ease;
    }

    .topbar-search:focus-within {
      border-color: var(--adm-primary-blue);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2);
    }

    .topbar-search input {
      background: transparent;
      border: none;
      outline: none;
      color: var(--adm-text-primary);
      font-size: 0.88rem;
      width: 100%;
    }

    .topbar-search kbd {
      font-size: 0.7rem;
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.08);
      color: var(--adm-text-muted);
      border: 1px solid var(--adm-border-subtle);
    }

    .topbar-right {
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }

    .topbar-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.48rem 0.95rem;
      border-radius: 0.6rem;
      font-size: 0.84rem;
      font-weight: 600;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      color: var(--adm-text-secondary);
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .topbar-btn:hover {
      background: var(--adm-surface-card-hover);
      color: var(--adm-text-primary);
      border-color: var(--adm-primary-blue);
    }

    .topbar-icon-btn {
      position: relative;
      width: 38px;
      height: 38px;
      border-radius: 0.6rem;
      display: flex;
      align-items: center;
      justify-content: center;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      color: var(--adm-text-secondary);
      cursor: pointer;
      font-size: 0.9rem;
      font-weight: 700;
      transition: all 0.2s ease;
    }

    .topbar-icon-btn:hover {
      background: var(--adm-surface-card-hover);
      color: var(--adm-text-primary);
      border-color: var(--adm-primary-blue);
    }

    .notif-badge {
      position: absolute;
      top: -4px;
      right: -4px;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #f43f5e;
      color: #fff;
      font-size: 0.65rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .user-profile-badge {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.35rem 0.85rem;
      border-radius: 0.75rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      cursor: pointer;
    }

    .avatar-ring {
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: linear-gradient(135deg, #f59e0b, #d97706);
      color: #fff;
      font-weight: 800;
      font-size: 0.85rem;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 10px rgba(245, 158, 11, 0.4);
    }

    .user-info {
      display: flex;
      flex-direction: column;
      line-height: 1.2;
    }

    .user-info strong {
      font-size: 0.85rem;
      color: var(--adm-text-primary);
    }

    .user-info span {
      font-size: 0.72rem;
      color: var(--adm-text-muted);
    }"""

new_topbar_css = """    .admin-topbar {
      height: var(--topbar-height);
      background: var(--adm-surface);
      border-bottom: 1px solid var(--adm-border);
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.5rem;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
      gap: 1rem;
    }

    .topbar-left {
      display: flex;
      align-items: center;
      gap: 1.25rem;
      flex-shrink: 0;
    }

    .logo-section {
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      user-select: none;
      white-space: nowrap;
      flex-shrink: 0;
    }

    .console-pill {
      font-size: 0.68rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      background: rgba(37, 99, 235, 0.15);
      border: 1px solid rgba(59, 130, 246, 0.3);
      color: #60a5fa;
      margin-left: 0.5rem;
      white-space: nowrap;
      flex-shrink: 0;
    }

    .topbar-search {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      padding: 0 0.85rem;
      height: 38px;
      border-radius: 0.65rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      width: 220px;
      flex-shrink: 1;
      min-width: 150px;
      transition: all 0.25s ease;
    }

    .topbar-search:focus-within {
      border-color: var(--adm-primary-blue);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2);
    }

    .topbar-search input {
      background: transparent;
      border: none;
      outline: none;
      color: var(--adm-text-primary);
      font-size: 0.85rem;
      width: 100%;
      white-space: nowrap;
    }

    .topbar-search kbd {
      font-size: 0.68rem;
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.08);
      color: var(--adm-text-muted);
      border: 1px solid var(--adm-border-subtle);
      white-space: nowrap;
    }

    .topbar-right {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      flex-shrink: 0;
      white-space: nowrap;
    }

    .topbar-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.45rem;
      height: 38px;
      padding: 0 0.85rem;
      border-radius: 0.6rem;
      font-size: 0.82rem;
      font-weight: 600;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      color: var(--adm-text-secondary);
      text-decoration: none;
      cursor: pointer;
      white-space: nowrap; /* PREVENTS 'Refresh Metrics' FROM WRAPPING */
      flex-shrink: 0;
      transition: all 0.2s ease;
      box-sizing: border-box;
    }

    .topbar-btn:hover {
      background: var(--adm-surface-card-hover);
      color: var(--adm-text-primary);
      border-color: var(--adm-primary-blue);
    }

    .topbar-icon-btn {
      position: relative;
      width: 38px;
      height: 38px;
      border-radius: 0.6rem;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      color: var(--adm-text-secondary);
      cursor: pointer;
      font-size: 0.88rem;
      font-weight: 700;
      white-space: nowrap;
      flex-shrink: 0;
      transition: all 0.2s ease;
      box-sizing: border-box;
    }

    .topbar-icon-btn:hover {
      background: var(--adm-surface-card-hover);
      color: var(--adm-text-primary);
      border-color: var(--adm-primary-blue);
    }

    .notif-badge {
      position: absolute;
      top: -4px;
      right: -4px;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #f43f5e;
      color: #fff;
      font-size: 0.65rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .user-profile-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.65rem;
      height: 42px;
      padding: 0 0.85rem;
      border-radius: 0.75rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      cursor: pointer;
      white-space: nowrap; /* PREVENTS 'Marcus Vance, COO' WRAPPING */
      flex-shrink: 0;
      box-sizing: border-box;
    }

    .avatar-ring {
      width: 30px;
      height: 30px;
      border-radius: 50%;
      background: linear-gradient(135deg, #f59e0b, #d97706);
      color: #fff;
      font-weight: 800;
      font-size: 0.78rem;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 10px rgba(245, 158, 11, 0.4);
      flex-shrink: 0;
    }

    .user-info {
      display: flex;
      flex-direction: column;
      line-height: 1.25;
      white-space: nowrap;
    }

    .user-info strong {
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--adm-text-primary);
      white-space: nowrap;
    }

    .user-info span {
      font-size: 0.68rem;
      color: var(--adm-text-muted);
      white-space: nowrap;
    }"""

if old_topbar_css in html:
    html = html.replace(old_topbar_css, new_topbar_css)
    print("Replaced topbar CSS successfully!")
else:
    print("Could not find exact old_topbar_css!")

# Replace CSS for Sidebar Navigation Items
old_sidebar_css = """    .admin-sidebar {
      width: var(--sidebar-width);
      background: var(--adm-surface);
      border-right: 1px solid var(--adm-border);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      height: calc(100vh - var(--topbar-height));
      position: sticky;
      top: var(--topbar-height);
      overflow-y: auto;
      padding: 1.25rem 0.85rem;
      box-shadow: 2px 0 10px rgba(0, 0, 0, 0.05);
    }

    body.rtl .admin-sidebar {
      border-right: none;
      border-left: 1px solid var(--adm-border);
    }

    .sidebar-header-box {
      padding: 1rem;
      border-radius: 0.85rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .node-status-title {
      font-size: 0.82rem;
      font-weight: 800;
      color: var(--adm-text-primary);
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }

    .status-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--adm-primary-emerald);
      box-shadow: 0 0 8px var(--adm-primary-emerald);
    }

    .node-subtext {
      font-size: 0.72rem;
      color: var(--adm-text-muted);
      margin-top: 0.2rem;
    }

    .active-pill {
      font-size: 0.68rem;
      font-weight: 800;
      padding: 0.2rem 0.55rem;
      border-radius: 9999px;
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }

    .sidebar-nav-label {
      font-size: 0.7rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--adm-text-muted);
      padding: 0.5rem 0.75rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.35rem;
    }

    .sidebar-menu-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }

    .nav-module-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.7rem 0.95rem;
      border-radius: 0.75rem;
      color: var(--adm-text-secondary);
      font-size: 0.88rem;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s ease;
      border: 1px solid transparent;
    }

    .nav-module-item:hover {
      background: var(--adm-surface-card);
      color: var(--adm-text-primary);
      border-color: var(--adm-border);
    }

    .nav-module-item.active {
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.15), rgba(59, 130, 246, 0.1));
      color: #60a5fa;
      border-color: rgba(59, 130, 246, 0.35);
      font-weight: 700;
    }

    .item-left {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .item-left i {
      width: 18px;
      text-align: center;
      font-size: 0.95rem;
    }

    .item-counter {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.15rem 0.55rem;
      border-radius: 9999px;
      background: var(--adm-surface-card);
      color: var(--adm-text-muted);
      border: 1px solid var(--adm-border-subtle);
    }

    .nav-module-item.active .item-counter {
      background: #2563eb;
      color: #ffffff;
      border-color: transparent;
    }"""

new_sidebar_css = """    .admin-sidebar {
      width: var(--sidebar-width);
      background: var(--adm-surface);
      border-right: 1px solid var(--adm-border);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      height: calc(100vh - var(--topbar-height));
      position: sticky;
      top: var(--topbar-height);
      overflow-y: auto;
      padding: 1.25rem 0.75rem;
      box-shadow: 2px 0 10px rgba(0, 0, 0, 0.05);
    }

    body.rtl .admin-sidebar {
      border-right: none;
      border-left: 1px solid var(--adm-border);
    }

    .sidebar-header-box {
      padding: 0.85rem 1rem;
      border-radius: 0.85rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      white-space: nowrap;
    }

    .node-status-title {
      font-size: 0.82rem;
      font-weight: 800;
      color: var(--adm-text-primary);
      display: flex;
      align-items: center;
      gap: 0.45rem;
      white-space: nowrap;
    }

    .status-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--adm-primary-emerald);
      box-shadow: 0 0 8px var(--adm-primary-emerald);
      flex-shrink: 0;
    }

    .node-subtext {
      font-size: 0.72rem;
      color: var(--adm-text-muted);
      margin-top: 0.2rem;
      white-space: nowrap;
    }

    .active-pill {
      font-size: 0.68rem;
      font-weight: 800;
      padding: 0.2rem 0.55rem;
      border-radius: 9999px;
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
      white-space: nowrap;
      flex-shrink: 0;
    }

    .sidebar-nav-label {
      font-size: 0.7rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--adm-text-muted);
      padding: 0.5rem 0.65rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.35rem;
      white-space: nowrap;
    }

    .sidebar-menu-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }

    .nav-module-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.62rem 0.8rem;
      border-radius: 0.75rem;
      color: var(--adm-text-secondary);
      font-size: 0.85rem;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s ease;
      border: 1px solid transparent;
      white-space: nowrap; /* PREVENTS SIDEBAR ITEMS WRAPPING ONTO 2 LINES */
      gap: 0.5rem;
      height: 42px; /* UNIFORM ROW HEIGHT */
      box-sizing: border-box;
    }

    .nav-module-item:hover {
      background: var(--adm-surface-card);
      color: var(--adm-text-primary);
      border-color: var(--adm-border);
    }

    .nav-module-item.active {
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.15), rgba(59, 130, 246, 0.1));
      color: #60a5fa;
      border-color: rgba(59, 130, 246, 0.35);
      font-weight: 700;
    }

    .item-left {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      white-space: nowrap;
      min-width: 0;
      flex: 1;
      overflow: hidden;
    }

    .item-left i {
      width: 20px;
      height: 20px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.95rem;
      flex-shrink: 0;
      text-align: center;
    }

    .item-left span {
      white-space: nowrap;
      font-size: 0.84rem;
      font-weight: 600;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .item-counter {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.2rem 0.55rem;
      border-radius: 9999px;
      background: var(--adm-surface-card);
      color: var(--adm-text-muted);
      border: 1px solid var(--adm-border-subtle);
      white-space: nowrap;
      flex-shrink: 0; /* BADGES NEVER SQUISHED */
    }

    .nav-module-item.active .item-counter {
      background: #2563eb;
      color: #ffffff;
      border-color: transparent;
    }"""

if old_sidebar_css in html:
    html = html.replace(old_sidebar_css, new_sidebar_css)
    print("Replaced sidebar CSS successfully!")
else:
    print("Could not find exact old_sidebar_css!")

# Update Media Query to 1120px for strict Mobile & Tablet adherence
old_media = """    @media (max-width: 1024px) {
      /* TOPBAR: ONLY LOGO ON LEFT AND HAMBURGER ON RIGHT! */
      .console-pill {
        display: none !important;
      }

      .topbar-search {
        display: none !important;
      }

      .topbar-right {
        display: none !important;
      }

      .hamburger-btn {
        display: flex !important;
      }

      /* HIDE DESKTOP SIDEBAR COMPLETELY */
      .admin-sidebar {
        display: none !important;
      }

      /* MAIN CONTENT OCCUPIES FULL WIDTH */
      .admin-main {
        width: 100% !important;
        padding: 1.5rem 1rem 3rem 1rem !important;
      }

      .metrics-telemetry-grid {
        grid-template-columns: 1fr;
      }

      @media (min-width: 640px) {
        .metrics-telemetry-grid {
          grid-template-columns: repeat(2, 1fr);
        }
      }
    }"""

new_media = """    @media (max-width: 1120px) {
      /* TOPBAR: ONLY LOGO ON LEFT AND HAMBURGER ON RIGHT FOR ALL MOBILE & TABLET DEVICES */
      .console-pill {
        display: none !important;
      }

      .topbar-search {
        display: none !important;
      }

      .topbar-right {
        display: none !important;
      }

      .hamburger-btn {
        display: flex !important;
      }

      /* HIDE DESKTOP SIDEBAR COMPLETELY */
      .admin-sidebar {
        display: none !important;
      }

      /* MAIN CONTENT OCCUPIES FULL WIDTH */
      .admin-main {
        width: 100% !important;
        padding: 1.5rem 1rem 3rem 1rem !important;
      }

      .metrics-telemetry-grid {
        grid-template-columns: 1fr;
      }

      @media (min-width: 640px) {
        .metrics-telemetry-grid {
          grid-template-columns: repeat(2, 1fr);
        }
      }
    }"""

if old_media in html:
    html = html.replace(old_media, new_media)
    print("Replaced media query successfully!")
else:
    print("Could not find exact old_media!")

with open('admin-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated admin-dashboard.html!")
