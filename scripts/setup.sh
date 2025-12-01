#!/bin/bash
# Setup pre-commit hooks for Linux/Mac/Git Bash

echo "Installing pre-commit hooks..."
pre-commit install
pre-commit install --hook-type commit-msg
echo "Pre-commit hooks installed successfully"
