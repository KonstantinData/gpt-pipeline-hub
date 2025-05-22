# PowerShell: Clean up old repository root

# Liste der Dateien, die entfernt werden sollen (nur im Root)
$obsoleteFiles = @(
  "LICENSE.txt",
  "README.md",
  "pyproject.toml",
  "requirements.lock",
  "requirements-dev.lock",
  "setup-structure-old.ps1"
)

# Entferne veraltete Dateien
foreach ($file in $obsoleteFiles) {
  if (Test-Path $file) {
    Remove-Item -Force $file
    Write-Host "🗑️ Entfernt: $file"
  }
}

# Leeren src-Ordner löschen (falls vorhanden und leer)
if ((Test-Path "src") -and ((Get-ChildItem "src" -Recurse | Measure-Object).Count -eq 0)) {
    Remove-Item -Recurse -Force "src"
    Write-Host "🗑️ Entfernt: src/ (leer)"
}


Write-Host "`n✅ Root-Verzeichnis erfolgreich bereinigt. Nur noch 'gpt-pipeline-hub/' bleibt aktiv."
