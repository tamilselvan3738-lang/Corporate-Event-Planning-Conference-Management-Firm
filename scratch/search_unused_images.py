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

# Let's search for corporate, office, desk, consultation, planning, guides, checklist, budget, venue, hybrid, insights, faq
for kw in ['guide', 'check', 'audit', 'plan', 'desk', 'office', 'consult', 'paper', 'tablet', 'screen', 'board', 'contract', 'report', 'book']:
    matching = [x for x in unique_items if kw in (x['name'] + ' ' + x['prompt']).lower()]
    print(f"\nKeyword '{kw}': {len(matching)} matches")
    for m in matching[:3]:
        print(f"  {m['name']}: {m['prompt'][:100]}... ({m['file']})")
