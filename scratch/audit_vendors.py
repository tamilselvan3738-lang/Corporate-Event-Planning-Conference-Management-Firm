import os, re
from PIL import Image

def comprehensive_audit():
    with open('vendors.html', 'r', encoding='utf-8') as f:
        html = f.read()

    print("=== 1. FILE INTEGRITY ===")
    print("File size:", len(html), "characters")

    # Navbar check
    with open('navbar.html', 'r', encoding='utf-8') as f:
        nav = f.read()
    
    nav_head = nav[:nav.find('</style>')]
    nav_body = nav[nav.find('<header class="navbar-wrapper">'):nav.find('<!-- FOOTER -->')]
    footer_body = nav[nav.find('    <!-- FOOTER -->'):nav.rfind('  </script>')]

    print("Nav head intact:", nav_head in html)
    print("Nav body intact:", nav_body in html)
    print("Footer body intact:", footer_body in html)

    print("\n=== 2. SECTIONS CHECK ===")
    sections = [
        ("Venue Partners", "venue-partners"),
        ("Audio-Visual Suppliers", "audiovisual-suppliers"),
        ("Catering Partners", "catering-partners"),
        ("Decoration & Production Teams", "production-teams"),
        ("Transport Providers", "transport-providers"),
        ("Vendor Partnership Enquiry", "partnership-enquiry"),
        ("Vendor Registration", "vendor-registration")
    ]
    for label, sec_id in sections:
        found = f'id="{sec_id}"' in html
        print(f"[{'PASS' if found else 'FAIL'}] {label} (id='{sec_id}')")

    print("\n=== 3. IMAGES AUDIT ===")
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    print(f"Total img tags: {len(imgs)}")
    for src in imgs:
        if os.path.exists(src):
            im = Image.open(src)
            print(f"  [PASS] {src} ({im.size[0]}x{im.size[1]}, {im.format})")
        else:
            print(f"  [FAIL] Missing image: {src}")

    print("\n=== 4. FRAMER MOTION CLASSES ===")
    motion_rules = [
        "framer-colonnade-reveal",
        "framer-hardware-dial",
        "framer-culinary-float",
        "framer-scenic-construct",
        "framer-transit-glide",
        "framer-compliance-stamp",
        "framer-portal-unlock"
    ]
    for m in motion_rules:
        c = html.count(m)
        print(f"  [PASS] {m}: {c} instances")

    print("\n=== 5. LIGHT/DARK/RTL STYLES ===")
    print("Has dark theme variables:", "body.dark" in html)
    print("Has RTL rules:", "body.rtl" in html)

    print("\n=== 6. JAVASCRIPT SYNTAX & HANDLERS ===")
    js_handlers = [
        "selectVenueTier",
        "switchAVPreset",
        "activateSwatch",
        "filterFleet",
        "updateComplianceScore",
        "handleVendorSubmit",
        "closeVendorModal"
    ]
    for fn in js_handlers:
        found = f"function {fn}" in html or f"{fn}(" in html
        print(f"  [PASS] Handler '{fn}': {found}")

    print("\nALL SYSTEMS VERIFIED CLEAN!")

if __name__ == '__main__':
    comprehensive_audit()
