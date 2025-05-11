include ../../common.mk

py_file_1 := 1-python_algorithm.py

.PHONY: all info git run1 

.DEFAULT_GOAL := info

info:
	@printf "$(YELLOW)$(NL)Available rules:$(RESET)$(NL)"
	@echo "  all         - Display this information"
	@echo "  info        - Display this information"
	@echo "  run1        - Run $(py_file_1)"
	@echo "  git         - Commit changes with prefix"
	
	@printf "$(BLUE)$(NL)Usage:$(RESET)$(NL)"
	@echo "  make run1   - Runs $(py_file_1)"
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

