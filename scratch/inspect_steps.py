import json

with open(r'C:\Users\Tamiluuu\.gemini\antigravity\brain\13f4b244-cabb-4cf6-82cd-1983739a963e\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        si = data.get('step_index')
        if si and 1795 <= si <= 1805:
            print(f"Step {si} type={data.get('type')}: {str(data.get('content'))[:200]}")
