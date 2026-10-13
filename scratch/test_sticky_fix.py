import subprocess, os

c = open('index.html', encoding='utf-8').read()

# 1. Update overflow-x to clip
c = c.replace('overflow-x: hidden;', 'overflow-x: clip;')

# 2. Update .nav-container position to sticky
old_nav_css = '''.nav-container {
      display: flex;'''
new_nav_css = '''.nav-container {
      position: sticky !important;
      top: 1rem !important;
      z-index: 1000 !important;
      display: flex;'''
assert old_nav_css in c, "old_nav_css not found"
c = c.replace(old_nav_css, new_nav_css)

# Inject scroll down by adding window.addEventListener('DOMContentLoaded', () => window.scrollTo(0, 600))
scroll_script = '''
<script>
window.addEventListener('load', () => {
  window.scrollTo(0, 700);
});
</script>
'''
c = c.replace('</body>', scroll_script + '</body>')

with open('scratch/test_sticky_page.html', 'w', encoding='utf-8') as f:
    f.write(c)

browser = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
out_path = os.path.abspath('scratch/test_sticky_page.png')
html_path = os.path.abspath('scratch/test_sticky_page.html')

cmd = [
    browser,
    '--headless',
    '--disable-gpu',
    f'--screenshot={out_path}',
    '--window-size=1280,800',
    f'file:///{html_path}'
]
subprocess.run(cmd, check=True)
print("Test sticky screenshot generated:", os.path.exists(out_path))
