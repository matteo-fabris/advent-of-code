setup:
	poetry env use python3.9
	poetry run pip install --upgrade pip

install:
	poetry lock
	poetry install