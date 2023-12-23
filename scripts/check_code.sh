#!/bin/sh
echo "Linting with pylint..."
poetry run pylint ./pypoeninja/**/*.py
poetry run pylint ./tests/**/*.py
echo "Linting with mypy..."
poetry run mypy .
echo "Linting with ruff..."
poetry run ruff ./pypoeninja
poetry run ruff ./tests
echo "Running tests..."
poetry run pytest
