Write-Output "Cleaning up old docs..."
Remove-Item docs/modules.rst -Force
Remote-Item docs/pypoeninja.rst -Force
Write-Output "Generate documentation files..."
poetry run sphinx-apidoc -o docs pypoeninja
Write-Output "Building the docs..."
poetry run sphinx-build -b html docs site-content
Write-Output "Measuring coverage..."
poetry run coverage run -m pytest
Write-Output "Generating coverage report..."
poetry run coverage html -d site-content/coverage-report
