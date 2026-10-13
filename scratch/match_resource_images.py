import os, json, glob

brain_dir = r'C:\Users\Tamiluuu\.gemini\antigravity\brain'
generated_images = []

for root, dirs, files in os.walk(brain_dir):
    for f in files:
        if f == 'transcript.jsonl':
            full = os.path.join(root, f)
            try:
                with open(full, 'r', encoding='utf-8', errors='ignore') as tf:
                    for line in tf:
                        if 'generate_image' in line and 'Prompt' in line:
                            data = json.loads(line)
                            for tc in data.get('tool_calls', []):
                                if tc.get('name') == 'generate_image':
                                    args = tc.get('args', {})
                                    conv_dir = os.path.dirname(os.path.dirname(os.path.dirname(full)))
                                    name = str(args.get('ImageName', '')).strip('\"')
                                    prompt = str(args.get('Prompt', '')).strip('\"')
                                    # find file
                                    matches = glob.glob(os.path.join(conv_dir, name + '_*.jpg'))
                                    if not matches:
                                        matches = glob.glob(os.path.join(conv_dir, name + '_*.png'))
                                    if not matches:
                                        p_exact = os.path.join(conv_dir, name + '.jpg')
                                        if os.path.exists(p_exact):
                                            matches = [p_exact]
                                    if matches:
                                        generated_images.append({
                                            'name': name,
                                            'prompt': prompt,
                                            'file': matches[0]
                                        })
            except Exception:
                pass

used_in_project = set(os.listdir('images'))
unique_candidates = [x for x in generated_images if os.path.basename(x['file']) not in used_in_project and (x['name'] + '.jpg') not in used_in_project]

print(f"Total unique Gemini candidate images: {len(unique_candidates)}")

# Search categories
categories = {
    '1_planning_guide': ['guide', 'playbook', 'planning', 'strategic', 'dossier', 'document', 'manual'],
    '2_checklist': ['checklist', 'schedule', 'timeline', 'preparation', 'inspect', 'audit', 'check', 'milestone'],
    '3_budget': ['budget', 'financial', 'cost', 'allocation', 'finance', 'calculator', 'investment', 'economic'],
    '4_venue_guide': ['venue', 'blueprint', 'floorplan', 'architectural', 'hall', 'atrium', 'property', 'space'],
    '5_hybrid_practices': ['hybrid', 'virtual', 'broadcast', 'studio', 'streaming', 'screen', 'digital', 'camera'],
    '6_industry_insights': ['insight', 'article', 'trend', 'report', 'research', 'publication', 'conference', 'summit'],
    '7_faq': ['faq', 'question', 'consultation', 'concierge', 'advisory', 'support', 'desk', 'interview']
}

for cat, keywords in categories.items():
    print(f"\n=== MATCHES FOR {cat} ===")
    matches = []
    for c in unique_candidates:
        text = (c['name'] + ' ' + c['prompt']).lower()
        score = sum(1 for kw in keywords if kw in text)
        if score > 0:
            matches.append((score, c))
    matches.sort(key=lambda x: x[0], reverse=True)
    for score, m in matches[:6]:
        print(f"Score {score}: [{m['name']}] -> {m['file']}")
        print(f"   {m['prompt'][:130]}...")
