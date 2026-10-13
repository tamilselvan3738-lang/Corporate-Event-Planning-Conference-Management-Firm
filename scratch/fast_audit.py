import glob, sys

sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    media_queries = []
    suspicious_lines = []
    for i, line in enumerate(lines):
        line_s = line.strip()
        if line_s.startswith('@media'):
            media_queries.append(line_s)
        elif any(k in line_s for k in ['min-width: 3', 'min-width: 4', 'min-width: 5', 'min-width: 6', 'min-width: 7', 'min-width: 8', 'min-width: 9']):
            if '@media' not in line_s:
                suspicious_lines.append((i+1, line_s))
        elif any(k in line_s for k in ['width: 4', 'width: 5', 'width: 6', 'width: 7', 'width: 8', 'width: 9', 'width: 10', 'width: 12']) and 'px' in line_s:
            if '@media' not in line_s and 'max-width' not in line_s:
                suspicious_lines.append((i+1, line_s))

    print(f"=== {f} ===")
    print(f"  @media queries ({len(media_queries)}): {media_queries[:4]}")
    if suspicious_lines:
        print(f"  Potential overflow lines ({len(suspicious_lines)}):")
        for num, text in suspicious_lines[:5]:
            print(f"    Line {num}: {text[:80]}")
