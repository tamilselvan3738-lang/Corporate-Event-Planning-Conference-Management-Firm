from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

im = Image.open('scratch/screenshot_375.png')
w, h = im.size

print("Sampling y every 10 pixels:")
for y in range(0, 300, 10):
    colors = [im.getpixel((x, y))[:3] for x in [10, 50, 100, 200, 300, 360]]
    print(f"y={y:3d}: x=10:{colors[0]}, x=50:{colors[1]}, x=100:{colors[2]}, x=360:{colors[5]}")
