# 📄 Prompt Lifecycle & Automation Architecture

This document describes the full lifecycle management system for prompts in the `gpt-pipeline-hub` repository. It defines how prompts are authored, evaluated, promoted, and deployed through a fully automated CI/CD pipeline.

---

## 🧱 Layered Directory Structure

```
prompts/
├── 00-templates/         # Creative prompt building blocks (non-production)
├── 01-examples/          # Test input/output examples (jsonl)
├── 02-production/        # Validated, deployable prompts (YAML)
├── 03-metadata/          # Task metadata: versioning, I/O types, description
├── 04-evals/             # Evaluation results (scoring, logs, JSONL)
└── 99-archive/           # Deprecated or retired prompt versions
```

Each layer serves a specific function in the lifecycle:

| Layer              | Purpose                                        |
| ------------------ | ---------------------------------------------- |
| `00-templates/`  | Exploratory prompts without constraints        |
| `01-examples/`   | Ground truth scenarios for automated scoring   |
| `02-production/` | Locked, versioned prompt files for deployment  |
| `03-metadata/`   | Descriptive metadata for each task             |
| `04-evals/`      | Logs and scoring outputs from CI evaluation    |
| `99-archive/`    | Retired, versioned, or deprecated prompt files |

---

## 🔁 Prompt Process Flow

1. **Start from Raw Data** → Load structured fields (e.g. part number, title, manufacturer)
2. **Create Prompt in `00-templates/`** → Iterate with examples, optimize structure
3. **Move to `01-examples/`** → Add input/output pairs as test basis
4. **Validate Prompt via `eval_runner.py`**
   * Reads examples for the task
   * Scores against expected outputs
   * Logs result to `04-evals/`
5. **If scoring passes threshold** , promote to `02-production/`
6. **CI/CD picks up change, builds Docker image**
7. **Deploy to AWS ECS**
8. **Auto-tag or rollback based on score regression**

---

## 🤖 CI/CD Automation Goals

All steps after commit are handled automatically:

| Stage             | Action                                        |
| ----------------- | --------------------------------------------- |
| CI: Validate      | Run `validate_prompt.py`on all YAML files   |
| CI: Evaluate      | Run `eval_runner.py`per task                |
| CI: Score check   | Compare score to threshold in metadata        |
| CD: Build Docker  | Image with pipeline + prompt loader           |
| CD: Push to ECR   | Versioned container image                     |
| CD: Deploy to ECS | AWS task definition update                    |
| CD: Rollback      | If score drops below threshold                |
| Docs & Logs       | Update `04-evals/`,`prompt_registry.yaml` |

---

## 📈 Evaluation and Promotion

Prompts are promoted only when:

* Their score meets or exceeds threshold
* Their metadata is up-to-date
* Their structure passes YAML validation

Prompts can be downgraded or archived:

* On failure
* On version supersession
* By manual override via promotion script

---

## 🛡️ Governance & Observability

* All prompt executions are versioned
* All test results are logged in `04-evals/`
* All metadata is centralized in `prompt_registry.yaml`
* Prompts can be self-evaluated using meta-prompts
* CI/CD security via GitHub OIDC (no secrets committed)

---

## ✅ End State: Fully Automated Lifecycle

Once a prompt is moved to `01-examples/` with metadata:

* It is automatically evaluated
* Scored and version-tracked
* Promoted or blocked based on score
* Deployed and audited without manual work

This ensures scalable, reproducible, secure prompt operations.

---

📍 Maintained by: PromptOps Core Team

🧠 Version: Architect Mode – 2025
