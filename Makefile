dev:
	uvicorn app.main:app --reload

migrate:
	alembic revision --autogenerate

db_upgrade:
	alembic upgrade head

db_downgrade:
	alembic downgrade -1

# フォーマッター, リンターなど
black:
	black ./app

isort:
	isort ./app

mypy:
	mypy ./app

flake8:
	pflake8 ./app

format:
	autoflake --recursive --in-place --remove-unused-variables --remove-all-unused-imports --expand-star-imports . --exclude __init__.py
	black ./app
	isort ./app

check:
	black ./app --check
	isort ./app --check-only
	mypy ./app
	pflake8 ./app

test:
	pytest ./app/tests

create_user:
	python -m app.commands.create_user -U admin -P admin -E admin@example.com

fixtures:
	python -m app.commands.fixtures.main

localimport:
	alembic downgrade base && alembic upgrade head && python -m app.commands.localimport.main

openapi:
	python -m app.commands.openapi -o ./docs/openapi.json

tbls:
	tbls doc --rm-dist
