for fn in ['admin-dashboard.html', 'user-dashboard.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    idx = c.find('id="logoutModal"')
    print(f"=== {fn} logoutModal action button ===")
    print(c[idx+550:idx+900])
