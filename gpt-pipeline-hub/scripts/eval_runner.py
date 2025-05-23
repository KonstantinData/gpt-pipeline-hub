
import argparse
import json
import os
from pathlib import Path
from datetime import datetime
import yaml
from typing import List, Dict

# --- Config ---
PROMPT_DIR = Path("prompts/02-production")
EXAMPLES_DIR = Path("prompts/01-examples")

# --- Helpers ---
def load_prompt_yaml(task_id: str) -> dict:
    path = PROMPT_DIR / f"{task_id}.yaml"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_json_examples(task_id: str) -> List[Dict]:
    dir_path = EXAMPLES_DIR / task_id
    examples = []
    for file in dir_path.glob("*.json"):
        with open(file, encoding="utf-8") as f:
            examples.append(json.load(f))
    return examples

def call_model(prompt: dict, input_data: dict) -> dict:
    # Simulate API call – replace with actual call if needed
    return {"result": f"Processed {input_data}"}

def evaluate(task_id: str) -> None:
    prompt_def = load_prompt_yaml(task_id)
    examples = load_json_examples(task_id)

    results = []
    for ex in examples:
        input_data = ex["input"]
        expected = ex["expected"]
        actual = call_model(prompt_def, input_data)

        results.append({
            "input": input_data,
            "expected": expected,
            "actual": actual
        })

    timestamp = datetime.utcnow().isoformat()
    out_path = Path("evals") / f"{task_id}_{timestamp}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"✅ Evaluation saved to {out_path}")

# --- CLI Entry ---
def main():
    parser = argparse.ArgumentParser(description="Evaluate a prompt against input examples.")
    parser.add_argument("task_id", help="Name of the task prompt (without extension)")
    args = parser.parse_args()

    evaluate(args.task_id)

if __name__ == "__main__":
    main()
