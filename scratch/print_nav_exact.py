import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

print('=== DESK NAV ===')
print(re.search(r'<ul class="nav-links">(.*?)</ul>', c, re.DOTALL).group(1))
print('=== MOB NAV ===')
print(re.search(r'<ul class="mobile-nav-links">(.*?)</ul>', c, re.DOTALL).group(1))
