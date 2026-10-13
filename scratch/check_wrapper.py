with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# find where app-wrapper closes
# does it close at the bottom before </body>?
print("Index of <div class=\"app-wrapper\">:", c.find('<div class="app-wrapper">'))
print("Index of footer:", c.find('<footer'))
print("Index of </body>:", c.find('</body>'))
print("End of file snippet:")
print(c[-500:].encode('ascii', errors='replace').decode('ascii'))
