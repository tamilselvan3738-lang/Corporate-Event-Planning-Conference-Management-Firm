import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('about.html', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'<nav class="nav-container">(.*?)</nav>', c, re.DOTALL)
if m:
    print("Full nav-container in about.html:")
    print(m.group(1))
