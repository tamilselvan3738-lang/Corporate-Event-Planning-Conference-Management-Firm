import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

files = sorted(glob.glob('*.html'))
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find all @media queries
    media_queries = re.findall(r'@media[^{]+\{', content)
    mq_cleaned = [re.sub(r'\s+', ' ', mq).strip() for mq in media_queries]
    
    # Check for fixed min-width > 280px
    fixed_min_widths = re.findall(r'([^{}]*min-width\s*:\s*([3-9]\d{2}|[1-9]\d{3})px[^{}]*)', content)
    
    # Check for fixed width > 320px
    fixed_widths = re.findall(r'([^{}]*width\s*:\s*([4-9]\d{2}|[1-9]\d{3})px[^{}]*)', content)
    
    print(f"=== {f} ===")
    print(f"  Media queries ({len(mq_cleaned)}): {mq_cleaned[:6]}")
    if fixed_min_widths:
        print(f"  Fixed min-widths > 280px ({len(fixed_min_widths)}):")
        for fmw, val in fixed_min_widths[:5]:
            print(f"    {fmw.strip()[:80]}")
    if fixed_widths:
        print(f"  Fixed widths > 380px ({len(fixed_widths)}):")
        for fw, val in fixed_widths[:4]:
            print(f"    {fw.strip()[:80]}")
