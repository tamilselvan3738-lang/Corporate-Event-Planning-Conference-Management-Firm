# -*- coding: utf-8 -*-
"""
fix_dashboard_layout.py
Comprehensive layout & alignment fixes for admin-dashboard.html:
1. Replaces native Windows scrollbar with a sleek, ultra-thin semi-transparent dark scrollbar.
2. Increases sidebar width to 340px and eliminates text truncation (Event Project Management fits completely).
3. Compacts topbar buttons (Home, Sovereign, Refresh) and scales search bar to 200px with clean placeholder.
4. Prevents horizontal overflow in topbar so profile badge is never cut off on the right.
5. Adds min-width: 0 and overflow-x: hidden to .admin-main so stat cards fit 100% width cleanly.
"""

with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update root variables
html = html.replace('--sidebar-width: 320px;', '--sidebar-width: 340px;')
html = html.replace('--sidebar-width: 290px;', '--sidebar-width: 340px;')

# 2. Add custom sleek scrollbar CSS right after root variables
scrollbar_css = """
    /* ==========================================================================
       CUSTOM ULTRA-SLEEK DARK SCROLLBAR (ELIMINATES UGLY WHITE WINDOWS SCROLLBAR)
       ========================================================================== */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }

    ::-webkit-scrollbar-track {
      background: transparent;
    }

    ::-webkit-scrollbar-thumb {
      background: rgba(59, 130, 246, 0.25);
      border-radius: 9999px;
    }

    ::-webkit-scrollbar-thumb:hover {
      background: rgba(59, 130, 246, 0.5);
    }

    * {
      scrollbar-width: thin;
      scrollbar-color: rgba(59, 130, 246, 0.25) transparent;
    }
"""

if '/* ==========================================================================\n       CUSTOM ULTRA-SLEEK DARK SCROLLBAR' not in html:
    html = html.replace('* {\n      box-sizing: border-box;', scrollbar_css + '\n    * {\n      box-sizing: border-box;')

# 3. Update .admin-topbar CSS
old_topbar_css_search = """    .admin-topbar {
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
    }"""

new_topbar_css_search = """    .admin-topbar {
      height: var(--topbar-height);
      background: var(--adm-surface);
      border-bottom: 1px solid var(--adm-border);
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.25rem;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
      gap: 0.75rem;
      width: 100%;
      box-sizing: border-box;
      max-width: 100vw;
    }"""

html = html.replace(old_topbar_css_search, new_topbar_css_search)

# 4. Update topbar-search CSS
old_search_css = """    .topbar-search {
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
    }"""

new_search_css = """    .topbar-search {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0 0.75rem;
      height: 38px;
      border-radius: 0.65rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      width: 200px;
      flex-shrink: 0;
      transition: all 0.25s ease;
    }"""

html = html.replace(old_search_css, new_search_css)

# 5. Update topbar-right and buttons CSS
old_btn_css = """    .topbar-right {
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
    }"""

new_btn_css = """    .topbar-right {
      display: flex;
      align-items: center;
      gap: 0.45rem;
      flex-shrink: 0;
      white-space: nowrap;
    }

    .topbar-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
      height: 38px;
      padding: 0 0.75rem;
      border-radius: 0.6rem;
      font-size: 0.82rem;
      font-weight: 600;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      color: var(--adm-text-secondary);
      text-decoration: none;
      cursor: pointer;
      white-space: nowrap;
      flex-shrink: 0;
      transition: all 0.2s ease;
      box-sizing: border-box;
    }"""

html = html.replace(old_btn_css, new_btn_css)

