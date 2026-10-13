import re

with open('about.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'<section\s+[^>]*id="([^"]+)"', text)
print("Sections in about.html:", sections)

imgs = re.findall(r'<img[^>]+src="([^"]+)"', text)
print("\nImages in about.html:", imgs)

framer = sorted(set(re.findall(r'framer-[a-zA-Z0-9\-]+', text)))
print("\nFramer classes in about.html:", framer)

for s in sections:
    m = re.search(r'<section[^>]*id="' + s + r'".*?</section>', text, re.DOTALL)
    if m:
        sec = m.group(0)
        lines = len(sec.splitlines())
        classes = set()
        for c in re.findall(r'class="([^"]+)"', sec):
            for part in c.split():
                if part.startswith('abt-') or part.startswith('about-'):
                    classes.add(part)
        print(f"\n=== Section #{s} ({lines} lines) ===")
        print(f"Classes: {sorted(classes)}")

