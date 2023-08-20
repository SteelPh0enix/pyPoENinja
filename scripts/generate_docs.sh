#!/bin/sh
echo "Cleaning up old docs..."
rm docs/modules.rst docs/pypoeninja.rst
echo "Generate documentation files..."
poetry run sphinx-apidoc -o docs pypoeninja
echo "Building the docs..."
poetry run sphinx-build -b html docs site-content
echo "Measuring coverage..."
poetry run coverage run -m pytest
echo "Generating coverage report..."
poetry run coverage html -d site-content/coverage-report
