.PHONY: install update shell format lint test sec export configs upgrade run migrate post-test


install:
	@poetry install

update:
	@poetry update

shell:
	@poetry shell

format:
	@blue app/ 
	@blue tests/ 

lint:
	@blue app/ tests/ --check
	@ruff check app/
	@ruff check tests/entities --ignore S101

test:
	@pytest -s tests/entities -x --cov=fast_zero -vv

post-test:
	@coverage html

configs:
	dynaconf -i src.config.settings list

upgrade:
	@poetry run alembic upgrade head

run:
	@poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8001

migrate:
	@poetry run alembic revision --autogenerate
