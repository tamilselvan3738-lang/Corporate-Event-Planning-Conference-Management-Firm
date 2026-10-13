import subprocess, os, sys

sys.stdout.reconfigure(encoding='utf-8')

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_file = os.path.abspath('index.html')
file_url = f"file:///{html_file.replace(os.sep, '/')}"
out_path = os.path.abspath('scratch/screenshot_375.png')

cmd = [
    chrome_path,
    '--headless=new',
    '--hide-scrollbars',
    '--window-size=375,812',
    f'--screenshot={out_path}',
    file_url
]
res = subprocess.run(cmd, capture_output=True, text=True)
print("Returncode:", res.returncode)
print("File exists:", os.path.exists(out_path))
if os.path.exists(out_path):
    print("File size:", os.path.getsize(out_path))
