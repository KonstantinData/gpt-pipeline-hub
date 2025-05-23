
# Contributing to GPT Pipeline Hub

Thank you for considering a contribution! Here's how to get started:

## 🛠 Environment Setup

Install [Rye](https://rye-up.com/):
```bash
curl -sSf https://rye-up.com/get | bash
rye sync
```

## 📦 Run Tests

```bash
rye run pytest
```

## ✅ Validate Prompts

```bash
rye run python scripts/validate_prompt.py
```

## 📊 Evaluate Prompts

```bash
rye run python scripts/eval_runner.py
```

## 📂 Prompt Rules

- Place examples in `prompts/01-examples/`
- Each file must have `input` and `expected`
- Use `.json` or `.jsonl`

## 🚀 GitHub Workflow

Commits to `main` trigger prompt validation and evaluation via CI.

## 🤝 Contribution Flow

1. Fork → Branch → PR
2. Add tests for any change
3. Link issues in PR description
