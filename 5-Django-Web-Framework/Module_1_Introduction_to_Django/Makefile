include ../project.mk

.PHONY: info git

.DEFAULT_GOAL := info

info:
	@printf "$(YELLOW)$(NL)Available rules:$(RESET)$(NL)"
	@echo "  info            - Display this information"
	@echo "  git             - Commit changes with prefix"
	@echo "  learnapp-run    - Run Django dev server for learnApp"
	@echo "  builddjango-run - Run Django dev server for buildDjango"
	
	@printf "$(BLUE)$(NL)Usage:$(RESET)$(NL)"
	@echo "  make info   - Display this information"
	@echo "  make git msg=\"your message\" - Commit with prefix"
	@echo "  make learnapp-run"
	@echo "  make builddjango-run$(NL)"

git:
	@if [ -z "$(msg)" ]; then \
		printf "$(RED)Error: Please provide a commit message using msg=\"your message\"$(RESET)$(NL)"; \
		exit 1; \
	fi
	@git add .
	@git commit -m '5th Course - Django Web Framework - Module 1: $(msg)'
	@printf "$(GREEN)Module-level changes committed with message: 5th Course - Django Web Framework - Module 1: $(msg)$(RESET)$(NL)"
	@git push
	@printf "$(YELLOW)Module-level changes pushed to remote repository$(RESET)$(NL)"

# --- Development (no Docker) -------------------------------------------------

.PHONY: learnapp-run builddjango-run

# Paths with spaces are quoted; we call the venv python directly (no activation)
LEARN_PRJ := 2) learnApp/myproject
LEARN_PY  := 2) learnApp/app-env/bin/python

BUILD_PRJ := 1) buildDjango/chefsTable
BUILD_PY  := 1) buildDjango/tutorial-env/bin/python

learnapp-run:
	cd "$(LEARN_PRJ)" && "$(LEARN_PY)" manage.py runserver

builddjango-run:
	cd "$(BUILD_PRJ)" && "$(BUILD_PY)" manage.py runserver
