import os, re

favicon_block = '''  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32x32.png">
  <link rel="shortcut icon" href="favicon.ico">
  <link rel="apple-touch-icon" href="assets/apple-touch-icon.png">'''

public_pages = [
    'index.html', 'navbar.html', 'home-2.html', 'about.html', 'services.html', 
    'contact.html', 'event-planning.html', 'portfolio.html', 'resources.html', 'vendors.html'
]

dashboards = ['admin-dashboard.html', 'user-dashboard.html']
auth_pages = ['login.html', 'registeration.html', 'registration.html', '404.html']

all_pages = public_pages + dashboards + auth_pages

print(f"Applying updates to {len(all_pages)} HTML files...")

# ==============================================================================
# 1. PROCESS ALL 16 FILES FOR FAVICON
# ==============================================================================
for fn in all_pages:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    # Add favicon if not present
    if 'favicon' not in c:
        if '</head>' in c:
            c = c.replace('</head>', f"{favicon_block}\n</head>")
            with open(fn, 'w', encoding='utf-8') as f_out:
                f_out.write(c)
            print(f"  [Favicon Added] {fn}")
        else:
            print(f"  [Warning: No </head>] {fn}")
    else:
        print(f"  [Favicon Already Present] {fn}")

# ==============================================================================
# 2. PROCESS PUBLIC PAGES (NAVBAR STICKY, LOGO LINKS, LOGIN BTN)
# ==============================================================================
for fn in public_pages:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    modified = False

    # A. Sticky Navbar CSS
    # 1. Change overflow-x: hidden on body to overflow-x: clip
    if 'overflow-x: hidden;' in c:
        c = c.replace('overflow-x: hidden;', 'overflow-x: clip;')
        modified = True

    # 2. Add sticky to .nav-container CSS
    old_nav_css = '.nav-container {\n      display: flex;'
    new_nav_css = '''.nav-container {
      position: -webkit-sticky !important;
      position: sticky !important;
      top: 1rem !important;
      z-index: 1000 !important;
      display: flex;'''

    if old_nav_css in c and 'position: sticky' not in c[:c.find(old_nav_css) + 100]:
        c = c.replace(old_nav_css, new_nav_css)
        modified = True

    # Also handle alternate formatting if any
    old_nav_css_alt = '.nav-container {\r\n      display: flex;'
    new_nav_css_alt = '''.nav-container {
      position: -webkit-sticky !important;
      position: sticky !important;
      top: 1rem !important;
      z-index: 1000 !important;
      display: flex;'''
    if old_nav_css_alt in c and 'position: sticky' not in c[:c.find(old_nav_css_alt) + 100]:
        c = c.replace(old_nav_css_alt, new_nav_css_alt)
        modified = True

    # B. Logo link redirection to index.html in navbar
    # Look for: <div class="logo-section"> ... </div> before <!-- CENTER: DESKTOP NAV LINKS -->
    # We replace <div class="logo-section"> with <a href="index.html" class="logo-section" style="text-decoration: none; cursor: pointer;">
    # and the closing </div> of logo-section with </a>
    if '<div class="logo-section">' in c:
        # Replace opening
        c = c.replace(
            '<div class="logo-section">',
            '<a href="index.html" class="logo-section" style="text-decoration: none; cursor: pointer;">'
        )
        # In navbar, the closing </div> is right before <!-- CENTER: DESKTOP NAV LINKS -->
        target_close = '</div>\n\n      <!-- CENTER: DESKTOP NAV LINKS -->'
        replacement_close = '</a>\n\n      <!-- CENTER: DESKTOP NAV LINKS -->'
        if target_close in c:
            c = c.replace(target_close, replacement_close)
        else:
            # check with \r\n
            target_close_crlf = '</div>\r\n\r\n      <!-- CENTER: DESKTOP NAV LINKS -->'
            replacement_close_crlf = '</a>\r\n\r\n      <!-- CENTER: DESKTOP NAV LINKS -->'
            if target_close_crlf in c:
                c = c.replace(target_close_crlf, replacement_close_crlf)
        modified = True

    # C. Logo link redirection in footer
    if '<div class="footer-brand-header">' in c:
        c = c.replace(
            '<div class="footer-brand-header">',
            '<a href="index.html" class="footer-brand-header" style="text-decoration: none; cursor: pointer;">'
        )
        target_footer_close = '</div>\n          <p class="footer-brand-desc">'
        replacement_footer_close = '</a>\n          <p class="footer-brand-desc">'
        if target_footer_close in c:
            c = c.replace(target_footer_close, replacement_footer_close)
        else:
            target_footer_close_crlf = '</div>\r\n          <p class="footer-brand-desc">'
            replacement_footer_close_crlf = '</a>\r\n          <p class="footer-brand-desc">'
            if target_footer_close_crlf in c:
                c = c.replace(target_footer_close_crlf, replacement_footer_close_crlf)
        modified = True

    # D. Login Button redirection
    # Find <button class="login-btn"> without onclick and add onclick="window.location.href='login.html'"
    old_btn = '<button class="login-btn">'
    new_btn = '<button class="login-btn" onclick="window.location.href=\'login.html\'" title="Client Portal Login">'
    if old_btn in c:
        c = c.replace(old_btn, new_btn)
        modified = True

    if modified:
        with open(fn, 'w', encoding='utf-8') as f_out:
            f_out.write(c)
        print(f"  [Public Page Updated] {fn} (Sticky nav, logo links, login btn)")
    else:
        print(f"  [Public Page Checked - No changes needed] {fn}")

