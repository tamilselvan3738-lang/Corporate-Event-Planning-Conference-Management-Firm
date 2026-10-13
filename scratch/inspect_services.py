import re

with open('services.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of services.html:", len(text))
sections = re.findall(r'<section\s+[^>]*id="([^"]+)"', text)
print("Sections in services.html:", sections)
imgs = re.findall(r'<img[^>]+src="([^"]+)"', text)
print("Images in services.html:", imgs)

framer = sorted(set(re.findall(r'framer-[a-zA-Z0-9\-]+', text)))
print("Framer classes in services.html:", framer)
