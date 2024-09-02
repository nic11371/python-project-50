install:
	poetry install

gendiff-start:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/hexlet_code-0.1.0-py3-none-any.whl

lint:
	poetry run flake8 gendiff

check:
	poetry run flake8 gendiff

test-coverage:
	poetry run coverage run -m pytest
	# poetry run pytest --cov=gendiff --cov-report xml tests/

test:
	poetry run pytest
