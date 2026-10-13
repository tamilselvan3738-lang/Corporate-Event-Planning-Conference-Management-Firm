with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'mobile-dropdown-toggle' in l or 'hamburger' in l or 'mobileMenu' in l:
        print(f"{i+1}: {l.strip()}")
