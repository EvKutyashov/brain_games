install: #установить зависимости
	poetry install
brain-games: 
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
prompt:
	poetry add prompt
lint:	
	poetry run flake8 brain_games
brain-even:
	poetry run brain-even
