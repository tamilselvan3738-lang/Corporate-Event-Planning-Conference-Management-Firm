import subprocess, os, sys

sys.stdout.reconfigure(encoding='utf-8')

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_file = os.path.abspath('index.html')
file_url = f"file:///{html_file.replace(os.sep, '/')}"

sizes = [
    (375, 812, 'scratch/screenshot_375.png'),
    (320, 600, 'scratch/screenshot_320.png'),
    (480, 800, 'scratch/screenshot_480.png'),
    (768, 1024, 'scratch/screenshot_768.png'),
]

for w, h, out in sizes:
    cmd = [
        chrome_path,
        '--headless=new',
        f'--window-size={w},{h}',
        f'--screenshot={out}',
        '--default-background-color=0',
        file_url
    ]
    subprocess.run(cmd, capture_output=True)
    print(f"Generated {out}: exists={os.path.exists(out)}")
