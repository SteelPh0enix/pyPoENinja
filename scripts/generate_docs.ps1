Write-Output "Cleaning up old docs..."
Remove-Item docs/source/modules.rst -Force -ErrorAction Ignore
Remove-Item docs/source/pypoeninja.rst -Force -ErrorAction Ignore
Write-Output "Generate documentation files..."
poetry run sphinx-apidoc -o docs/source pypoeninja
Write-Output "Building the docs..."
poetry run sphinx-build -b html docs/source site-content
Write-Output "Measuring coverage..."
poetry run coverage run -m pytest
Write-Output "Generating coverage report..."
poetry run coverage html -d site-content/coverage-report
