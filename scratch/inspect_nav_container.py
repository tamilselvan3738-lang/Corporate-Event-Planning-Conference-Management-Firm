with open('navbar.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
idx = c.find('.nav-container {')
print(c[idx:idx+500])
