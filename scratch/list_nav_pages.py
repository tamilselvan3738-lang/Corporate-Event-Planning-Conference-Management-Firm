import glob, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if 'nav-container' in content:
        # Check if .active style exists in style tag
        has_nav_active_style = 'nav-links' in content and '.active' in content
        print(f"{f}: has_nav=True, has_nav_active_style={has_nav_active_style}")
