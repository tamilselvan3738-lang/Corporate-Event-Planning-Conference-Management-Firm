import subprocess, os, json, sys

sys.stdout.reconfigure(encoding='utf-8')

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_file = os.path.abspath('index.html')
file_url = f"file:///{html_file.replace(os.sep, '/')}"

test_html = os.path.abspath('scratch/debug_nav.html')

# We can create a test page that logs getBoundingClientRect() to console
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

debug_script = """
<script>
window.addEventListener('load', () => {
  const nav = document.querySelector('.nav-container');
  const logo = document.querySelector('.logo-section');
  const right = document.querySelector('.right-section');
  const hamb = document.getElementById('hamburgerBtn');
  const navLinks = document.querySelector('.nav-links');

  const info = {
    window: { width: window.innerWidth, height: window.innerHeight },
    nav: nav ? nav.getBoundingClientRect() : null,
    logo: logo ? logo.getBoundingClientRect() : null,
    right: right ? right.getBoundingClientRect() : null,
    hamb: hamb ? hamb.getBoundingClientRect() : null,
    hamb_style: hamb ? {
      display: getComputedStyle(hamb).display,
      visibility: getComputedStyle(hamb).visibility,
      opacity: getComputedStyle(hamb).opacity,
      width: getComputedStyle(hamb).width,
      height: getComputedStyle(hamb).height,
      position: getComputedStyle(hamb).position
    } : null,
    nav_links_display: navLinks ? getComputedStyle(navLinks).display : null
  };
  console.log('NAV_DEBUG_START' + JSON.stringify(info) + 'NAV_DEBUG_END');
  document.title = 'NAV_DEBUG_START' + JSON.stringify(info) + 'NAV_DEBUG_END';
});
</script>
"""

content = content.replace('</body>', debug_script + '</body>')
with open(test_html, 'w', encoding='utf-8') as f:
    f.write(content)

test_url = f"file:///{test_html.replace(os.sep, '/')}"

for w in [320, 375, 480, 768, 1024]:
    cmd = [
        chrome_path,
        '--headless=new',
        f'--window-size={w},800',
        '--dump-dom',
        test_url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if 'NAV_DEBUG_START' in res.stdout:
        info_json = res.stdout.split('NAV_DEBUG_START')[1].split('NAV_DEBUG_END')[0]
        data = json.loads(info_json)
        print(f"\n=== Viewport {w}px ===")
        print("  Nav rect:", data['nav'])
        print("  Logo rect:", data['logo'])
        print("  Right rect:", data['right'])
        print("  Hamb rect:", data['hamb'])
        print("  Hamb style:", data['hamb_style'])
        print("  Nav links display:", data['nav_links_display'])