# ==============================================================================
# 3. PROCESS DASHBOARDS (DRAWER LOGO LINK, LOGOUT REDIRECTION)
# ==============================================================================
for fn in dashboards:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    modified = False

    # Drawer logo replacement:
    # Look for <div class="logo-section"> in drawer
    if '<div class="logo-section">' in c:
        c = c.replace(
            '<div class="logo-section">',
            '<a href="index.html" class="logo-section" style="text-decoration: none; cursor: pointer;">'
        )
        # Find closing </div> before <!-- Close Drawer Button -->
        target_dash_close = '</div>\n      <button class="drawer-close-btn"'
        replacement_dash_close = '</a>\n      <button class="drawer-close-btn"'
        if target_dash_close in c:
            c = c.replace(target_dash_close, replacement_dash_close)
        else:
            target_dash_close_crlf = '</div>\r\n      <button class="drawer-close-btn"'
            replacement_dash_close_crlf = '</a>\r\n      <button class="drawer-close-btn"'
            if target_dash_close_crlf in c:
                c = c.replace(target_dash_close_crlf, replacement_dash_close_crlf)
        modified = True

    # Logout button redirection
    # Ensure sidebarLogoutBtn has onclick
    old_logout = '<a class="nav-module-item logout-item" id="sidebarLogoutBtn">'
    new_logout = '<a class="nav-module-item logout-item" id="sidebarLogoutBtn" href="login.html" onclick="window.location.href=\'login.html\'">'
    if old_logout in c:
        c = c.replace(old_logout, new_logout)
        modified = True

    # Also topbar / drawer logout button
    if 'id="drawerLogoutBtn"' in c and 'onclick="window.location.href=\'login.html\'"' not in c:
        c = re.sub(
            r'(<button[^>]*id="drawerLogoutBtn"[^>]*?)>',
            r'\1 onclick="window.location.href=\'login.html\'">',
            c
        )
        modified = True

    if modified:
        with open(fn, 'w', encoding='utf-8') as f_out:
            f_out.write(c)
        print(f"  [Dashboard Updated] {fn} (Drawer logo link, logout redirect)")
    else:
        print(f"  [Dashboard Checked - No changes needed] {fn}")

# ==============================================================================
# 4. ALSO UPDATE BUILDER SCRIPTS
# ==============================================================================
builder_scripts = [
    'scratch/build_login_page.py',
    'scratch/build_registration_page.py',
    'scratch/build_404_page.py'
]

for bs in builder_scripts:
    if os.path.exists(bs):
        with open(bs, 'r', encoding='utf-8') as f:
            bc = f.read()
        if 'favicon' not in bc and '</head>' in bc:
            bc = bc.replace('</head>', f"{favicon_block}\n</head>")
            with open(bs, 'w', encoding='utf-8') as f_out:
                f_out.write(bc)
            print(f"  [Builder Script Updated with Favicon] {bs}")

print("All updates completed successfully!")
