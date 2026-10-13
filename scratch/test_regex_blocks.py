import glob, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pattern = r'<!-- CENTER: DESKTOP NAV LINKS -->(.*?)<!-- RIGHT: ICONS & LOGIN -->'
m = re.search(pattern, c, re.DOTALL)
if m:
    print("Found desktop nav block! Length:", len(m.group(1)))
    print(m.group(1)[:300])

mob_pattern = r'<!-- MOBILE MENU -->(.*?)<div class="mobile-actions">'
m2 = re.search(mob_pattern, c, re.DOTALL)
if m2:
    print("Found mobile nav block! Length:", len(m2.group(1)))
    print(m2.group(1)[:300])