# 6. Update user profile badge CSS
old_profile_css = """    .user-profile-badge {
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

new_profile_css = """    .user-profile-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.55rem;
      height: 40px;
      padding: 0 0.75rem;
      border-radius: 0.75rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      cursor: pointer;
      white-space: nowrap;
      flex-shrink: 0;
      box-sizing: border-box;
    }

    .avatar-ring {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: linear-gradient(135deg, #f59e0b, #d97706);
      color: #fff;
      font-weight: 800;
      font-size: 0.75rem;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 10px rgba(245, 158, 11, 0.4);
      flex-shrink: 0;
    }

    .user-info {
      display: flex;
      flex-direction: column;
      line-height: 1.15;
      white-space: nowrap;
    }

    .user-info strong {
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--adm-text-primary);
      white-space: nowrap;
    }

    .user-info span {
      font-size: 0.68rem;
      color: var(--adm-text-muted);
      white-space: nowrap;
    }"""

html = html.replace(old_profile_css, new_profile_css)

# 7. Update .admin-main CSS (add min-width: 0 to fix flexbox overflow)
old_main_css = """    .admin-main {
      flex: 1;
      padding: 2rem 2.25rem 4rem 2.25rem;
      background: var(--adm-bg);
      overflow-y: auto;
    }"""

new_main_css = """    .admin-main {
      flex: 1;
      min-width: 0;
      width: 100%;
      box-sizing: border-box;
      padding: 1.75rem 2rem 4rem 2rem;
      background: var(--adm-bg);
      overflow-y: auto;
      overflow-x: hidden;
    }"""

html = html.replace(old_main_css, new_main_css)

# 8. Update Topbar HTML to use concise text labels (Home, Sovereign, Refresh) + clean placeholder
old_topbar_html = """      <!-- Desktop Search (Hidden on Mobile & Tab <= 1024px) -->
      <div class="topbar-search">
        <i class="fas fa-search" style="color: var(--adm-text-muted);"></i>
        <input type="text" id="topbarSearchInput" placeholder="Quick Search (Ctrl + K)">
        <kbd>Ctrl K</kbd>
      </div>
    </div>

    <!-- Desktop Actions & Profile (Hidden on Mobile & Tab <= 1024px) -->
    <div class="topbar-right">
      <a href="index.html" class="topbar-btn">
        <i class="fas fa-home"></i> Back to Home
      </a>
      <a href="home-2.html" class="topbar-btn">
        <i class="fas fa-crown text-amber-400"></i> Sovereign Portal
      </a>
      <button class="topbar-btn" id="refreshMetricsBtn">
        <i class="fas fa-sync-alt"></i> Refresh Metrics
      </button>"""

new_topbar_html = """      <!-- Desktop Search (Hidden on Mobile & Tab <= 1024px) -->
      <div class="topbar-search">
        <i class="fas fa-search" style="color: var(--adm-text-muted);"></i>
        <input type="text" id="topbarSearchInput" placeholder="Quick Search...">
        <kbd>Ctrl K</kbd>
      </div>
    </div>

    <!-- Desktop Actions & Profile (Hidden on Mobile & Tab <= 1024px) -->
    <div class="topbar-right">
      <a href="index.html" class="topbar-btn" title="Back to Home Page">
        <i class="fas fa-home"></i> <span>Home</span>
      </a>
      <a href="home-2.html" class="topbar-btn" title="Sovereign Event Portal">
        <i class="fas fa-crown" style="color: #fbbf24;"></i> <span>Sovereign</span>
      </a>
      <button class="topbar-btn" id="refreshMetricsBtn" title="Refresh Live Metrics">
        <i class="fas fa-sync-alt"></i> <span>Refresh</span>
      </button>"""

html = html.replace(old_topbar_html, new_topbar_html)

# 9. Update sidebar items padding & font size to eliminate text truncation
old_nav_item_css = """    .nav-module-item {
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
    }"""

new_nav_item_css = """    .nav-module-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.62rem 0.85rem;
      border-radius: 0.75rem;
      color: var(--adm-text-secondary);
      font-size: 0.86rem;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s ease;
      border: 1px solid transparent;
      white-space: nowrap;
      gap: 0.5rem;
      height: 42px;
      box-sizing: border-box;
      width: 100%;
    }"""

html = html.replace(old_nav_item_css, new_nav_item_css)

with open('admin-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied comprehensive layout and alignment fixes to admin-dashboard.html!")
