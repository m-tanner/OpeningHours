#!/bin/zsh
# run from project root as
# /bin/zsh ci.sh

echo "Running: source activate venv/bin/activate"
source activate venv/bin/activate

echo "Running: pylint -j 0 src/ --errors-only"
pylint -j 0 src/ --errors-only
echo "Running: pylint -j 0 tests/ --errors-only"
pylint -j 0 tests/ --errors-only

echo "Running: flake8 src/"
flake8 src/
echo "Running: flake8 tests/"
flake8 tests/

echo "Running: black --check src/"
black --check src/
echo "Running: black --check tests/"
black --check tests/

echo "Running: pytype"
pytype

echo "Running: coverage run --source=src/ -m pytest tests/ -s -v --disable-pytest-warnings"
coverage run --source=src/ -m pytest tests/ -s -v --disable-pytest-warnings
echo "Running: coverage report --omit='src/app/*' -m --fail-under=100"
coverage report --omit='src/app/*' -m --fail-under=100
