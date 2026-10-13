with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="mobileMenu"')
idx2 = c.find('</div>', idx)
print(c[idx2:idx2+1000].encode('ascii', errors='replace').decode('ascii'))
