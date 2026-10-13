import glob, sys
sys.stdout.reconfigure(encoding='utf-8')

pages = [
    'index.html', 'home-2.html', 'about.html', 'services.html', 
    'portfolio.html', 'event-planning.html', 'vendors.html', 
    'resources.html', 'contact.html', 'navbar.html'
]

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    has_right = '<!-- RIGHT: ICONS & LOGIN -->' in c
    has_mobile = '<!-- MOBILE MENU -->' in c
    has_mobile_actions = '<div class="mobile-actions">' in c
    print(f"{p}: right_icons={has_right}, mobile_menu={has_mobile}, mobile_actions={has_mobile_actions}")
