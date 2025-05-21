include ../project.mk

py_file_1  := 1-python_module.py
py_file_2  := 2-python_import_statement.py
py_file_3  := 3-python_scope.py
py_file_4  := 4-python_test1.py
py_file_5  := 5-python_test_packages.py
py_file_6  := 6-python_test1.py

.PHONY: all info git run1 run2 run3 run4 run5 run6

.DEFAULT_GOAL := info

info:
	@printf "$(YELLOW)$(NL)Available rules:$(RESET)$(NL)"
	@echo "  info        - Display this information"
	@echo "  all         - Run all Python files"
	@echo "  run1        - Run $(py_file_1)"
	@echo "  run2        - Run $(py_file_2)"
	@echo "  run3        - Run $(py_file_3)"
	@echo "  run4        - Run $(py_file_4)"
	@echo "  run5        - Run $(py_file_5)"
	@echo "  run6        - Run $(py_file_6)"
	@echo "  git         - Commit changes with prefix"
	
	@printf "$(BLUE)$(NL)Usage:$(RESET)$(NL)"
	@echo "  make run1   - Runs $(py_file_1)"
	@echo "  make run2   - Runs $(py_file_2)"
	@echo "  make run3   - Runs $(py_file_3)"
	@echo "  make run4   - Runs $(py_file_4)"
	@echo "  make run5   - Runs $(py_file_5)"
	@echo "  make run6   - Runs $(py_file_6)"
	@echo "  make git MSG=\"your message\" - Commit with prefix$(NL)"

git:
	@if [ -z "$(MSG)" ]; then \
		printf "$(RED)Error: Please provide a commit message using MSG=\"your message\"$(RESET)$(NL)"; \
		exit 1; \
	fi
	@git add .
	@git commit -m '2nd Course - Programming in Python - Module 4: $(MSG)'
	@printf "$(GREEN)Module-level changes committed with message: 2nd Course - Programming in Python - Module 4: $(MSG)$(RESET)$(NL)"
	@git push
	@printf "$(YELLOW)Module-level changes pushed to remote repository$(RESET)$(NL)"

run1: check_container
	@docker exec $(CONTAINER) python $(M4)$(py_file_1)

run2: check_container
	@docker exec $(CONTAINER) python $(M4)$(py_file_2)

run3: check_container
	@docker exec $(CONTAINER) python $(M4)$(py_file_3)

run4: check_container
	@docker exec $(CONTAINER) python $(M4)$(py_file_4)

run5: check_container
	@docker exec $(CONTAINER) python -m pytest $(M4)$(py_file_5)

run6: check_container
	@docker exec $(CONTAINER) python -m pytest --rich --color=yes $(M4)$(py_file_6)

all: run1 run2 run3 run4 run5
	@printf "$(GREEN)All Python files have been executed$(RESET)$(NL)"