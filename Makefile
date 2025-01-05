# Makefile for Python project

# Variables
PYTHON := python3

# Default targets
.PHONY: install lint test format

# Install dependencies
install:
	python -m pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py devopslib

# Test code with pytest
test:
	python -m pytest -vv --cov=devopslib test_*.py

# Format code with Black
format:
	black *.py devopslib/*.py

all: install lint test format 
