with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('footer')
if idx != -1:
    footer_text = c[idx:idx+2500]
    import re
    logos = re.findall(r'<[^>]*logo[^>]*>[\s\S]*?</[^>]*>', footer_text, re.IGNORECASE)
    for l in logos:
        print("FOOTER LOGO:", l[:150].replace('\n', ' '))
else:
    print("No footer found")
