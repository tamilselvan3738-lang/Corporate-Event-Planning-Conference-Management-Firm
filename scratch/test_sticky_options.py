import subprocess, os

c = open('index.html', encoding='utf-8').read()

# Let's test Option A:
# In app-wrapper: remove justify-content: space-between (which can mess with flex item positions)
# And make nav-container sticky
opt_a = c.replace('overflow-x: hidden;', 'overflow-x: clip;')
opt_a = opt_a.replace(
    'justify-content: space-between;',
    '/* justify-content: space-between; */'
)
opt_a = opt_a.replace(
    '.nav-container {\n      display: flex;',
    '.nav-container {\n      position: -webkit-sticky !important;\n      position: sticky !important;\n      top: 1rem !important;\n      z-index: 1000 !important;\n      display: flex;'
)

# Inject scroll
scroll_js = '''
<script>
window.addEventListener('load', () => {
  setTimeout(() => {
    window.scrollTo(0, 1200);
  }, 100);
});
</script>
'''
opt_a = opt_a.replace('</body>', scroll_js + '</body>')

with open('scratch/opt_a.html', 'w', encoding='utf-8') as f:
    f.write(opt_a)

browser = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
cmd = [
    browser,
    '--headless',
    '--disable-gpu',
    f'--screenshot={os.path.abspath("scratch/opt_a.png")}',
    '--window-size=1280,800',
    f'file:///{os.path.abspath("scratch/opt_a.html")}'
]
subprocess.run(cmd, check=True)
print("Opt A screenshot created")
