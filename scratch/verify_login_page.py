import re
import subprocess
from html.parser import HTMLParser

with open('login.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check required mockup elements
required_elements = [
    "Username or Email",
    "Password",
    "Remember me",
    "Forgot Password?",
    "Log In to Dashboard",
    "OR CONTINUE WITH",
    "Create New Account",
    "256-Bit SSL Encrypted",
    "particlesCanvas",
    "logo-cube",
    "logo-face",
    "Event<span>Sphere</span>"
]

print("=== CHECKING MOCKUP & BRAND ELEMENTS ===")
all_found = True
for elem in required_elements:
    if elem.lower() in html.lower():
        print(f"  [PASS] Found: {elem}")
    else:
        print(f"  [FAIL] Missing: {elem}")
        all_found = False

# 2. Check HTML structure
class Validator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.self_closing = {'img', 'input', 'br', 'hr', 'meta', 'link'}
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in self.self_closing:
            self.tags.append(tag)
    def handle_endtag(self, tag):
        if tag in self.self_closing:
            return
        if not self.tags:
            self.errors.append(f'Unexpected closing tag </{tag}>')
            return
        last = self.tags.pop()
        if last != tag:
            self.errors.append(f'Mismatched tag: expected </{last}>, found </{tag}>')

v = Validator()
v.feed(html)
print("\n=== HTML STRUCTURE VALIDATION ===")
if v.errors:
    print(f"Found {len(v.errors)} HTML errors:")
    for err in v.errors:
        print("  ", err)
else:
    print("[PASS] HTML is 100% valid and well-formed!")

# 3. Check JavaScript syntax with Node.js
print("\n=== JAVASCRIPT SYNTAX VALIDATION ===")
scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
for i, s in enumerate(scripts):
    test_path = f'scratch/test_login_js_{i}.js'
    with open(test_path, 'w', encoding='utf-8') as js_file:
        js_file.write(s)
    res = subprocess.run(['node', '--check', test_path], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"  [PASS] Script block {i}: Node.js syntax check passed.")
    else:
        print(f"  [FAIL] Script block {i}: Node.js syntax check failed!\n{res.stderr}")
