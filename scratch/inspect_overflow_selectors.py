with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'([^}]*\{[^}]*overflow[^}]*\})', c)
for m in matches:
    selector = m.split('{')[0].strip()
    ov_lines = [l.strip() for l in m.split('{')[1].split(';') if 'overflow' in l]
    print(f"SELECTOR: {selector} => {ov_lines}")
