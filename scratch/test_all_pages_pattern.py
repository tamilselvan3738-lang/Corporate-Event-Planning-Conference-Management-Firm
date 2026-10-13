import glob, sys, re
sys.stdout.reconfigure(encoding='utf-8')

pages = [
    'index.html', 'home-2.html', 'about.html', 'services.html', 
    'portfolio.html', 'event-planning.html', 'vendors.html', 
    'resources.html', 'contact.html', 'navbar.html'
]

pattern_desk = r'<!-- CENTER: DESKTOP NAV LINKS -->(.*?)<!-- RIGHT: ICONS & LOGIN -->'
pattern_mob = r'<!-- MOBILE MENU -->(.*?)<div class="mobile-actions">'

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    m_desk = re.search(pattern_desk, c, re.DOTALL)
    m_mob = re.search(pattern_mob, c, re.DOTALL)
    print(f"{p}: desk={m_desk is not None} ({len(m_desk.group(1)) if m_desk else 0}), mob={m_mob is not None} ({len(m_mob.group(1)) if m_mob else 0})")
