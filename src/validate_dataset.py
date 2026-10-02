import json
from pathlib import Path

DATASET_PATH=Path("/home/sadhaka_19745/Desktop/llm-reasoning-error-analysis/data/raw/reasoningv0.jsonl")

def validate_dataset(path):
    required_fields={"id","category","question","answer"}
    with open(path,"r",encoding="utf-8") as file:
        lines= file.readlines()

    seen_ids= set()

    for line_number,line in enumerate(lines,start=1):
        if not line.strip():
            continue

        try:
            item=json.loads(line)
        except json.JSONDecodeError as e:
            print("Invalid JSON on line {line_number}:{e}")
            return False

        missing = required_fields - item.keys()

        if missing:
            print(
                f"Line {line_number} is missing fields: {missing}"
            )
            return False

        if item["id"] in seen_ids:
            print(f"Duplicate ID found: {item['id']}")
            return False

        seen_ids.add(item["id"])

    print(f"Dataset valid: {len(seen_ids)} examples")
    return True


if __name__ == "__main__":
    validate_dataset(DATASET_PATH)