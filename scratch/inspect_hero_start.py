with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('<!-- HERO SECTION')
if idx == -1:
    idx = c.find('Engineering Masterclass')
print(c[idx-300:idx+300].encode('ascii', errors='replace').decode('ascii'))
