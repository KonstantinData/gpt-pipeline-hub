# eval_chain.py
# ------------------------------------------
# Purpose:
#   Execute a full evaluation pipeline by chaining multiple eval_runner stages.
# Steps:
#   - feature_determination_latest
#   - use_case_determination_latest (requires features)
#   - industry_classification_latest (requires features + use cases)
#   - company_determination_latest (requires all previous)

import subprocess
import json
from pathlib import Path
from datetime import datetime

# Base directory for evaluation output
EVAL_DIR = Path("evals")


# Load JSON result by task ID
# -----------------------------
def load_latest_result(task_id: str) -> dict:
    matching = sorted(EVAL_DIR.glob(f"{task_id}_*.json"), reverse=True)
    if not matching:
        raise FileNotFoundError(f"No evaluation result found for: {task_id}")

    selected_file = matching[0]
    print(f"📄 Selected latest result: {selected_file.name}")

    with open(selected_file, encoding="utf-8") as f:
        return json.load(f)


# Run eval_runner for a given task ID
# -----------------------------------
def run_eval(task_id: str):
    """
    Executes eval_runner for a single task.
    Optional: Consider allowing dynamic prompt injection here using input
    from previous stages to simulate real chaining behavior.
    """
    print(f"🚀 Running: {task_id}")
    subprocess.run(["python", "scripts/eval_runner.py", task_id], check=True)


# Main pipeline logic
# ---------------------
def main():
    # 1. Determine features
    run_eval("feature_determination_latest")
    features = load_latest_result("feature_determination_latest")

    # 2. Determine use cases using features
    # This call could use `features` as part of a constructed input
    # if chaining behavior is desired beyond just sequence.
    run_eval("use_case_determination_latest")
    use_cases = load_latest_result("use_case_determination_latest")

    # 3. Classify industries using features + use cases
    run_eval("industry_classification_latest")
    industries = load_latest_result("industry_classification_latest")

    # 4. Determine companies using full context
    run_eval("company_determination_latest")
    companies = load_latest_result("company_determination_latest")

    # Write summary of evaluation
    summary = {
        "feature_count": len(features),
        "use_case_count": len(use_cases),
        "industry_count": len(industries),
        "company_count": len(companies),
        "timestamp": datetime.utcnow().isoformat(),
    }
    summary_path = EVAL_DIR / "pipeline_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print("✅ Full evaluation pipeline complete.")
    print(f"📊 Summary written to {summary_path}")


if __name__ == "__main__":
    main()
