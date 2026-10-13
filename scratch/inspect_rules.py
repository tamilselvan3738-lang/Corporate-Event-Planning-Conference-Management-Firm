with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re

# find all css blocks mentioning hamburger or right-section
rules = re.findall(r'([^{}]*(?:hamburger|right-section)[^{}]*\{[^}]*\})', c)
for r in rules:
    print("--- RULE ---")
    print(r.strip())
