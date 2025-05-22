# Root
$base = "gpt-pipeline-hub"
$dirs = @(
  "$base", "$base/prompts", "$base/cli", "$base/infra",
  "$base/tests", "$base/docs", "$base/.github/workflows",
  "$base/src/gpt_pipeline_hub"
)

# 🔁 Neue Prompt Tasks
$tasks = @(
  "feature_determination",
  "use_case_determination",
  "industry_classification",
  "company_assignment",
  "contact_assignment"
)

# Verzeichnisse für jeden Task
foreach ($task in $tasks) {
  $prefix = "$base/prompts/$task"
  $dirs += "$prefix/prompts", "$prefix/examples", "$prefix/tests"
}

# Erstelle Verzeichnisse
$dirs | ForEach-Object { New-Item -ItemType Directory -Path $_ -Force | Out-Null }

# Standarddateien
New-Item "$base/README.md" -ItemType File -Force
New-Item "$base/LICENSE" -ItemType File -Force
New-Item "$base/.gitignore" -ItemType File -Force
New-Item "$base/requirements.txt" -ItemType File -Force
New-Item "$base/src/gpt_pipeline_hub/__init__.py" -ItemType File -Force
New-Item "$base/.github/workflows/ci-cd.yml" -ItemType File -Force
New-Item "$base/cli/validate_prompt.py" -ItemType File -Force
New-Item "$base/cli/score_prompt.py" -ItemType File -Force
New-Item "$base/cli/run_pipeline.py" -ItemType File -Force
New-Item "$base/infra/aws_s3.tf" -ItemType File -Force
New-Item "$base/infra/aws_iam.tf" -ItemType File -Force
New-Item "$base/infra/ecs_taskdef.json" -ItemType File -Force
New-Item "$base/tests/test_cli.py" -ItemType File -Force

# Platzhalter-Inhalte für Prompts
foreach ($task in $tasks) {
  $t = "$base/prompts/$task"
  New-Item "$t/metadata.yaml" -ItemType File -Force
  Set-Content "$t/prompts/${task}_v1.txt" "# Prompt Template v1 for $task"
  Set-Content "$t/examples/example1_input.txt" "# Example input"
  Set-Content "$t/examples/example1_expected.txt" "# Expected output"
}

Write-Host "✅ Struktur mit aktualisierten Prompt-Tasks erstellt."
