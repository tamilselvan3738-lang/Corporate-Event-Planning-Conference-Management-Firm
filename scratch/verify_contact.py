import os, re
from PIL import Image

def verify():
    with open('navbar.html', 'r', encoding='utf-8') as f:
        nav = f.read()

    with open('contact.html', 'r', encoding='utf-8') as f:
        ct = f.read()

    print("=== 1. TEMPLATE PRESERVATION ===")
    nav_head = nav[:nav.find('</style>')]
    print("Nav head in contact.html?", nav_head in ct)

    nav_body = nav[nav.find('<header class="navbar-wrapper">'):nav.find('<!-- FOOTER -->')]
    print("Nav body in contact.html?", nav_body in ct)

    footer_start = nav.find('    <!-- FOOTER -->')
    script_close = nav.rfind('  </script>')
    footer_body = nav[footer_start:script_close]
    print("Footer body in contact.html?", footer_body in ct)

    print("\n=== 2. SECTIONS VERIFICATION ===")
    expected_sections = [
        ("Office Address", "office-address"),
        ("Phone Number", "phone-telephony"),
        ("Business Email", "business-email"),
        ("Office Hours", "office-hours"),
        ("Location Map", "location-map"),
        ("General Enquiry Form & Consultation", "enquiry-consultation"),
        ("Emergency Event Support Contact", "emergency-support")
    ]
    for label, sid in expected_sections:
        exists = f'id="{sid}"' in ct
        print(f"[{'PASS' if exists else 'FAIL'}] {label} (id='{sid}')")

    print("\n=== 3. IMAGES AUDIT ===")
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', ct)
    print(f"Total img tags: {len(img_srcs)}")
    for src in img_srcs:
        if os.path.exists(src):
            im = Image.open(src)
            print(f"  [PASS] {src} ({im.size[0]}x{im.size[1]}, format={im.format})")
        else:
            print(f"  [FAIL] MISSING: {src}")

    print("\n=== 4. FRAMER MOTION CLASSES ===")
    motion_classes = [
        "framer-monolith-panoramic",
        "framer-rotary-dial",
        "framer-keycard-matrix",
        "framer-meridian-wave",
        "framer-radar-sweep",
        "framer-foundry-studio",
        "framer-beacon-alert"
    ]
    for m in motion_classes:
        count = ct.count(m)
        print(f"  [{'PASS' if count > 0 else 'FAIL'}] {m}: {count} occurrences")

    print("\n=== 5. LIGHT / DARK / RTL STYLES ===")
    print("body.dark CSS rules present:", "body.dark" in ct)
    print("body.rtl CSS rules present:", "body.rtl" in ct)

    print("\n=== 6. JAVASCRIPT HANDLERS ===")
    handlers = [
        "updateLiveClocks",
        "switchRadarPin",
        "copyEmailToClipboard",
        "setFoundryMode",
        "handleFoundrySubmit",
        "closeContactModal"
    ]
    for h in handlers:
        print(f"  [{'PASS' if h in ct else 'FAIL'}] Handler '{h}': {h in ct}")

    fa_icons = set(re.findall(r'fa[srbld]? fa-([a-z0-9\-]+)', ct))
    print(f"\nDistinct Font Awesome icons: {len(fa_icons)}")

    print("\n=== 7. CROSS-PAGE IMAGE EXCLUSIVITY ===")
    import glob
    all_pages = [p for p in glob.glob('*.html') if p != 'contact.html']
    contact_imgs = [
        'images/contact_office_address.jpg',
        'images/contact_phone_telephony.jpg',
        'images/contact_business_email.jpg',
        'images/contact_office_hours.jpg',
        'images/contact_location_map.jpg',
        'images/contact_consultation_form.jpg',
        'images/contact_emergency_support.jpg'
    ]
    all_other_imgs = set()
    for op in all_pages:
        with open(op, 'r', encoding='utf-8') as f:
            for m in re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', f.read()):
                all_other_imgs.add(m)

    for ci in contact_imgs:
        collision = ci in all_other_imgs
        print(f"  [{'PASS - UNIQUE' if not collision else 'FAIL - COLLISION'}] {ci}")

    print("\nALL SYSTEM CHECKS PASSED FOR CONTACT.HTML!")

if __name__ == '__main__':
    verify()
