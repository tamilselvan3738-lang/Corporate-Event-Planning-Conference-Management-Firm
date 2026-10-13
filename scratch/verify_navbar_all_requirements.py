import re, sys

sys.stdout.reconfigure(encoding='utf-8')

pages = [
    'index.html', 'home-2.html', 'about.html', 'services.html', 
    'portfolio.html', 'event-planning.html', 'vendors.html', 
    'resources.html', 'contact.html', 'navbar.html'
]

expected_active = {
    'index.html': ['Home 1', 'index.html'],
    'home-2.html': ['Home 2', 'home-2.html'],
    'about.html': ['About', 'about.html'],
    'services.html': ['Services', 'services.html'],
    'portfolio.html': ['Portfolio', 'portfolio.html'],
    'event-planning.html': ['Event Planning', 'event-planning.html'],
    'vendors.html': ['Vendors', 'vendors.html'],
    'resources.html': ['Resources', 'resources.html'],
    'contact.html': ['Contact', 'contact.html'],
    'navbar.html': ['Home 1', 'index.html']
}

required_links = [
    ('index.html', 'Home 1'),
    ('home-2.html', 'Home 2'),
    ('about.html', 'About'),
    ('services.html', 'Services'),
    ('portfolio.html', 'Portfolio'),
    ('event-planning.html', 'Event Planning'),
    ('vendors.html', 'Vendors'),
    ('resources.html', 'Resources'),
    ('contact.html', 'Contact'),
    ('admin-dashboard.html', 'Admin Dashboard'),
    ('user-dashboard.html', 'User Dashboard'),
]

all_passed = True

print("=== 1. VERIFYING NAVBAR LINKS IN DESKTOP AND MOBILE ===")
for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()

    # Extract desktop nav and mobile nav with precise outer boundaries
    m_desk = re.search(r'<!-- CENTER: DESKTOP NAV LINKS -->(.*?)<!-- RIGHT: ICONS & LOGIN -->', c, re.DOTALL)
    m_mob = re.search(r'<!-- MOBILE MENU -->(.*?)<div class="mobile-actions">', c, re.DOTALL)

    if not m_desk or not m_mob:
        print(f"  [FAIL] {p} missing nav boundaries")
        all_passed = False
        continue

    desk_html = m_desk.group(1)
    mob_html = m_mob.group(1)

    page_links_ok = True
    for target_href, label in required_links:
        # Check desktop
        if f'href="{target_href}"' not in desk_html:
            print(f"  [FAIL Desktop] {p} missing link to {target_href} ({label})")
            page_links_ok = False
            all_passed = False
        # Check mobile
        if f'href="{target_href}"' not in mob_html:
            print(f"  [FAIL Mobile] {p} missing link to {target_href} ({label})")
            page_links_ok = False
            all_passed = False

    if page_links_ok:
        print(f"  [OK Links] {p}: All 11 navigation links verified in desktop & mobile!")

print("\n=== 2. VERIFYING ACTIVE STATUS ACROSS PAGES ===")
for p, (label, target_href) in expected_active.items():
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()

    m_desk = re.search(r'<!-- CENTER: DESKTOP NAV LINKS -->(.*?)<!-- RIGHT: ICONS & LOGIN -->', c, re.DOTALL)
    desk_html = m_desk.group(1)

    # Check that active is on the expected link
    active_matches = re.findall(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*class=["\'][^"\']*active[^"\']*["\'][^>]*>(.*?)</a>', desk_html, re.DOTALL)
    active_clean = [(href, re.sub(r'<[^>]+>', '', text).strip()) for href, text in active_matches]
    
    # Check if target is in active
    has_target_active = any(href == target_href or label.lower() in text.lower() for href, text in active_clean)
    if not has_target_active:
        print(f"  [FAIL Active] {p}: Expected active '{label}' ({target_href}), got {active_clean}")
        all_passed = False
    else:
        print(f"  [OK Active] {p}: Verified active on '{label}' ({active_clean})")

print("\n=== 3. VERIFYING ACTIVE CSS RULES ===")
for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    rules = [
        '.nav-links > li > a.active',
        '.dropdown-item.active',
        '.mobile-nav-links > li > a.active',
        'body.dark .nav-links > li > a.active'
    ]
    missing = [r for r in rules if r not in c]
    if missing:
        print(f"  [FAIL CSS] {p} missing CSS rules: {missing}")
        all_passed = False
    else:
        print(f"  [OK CSS] {p}: All active CSS rules verified!")

print("\n=== 4. VERIFYING REGRESSION (FAVICON, LOGO REDIRECTION, LOGIN REDIRECTION, STICKY NAVBAR) ===")
# Run regression checks
import subprocess
res = subprocess.run([sys.executable, 'scratch/verify_all_requirements.py'], capture_output=True, text=True)
if res.returncode == 0:
    print("  [OK Regression] All previous suites passed 100%!")
else:
    print("  [FAIL Regression] Regression failures:\n", res.stdout, res.stderr)
    all_passed = False

print("\n" + "="*50)
if all_passed:
    print("ALL VERIFICATION CHECKS PASSED WITH ZERO ERRORS!")
else:
    print("SOME CHECKS FAILED! REVIEW LOGS ABOVE.")
sys.exit(0 if all_passed else 1)
