from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

im = Image.open('scratch/nav_crop_real.png')
w, h = im.size

non_white_right = []
for y in range(h):
    for x in range(250, w):
        p = im.getpixel((x, y))
        # if not background blue and not white
        if not (p[0] > 220 and p[1] > 230 and p[2] > 240):
            non_white_right.append((x, y, p))

print(f"Non-white/background pixels in x >= 250: count={len(non_white_right)}")
for pt in non_white_right[:10]:
    print(f"  x={pt[0]}, y={pt[1]}: RGB={pt[2][:3]}")
