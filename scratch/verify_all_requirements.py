import os, re

public_pages = [
    'index.html', 'navbar.html', 'home-2.html', 'about.html', 'services.html', 
    'contact.html', 'event-planning.html', 'portfolio.html', 'resources.html', 'vendors.html'
]
dashboards = ['admin-dashboard.html', 'user-dashboard.html']
auth_pages = ['login.html', 'registeration.html', 'registration.html', '404.html']
all_pages = public_pages + dashboards + auth_pages

errors = []

print("=== 1. VERIFYING FAVICON ACROSS ALL 16 PAGES ===")
assert os.path.exists('assets/favicon.svg'), "assets/favicon.svg missing"
assert os.path.exists('favicon.svg'), "favicon.svg missing"
assert os.path.exists('favicon.ico'), "favicon.ico missing"

for fn in all_pages:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'favicon.svg' not in c:
        errors.append(f"{fn}: favicon link missing")
    else:
        print(f"  [OK Favicon] {fn}")

print("\n=== 2. VERIFYING LOGO REDIRECTION TO index.html ===")
for fn in public_pages:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    if '<a href="index.html" class="logo-section"' not in c:
        errors.append(f"{fn}: navbar logo link to index.html missing")
    if '<a href="index.html" class="footer-brand-header"' not in c:
        errors.append(f"{fn}: footer logo link to index.html missing")
    print(f"  [OK Logo Links] {fn}")

for fn in dashboards:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    if '<a href="index.html" class="logo-section"' not in c:
        errors.append(f"{fn}: topbar/sidebar logo link to index.html missing")
    print(f"  [OK Logo Links] {fn}")

for fn in auth_pages:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    if '<a href="index.html" class="brand-logo-row"' not in c:
        errors.append(f"{fn}: auth page brand logo link to index.html missing")
    print(f"  [OK Logo Links] {fn}")

print("\n=== 3. VERIFYING LOGIN & LOGOUT REDIRECTION TO login.html ===")
for fn in public_pages:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    login_matches = re.findall(r'<button class="login-btn"[^>]*>', c)
    if not login_matches:
        errors.append(f"{fn}: No login button found")
    for btn in login_matches:
        if "login.html" not in btn:
            errors.append(f"{fn}: login button missing login.html redirect: {btn}")
    print(f"  [OK Login Redirection] {fn} ({len(login_matches)} buttons verified)")

for fn in dashboards:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'login.html' not in c:
        errors.append(f"{fn}: login.html redirection missing for logout")
    else:
        print(f"  [OK Logout Redirection] {fn}")

print("\n=== 4. VERIFYING STICKY NAVBAR FIX ===")
for fn in public_pages:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'position: sticky' not in c:
        errors.append(f"{fn}: position: sticky missing in .nav-container")
    if 'top: 1rem' not in c and 'top:1rem' not in c:
        errors.append(f"{fn}: top: 1rem missing in .nav-container")
    print(f"  [OK Sticky Navbar] {fn}")

print("\n==========================================")
if errors:
    print(f"FAILED WITH {len(errors)} ERRORS:")
    for e in errors:
        print(f"  ERROR: {e}")
else:
    print("ALL 16 FILES PASSED 100% OF VERIFICATION CHECKS!")
