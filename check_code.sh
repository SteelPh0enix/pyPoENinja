#!/bin/sh
./format_code.sh
echo "Linting with flake8..."
poetry run flake8 .
echo "Running tests..."
poetry run pytest
