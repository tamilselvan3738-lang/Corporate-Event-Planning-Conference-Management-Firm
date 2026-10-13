import os, re, glob, subprocess
from PIL import Image

def verify():
    with open('navbar.html', 'r', encoding='utf-8') as f:
        nav = f.read()

    with open('about.html', 'r', encoding='utf-8') as f:
        ab = f.read()

    print("=== 1. TEMPLATE PRESERVATION ===")
    nav_head = nav[:nav.find('</style>')]
    print("Nav head in about.html?", nav_head in ab)

    nav_body = nav[nav.find('<header class="navbar-wrapper">'):nav.find('<!-- FOOTER -->')]
    print("Nav body in about.html?", nav_body in ab)

    footer_start = nav.find('<!-- FOOTER -->')
    body_close = nav.rfind('</body>')
    footer_body = nav[footer_start:body_close]
    print("Footer body in about.html?", footer_body in ab)

    closing_part = nav[nav.rfind('</body>'):]
    print("Closing tags preserved?", ab.endswith(closing_part))

    print("\n=== 2. SECTIONS AUDIT ===")
    expected_sections = [
        ("Company Heritage", "company-heritage"),
        ("Mission & Vision", "mission-vision"),
        ("Philosophy", "philosophy"),
        ("Leadership Team", "leadership-team"),
        ("Specialists", "specialists"),
        ("Client Portfolio", "client-portfolio"),
        ("Safety & Advantage", "safety-advantage")
    ]
    for label, sid in expected_sections:
        exists = f'id="{sid}"' in ab
        print(f"[{'PASS' if exists else 'FAIL'}] {label} (id='{sid}')")

    print("\n=== 3. IMAGES AUDIT ===")
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', ab)
    print(f"Total img tags: {len(img_srcs)}")
    for src in img_srcs:
        if os.path.exists(src):
            im = Image.open(src)
            print(f"  [PASS] {src} ({im.size[0]}x{im.size[1]}, format={im.format})")
        else:
            print(f"  [FAIL] MISSING: {src}")

    print("\n=== 4. CROSS-PAGE IMAGE EXCLUSIVITY ===")
    all_pages = [p for p in glob.glob('*.html') if p != 'about.html']
    all_other_imgs = set()
    for op in all_pages:
        with open(op, 'r', encoding='utf-8') as f:
            for m in re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', f.read()):
                all_other_imgs.add(m)

    for src in set(img_srcs):
        collision = src in all_other_imgs
        print(f"  [{'PASS - UNIQUE' if not collision else 'FAIL - COLLISION'}] {src}")

    print("\n=== 5. FRAMER MOTION CLASSES AUDIT ===")
    motion_classes = [
        "framer-epoch-chronicle",
        "framer-polarity-gyro",
        "framer-triad-pedestal",
        "framer-council-quad",
        "framer-division-matrix",
        "framer-marquee-portfolio",
        "framer-citadel-moat"
    ]
    all_other_motion = set()
    for op in all_pages:
        with open(op, 'r', encoding='utf-8') as f:
            for m in re.findall(r'framer-[a-zA-Z0-9\-]+', f.read()):
                all_other_motion.add(m)

    for m in motion_classes:
        count = ab.count(m)
        is_novel = m not in all_other_motion
        print(f"  [{'PASS' if count > 0 and is_novel else 'FAIL'}] {m}: {count} occurrences (Novel: {is_novel})")

    print("\n=== 6. JAVASCRIPT SYNTAX CHECK (NODE --CHECK) ===")
    scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', ab, re.DOTALL)
    print(f"Total script blocks found: {len(scripts)}")
    for idx, s in enumerate(scripts):
        fname = f'scratch/abt_temp_script_{idx}.js'
        with open(fname, 'w', encoding='utf-8') as out:
            out.write(s)
        res = subprocess.run(['node', '--check', fname], capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  [PASS] Script block {idx}: Syntax valid")
        else:
            print(f"  [FAIL] Script block {idx}: Syntax error!\n{res.stderr}")

    print("\n=== 7. LIGHT / DARK / RTL STYLES ===")
    print("body.dark CSS rules present:", "body.dark" in ab)
    print("body.rtl CSS rules present:", "body.rtl" in ab)

    fa_icons = set(re.findall(r'fa[srbld]? fa-([a-z0-9\-]+)', ab))
    print(f"\nDistinct Font Awesome icons: {len(fa_icons)}")

    print("\nALL SYSTEM CHECKS COMPLETED FOR ABOUT.HTML!")

if __name__ == '__main__':
    verify()
