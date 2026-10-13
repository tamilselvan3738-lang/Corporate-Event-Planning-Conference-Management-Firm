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
    print(f"{p}: has '/* ===== RIGHT SECTION ===== */': {'/* ===== RIGHT SECTION ===== */' in c}")
