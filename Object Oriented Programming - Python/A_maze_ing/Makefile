run:
	python3 a_maze_ing.py config.txt

install:
	pip install python-dotenv flake8 mypy

debug:
	python3 -m pdb a_maze_ing.py

clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name ".mypy_cache" -type d -exec rm -rf {} +

lint:
	flake8
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8
	mypy --strict .
