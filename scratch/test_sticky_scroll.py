import subprocess, os

# Create a test version of index.html with sticky navbar
c = open('index.html', encoding='utf-8').read()

# Replace overflow-x: hidden on body
c_test = c.replace('overflow-x: hidden;', 'overflow-x: clip;')
# Replace nav-container position: relative with sticky
c_test = c_test.replace(
    '.nav-container {\n      display: flex;',
    '.nav-container {\n      position: sticky !important;\n      top: 1rem !important;\n      z-index: 1000 !important;\n      display: flex;'
)

with open('scratch/test_sticky_index.html', 'w', encoding='utf-8') as f:
    f.write(c_test)

browser = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html_path = os.path.abspath('scratch/test_sticky_index.html')

# We can run edge with a script to scroll down
# Or use python with a simple injected script that scrolls before screenshot
script_to_scroll = '''
window.scrollTo(0, 1000);
'''
c_scrolled = c_test.replace('</body>', f'<script>{script_to_scroll}</script></body>')
with open('scratch/test_sticky_scrolled.html', 'w', encoding='utf-8') as f:
    f.write(c_scrolled)

out_path = os.path.abspath('scratch/sticky_scrolled_rendered.png')
html_scrolled_path = os.path.abspath('scratch/test_sticky_scrolled.html')

cmd = [
    browser,
    '--headless',
    '--disable-gpu',
    f'--screenshot={out_path}',
    '--window-size=1280,800',
    f'file:///{html_scrolled_path}'
]
subprocess.run(cmd, check=True)
print("Scrolled screenshot created:", os.path.exists(out_path))
