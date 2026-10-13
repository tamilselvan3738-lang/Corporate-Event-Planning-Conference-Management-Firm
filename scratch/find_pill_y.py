from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

im = Image.open('scratch/screenshot_375.png')
w, h = im.size

# Find white pill y range
pill_ys = []
for y in range(h):
    # sample x=100
    p = im.getpixel((100, y))
    if p[0] > 248 and p[1] > 248 and p[2] > 248:
        pill_ys.append(y)

if pill_ys:
    print(f"Pill y range at x=100: [{min(pill_ys)}, {max(pill_ys)}]")

# Now let's find ANY dark pixels inside this y range
if pill_ys:
    min_y = min(pill_ys)
    max_y = max(pill_ys)
    dark_pts = []
    for x in range(w):
        for y in range(min_y, max_y + 1):
            p = im.getpixel((x, y))
            if p[0] < 80 and p[1] < 80 and p[2] < 80:
                dark_pts.append((x, y))
    print(f"Dark pixels in pill: total={len(dark_pts)}")
    if dark_pts:
        print(f"Dark x range: [{min(p[0] for p in dark_pts)}, {max(p[0] for p in dark_pts)}]")
        right_pts = [p for p in dark_pts if p[0] > 200]
        if right_pts:
            print(f"Right pts x range: [{min(p[0] for p in right_pts)}, {max(p[0] for p in right_pts)}]")
        else:
            print("No dark pixels with x > 200")
