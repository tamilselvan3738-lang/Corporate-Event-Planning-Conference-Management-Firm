with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'<button[^>]*theme[^>]*>.*?</button>', c, re.DOTALL | re.IGNORECASE)
for m in matches:
    print('BUTTON:', m)

# Also check admin-dashboard.html and user-dashboard.html
for fn in ['admin-dashboard.html', 'user-dashboard.html']:
    c2 = open(fn, encoding='utf-8').read()
    m2 = re.findall(r'<button[^>]*theme[^>]*>.*?</button>', c2, re.DOTALL | re.IGNORECASE)
    print(f'{fn} BUTTONS:', m2[:2])
