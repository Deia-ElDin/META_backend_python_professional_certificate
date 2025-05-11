include ../../common.mk

py_file_1 := 1-python_algorithm.py
py_file_2 := 2-python_pure_vs_traditional_functions.py
py_file_3 := 3-string_reversal.py
py_file_4 := 4-python_map_filter.py

.PHONY: all info git run1 run2 run3 run4

.DEFAULT_GOAL := info

info:
	@printf "$(YELLOW)$(NL)Available rules:$(RESET)$(NL)"
	@echo "  all         - Display this information"
	@echo "  info        - Display this information"
	@echo "  run1        - Run $(py_file_1)"
	@echo "  run2        - Run $(py_file_2)"
	@echo "  run3        - Run $(py_file_3)"
	@echo "  run4        - Run $(py_file_4)"
	@echo "  git         - Commit changes with prefix"
	
	@printf "$(BLUE)$(NL)Usage:$(RESET)$(NL)"
	@echo "  make run1   - Runs $(py_file_1)"
	@echo "  make run2   - Runs $(py_file_2)"
	@echo "  make run3   - Runs $(py_file_3)"
	@echo "  make run4   - Runs $(py_file_4)"
	@echo "  make git MSG=\"your message\" - Commit with prefix$(NL)"

git:
	@if [ -z "$(MSG)" ]; then \
		printf "$(RED)Error: Please provide a commit message using MSG=\"your message\"$(RESET)$(NL)"; \
		exit 1; \
	fi
	@git add .
	@git commit -m '2nd Course - Programming in Python - Module 3: $(MSG)'
	@printf "$(GREEN)Module-level changes committed with message: 2nd Course - Programming in Python - Module 3: $(MSG)$(RESET)$(NL)"
	@git push
	@printf "$(YELLOW)Module-level changes pushed to remote repository$(RESET)$(NL)"

run1: check_container
	@docker exec $(CON_NAME) python $(C2_M3)$(py_file_1)

run2: check_container
	@docker exec $(CON_NAME) python $(C2_M3)$(py_file_2)

run3: check_container
	@docker exec $(CON_NAME) python $(C2_M3)$(py_file_3)

run4: check_container
	@docker exec $(CON_NAME) python $(C2_M3)$(py_file_4)
