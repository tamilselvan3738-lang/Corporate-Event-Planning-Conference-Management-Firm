import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx_start = c.find('<div class="app-wrapper">')
count = 0
end_pos = -1

for m in re.finditer(r'</?div\b', c):
    tag = m.group(0)
    pos = m.start()
    if pos >= idx_start:
        if tag == '<div':
            count += 1
        elif tag == '</div':
            count -= 1
            if count == 0:
                end_pos = pos
                break

print("Wrapper closed at position:", end_pos)
print("Footer position:", c.find('<footer'))
print("Snippet around wrapper end:")
print(c[end_pos-100:end_pos+100].encode('ascii', errors='replace').decode('ascii'))
