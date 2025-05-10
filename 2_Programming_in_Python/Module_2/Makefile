include ../common.mk

GIT_COMMIT_PREFIX := "2nd Course - Programming in Python - Module 2"

py_file_1 := puthon_functions.py

.PHONY: all info git run1 run2 run3 run4 run5 run6 run7 run8 run9 run10 run11	

info:
	@printf "$(YELLOW)$(NL)Available rules:$(RESET)$(NL)"
	@echo "  all         - Display this information"
	@echo "  info        - Display this information"
	@echo "  run1        - Run $(py_file_1)"
	@echo "  git         - Commit changes with prefix"
	
	@printf "$(BLUE)$(NL)Usage:$(RESET)$(NL)"
	@echo "  make run1   - Runs $(py_file_1)"
	@echo "  make git MSG=\"your message\" - Commit with prefix$(NL)"

check_container:
	@docker ps | grep $(CON_NAME) > /dev/null || (printf "$(RED)Error: Container $(CON_NAME) is not running. Run 'make all' in the project directory first.$(RESET)$(NL)"; exit 1)

git:
	@if [ -z "$(MSG)" ]; then \
		printf "$(RED)Error: Please provide a commit message using MSG=\"your message\"$(RESET)$(NL)"; \
		exit 1; \
	fi
	@git add .
	@git commit -m '$(GIT_COMMIT_PREFIX): $(MSG)'
	@printf "$(GREEN)Module-level changes committed with message: 2nd Course - Programming in Python - Module 2: $(MSG)$(RESET)$(NL)"
	@git push
	@printf "$(YELLOW)Module-level changes pushed to remote repository$(RESET)$(NL)"

run1: check_container
	@docker exec $(CON_NAME) python /app/Module_2/$(py_file_1)
