with open('about.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
m = re.search(r'<ul class="nav-links">(.*?)</ul>', c, re.DOTALL)
if m:
    print("about.html nav-links:")
    print(m.group(1))
