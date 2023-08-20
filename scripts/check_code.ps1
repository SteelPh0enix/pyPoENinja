Write-Output "Linting with flake8..."
poetry run flake8 .
Write-Output "Running tests..."
poetry run pytest
