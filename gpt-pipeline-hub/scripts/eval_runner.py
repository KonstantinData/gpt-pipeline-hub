import argparse
import json
import os
from pathlib import Path
from datetime import datetime
import yaml


# Optional: Simuliere OpenAI API Response (Mock)
def call_model(prompt: str, input_data: dict) -> dict:
    return {"result": f"Processed {input_data}"}  # Dummy


# Lade Prompt aus Datei
def load_prompt(task_id: str) -> str:
    prompt_path = Path("prompts/02-production") / f"{task_id}.yaml"
    with open(prompt_path, encoding="utf-8") as f:
        prompt_def = yaml.safe_load(f)
    return prompt_def


# Lade Beispiele aus examples-Verzeichnis
def load_examples(task_id: str):
    examples_dir = Path("prompts/01-examples") / task_id
    examples = []
    for file in examples_dir.glob("*.json"):
        with open(file, encoding="utf-8") as f:
            examples.append(json.load(f))
    return examples


# Hauptausführung
def run_eval(task_id: str):
    prompt_def = load_prompt(task_id)
    examples = load_examples(task_id)

    results = []
    for example in examples:
        input_data = example["input"]
        expected = example["expected"]
        response = call_model(prompt_def["role"], input_data)

        results.append(
            {
                "input": input_data,
                "expected": expected,
                "actual": response,
                "match": response == expected,
            }
        )

    eval_dir = Path(f"prompts/04-evals/{task_id}")
    eval_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.utcnow().isoformat(timespec="seconds")
    output_file = eval_dir / f"results_{timestamp}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"✅ Evaluation results saved to: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run prompt evaluation")
    parser.add_argument(
        "--task", required=True, help="Task ID, e.g. 'feature_determination_v1'"
    )
    args = parser.parse_args()
    run_eval(args.task)
