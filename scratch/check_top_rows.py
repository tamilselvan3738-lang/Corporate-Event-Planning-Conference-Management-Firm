from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

im = Image.open('scratch/screenshot_375.png')
w, h = im.size

print("Checking rows y=35 to y=85:")
for y in range(35, 85, 2):
    xs = [x for x in range(w) if im.getpixel((x, y))[0] < 80 and im.getpixel((x, y))[1] < 80 and im.getpixel((x, y))[2] < 80]
    if xs:
        print(f"y={y:2d}: count={len(xs)}, min_x={min(xs)}, max_x={max(xs)}")
