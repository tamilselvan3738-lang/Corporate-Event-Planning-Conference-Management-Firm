import os, re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for fn in sorted(html_files):
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    # Search for logo or brand
    matches = re.findall(r'<a[^>]*?(?:href=[^>]*?)?>[\s\S]*?(?:EventSphere|logo|brand)[\s\S]*?</a>', c, re.IGNORECASE)
    print(f"=== {fn} ===")
    found = False
    for m in matches:
        if 'EventSphere' in m or 'logo' in m.lower():
            # print first 150 chars of opening tag and content
            tag = m.split('>')[0] + '>'
            text_snippet = re.sub(r'\s+', ' ', m)[:100]
            print(f"  TAG: {tag} | SNIPPET: {text_snippet}")
            found = True
            break
    if not found:
        print("  NO LOGO LINK FOUND")
