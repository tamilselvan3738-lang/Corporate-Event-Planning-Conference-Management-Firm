import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

print('Title:', re.findall(r'<title>(.*?)</title>', c))
print('Fonts:', re.findall(r'href=[\'"](https://fonts\.googleapis\.com[^\'"]+)[\'"]', c))
print('CSS links:', re.findall(r'href=[\'"]([^\'"]+\.css[^\'"]*)[\'"]', c))

# Let's inspect the logo HTML in navbar.html or index.html
with open('navbar.html', 'r', encoding='utf-8') as f:
    nav = f.read()

logo_start = nav.find('<!-- LEFT: LOGO')
if logo_start != -1:
    print('Navbar Logo snippet:\n', nav[logo_start:logo_start+1200].encode('ascii', 'replace').decode('ascii'))

# Inspect primary theme colors in navbar.html
print('\nRoot CSS variables in navbar.html:')
root_start = nav.find(':root {')
if root_start != -1:
    print(nav[root_start:root_start+800].encode('ascii', 'replace').decode('ascii'))

