# PowerShell: Setup für neues LLM-Prompt-Repo
$base = "gpt-pipeline-hub"

$folders = @(
  "$base/prompts",
  "$base/evals",
  "$base/cli",
  "$base/scripts",
  "$base/tests",
  "$base/docs",
  "$base/.github/workflows"
)

# Create folders
$folders | ForEach-Object { New-Item -ItemType Directory -Path $_ -Force | Out-Null }

# Standarddateien
New-Item "$base/README.md" -ItemType File -Force | Out-Null
New-Item "$base/LICENSE" -ItemType File -Force | Out-Null
New-Item "$base/requirements.txt" -ItemType File -Force | Out-Null
New-Item "$base/pyproject.toml" -ItemType File -Force | Out-Null
New-Item "$base/.github/workflows/ci.yml" -ItemType File -Force | Out-Null
New-Item "$base/docs/architecture.md" -ItemType File -Force | Out-Null
New-Item "$base/tests/test_run_prompt.py" -ItemType File -Force | Out-Null
New-Item "$base/cli/run_prompt.py" -ItemType File -Force | Out-Null

Write-Host "✅ Neue Repository-Struktur für 'gpt-pipeline-hub' erstellt."
