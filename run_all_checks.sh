#!/bin/sh

# Run black for code formatting
black .

# Run pylint for linting
pylint src/ libs/ tests/

# Run pydocstyle for docstring conventions
pydocstyle src/ libs/ tests/

# Run pre-commit hooks
pre-commit run --all-files
