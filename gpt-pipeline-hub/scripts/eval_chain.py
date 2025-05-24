# eval_chain.py
# ------------------------------------------
# Purpose:
#   Execute a full evaluation pipeline by chaining multiple eval_runner stages.
# Adds:
#   - Token estimation and cost calculation
#   - Logging to evals/token_costs.json and pipeline_summary.json

import subprocess
import json
from pathlib import Path
from datetime import datetime

EVAL_DIR = Path("evals")
KNOWN_COMPANIES_FILE = EVAL_DIR / "known_companies.json"
TOKEN_COST_FILE = EVAL_DIR / "token_costs.json"

# Token price per 1K tokens (USD)
MODEL_PRICING = {"gpt-4.1": {"input": 0.01, "output": 0.03}}


def load_latest_result(task_id: str) -> dict:
    matching = sorted(EVAL_DIR.glob(f"{task_id}_*.json"), reverse=True)
    if not matching:
        raise FileNotFoundError(f"No evaluation result found for: {task_id}")
    selected_file = matching[0]
    print(f"📄 Selected latest result: {selected_file.name}")
    with open(selected_file, encoding="utf-8") as f:
        return json.load(f)


def run_eval(task_id: str):
    print(f"🚀 Running: {task_id}")
    subprocess.run(["python", "scripts/eval_runner.py", task_id], check=True)


def estimate_cost(results: list, model: str) -> dict:
    input_tokens = sum(len(json.dumps(x.get("input", {}))) // 4 for x in results)
    output_tokens = sum(
        len(x.get("actual", {}).get("result", "")) // 4 for x in results
    )
    pricing = MODEL_PRICING.get(model, {"input": 0, "output": 0})
    return {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "input_cost": round((input_tokens / 1000) * pricing["input"], 4),
        "output_cost": round((output_tokens / 1000) * pricing["output"], 4),
        "total_cost": round(
            (input_tokens / 1000) * pricing["input"]
            + (output_tokens / 1000) * pricing["output"],
            4,
        ),
    }


def extract_companies(result: list) -> set:
    return set(
        entry["actual"]["result"]
        for entry in result
        if "result" in entry.get("actual", {})
    )


def load_known_companies() -> set:
    if not KNOWN_COMPANIES_FILE.exists():
        return set()
    with open(KNOWN_COMPANIES_FILE, encoding="utf-8") as f:
        return set(json.load(f))


def save_known_companies(companies: set):
    with open(KNOWN_COMPANIES_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted(list(companies)), f, indent=2)


def main():
    cost_log = {}

    run_eval("feature_determination_latest")
    features = load_latest_result("feature_determination_latest")
    cost_log["feature_determination"] = estimate_cost(features, "gpt-4.1")

    run_eval("use_case_determination_latest")
    use_cases = load_latest_result("use_case_determination_latest")
    cost_log["use_case_determination"] = estimate_cost(use_cases, "gpt-4.1")

    run_eval("industry_classification_latest")
    industries = load_latest_result("industry_classification_latest")
    cost_log["industry_classification"] = estimate_cost(industries, "gpt-4.1")

    run_eval("company_determination_latest")
    companies_result = load_latest_result("company_determination_latest")
    cost_log["company_determination"] = estimate_cost(companies_result, "gpt-4.1")

    known_companies = load_known_companies()
    new_companies = extract_companies(companies_result) - known_companies
    if new_companies:
        known_companies.update(new_companies)
        save_known_companies(known_companies)
        print(f"✅ Added {len(new_companies)} new companies to known list.")
    else:
        print("ℹ️ No new companies found.")

    summary = {
        "feature_count": len(features),
        "use_case_count": len(use_cases),
        "industry_count": len(industries),
        "company_count": len(companies_result),
        "new_company_count": len(new_companies),
        "timestamp": datetime.utcnow().isoformat(),
        "total_cost_usd": round(sum(x["total_cost"] for x in cost_log.values()), 4),
    }
    summary_path = EVAL_DIR / "pipeline_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    with open(TOKEN_COST_FILE, "w", encoding="utf-8") as f:
        json.dump(cost_log, f, indent=2)

    print("✅ Full evaluation pipeline complete.")
    print(f"📊 Summary written to {summary_path}")
    print(f"💰 Token cost breakdown written to {TOKEN_COST_FILE}")


if __name__ == "__main__":
    main()
