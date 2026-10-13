with open('navbar.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('<nav')
if idx != -1:
    print("NAV IN navbar.html:")
    print(c[idx:idx+800].encode('ascii', errors='replace').decode('ascii'))
