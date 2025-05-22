# PowerShell: GPT-Pipeline-Hub Architect Mode Setup
$base = "gpt-pipeline-hub"

$folders = @(
  "$base/prompts/00-templates",
  "$base/prompts/01-examples",
  "$base/prompts/02-production",
  "$base/prompts/03-metadata",
  "$base/prompts/04-evals",
  "$base/prompts/98-drafts",
  "$base/evals",
  "$base/cli",
  "$base/tests",
  "$base/scripts",
  "$base/docs",
  "$base/.github/workflows"
)

# Erzeuge Verzeichnisse mit README.md als Platzhalter
$folders | ForEach-Object {
  New-Item -ItemType Directory -Force -Path $_ | Out-Null
  New-Item -ItemType File -Force -Path "$_/README.md" | Out-Null
}

# Basisdateien im Hauptverzeichnis
New-Item "$base/README.md" -ItemType File -Force | Out-Null
New-Item "$base/LICENSE" -ItemType File -Force | Out-Null
New-Item "$base/requirements.txt" -ItemType File -Force | Out-Null
New-Item "$base/pyproject.toml" -ItemType File -Force | Out-Null
New-Item "$base/.gitignore" -ItemType File -Force | Out-Null
New-Item "$base/.github/workflows/ci.yml" -ItemType File -Force | Out-Null

Write-Host "✅ GPT-Pipeline-Hub Struktur im Architect Mode erfolgreich erstellt."
