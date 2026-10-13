with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('<footer')
if idx != -1:
    print(c[idx+1000:idx+2000].encode('ascii', errors='replace').decode('ascii'))
