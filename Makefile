

ifndef VIRTUAL_ENV
	venv=install
endif

SOURCE_ROOT=sbx
PYTHON_SCRIPT=main.py

install:
	@echo "-------------------"
	@echo "install venv"
	@echo "-------------------"
	python -m venv venv
	venv/bin/pip install -r requirements.txt

default: $(venv)
	@echo "-------------------"
	@echo "run ${PYTHON_SCRIPT}"
	@echo "-------------------"
	venv/bin/ptw ${PYTHON_SCRIPT} -- -vv

clean:
	@echo "-------------------"
	@echo "clean: clean all generated artifacts (docker-compose volumnes, build/, dist/, docs/_build/, *.pyc, etc)"
	@echo "-------------------"
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info
	rm -fr .eggs
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find ./${SOURCE_ROOT} -name '**__pycache__' -exec rm -rf {} +
	find . -name '.pytest_cache' -exec rm -rf {} +
	find . -name '.coverage' -exec rm -rf {} +
	find . -name 'test.db' -exec rm -f {} +
	rm -fr ci_reports
	find . -name '*.log' -exec rm -f {} +
	rm -rf docs/_build
	rm -rf docs/${SOURCE_ROOT}*.rst
	rm -rf docs/modules.rst
	# docker-compose --file docker-compose.yml --file docker-compose.test.yml down --volumes
