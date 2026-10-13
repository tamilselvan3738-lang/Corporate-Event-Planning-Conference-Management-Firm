pages = ['index.html', 'navbar.html', 'home-2.html', 'about.html', 'services.html', 'contact.html', 'event-planning.html', 'portfolio.html', 'resources.html', 'vendors.html']

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    idx = c.find('.nav-container {')
    print(f"=== {p} ===")
    if idx != -1:
        print(c[idx:idx+250].replace('\n', ' '))
    else:
        print("  NO .nav-container { found!")
