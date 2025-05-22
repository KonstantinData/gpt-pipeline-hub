# 🧠 GPT Pipeline Hub

A modular, secure, and production-grade **prompt lifecycle management system** for large language models (LLMs), built for **classification, extraction, and matching** use cases. Designed for enterprise-grade deployment on AWS ECS, with CI/CD, encryption, and GDPR compliance baked in.

---

## 📌 Overview

This repository serves as the **source of truth** for managing versioned prompt templates, execution pipelines, infrastructure-as-code, and deployment workflows — fully aligned with Architect Mode.

Supported tasks:

* ✅ Feature Determination
* ✅ Use Case Determination
* ✅ Industry Classification
* ✅ Company Assignment
* ✅ Contact Assignment

---

## 📁 Repository Structure (Architect Mode)

```
gpt-pipeline-hub/
├── prompts/
│   ├── 00-templates/       # Reusable building blocks and components
│   ├── 01-examples/        # Sample input/output pairs for each prompt
│   ├── 02-production/      # Validated prompt YAMLs, versioned
│   ├── 03-metadata/        # Prompt description, constraints, input/output schema
│   ├── 04-evals/           # CI evaluation outputs, scorecards
│   └── 98-drafts/          # Exploratory drafts, early-stage iterations
├── cli/                    # Prompt runners, validators, scorers
├── scripts/                # Setup, promotion, evaluation tools
├── tests/                  # Unit/integration tests
├── infra/                  # Terraform modules: S3, IAM, ECS
├── evals/                  # Central benchmark definitions and mappings
├── docs/                   # Architecture, CI logic, onboarding
├── .github/workflows/      # GitHub Actions CI/CD workflows
├── README.md               # This file
├── LICENSE                 # Custom MIT license with restrictions
├── pyproject.toml          # Python project configuration
└── requirements.txt        # Dependency management
```

---

## 🚀 Quickstart (Dev)

```bash
# Install dependencies
pip install -r requirements.txt

# Validate prompts
python cli/validate_prompt.py

# Score prompts using test data
python cli/score_prompt.py

# Run pipeline
python cli/run_pipeline.py --input test.json --output output.json
```

---

## 🔄 Prompt Lifecycle

Prompts follow a structured lifecycle and are modular by design:

* `00-templates/`: Jinja-style or YAML building blocks
* `01-examples/`: Input/output test pairs (used in CI)
* `02-production/`: Active YAML prompts for use in inference
* `03-metadata/`: Formal definitions, input/output schema, changelogs
* `04-evals/`: Evaluation output from CI scoring pipelines
* `98-drafts/`: Early-stage, unvalidated experiments

All prompts are versioned, schema-validated, and CI-tested.

---

## ☁️ Infrastructure (Terraform)

* `infra/aws_s3.tf`: GDPR-compliant S3 buckets
* `infra/aws_iam.tf`: IAM roles for GitHub OIDC, ECS task definitions
* `infra/ecs_taskdef.json`: Secure deployment configuration

### S3 Layout

* `raw_data/`: Original inputs (PII scope, encrypted)
* `sanitized_data/`: Outputs (ready for analysis, compliant)

---

## 🔁 CI/CD Pipeline

Defined in `.github/workflows/ci.yml`, the pipeline:

* Lints and validates prompt schemas
* Tests and benchmarks prompt performance
* Builds Docker containers
* Pushes to Amazon ECR
* Deploys to ECS
* Tags and promotes validated prompt versions
* Rolls back on threshold violation

Security: OIDC-based, no static AWS keys.

---

## 🧪 Reproducibility & Audit

* All prompts have changelogs and schema versions
* Prompt executions are logged with version + hash
* Data batches hashed with SHA-256
* Evaluations stored in `04-evals/`
* Execution environments Dockerized for consistency
* CloudTrail + S3 access logging enabled

---

## 🛡 Security & Compliance

* 🔐 KMS-encrypted S3 buckets
* 📜 TLS in transit, IAM least privilege
* 📊 CI/CD deploy gates enforce accuracy
* 🧾 Prompt audit trail with rollback tagging
* 📍 Region lock & data deletion policies

---

## 📄 License

This project is licensed under a customized [MIT License](LICENSE.txt "double click") with additional restrictions.

* ✅ Use allowed for non-commercial, research, and internal applications
* ❌ Commercial use, resale, or model training/fine-tuning on prompt content is prohibited without permission

See [LICENSE](LICENSE.txt "double click") for details.

---

## ✍️ Maintainers

* Prompt Engineering & Infra: Konstantin Milonas
* Contact: [i](mailto:prompts@yourcompany.com)nfo@condata.io

---

## ✅ Status: Architect Mode Bootstrapped

The structure is production-ready and optimized for scalable, secure LLM-based classification pipelines. Ready for:

* CI/CD integration
* Team collaboration
* Secure AWS deployment
* Structured prompt testing and versioning
