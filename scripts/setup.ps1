# Setup pre-commit hooks for Windows/PowerShell
Write-Host "Installing pre-commit hooks..." -ForegroundColor Cyan
pre-commit install
pre-commit install --hook-type commit-msg
Write-Host "Pre-commit hooks installed successfully" -ForegroundColor Green
