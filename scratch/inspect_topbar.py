with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos1 = c.find('class="topbar-search"')
pos2 = c.find('<!-- Hamburger')
print(c[pos1-12:pos2])
