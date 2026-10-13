with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
idx = c.find('<div class="app-wrapper">')
# Find tags directly inside app-wrapper
sub = c[idx:idx+3000]
print(sub[:1500].encode('ascii', errors='replace').decode('ascii'))
