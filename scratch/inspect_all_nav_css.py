with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's inspect all styles affecting nav-container, header, and app-wrapper
import re
css_blocks = re.findall(r'(\.[a-zA-Z0-9_-]+\s*\{[^}]+\})', c)
for b in css_blocks:
    if any(k in b for k in ['nav-container', 'app-wrapper', 'body {', 'html, body']):
        print("CSS BLOCK:")
        print(b[:250])
        print("---")
