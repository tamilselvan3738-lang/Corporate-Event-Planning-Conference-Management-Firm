with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
for m in re.finditer(r'fa-(?:sun|moon)', c):
    idx = m.start()
    print('FOUND:', c[idx-60:idx+80])
