with open('navbar.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'.{0,50}login-btn.{0,100}', c)
for m in matches:
    print("LOGIN BTN IN NAVBAR:", m.replace('\n', ' '))

# Check JS in navbar.html
print("JS with login in navbar.html:")
for line in c.split('\n'):
    if 'login' in line.lower():
        print(" ", line.strip())
