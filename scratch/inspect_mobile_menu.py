with open('navbar.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('.mobile-menu {')
print(c[idx:idx+400])
