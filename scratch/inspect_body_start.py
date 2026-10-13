with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('<body')
print(c[idx:idx+800].encode('ascii', errors='replace').decode('ascii'))
