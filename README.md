# uvdatabricks

Databricks Asset Bundle (DAB) project using UV as a modern Python dependency manager.

## Description

This project implements a data pipeline in Databricks that works with NYC taxi data. It uses Databricks Asset Bundles for deployment management and UV for Python dependency management.

## Requirements

- Python >= 3.10
- [UV](https://docs.astral.sh/uv/getting-started/installation/) - Dependency manager
- [Databricks CLI](https://docs.databricks.com/dev-tools/cli/databricks-cli.html)
- Pre-commit (automatically installed with setup)

## Initial Setup

### 1. Clone the repository

```bash
git clone https://github.com/pblsnchzrmro/databricks-dab-uv.git
cd databricks-dab-uv
```

### 2. Install dependencies

```bash
uv sync --all-extras --group dev
```

### 3. Configure pre-commit hooks

**Windows (PowerShell):**

```powershell
.\scripts\setup.ps1
```

**Linux/Mac:**

```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

This will install pre-commit hooks that automatically run:

- Basic checks (YAML, JSON)
- Ruff (linting and formatting)
- Mypy (type checking)
- Conventional Commits (commit message validation)

## Local Development

### Run tests

```bash
uv run pytest
```

### With coverage

```bash
uv run pytest --cov=src
```

### Linting and formatting

```bash
# Lint
uv run ruff check .

# Format
uv run ruff format .
```

### Type checking

```bash
uv run mypy src --pretty --show-error-codes
```

## Databricks Deployment

### 1. Authentication

```bash
databricks configure
```

### 2. Deploy to development

```bash
databricks bundle deploy --target dev
```

### 3. Deploy to production

```bash
databricks bundle deploy --target prod
```

### 4. Run the job

```bash
databricks bundle run
```

## CI/CD

The project includes three GitHub Actions workflows:

### 1. **Quality Checks** (`.github/workflows/quality-checks.yml`)

Runs on PRs and checks:

- Linting with Ruff
- Type checking with Mypy
- Tests with Pytest + coverage
- HTML and JSON report generation

### 2. **Validate Bundle** (`.github/workflows/validate.yml`)

Validates the Databricks bundle configuration on PRs.

### 3. **Deploy** (`.github/workflows/deploy.yml`)

Automatically deploys to `dev` or `prod` based on branch.

## Project Structure

```text
databricks-dab-uv/
├── .github/
│   └── workflows/          # GitHub Actions workflows
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── databricks.yml          # DAB configuration
├── pyproject.toml          # Project dependencies and configuration
├── resources/              # Job/pipeline definitions
├── scripts/                # Setup scripts
│   ├── setup.ps1          # Setup for Windows
│   └── setup.sh           # Setup for Linux/Mac
├── src/
│   ├── load.py            # Main script
│   └── uvdatabricks/      # Python package
│       ├── logger/        # Logging module
│       └── utils/         # Utilities (taxis, etc.)
└── tests/                 # Unit tests
```

## Commit Conventions

This project uses [Conventional Commits](https://www.conventionalcommits.org/):

```text
feat: new feature
fix: bug fix
docs: documentation changes
chore: maintenance tasks
test: add or modify tests
refactor: code refactoring
```

## Documentation

- [Databricks Asset Bundles](https://docs.databricks.com/dev-tools/bundles/index.html)
- [UV Package Manager](https://docs.astral.sh/uv/)
- [Databricks CLI](https://docs.databricks.com/dev-tools/cli/databricks-cli.html)
