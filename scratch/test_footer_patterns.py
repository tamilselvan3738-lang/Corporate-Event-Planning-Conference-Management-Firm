import glob, sys, re
sys.stdout.reconfigure(encoding='utf-8')

pages = [
    'index.html', 'home-2.html', 'about.html', 'services.html', 
    'portfolio.html', 'event-planning.html', 'vendors.html', 
    'resources.html', 'contact.html', 'navbar.html'
]

pattern_footer = r'<!-- COL 2: MAIN NAVIGATION -->(.*?)<!-- COL 3:'

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    m_foot = re.search(pattern_footer, c, re.DOTALL)
    print(f"{p}: footer_nav={m_foot is not None} ({len(m_foot.group(1)) if m_foot else 0})")
