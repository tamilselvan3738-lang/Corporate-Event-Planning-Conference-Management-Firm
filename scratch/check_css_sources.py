import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    styles = re.findall(r'<style\b[^>]*>(.*?)</style>', content, re.DOTALL)
    links_css = re.findall(r'<link\s+[^>]*rel=["\']stylesheet["\'][^>]*href=["\']([^"\']*)["\']', content)
    print(f"{f}: {len(styles)} style tags (total {sum(len(s) for s in styles)} chars), css links: {links_css}")
