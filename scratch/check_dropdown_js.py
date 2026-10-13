import glob, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in ['index.html', 'navbar.html', 'about.html']:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    print(f"=== {f} ===")
    if 'dropdown-toggle' in content:
        lines = [line.strip() for line in content.split('\n') if 'dropdown-toggle' in line]
        print(f"  dropdown-toggle occurrences: {len(lines)}")
        for l in lines:
            print("   ", l[:120])
