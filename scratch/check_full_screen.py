from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

for w in [320, 375, 480]:
    im = Image.open(f'scratch/screenshot_{w}.png')
    print(f"=== Width {w} total image size: {im.size} ===")
    # Look for dark pixels with y between 10 and 60
    dark_xs = []
    for x in range(im.size[0]):
        for y in range(10, 60):
            p = im.getpixel((x, y))
            if p[0] < 80 and p[1] < 80 and p[2] < 80:
                dark_xs.append((x, y))
    
    if dark_xs:
        # group into left (logo/text) and right (hamburger)
        right_dark = [pt for pt in dark_xs if pt[0] > 120]
        print(f"  Dark points found in y=[10,60]: total={len(dark_xs)}, in x>120: {len(right_dark)}")
        if right_dark:
            print(f"  Right dark x range: [{min(p[0] for p in right_dark)}, {max(p[0] for p in right_dark)}]")
        else:
            print("  NO dark pixels found in x > 120!")
