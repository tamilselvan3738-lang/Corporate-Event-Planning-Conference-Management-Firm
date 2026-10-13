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
                                    # Root conversation dir is 3 levels up from transcript.jsonl
                                    conv_dir = os.path.dirname(os.path.dirname(os.path.dirname(full)))
                                    generated_images.append({
                                        'name': str(args.get('ImageName', '')).strip('\"'),
                                        'prompt': str(args.get('Prompt', '')).strip('\"'),
                                        'conv_dir': conv_dir
                                    })
            except Exception as e:
                pass

print(f"Total generate_image calls found: {len(generated_images)}")

# Check which ones exist on disk in their conv_dir
found = []
for item in generated_images:
    pattern = os.path.join(item['conv_dir'], item['name'] + '_*.jpg')
    matches = glob.glob(pattern)
    if not matches:
        pattern_png = os.path.join(item['conv_dir'], item['name'] + '_*.png')
        matches = glob.glob(pattern_png)
    if not matches:
        pattern_exact = os.path.join(item['conv_dir'], item['name'] + '.jpg')
        if os.path.exists(pattern_exact):
            matches = [pattern_exact]
    if matches:
        item['file'] = matches[0]
        found.append(item)

print(f"Total matched generated image files: {len(found)}")

# Filter for those not already in our images/ directory
used_in_project = set(os.listdir('images'))
available = [x for x in found if os.path.basename(x['file']) not in used_in_project and (x['name'] + '.jpg') not in used_in_project]
print(f"Total available unused Gemini generated images: {len(available)}")

for x in available:
    print(f"NAME: {x['name']}")
    print(f"  FILE: {x['file']}")
    print(f"  PROMPT: {x['prompt'][:140]}")
    print("-" * 50)
