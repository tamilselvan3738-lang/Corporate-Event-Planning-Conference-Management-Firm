import os, json, glob

brain_dir = r'C:\Users\Tamiluuu\.gemini\antigravity\brain'
all_items = []

for root, dirs, files in os.walk(brain_dir):
    for f in files:
        if f == 'transcript.jsonl':
            full = os.path.join(root, f)
            conv_dir = os.path.dirname(os.path.dirname(os.path.dirname(full)))
            try:
                with open(full, 'r', encoding='utf-8', errors='ignore') as tf:
                    for line in tf:
                        if 'generate_image' in line and 'Prompt' in line:
                            data = json.loads(line)
                            for tc in data.get('tool_calls', []):
                                if tc.get('name') == 'generate_image':
                                    args = tc.get('args', {})
                                    name = str(args.get('ImageName', '')).strip('\"')
                                    prompt = str(args.get('Prompt', '')).strip('\"')
                                    matches = glob.glob(os.path.join(conv_dir, name + '_*.jpg'))
                                    if not matches:
                                        p_exact = os.path.join(conv_dir, name + '.jpg')
                                        if os.path.exists(p_exact): matches = [p_exact]
                                    if matches:
                                        all_items.append({'name': name, 'prompt': prompt, 'file': matches[0]})
            except Exception:
                pass

used_in_project = set(os.listdir('images'))
# de-duplicate by file
seen_files = set()
unique_items = []
for item in all_items:
    if item['file'] not in seen_files and os.path.basename(item['file']) not in used_in_project and (item['name'] + '.jpg') not in used_in_project:
        seen_files.add(item['file'])
        unique_items.append(item)

print(f"Total distinct unused generated images: {len(unique_items)}")

categories = {
    '1_headquarters': ['headquarters', 'building', 'exterior', 'lobby', 'reception', 'atrium', 'facade', 'architecture'],
    '2_phone': ['phone', 'call', 'support', 'headset', 'telephony', 'operator', 'dispatch', 'liaison'],
    '3_email': ['email', 'digital', 'tablet', 'screen', 'laptop', 'vault', 'encrypted', 'data'],
    '4_hours': ['office', 'workspace', 'clock', 'time', 'schedule', 'consultation', 'desk'],
    '5_map': ['map', 'location', 'satellite', 'transit', 'aerial', 'cartography', 'city', 'district'],
    '6_form': ['consultation', 'meeting', 'inquiry', 'form', 'conference', 'client', 'boardroom'],
    '7_emergency': ['emergency', 'command', 'incident', 'control', 'bunker', 'security', 'alert', 'rapid']
}

for cat, keywords in categories.items():
    print(f"\n=== MATCHES FOR {cat} ===")
    matches = []
    for c in unique_items:
        text = (c['name'] + ' ' + c['prompt']).lower()
        score = sum(1 for kw in keywords if kw in text)
        if score > 0:
            matches.append((score, c))
    matches.sort(key=lambda x: x[0], reverse=True)
    for score, m in matches[:5]:
        print(f"Score {score}: [{m['name']}] -> {m['file']}")
        print(f"   Prompt: {m['prompt'][:130]}...")
