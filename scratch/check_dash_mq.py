import re, sys

sys.stdout.reconfigure(encoding='utf-8')

for f in ['admin-dashboard.html', 'user-dashboard.html']:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    mqs = re.findall(r'@media[^{]+\{', content)
    print(f"=== {f} ===")
    for mq in mqs:
        print(" ", mq.strip())
