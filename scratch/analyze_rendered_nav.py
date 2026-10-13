from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

for w in [320, 375, 480, 768]:
    im = Image.open(f'scratch/nav_crop_{w}.png')
    # find bounding box of white pill (pixels near white: >245, >245, >245)
    pill_xs = []
    # find bounding box of hamburger (dark pixels: < 80, < 80, < 80 in right half)
    hamb_pts = []
    
    width, height = im.size
    for x in range(width):
        for y in range(height):
            p = im.getpixel((x, y))
            if p[0] > 248 and p[1] > 248 and p[2] > 248:
                pill_xs.append(x)
            if x > width // 2 and p[0] < 80 and p[1] < 80 and p[2] < 80:
                hamb_pts.append((x, y))

    pill_left = min(pill_xs) if pill_xs else -1
    pill_right = max(pill_xs) if pill_xs else -1
    hamb_left = min(p[0] for p in hamb_pts) if hamb_pts else -1
    hamb_right = max(p[0] for p in hamb_pts) if hamb_pts else -1

    print(f"=== Width {w} ===")
    print(f"  Pill x range: [{pill_left}, {pill_right}] (width={pill_right - pill_left + 1})")
    print(f"  Hamburger x range: [{hamb_left}, {hamb_right}]")
    if hamb_right > pill_right:
        print(f"  --> ALIGNMENT ERROR: Hamburger spills {hamb_right - pill_right}px outside the pill!")
    else:
        margin_right = pill_right - hamb_right
        print(f"  --> Hamburger inside pill, {margin_right}px from right edge.")
