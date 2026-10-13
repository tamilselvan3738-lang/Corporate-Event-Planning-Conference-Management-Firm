import os, re

html_files = [f for f in sorted(os.listdir('.')) if f.endswith('.html')]

print(f"Total HTML files: {len(html_files)}")

for fn in html_files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    has_fav = 'favicon' in c
    has_nav = 'nav-container' in c
    has_login_btn = 'login-btn' in c
    has_logo_sec = 'logo-section' in c or 'brand-logo-row' in c or 'footer-brand-header' in c

    print(f"{fn:22} | Favicon: {str(has_fav):5} | Nav: {str(has_nav):5} | LoginBtn: {str(has_login_btn):5} | Logo: {str(has_logo_sec):5}")
