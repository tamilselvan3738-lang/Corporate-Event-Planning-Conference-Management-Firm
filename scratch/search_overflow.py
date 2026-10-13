with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'[^{};]*overflow[^{};]*:[^;]+;', c)
for m in matches:
    print(m.strip())
