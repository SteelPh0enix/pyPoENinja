Write-Output "Formatting and fixing issues..."
poetry run ruff --fix ./pypoeninja
poetry run ruff --fix ./tests
