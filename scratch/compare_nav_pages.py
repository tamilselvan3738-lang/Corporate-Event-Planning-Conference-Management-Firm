import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

pages = [
    'index.html', 'home-2.html', 'about.html', 'services.html', 
    'portfolio.html', 'event-planning.html', 'vendors.html', 
    'resources.html', 'contact.html', 'navbar.html'
]

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract desktop nav-links
    m_desk = re.search(r'<ul class="nav-links">(.*?)</ul>', content, re.DOTALL)
    # Extract mobile nav-links
    m_mob = re.search(r'<ul class="mobile-nav-links">(.*?)</ul>', content, re.DOTALL)
    
    desk_len = len(m_desk.group(1)) if m_desk else 0
    mob_len = len(m_mob.group(1)) if m_mob else 0
    print(f"{p}: desk_found={m_desk is not None} ({desk_len} chars), mob_found={m_mob is not None} ({mob_len} chars)")
