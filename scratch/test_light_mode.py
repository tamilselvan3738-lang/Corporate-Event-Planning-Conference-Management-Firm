import subprocess, os
from PIL import Image

c = open('login.html', encoding='utf-8').read()
c_light = c.replace('<body>', '<body class="light">').replace('id="themeIcon" class="fa-solid fa-sun"', 'id="themeIcon" class="fa-solid fa-moon"')
with open('scratch/login_light_test.html', 'w', encoding='utf-8') as f:
    f.write(c_light)

browser = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
out_path = os.path.abspath('scratch/login_light_rendered.png')
html_path = os.path.abspath('scratch/login_light_test.html')
cmd = [
    browser,
    '--headless',
    '--disable-gpu',
    f'--screenshot={out_path}',
    '--window-size=1280,800',
    f'file:///{html_path}'
]
subprocess.run(cmd, check=True)

im = Image.open(out_path)
w, h = im.size
crop = im.crop((w - 180, 0, w, 100))
crop.save('scratch/login_light_top.png')
print('Light mode test completed!')
