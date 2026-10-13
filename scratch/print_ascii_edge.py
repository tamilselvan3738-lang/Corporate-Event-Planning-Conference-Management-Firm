from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

img_path = 'C:/Users/Tamiluuu/.gemini/antigravity/brain/13f4b244-cabb-4cf6-82cd-1983739a963e/.user_uploaded/media_1791863836820_108cb860.png'
im = Image.open(img_path)

for y in range(25, 55):
    line = ""
    for x in range(195, 207):
        p = im.getpixel((x, y))
        if p[0] < 80 and p[1] < 80 and p[2] < 80:
            line += "#"
        else:
            line += "."
    if "#" in line:
        print(f"y={y:2d}: {line}")
