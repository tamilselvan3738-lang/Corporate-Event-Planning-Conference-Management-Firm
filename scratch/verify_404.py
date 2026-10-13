with open('404.html', 'r', encoding='utf-8') as f:
    c = f.read()

assert 'id="particlesCanvas"' in c
assert 'btn-3d-switch' in c
assert 'fa-solid fa-sun' in c
assert 'fa-solid fa-right-left' in c
assert 'toggleTheme()' in c
assert 'toggleRTL()' in c
assert 'index.html' in c
assert 'login.html' in c
print('Verified! 404.html is ready and clean. File length:', len(c))
