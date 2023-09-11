#!/bin/sh
echo "Sorting imports..."
poetry run isort pypoeninja/* tests/*
echo "Formatting with black..."
poetry run black pypoeninja/* tests/*
