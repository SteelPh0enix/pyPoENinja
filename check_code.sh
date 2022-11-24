#!/bin/sh
echo "Formatting with black..."
poetry run black pypoeninja/* tests/*
echo "Linting with flake8..."
poetry run flake8 .
echo "Running tests..."
poetry run pytest
