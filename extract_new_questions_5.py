import re
import json

def extract_questions(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    questions = []

    # Matches "**5.1.1 - INTERMEDIATE**: Question text" or "**6.1.1 - ADVANCED**: Question text"
    pattern = re.compile(r'^\*\*(\d+\.\d+\.\d+) - (INTERMEDIATE|ADVANCED)\*\*:\s+(.*)')

    for line in lines:
        line = line.strip()
        if not line:
            continue

        match = pattern.match(line)
        if match:
            q_id_str = match.group(1)
            q_text = match.group(3)
            questions.append({'id': q_id_str, 'question': q_text})
        else:
            pass

    return questions

questions = extract_questions('new_questions_5.md')

print(f"Found {len(questions)} questions.")

# Save to json
with open('new_questions_5.json', 'w') as f:
    json.dump(questions, f, indent=2)

print("Saved to new_questions_5.json")
