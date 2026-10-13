with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('.app-wrapper')
print(c[idx:idx+400])
