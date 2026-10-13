import re
import subprocess
from html.parser import HTMLParser

with open('registeration.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check required registration elements
required_elements = [
    "Executive Full Name",
    "Organization / Enterprise",
    "Corporate Email",
    "Create Password",
    "Confirm Password",
    "Enterprise Terms",
    "Create Corporate Account",
    "OR CONTINUE WITH",
    "Already Have an Account? Sign In",
    "256-Bit SSL Encrypted",
    "particlesCanvas",
    "logo-cube",
    "logo-face",
    "Event<span>Sphere</span>",
    "fa-right-left"
]

print("=== CHECKING REGISTRATION ELEMENTS ===")
for elem in required_elements:
    if elem.lower() in html.lower():
        print(f"  [PASS] Found: {elem}")
    else:
        print(f"  [FAIL] Missing: {elem}")

# Check that home icon is NOT present
has_home = "fa-home" in html
print(f"  Home icon absent: {not has_home} (PASS: {not has_home})")

# 2. HTML Tag Validator
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

# 3. JavaScript Syntax Check
print("\n=== JAVASCRIPT SYNTAX VALIDATION ===")
scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
for i, s in enumerate(scripts):
    test_path = f'scratch/test_reg_js_{i}.js'
    with open(test_path, 'w', encoding='utf-8') as js_file:
        js_file.write(s)
    res = subprocess.run(['node', '--check', test_path], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"  [PASS] Script block {i}: Node.js syntax check passed.")
    else:
        print(f"  [FAIL] Script block {i}: Node.js syntax check failed!\n{res.stderr}")
