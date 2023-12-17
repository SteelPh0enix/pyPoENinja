#!/bin/sh
echo "Cleaning up old docs..."
rm docs/source/modules.rst
rm docs/source/pypoeninja.rst
echo "Generate documentation files..."
poetry run sphinx-apidoc -o docs/source pypoeninja
echo "Building the docs..."
poetry run sphinx-build -b html docs/source site-content
echo "Measuring coverage..."
poetry run coverage run -m pytest
echo "Generating coverage report..."
poetry run coverage html -d site-content/coverage-report
