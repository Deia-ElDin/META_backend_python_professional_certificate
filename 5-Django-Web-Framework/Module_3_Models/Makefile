include ../project.mk

.PHONY: info git build up down logs sh django-startproject django-startapp migrate makemigrations superuser run freeze

.DEFAULT_GOAL := info

info:
	@printf "$(YELLOW)$(NL)Available rules (Module 3 - Models, Docker):$(RESET)$(NL)"
	@echo "  info               - Display this information"
	@echo "  git                - Commit changes with prefix"
	@echo "  build              - Build Docker image"
	@echo "  up                 - Start container in background"
	@echo "  down               - Stop and remove containers"
	@echo "  logs               - Tail logs"
	@echo "  sh                 - Shell into web container"
	@echo "  django-startproject- Create Django project in /app (NAME=models_project)"
	@echo "  django-startapp    - Create app (APP=myapp)"
	@echo "  run                - Run dev server at :8000"
	@echo "  migrate            - Run migrations"
	@echo "  makemigrations     - Make migrations"
	@echo "  superuser          - Create superuser"
	@echo "  freeze             - Export requirements.txt$(NL)"

git:
	@if [ -z "$(msg)" ]; then \
		printf "$(RED)Error: Please provide a commit message using msg=\"your message\"$(RESET)$(NL)"; \
		exit 1; \
	fi
	@git add .
	@git commit -m '5th Course - Django Web Framework - Module 3: $(msg)'
	@printf "$(GREEN)Module-level changes committed with message: 5th Course - Django Web Framework - Module 3: $(msg)$(RESET)$(NL)"
	@git push
	@printf "$(YELLOW)Module-level changes pushed to remote repository$(RESET)$(NL)"

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f web

sh:
	docker compose exec web bash

NAME ?= models_project
django-startproject:
	docker compose exec web bash -lc "django-admin startproject $(NAME) ."

APP ?= myapp
django-startapp:
	docker compose exec web bash -lc "python manage.py startapp $(APP)"

run:
	docker compose exec -T web bash -lc "python manage.py runserver 0.0.0.0:8000"

migrate:
	docker compose exec -T web bash -lc "python manage.py migrate"

makemigrations:
	docker compose exec -T web bash -lc "python manage.py makemigrations"

superuser:
	docker compose exec web bash -lc "python manage.py createsuperuser"

freeze:
	docker compose exec -T web bash -lc "pip freeze > requirements.txt"


