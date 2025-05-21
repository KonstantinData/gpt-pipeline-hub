
# 🧠 GPT Pipeline Hub

A modular, secure, and production-grade **prompt lifecycle management system** for large language models (LLMs), built for **classification, extraction, and matching** use cases. Designed for enterprise-grade deployment on AWS ECS, with CI/CD, encryption, and GDPR compliance baked in.

---

## 📌 Overview

This repository serves as the **source of truth** for managing versioned prompt templates, execution pipelines, infrastructure-as-code, and deployment workflows.

Supported tasks:

- ✅ Use Case Extraction
- ✅ Industry Classification
- ✅ Company Matching
- ✅ Contact Extraction

---

## 📁 Repository Structure

```
📦 gpt-pipeline-hub/
┣ 📄 README.md               ← Project documentation
┣ 📄 pyproject.toml          ← Python packaging
┣ 📄 requirements.lock       ← Locked prod dependencies
┣ 📂 src/gpt_pipeline_hub/   ← Main pipeline logic (to be implemented)
┣ 📂 prompts/                ← Prompt templates & metadata (per topic)
┣ 📂 cli/                    ← CLI tools: validate, score, run
┣ 📂 infra/                  ← Terraform for S3, IAM, ECS setup
┣ 📂 tests/                  ← Unit/integration tests
┣ 📂 .github/workflows/      ← GitHub Actions for CI/CD
```

---

## 🚀 Quickstart (Dev)

```bash
# Install dependencies (e.g. via pyenv or poetry)
pip install -r requirements.lock

# Validate prompts
python cli/validate_prompt.py

# Score prompts using test data
python cli/score_prompt.py

# Run pipeline (e.g. locally or via ECS)
python cli/run_pipeline.py --input test.json --output output.json
```

---

## 🧰 Prompt Topics & Lifecycle

Each task lives under `prompts/<topic>/` and includes:

- `prompts/`: Prompt templates (`*_v1.txt`, `*_v2.txt`, …)
- `metadata.yaml`: Version tracking, inputs/outputs, current dev/prod pointer
- `examples/`: Sample input/output pairs
- `tests/`: Unit test coverage and behavior validation

Prompts are managed like code: versioned, validated, and tested via CI/CD.

---

## 🛠️ CLI Tools

All located in `cli/`, each script is modular and container-ready:

- `validate_prompt.py`: Checks prompt metadata, placeholder syntax, required fields
- `score_prompt.py`: Runs prompt on example inputs and reports accuracy/F1
- `run_pipeline.py`: Executes full pipeline (reads raw data, applies prompts, writes sanitized output)

---

## ☁️ AWS Infrastructure (Terraform)

- `infra/aws_s3.tf`: GDPR-compliant S3 buckets with encryption and lifecycle rules
- `infra/aws_iam.tf`: OIDC IAM roles for ECS and GitHub Actions
- `infra/ecs_taskdef.json`: ECS Task Definitions for containerized deployment

**S3 Folders:**

- `raw_data/`: Unprocessed, possibly PII-containing data (strict access)
- `sanitized_data/`: Anonymized or classified output (safe for downstream usage)

---

## 🔁 CI/CD with GitHub Actions

Located in `.github/workflows/ci-cd.yml`, our pipeline:

- Validates prompt templates and metadata
- Runs unit/integration tests
- Evaluates prompt scoring on test data
- Builds Docker image, pushes to ECR
- Deploys to ECS on successful quality gate
- Auto-rolls back if performance degrades

**Security:** Uses OIDC authentication – no long-lived AWS credentials stored.

---

## 🧪 Reproducibility & Audit

- Prompt templates are versioned with changelogs and metrics
- Data batches and datasets are hashed (SHA-256)
- All executions log input/output references with prompt version
- Dockerized environment ensures consistent runtime
- CloudTrail + S3 access logs track every interaction

---

## 📈 Future Enhancements

- Airflow DAG integration for orchestration
- Real-time monitoring + anomaly detection via CloudWatch
- Automated scoring on live production samples
- Full metadata search interface for all prompt versions

---

## 🛡 Security & Compliance

- 🔐 Encryption at rest (KMS), in transit (TLS)
- 🧾 IAM Least Privilege: ECS tasks, CI/CD roles
- 📍 Data residency enforcement (e.g., eu-central-1)
- 📊 PII minimization + lifecycle deletion (S3 rules)
- 📓 Prompt audit logging + rollback tags

---

## 📄 License

This project is open-source and AWS-native only. No proprietary dependencies. Complies with GDPR and follows best practices for enterprise ML systems.

---

## ✍️ Maintainers

- AI DevOps Engineering – `devops@yourcompany.com`
- Prompt Architects – `prompts@yourcompany.com`

---

## ✅ Status: Bootstrapped

Ready for:

- Team contributions
- Prompt onboarding
- Secure AWS deployment
