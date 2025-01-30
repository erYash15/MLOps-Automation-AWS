#!/bin/bash

set -e  # Exit immediately if any command fails
set -x  # Print commands before execution (debug mode)

# Install required tools
echo "Installing linting tools..."

# Create Pre-commit config
echo "repos:
  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black

  - repo: https://github.com/PyCQA/isort
    rev: 5.12.0
    hooks:
      - id: isort
" > .pre-commit-config.yaml
