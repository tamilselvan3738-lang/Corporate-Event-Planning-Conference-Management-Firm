import json, sys

with open(r'C:\Users\Tamiluuu\.gemini\antigravity\brain\13f4b244-cabb-4cf6-82cd-1983739a963e\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'USER_INPUT':
            si = data.get('step_index')
            content = data.get('content', '')
            media = data.get('media', [])
            # Print only from step 1500 onwards
            if si >= 1500:
                print(f"=== STEP {si} ===")
                for l in content.split('\n')[:5]:
                    print(" ", l.encode('ascii', errors='replace').decode('ascii'))
                if media:
                    print("  Media:", media)
