import subprocess, os
from PIL import Image

browser = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# 1. Dark Mode Screenshot
out_dark = os.path.abspath('scratch/404_rendered_dark.png')
html_path = os.path.abspath('404.html')
cmd_dark = [
    browser,
    '--headless',
    '--disable-gpu',
    f'--screenshot={out_dark}',
    '--window-size=1280,850',
    f'file:///{html_path}'
]
subprocess.run(cmd_dark, check=True)
print('Dark mode screenshot captured:', os.path.exists(out_dark))

# 2. Light Mode Screenshot
c = open('404.html', encoding='utf-8').read()
c_light = c.replace('<body>', '<body class="light">').replace('id="themeIcon" class="fa-solid fa-sun"', 'id="themeIcon" class="fa-solid fa-moon"')
with open('scratch/404_light_test.html', 'w', encoding='utf-8') as f:
    f.write(c_light)

out_light = os.path.abspath('scratch/404_rendered_light.png')
html_light_path = os.path.abspath('scratch/404_light_test.html')
cmd_light = [
    browser,
    '--headless',
    '--disable-gpu',
    f'--screenshot={out_light}',
    '--window-size=1280,850',
    f'file:///{html_light_path}'
]
subprocess.run(cmd_light, check=True)
print('Light mode screenshot captured:', os.path.exists(out_light))
