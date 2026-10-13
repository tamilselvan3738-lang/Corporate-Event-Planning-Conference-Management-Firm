with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('<footer')
if idx != -1:
    print(c[idx:idx+1000].encode('ascii', errors='replace').decode('ascii'))
