import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

files = sorted(glob.glob('*.html'))
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    has_nav = 'class="nav-container"' in content or "class='nav-container'" in content
    has_active_css = '.active' in content
    print(f"=== {f} ===")
    print(f"  has .nav-container: {has_nav}")
    # find any .active styling related to nav
    nav_active_styles = re.findall(r'(\.nav-links[^{]*\.active[^{]*\{[^}]*\})', content)
    if nav_active_styles:
        print(f"  nav active styles: {nav_active_styles}")
    else:
        # search for any nav active
        gen_active = re.findall(r'([^{}]*nav[^{}]*active[^{]*\{[^}]*\})', content, re.IGNORECASE)
        print(f"  general nav active styles: {gen_active[:2]}")
