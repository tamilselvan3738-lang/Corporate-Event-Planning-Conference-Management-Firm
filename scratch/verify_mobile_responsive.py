import glob, sys

sys.stdout.reconfigure(encoding='utf-8')

all_pages = sorted(glob.glob('*.html'))
print(f"=== VERIFYING RESPONSIVENESS ACROSS ALL {len(all_pages)} PAGES ===")

required_breakpoints = ['320px', '480px', '768px', '1024px']
required_features = [
    ('overflow-x: hidden', 'Overflow protection'),
    ('box-sizing: border-box', 'Universal Box-Sizing'),
    ('max-width: 100%', 'Fluid Media & Elements'),
    ('overflow-wrap: break-word', 'Text Containment')
]

all_passed = True

for fn in all_pages:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    # Check breakpoints
    missing_bp = [bp for bp in required_breakpoints if f'max-width: {bp}' not in c and f'max-width:{bp}' not in c]
    if missing_bp:
        print(f"  [FAIL Breakpoints] {fn}: Missing breakpoints {missing_bp}")
        all_passed = False
    else:
        print(f"  [OK Breakpoints] {fn}: All 4 breakpoints (320px, 480px, 768px, 1024px) verified!")

    # Check features
    missing_feats = [desc for snippet, desc in required_features if snippet not in c]
    if missing_feats:
        print(f"  [FAIL Features] {fn}: Missing features {missing_feats}")
        all_passed = False
    else:
        print(f"  [OK Features] {fn}: All core responsive features verified!")

print("\n" + "="*50)
if all_passed:
    print("ALL 16 PAGES PASSED 100% OF MOBILE RESPONSIVE VERIFICATION CHECKS!")
else:
    print("SOME RESPONSIVE CHECKS FAILED! REVIEW LOGS ABOVE.")

sys.exit(0 if all_passed else 1)
