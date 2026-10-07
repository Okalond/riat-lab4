param(
    [string]$Python
)

$ErrorActionPreference = "Stop"
Push-Location $PSScriptRoot
try {
    $venvPython = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
    if (-not (Test-Path -LiteralPath $venvPython)) {
        if (-not $Python) {
            $bundledPython = Join-Path ([Environment]::GetFolderPath("UserProfile")) ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
            $Python = if (Test-Path -LiteralPath $bundledPython) { $bundledPython } else { "python" }
        }
        & $Python -m venv .venv
        if ($LASTEXITCODE -ne 0) { throw "Cannot create Python environment." }
    }
    & $venvPython -m pip install -r requirements-dev.txt
    if ($LASTEXITCODE -ne 0) { throw "Dependency installation failed." }
    & $venvPython -m pytest --junitxml=test-results/junit.xml
    if ($LASTEXITCODE -ne 0) { throw "Tests failed." }
    & $venvPython -m black --check app.py test_app.py
    if ($LASTEXITCODE -ne 0) { throw "Formatting check failed." }
}
finally {
    Pop-Location
}
