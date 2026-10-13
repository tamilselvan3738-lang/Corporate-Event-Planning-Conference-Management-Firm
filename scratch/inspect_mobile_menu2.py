with open('navbar.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = [m.start() for m in re.finditer(r'\.mobile-menu\s*\{', c)]
for idx in matches:
    print("MATCH:")
    print(c[idx:idx+350])
