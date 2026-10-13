import os, re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for fn in sorted(html_files):
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    # Search for login/logout buttons or links
    # Look for button or a tags containing login or logout
    pattern = re.compile(r'(<(?:a|button)[^>]*?>[\s\S]*?(?:log\s*in|log\s*out|sign\s*in|sign\s*out)[\s\S]*?</(?:a|button)>)', re.IGNORECASE)
    matches = pattern.findall(c)

    # Also search for IDs or classes containing login or logout
    id_pattern = re.compile(r'(<(?:a|button)[^>]*?(?:id|class)=[\'"][^\'"]*?(?:login|logout)[^\'"]*?[\'"][^>]*?>)', re.IGNORECASE)
    id_matches = id_pattern.findall(c)

    print(f"=== {fn} ===")
    seen = set()
    for m in matches + id_matches:
        clean = re.sub(r'\s+', ' ', m)[:150].strip()
        if clean not in seen:
            seen.add(clean)
            print(f"  {clean}")
