import os, re, glob, subprocess
from PIL import Image

def verify():
    with open('navbar.html', 'r', encoding='utf-8') as f:
        nav = f.read()

    with open('resources.html', 'r', encoding='utf-8') as f:
        rc = f.read()

    print("=== 1. TEMPLATE PRESERVATION ===")
    nav_head = nav[:nav.find('</style>')]
    print("Nav head in resources.html?", nav_head in rc)

    nav_body = nav[nav.find('<header class="navbar-wrapper">'):nav.find('<!-- FOOTER -->')]
    print("Nav body in resources.html?", nav_body in rc)

    footer_start = nav.find('<!-- FOOTER -->')
    body_close = nav.rfind('</body>')
    footer_body = nav[footer_start:body_close]
    print("Footer body in resources.html?", footer_body in rc)

    closing_part = nav[nav.rfind('</body>'):]
    print("Closing tags preserved?", rc.endswith(closing_part))

    print("\n=== 2. SECTIONS AUDIT ===")
    expected_sections = [
        ("Corporate Event Planning Guides", "planning-guides"),
        ("Conference Preparation Checklist", "preparation-checklist"),
        ("Event Budget Planning Guide", "budget-guide"),
        ("Venue Selection Guide", "venue-guide"),
        ("Hybrid Event Best Practices", "hybrid-practices"),
        ("Industry Insights & Articles", "industry-insights"),
        ("Frequently Asked Questions", "faq")
    ]
    for label, sid in expected_sections:
        exists = f'id="{sid}"' in rc
        print(f"[{'PASS' if exists else 'FAIL'}] {label} (id='{sid}')")

    print("\n=== 3. IMAGES AUDIT ===")
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', rc)
    print(f"Total img tags: {len(img_srcs)}")
    for src in img_srcs:
        if os.path.exists(src):
            im = Image.open(src)
            print(f"  [PASS] {src} ({im.size[0]}x{im.size[1]}, format={im.format})")
        else:
            print(f"  [FAIL] MISSING: {src}")

    print("\n=== 4. CROSS-PAGE IMAGE EXCLUSIVITY ===")
    all_pages = [p for p in glob.glob('*.html') if p != 'resources.html']
    all_other_imgs = set()
    for op in all_pages:
        with open(op, 'r', encoding='utf-8') as f:
            for m in re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', f.read()):
                all_other_imgs.add(m)

    for src in img_srcs:
        collision = src in all_other_imgs
        print(f"  [{'PASS - UNIQUE' if not collision else 'FAIL - COLLISION'}] {src}")

    print("\n=== 5. FRAMER MOTION CLASSES AUDIT ===")
    motion_classes = [
        "framer-codex-stack",
        "framer-mission-gauge",
        "framer-ledger-cascade",
        "framer-spatial-radar",
        "framer-telemetry-nexus",
        "framer-monograph-editorial",
        "framer-vault-accordion"
    ]
    all_other_motion = set()
    for op in all_pages:
        with open(op, 'r', encoding='utf-8') as f:
            for m in re.findall(r'framer-[a-zA-Z0-9\-]+', f.read()):
                all_other_motion.add(m)

    for m in motion_classes:
        count = rc.count(m)
        is_novel = m not in all_other_motion
        print(f"  [{'PASS' if count > 0 and is_novel else 'FAIL'}] {m}: {count} occurrences (Novel: {is_novel})")

    print("\n=== 6. JAVASCRIPT SYNTAX CHECK (NODE --CHECK) ===")
    scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', rc, re.DOTALL)
    print(f"Total script blocks found: {len(scripts)}")
    for idx, s in enumerate(scripts):
        fname = f'scratch/res_temp_script_{idx}.js'
        with open(fname, 'w', encoding='utf-8') as out:
            out.write(s)
        res = subprocess.run(['node', '--check', fname], capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  [PASS] Script block {idx}: Syntax valid")
        else:
            print(f"  [FAIL] Script block {idx}: Syntax error!\n{res.stderr}")

    print("\n=== 7. LIGHT / DARK / RTL STYLES ===")
    print("body.dark CSS rules present:", "body.dark" in rc)
    print("body.rtl CSS rules present:", "body.rtl" in rc)

    fa_icons = set(re.findall(r'fa[srbld]? fa-([a-z0-9\-]+)', rc))
    print(f"\nDistinct Font Awesome icons: {len(fa_icons)}")

    print("\nALL SYSTEM CHECKS COMPLETED!")

if __name__ == '__main__':
    verify()
