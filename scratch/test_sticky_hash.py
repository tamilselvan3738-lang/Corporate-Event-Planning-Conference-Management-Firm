import subprocess, os

browser = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
out_path = os.path.abspath('scratch/sticky_hash_rendered.png')
html_path = os.path.abspath('scratch/test_sticky_page.html')

cmd = [
    browser,
    '--headless',
    '--disable-gpu',
    f'--screenshot={out_path}',
    '--window-size=1280,800',
    f'file:///{html_path}#featured-venues'
]
subprocess.run(cmd, check=True)
print("Hash screenshot generated:", os.path.exists(out_path))
