import re

files = ['login.html', 'registeration.html', 'registration.html']

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"=== Checking {fn} ===")
    assert 'fa-solid fa-sun' in content, f"fa-solid fa-sun missing in {fn}"
    assert 'fa-solid fa-right-left' in content, f"fa-solid fa-right-left missing in {fn}"
    assert 'fa-cog' not in content, f"fa-cog still found in {fn}"
    assert 'themeToggleBtn' in content, f"themeToggleBtn missing in {fn}"
    assert 'rtlToggleBtn' in content, f"rtlToggleBtn missing in {fn}"
    assert 'toggleTheme()' in content, f"toggleTheme() missing in {fn}"
    assert 'toggleRTL()' in content, f"toggleRTL() missing in {fn}"
    assert 'toast' not in content.lower() or 'notoast' in content.lower(), f"Unexpected toast reference in {fn}"
    print(f"  All assertions passed for {fn}! File size: {len(content)} chars.")
