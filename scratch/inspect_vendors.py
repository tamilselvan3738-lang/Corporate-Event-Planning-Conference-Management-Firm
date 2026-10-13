import re

with open('vendors.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'<section\s+id="([^"]+)"([^>]*)>', text)
print("Sections in vendors.html:")
for s, attr in sections:
    print(f" - #{s}: {attr.strip()}")

classes = set(re.findall(r'class="([^"]+)"', text))
all_classes = set()
for c in classes:
    for item in c.split():
        if item.startswith('vnd-') or item.startswith('vp-'):
            all_classes.add(item)

print(f"\nTotal custom classes ({len(all_classes)}):")
print(sorted(all_classes)[:40])

for s, _ in sections:
    sec_match = re.search(r'<section\s+id="' + s + r'".*?</section>', text, re.DOTALL)
    if sec_match:
        sec_text = sec_match.group(0)
        grids = re.findall(r'class="([^"]*(?:grid|flex|layout|card|col|deck|matrix|timeline|table|row)[^"]*)"', sec_text)
        print(f"\n--- Section #{s} structural classes ---")
        print(set(grids))
