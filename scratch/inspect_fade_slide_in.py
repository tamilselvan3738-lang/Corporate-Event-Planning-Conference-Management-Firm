with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('fadeSlideIn')
print(c[idx-50:idx+350])
