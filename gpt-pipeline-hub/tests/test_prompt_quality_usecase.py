# test\_prompt\_quality\_usecase.py

# --------------------------------------

# Purpose:

# Unit test to verify that a given prompt template for use case extraction

# passes all defined quality checks in English.

# Goals:

# - Ensure prompt templates conform to quality standards

# - Enable automatic CI checks for regression prevention

# Use Cases:

# - Part of pre-merge checks in CI pipelines

# - Local test validation for prompt authors

from prompt\_quality.validate\_prompt\_quality\_en import validate\_prompt\_en
import json

# Test quality of a use case extraction template prompt

# -----------------------------------------------------

def test\_usecase\_extraction\_quality():
with open("prompts/templates/usecase\_extraction.template.json") as f:
template = json.load(f)

```
# Assumes the 'instruction' field contains the prompt body
prompt_text = template["instruction"]
result = validate_prompt_en(prompt_text)

# All checks must pass
for check, passed in result.items():
    assert passed, f"Prompt failed on: {check}"
```
