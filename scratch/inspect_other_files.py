import glob, sys
sys.stdout.reconfigure(encoding='utf-8')

other_files = ['admin-dashboard.html', 'user-dashboard.html', 'login.html', 'registeration.html', 'registration.html', '404.html']
for f in other_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    print(f"=== {f} ===")
    lines = content.split('\n')
    header_lines = [line.strip() for line in lines if '<header' in line or '<nav' in line or 'class="topbar"' in line or 'class="top-bar"' in line or 'navbar' in line.lower()]
    print(f"  matching lines ({len(header_lines)}): {header_lines[:5]}")
