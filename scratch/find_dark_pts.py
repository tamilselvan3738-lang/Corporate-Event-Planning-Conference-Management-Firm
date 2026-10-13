from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

img_path = 'C:/Users/Tamiluuu/.gemini/antigravity/brain/13f4b244-cabb-4cf6-82cd-1983739a963e/.user_uploaded/media_1791863836820_108cb860.png'
im = Image.open(img_path)
w, h = im.size

dark_pts = []
for x in range(150, w):
    for y in range(h):
        p = im.getpixel((x, y))
        # if dark line
        if p[0] < 80 and p[1] < 80 and p[2] < 80 and p[3] > 200:
            dark_pts.append((x, y))

if dark_pts:
    min_x = min(pt[0] for pt in dark_pts)
    max_x = max(pt[0] for pt in dark_pts)
    min_y = min(pt[1] for pt in dark_pts)
    max_y = max(pt[1] for pt in dark_pts)
    print(f"Dark pixels found between x=[{min_x}, {max_x}] and y=[{min_y}, {max_y}]")
    print(f"Total dark pixels: {len(dark_pts)}")
else:
    print("No dark pixels in x >= 150")
