from PIL import Image
import os, sys

sys.stdout.reconfigure(encoding='utf-8')

im = Image.open('scratch/screenshot_375.png')
print("Screenshot size:", im.size)

# Crop the top 120px (the navbar)
nav_crop = im.crop((0, 0, im.width, 120))
nav_crop.save('scratch/nav_crop_375.png')
print("Saved scratch/nav_crop_375.png")

# Also test width 320, 480, 768
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_file = os.path.abspath('index.html')
file_url = f"file:///{html_file.replace(os.sep, '/')}"

import subprocess
for w in [320, 480, 768]:
    out = os.path.abspath(f'scratch/screenshot_{w}.png')
    cmd = [
        chrome_path,
        '--headless=new',
        '--hide-scrollbars',
        f'--window-size={w},800',
        f'--screenshot={out}',
        file_url
    ]
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(out):
        im_w = Image.open(out)
        crop_w = im_w.crop((0, 0, w, 120))
        crop_w.save(f'scratch/nav_crop_{w}.png')
        print(f"Generated nav_crop_{w}.png")
