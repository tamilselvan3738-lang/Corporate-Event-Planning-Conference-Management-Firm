import json

with open(r'C:\Users\Tamiluuu\.gemini\antigravity\brain\13f4b244-cabb-4cf6-82cd-1983739a963e\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        content = str(data.get('content', ''))
        step = data.get('step_index')
        source = data.get('source')
        if 'fa-cog' in content:
            print(f'Step {step} ({source}): {content[:150]}...')
