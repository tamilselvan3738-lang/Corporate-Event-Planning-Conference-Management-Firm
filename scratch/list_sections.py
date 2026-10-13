with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
sections = re.findall(r'<section[^>]*id=[\'"][^\'"]*[\'"][^>]*>', c)
print("Sections in index.html:")
for s in sections:
    print(" ", s)
