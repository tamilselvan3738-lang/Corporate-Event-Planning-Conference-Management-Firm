import re

for fn in ['index.html', 'navbar.html', 'admin-dashboard.html', 'user-dashboard.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"=== {fn} ===")
    logos = re.findall(r'<a[^>]*?(?:logo|brand)[^>]*?>.*?</a>', c, re.DOTALL | re.IGNORECASE)
    for l in logos[:2]:
        print("  LOGO LINK:", l[:200].replace('\n', ' '))
