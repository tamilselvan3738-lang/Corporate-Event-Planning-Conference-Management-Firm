import os, re, glob, subprocess
from PIL import Image

def verify():
    with open('navbar.html', 'r', encoding='utf-8') as f:
        nav = f.read()

    with open('services.html', 'r', encoding='utf-8') as f:
        srv = f.read()

    print("=== 1. TEMPLATE PRESERVATION ===")
    nav_head = nav[:nav.find('</style>')]
    print("Nav head in services.html?", nav_head in srv)

    nav_body = nav[nav.find('<header class="navbar-wrapper">'):nav.find('<!-- FOOTER -->')]
    print("Nav body in services.html?", nav_body in srv)

    footer_start = nav.find('<!-- FOOTER -->')
    body_close = nav.rfind('</body>')
    footer_body = nav[footer_start:body_close]
    print("Footer body in services.html?", footer_body in srv)

    closing_part = nav[nav.rfind('</body>'):]
    print("Closing tags preserved?", srv.endswith(closing_part))

    print("\n=== 2. SECTIONS AUDIT ===")
    expected_sections = [
        ("Corporate Event Management", "corporate-events"),
        ("Conference Management", "conference-management"),
        ("Venue Sourcing & Capacity Planning", "venue-sourcing"),
        ("Audio-Visual Production", "audiovisual-production"),
        ("Event Design & Branding", "design-branding"),
        ("Catering & Hospitality", "hospitality-catering"),
        ("Delegate & Guest Logistics", "delegate-logistics")
    ]
    print(f"Total sections: {len(expected_sections)}")
    for label, sid in expected_sections:
        exists = f'id="{sid}"' in srv
        print(f"[{'PASS' if exists else 'FAIL'}] {label} (id='{sid}')")

    print("\n=== 3. CONTENT SUB-ITEMS COVERAGE AUDIT ===")
    sub_items = [
        # Corporate Events
        "Business Meetings", "Annual General Meetings", "Corporate Celebrations", "Executive Retreats", "Employee Engagement Events",
        # Conference Management
        "International Conferences", "Industry Conferences", "Leadership Summits", "Business Conventions", "Multi-Day Conferences",
        # Venue Sourcing
        "Conference Halls", "Hotels & Resorts", "Convention Centres", "Outdoor Event Spaces", "Capacity Planning",
        # Audio-Visual Production
        "Sound Systems", "LED Walls", "Stage Lighting", "Live Streaming", "Hybrid Conference",
        # Event Design & Branding
        "Stage & Set", "Event Branding", "Exhibition Booth", "Signage", "Presentation Design",
        # Catering & Hospitality
        "Corporate Catering", "Delegate Refreshment", "VIP Hospitality", "Dietary", "Accommodation",
        # Delegate & Guest Management
        "Guest Registration", "Digital Invitations", "Check-In", "Speaker Coordination", "Delegate Communication",
        # Event Logistics
        "Transportation", "Equipment Management", "Vendor Coordination", "On-Site", "Risk Management"
    ]
    missing = []
    for item in sub_items:
        if item.lower() not in srv.lower():
            missing.append(item)
    if not missing:
        print(f"  [PASS] All {len(sub_items)} required capability topics and sub-items verified in content!")
    else:
        print(f"  [FAIL] Missing topics: {missing}")

    print("\n=== 4. IMAGES AUDIT ===")
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', srv)
    print(f"Total img tags: {len(img_srcs)}")
    for src in img_srcs:
        if os.path.exists(src):
            im = Image.open(src)
            print(f"  [PASS] {src} ({im.size[0]}x{im.size[1]}, format={im.format})")
        else:
            print(f"  [FAIL] MISSING: {src}")

    print("\n=== 5. CROSS-PAGE IMAGE EXCLUSIVITY ===")
    all_pages = [p for p in glob.glob('*.html') if p != 'services.html']
    all_other_imgs = set()
    for op in all_pages:
        with open(op, 'r', encoding='utf-8') as f:
            for m in re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', f.read()):
                all_other_imgs.add(m)

    for src in img_srcs:
        collision = src in all_other_imgs
        print(f"  [{'PASS - UNIQUE' if not collision else 'FAIL - COLLISION'}] {src}")

    print("\n=== 6. FRAMER MOTION CLASSES AUDIT ===")
    motion_classes = [
        "framer-boardroom-elevation",
        "framer-plenary-amphitheater",
        "framer-spatial-cadence",
        "framer-broadcast-matrix",
        "framer-sculptural-prism",
        "framer-gastronomic-concierge",
        "framer-concourse-dispatch"
    ]
    all_other_motion = set()
    for op in all_pages:
        with open(op, 'r', encoding='utf-8') as f:
            for m in re.findall(r'framer-[a-zA-Z0-9\-]+', f.read()):
                all_other_motion.add(m)

    for m in motion_classes:
        count = srv.count(m)
        is_novel = m not in all_other_motion
        print(f"  [{'PASS' if count > 0 and is_novel else 'FAIL'}] {m}: {count} occurrences (Novel: {is_novel})")

    print("\n=== 7. JAVASCRIPT SYNTAX CHECK (NODE --CHECK) ===")
    scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', srv, re.DOTALL)
    print(f"Total script blocks found: {len(scripts)}")
    for idx, s in enumerate(scripts):
        fname = f'scratch/srv_temp_script_{idx}.js'
        with open(fname, 'w', encoding='utf-8') as out:
            out.write(s)
        res = subprocess.run(['node', '--check', fname], capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  [PASS] Script block {idx}: Syntax valid")
        else:
            print(f"  [FAIL] Script block {idx}: Syntax error!\n{res.stderr}")

    print("\n=== 8. LIGHT / DARK / RTL STYLES ===")
    print("body.dark CSS rules present:", "body.dark" in srv)
    print("body.rtl CSS rules present:", "body.rtl" in srv)

    fa_icons = set(re.findall(r'fa[srbld]? fa-([a-z0-9\-]+)', srv))
    print(f"\nDistinct Font Awesome icons: {len(fa_icons)}")

    print("\nALL SYSTEM CHECKS COMPLETED FOR SERVICES.HTML!")

if __name__ == '__main__':
    verify()
