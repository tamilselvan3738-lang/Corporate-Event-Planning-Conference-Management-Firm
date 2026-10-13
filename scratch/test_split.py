with open('navbar.html', 'r', encoding='utf-8') as f:
    nav = f.read()

head_split = '</style>'
head_idx = nav.find(head_split)
head_before = nav[:head_idx]

nav_body_start = nav.find('<header class="navbar-wrapper">')
footer_start = nav.find('<!-- FOOTER -->')
header_html = nav[nav_body_start:footer_start]

footer_end = nav.rfind('</body>')
footer_html = nav[footer_start:footer_end]
closing_html = nav[footer_end:]

print('Head length:', len(head_before))
print('Header length:', len(header_html))
print('Footer length:', len(footer_html))
print('Closing length:', len(closing_html))
