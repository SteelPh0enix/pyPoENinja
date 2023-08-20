Write-Output "Sorting imports..."
poetry run isort pypoeninja/* tests/*
Write-Output "Formatting with black..."
poetry run black pypoeninja/* tests/*
