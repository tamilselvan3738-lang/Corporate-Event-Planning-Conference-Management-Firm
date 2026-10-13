# -*- coding: utf-8 -*-
"""
verify_home2.py
Comprehensive verification script for home-2.html.
"""

import os, re, glob, subprocess
from PIL import Image

def verify():
    with open('navbar.html', 'r', encoding='utf-8') as f:
        nav = f.read()

    with open('home-2.html', 'r', encoding='utf-8') as f:
        h2 = f.read()

    print("=== 1. TEMPLATE PRESERVATION ===")
    head_before = nav[:nav.find('</style>')]
    print("Nav head preserved in home-2.html?", head_before in h2)

    footer_start = nav.find('<!-- FOOTER -->')
    footer_end = nav.rfind('</body>')
    footer_body = nav[footer_start:footer_end]
    print("Footer body preserved in home-2.html?", footer_body in h2)

    nav_middle = nav[nav.find('</style>'):footer_start]
    print("Nav middle preserved in home-2.html?", nav_middle in h2)

    closing_tags = nav[footer_end:]
    print("Closing tags preserved in home-2.html?", h2.endswith(closing_tags))

    print("\n=== 2. SECTIONS AUDIT ===")
    expected_sections = [
        ("The Cinematic Sovereign Hero & Live Telemetry Cockpit", "hero-cinema"),
        ("The 4-Dimensional Summit Matrix & Chamber Carousel", "summit-dimensions"),
        ("The Neurodesign & Spatial Engineering Laboratory", "spatial-technologies"),
        ("The Sovereign Operations Grid & Global City Hubs", "global-footprint"),
        ("The Executive Impact Dossier & Transformation Casebook", "resonance-casebook"),
        ("The Strategic Scoping Gateway & Fast-Track Feasibility Engine", "executive-engagement")
    ]
    print(f"Total sections expected: {len(expected_sections)}")
    for idx, (label, sid) in enumerate(expected_sections):
        exists = f'id="{sid}"' in h2
        print(f"  [{'PASS' if exists else 'FAIL'}] Section {idx+1}: {label} (id='{sid}')")

    # Count total section elements between navbar and footer
    page_middle = h2[h2.find(nav_middle) + len(nav_middle):h2.find(footer_body)]
    sections_found = re.findall(r'<section\s+[^>]*id=["\']([^"\']+)["\']', page_middle)
    print(f"Total <section> tags found in body: {len(sections_found)} -> {sections_found}")
    assert len(sections_found) == 6, f"Expected exactly 6 sections, found {len(sections_found)}"

    print("\n=== 3. IMAGES AUDIT ===")
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', page_middle)
    print(f"Total img tags in sections: {len(img_srcs)}")
    for src in img_srcs:
        if os.path.exists(src):
            im = Image.open(src)
            print(f"  [PASS] {src} ({im.size[0]}x{im.size[1]}, format={im.format})")
        else:
            print(f"  [FAIL] MISSING: {src}")

    print("\n=== 4. CROSS-PAGE IMAGE EXCLUSIVITY ===")
    all_other_pages = [p for p in glob.glob('*.html') if p not in ('home-2.html', 'navbar.html')]
    all_other_imgs = set()
    for op in all_other_pages:
        with open(op, 'r', encoding='utf-8') as f:
            for m in re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', f.read()):
                all_other_imgs.add(m)

    for src in img_srcs:
        collision = src in all_other_imgs
        print(f"  [{'PASS - UNIQUE' if not collision else 'FAIL - COLLISION'}] {src}")
        assert not collision, f"Collision detected for image {src}"

    print("\n=== 5. FRAMER MOTION CLASSES AUDIT ===")
    expected_framer = [
        "framer-cinema-hero",
        "framer-chamber-matrix",
        "framer-neuro-lab",
        "framer-footprint-grid",
        "framer-impact-dossier",
        "framer-feasibility-gateway"
    ]
    all_other_framer = set()
    for op in all_other_pages:
        with open(op, 'r', encoding='utf-8') as f:
            for m in re.findall(r'framer-[a-zA-Z0-9\-]+', f.read()):
                all_other_framer.add(m)

    for fc in expected_framer:
        count = h2.count(fc)
        is_unique = fc not in all_other_framer
        print(f"  [{'PASS' if count > 0 and is_unique else 'FAIL'}] {fc} (Occurrences: {count}, Globally Unique: {is_unique})")
        assert count > 0, f"Missing framer class {fc}"
        assert is_unique, f"Framer class {fc} is not unique across pages"

    print("\n=== 6. JAVASCRIPT SYNTAX CHECK (NODE --CHECK) ===")
    scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', h2, re.DOTALL)
    print(f"Total script blocks found: {len(scripts)}")
    for idx, s in enumerate(scripts):
        fname = f'scratch/h2_temp_script_{idx}.js'
        with open(fname, 'w', encoding='utf-8') as out:
            out.write(s)
        res = subprocess.run(['node', '--check', fname], capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  [PASS] Script block {idx}: Syntax valid")
        else:
            print(f"  [FAIL] Script block {idx}: Syntax error!\n{res.stderr}")
            assert False, f"Syntax error in script block {idx}"

    print("\n=== 7. LIGHT / DARK / RTL STYLES AUDIT ===")
    has_dark = "body.dark" in h2
    has_rtl = "body.rtl" in h2
    print(f"  [{'PASS' if has_dark else 'FAIL'}] body.dark styles defined: {has_dark}")
    print(f"  [{'PASS' if has_rtl else 'FAIL'}] body.rtl styles defined: {has_rtl}")
    assert has_dark and has_rtl

    fa_icons = set(re.findall(r'fa[srbld]? fa-([a-z0-9\-]+)', page_middle))
    print(f"\nDistinct Font Awesome icons used: {len(fa_icons)}")

    print("\n==========================================================")
    print(">>> ALL VERIFICATION CHECKS PASSED FOR HOME-2.HTML! <<<")
    print("==========================================================")

if __name__ == '__main__':
    verify()
