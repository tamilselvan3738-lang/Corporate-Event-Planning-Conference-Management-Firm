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
    has_nav_links_css = '.nav-links > li > a' in c
    has_dropdown_item_css = '.dropdown-item' in c
    has_mobile_nav_links_css = '.mobile-nav-links' in c
    print(f"{p}: nav_links_css={has_nav_links_css}, dropdown_item_css={has_dropdown_item_css}, mobile_nav_links_css={has_mobile_nav_links_css}")
