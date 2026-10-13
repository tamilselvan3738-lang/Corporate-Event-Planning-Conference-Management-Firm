import glob, re

files = sorted(glob.glob('*.html'))
print(f"Total HTML files: {len(files)}")

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    has_nav = 'nav-container' in content
    has_mobile_drawer = 'mobile-drawer' in content or 'drawer-nav' in content
    print(f"\n--- {f} (nav-container: {has_nav}, mobile_drawer: {has_mobile_drawer}) ---")
    if has_nav:
        # Extract nav HTML snippet
        nav_match = re.search(r'(<header\b.*?</header>|<nav\b.*?</nav>|\.nav-container\b.*?</div>)', content, re.DOTALL)
        # Find all a tags within nav-links or nav-menu
        links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', content, re.DOTALL)
        nav_related_links = [
            (href, re.sub(r'<[^>]+>', '', text).strip()) 
            for href, text in links 
            if any(k in text.lower() for k in ['home', 'about', 'service', 'planning', 'portfolio', 'resource', 'contact', 'vendor', 'dashboard', 'admin', 'user'])
        ]
        for href, text in nav_related_links[:15]:
            print(f"  [{text}] -> {href}")
