for fn in ['admin-dashboard.html', 'user-dashboard.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"=== {fn} ===")
    for line in c.split('\n'):
        if 'logout' in line.lower() or 'sign-out' in line.lower():
            print(" ", line.strip()[:140])
