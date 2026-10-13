import os, re, glob
from PIL import Image

def analyze():
    pages = sorted(glob.glob('*.html'))
    print(f"Found pages: {pages}")
    for p in pages:
        with open(p, 'r', encoding='utf-8') as f:
            txt = f.read()
        sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', txt)
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', txt)
        framer = sorted(set(re.findall(r'framer-[a-zA-Z0-9\-]+', txt)))
        print(f"\n==================== {p} ====================")
        print(f"Sections ({len(sections)}): {sections}")
        print(f"Images ({len(imgs)}): {imgs}")
        print(f"Framer classes: {framer}")

if __name__ == '__main__':
    analyze()
