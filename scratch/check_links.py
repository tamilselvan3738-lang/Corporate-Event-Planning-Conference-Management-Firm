import os, re

for fname in ['index.html', 'navbar.html', 'admin-dashboard.html', 'user-dashboard.html', 'login.html', 'registeration.html', 'registration.html']:
    if os.path.exists(fname):
        c = open(fname, encoding='utf-8').read()
        links = re.findall(r'href=[\'"][^\'"]*(?:login|regist)[^\'"]*[\'"]', c)
        print(f'{fname}: {links}')
