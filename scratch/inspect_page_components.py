import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    grids = set(re.findall(r'class="([^"]*grid[^"]*)"', content))
    cards = set(re.findall(r'class="([^"]*card[^"]*)"', content))
    sections = set(re.findall(r'<section\s+[^>]*class="([^"]*)"', content))
    print(f"=== {f} ===")
    print(f"  Sections ({len(sections)}): {list(sections)[:3]}")
    print(f"  Grids ({len(grids)}): {list(grids)[:4]}")
    print(f"  Cards ({len(cards)}): {list(cards)[:4]}")
