with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Engineering Masterclass')
print(c[idx-800:idx].encode('ascii', errors='replace').decode('ascii'))
