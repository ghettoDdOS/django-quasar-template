# Including commands
run-django-server:
	cd backend && poetry run task server localhost:8000

run-quasar-server:
	cd frontend && quasar dev -m pwa

install-backend:
	cd backend && poetry run pip install -U setuptools
	cd backend && poetry install --no-root

install-frontend:
	cd frontend && yarn

.PHONY: createadmin
createadmin:
	cd backend && poetry run task createsuperuser

.PHONY: migrate
migrate:
	cd backend && poetry run task migrate

.PHONY: migrations
migrations:
	cd backend && poetry run task makemigrations

# Primary commands
.PHONY: install
install:
	@make -j 2 install-backend install-frontend
	cd backend && poetry run task initconfig --debug
	@make migrate
	cd backend && poetry run task defaultadmin

.PHONY: run
run:
	@make -j 2 run-django-server run-quasar-server
