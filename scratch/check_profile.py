from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

img_path = 'C:/Users/Tamiluuu/.gemini/antigravity/brain/13f4b244-cabb-4cf6-82cd-1983739a963e/.user_uploaded/media_1791863836820_108cb860.png'
im = Image.open(img_path)
w, h = im.size

# Let's check where the white pill is:
# The background is light blue #f0f4fe (~ 240, 244, 254).
# The white pill is pure white 255, 255, 255.
for x in range(0, w, 10):
    p = im.getpixel((x, 40))
    print(f"x={x:3d}: RGB={p[:3]}")
