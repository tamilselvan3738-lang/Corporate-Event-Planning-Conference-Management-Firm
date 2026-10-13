import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

rules = re.findall(r'([^{}]*(?:hamburger|right-section)[^{}]*\{[^}]*\})', c)
for i, r in enumerate(rules):
    print(f"--- RULE {i+1} ---")
    print(r.strip())
