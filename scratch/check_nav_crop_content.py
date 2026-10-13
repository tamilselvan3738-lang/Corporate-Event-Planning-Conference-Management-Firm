from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

im = Image.open('scratch/nav_crop_real.png')
w, h = im.size

# Check what x coordinates have non-white, non-background pixels
for y in range(0, h, 10):
    colored_xs = [x for x in range(w) if not (im.getpixel((x,y))[0] > 240 and im.getpixel((x,y))[1] > 240 and im.getpixel((x,y))[2] > 240)]
    if colored_xs:
        print(f"y={y:3d} (abs y={y+30}): min_x={min(colored_xs)}, max_x={max(colored_xs)}, count={len(colored_xs)}")
