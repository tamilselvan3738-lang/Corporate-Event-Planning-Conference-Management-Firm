for fn in ['navbar.html', 'index.html', 'admin-dashboard.html', 'user-dashboard.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"=== {fn} ===")
    for line in c.split('\n'):
        if any(k in line.lower() for k in ['position: sticky', 'position: fixed', '.nav-container', 'header {', '.navbar', '.admin-topbar']):
            print(" ", line.strip()[:140])
