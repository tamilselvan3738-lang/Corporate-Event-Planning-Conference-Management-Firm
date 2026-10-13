import re

for fn in ['admin-dashboard.html', 'user-dashboard.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"=== {fn} ===")
    matches = re.findall(r'<[^>]*?(?:logo|brand)[^>]*?>', c, re.IGNORECASE)
    for m in matches:
        print(" ", m)
