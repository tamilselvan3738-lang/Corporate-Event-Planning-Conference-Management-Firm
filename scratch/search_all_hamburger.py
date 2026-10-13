import glob, sys

sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    lines = content.split('\n')
    for i, l in enumerate(lines):
        if '.hamburger' in l or 'hamburgerBtn' in l or 'hamburger-btn' in l:
            print(f"{f}:{i+1} -> {l.strip()}")
