shell = /bin/bash


PREFIX=slido_assignment


.PHONY: style
style:
	black .
	flake8 .

.ONESHELL:	
.PHONY: reqs
reqs:
	( \
	source .venv/${PREFIX}/bin/activate; \
	pip install --no-cache-dir --upgrade pip; \
	pip install wheel isort; \
	for name in $$( find . -type f -name "*.pip" ); \
	do \
		echo $${name}; \
		pip install --no-cache-dir -r $${name}; \
	done; \
	pre-commit install; \
	)

.PHONY: venv
venv:
	python3 -m venv .venv/${PREFIX}
	make reqs
	@echo "Please use 'source .venv/${PREFIX}/bin/activate' to start using the venv"

# Cleaning
.PHONY: clean
clean:
	find . -type f -name "*.DS_Store" -ls -delete
	find . | grep -E "(__pycache__|.mypy_cache|\.pyc|\.pyo|\.tox)" | xargs rm -rf
	find . | grep -E ".pytest_cache" | xargs rm -rf
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	find . | grep -E ".trash" | xargs rm -rf
	make style
	rm -f .coverage

.PHONY: help
help:
	@echo "Please use 'source .venv/${PREFIX}/bin/activate' to start using the venv"
	@echo "Commands     :"
	@echo "venv         : creates a virtual environment and install all requirements"
	@echo "style        : executes style formatting."
	@echo "clean        : cleans all unnecessary files."
	@echo "test         : run all tests in repo."
	@echo "test_with_prints   : run all tests in repo with logs and prints."