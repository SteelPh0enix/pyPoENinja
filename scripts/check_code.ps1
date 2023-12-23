Write-Output "Linting with pylint..."
poetry run pylint ./pypoeninja/**/*.py
poetry run pylint ./tests/**/*.py
Write-Output "Linting with mypy..."
poetry run mypy .
Write-Output "Linting with ruff..."
poetry run ruff ./pypoeninja
poetry run ruff ./tests
Write-Output "Running tests..."
poetry run pytest
