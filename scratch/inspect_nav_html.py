with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('nav-container')
print("HTML around nav-container in index.html:")
print(c[idx-200:idx+400].encode('ascii', errors='replace').decode('ascii'))
