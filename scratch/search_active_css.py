import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in ['index.html', 'navbar.html', 'about.html', 'services.html']:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    print(f"=== {f} ===")
    matches = re.findall(r'([^{}]*nav-link[^{}]*\{[^}]*\})', content)
    for m in matches[:5]:
        print("  ", m.strip().replace('\n', ' '))
    matches2 = re.findall(r'([^{}]*\.active[^{}]*\{[^}]*\})', content)
    for m in matches2[:5]:
        print("  active:", m.strip().replace('\n', ' '))
