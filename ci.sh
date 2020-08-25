#!/bin/zsh
# run from project root as
# /bin/zsh ci.sh


source activate venv/bin/activate

pylint -j 0 src/ --errors-only
pylint -j 0 tests/ --errors-only

flake8 src/
flake8 tests/

black --check src/
black --check tests/

pytype

coverage run --source=src/ -m pytest tests/ -s -v --disable-pytest-warnings
coverage report --omit='src/app/*' -m --fail-under=100