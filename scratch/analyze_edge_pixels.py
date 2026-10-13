from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

img_path = 'C:/Users/Tamiluuu/.gemini/antigravity/brain/13f4b244-cabb-4cf6-82cd-1983739a963e/.user_uploaded/media_1791863836820_108cb860.png'
im = Image.open(img_path)
w, h = im.size

# Let's inspect the rightmost 30 pixels across all rows
print(f"Image width: {w}, height: {h}")

# Check right edge pixels
right_pixels = [im.getpixel((w - 5, y)) for y in range(0, h, 5)]
print("Right edge (-5px) sample colors:")
for y, p in zip(range(0, h, 5), right_pixels):
    if p[3] > 0 and (p[0] < 50 and p[1] < 50 and p[2] < 50):
        print(f"  Dark pixel at y={y}: {p}")
