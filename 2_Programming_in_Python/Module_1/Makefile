YELLOW   := \033[1;33m
GREEN    := \033[1;32m
BLUE     := \033[1;34m
RED      := \033[1;31m
RESET    := \033[0m
NL       := \n

CON_NAME := course_2_programming_in_python_con

GIT_COMMIT_PREFIX := "2nd Course - Programming in Python - Module 1"

py_file_1 := python_syntax.py
py_file_2 := python_datatypes.py
py_file_3 := pythn_string.py
py_file_4 := python_typecasting.py
py_file_5 := python_userinput.py
py_file_6 := python_test1.py
py_file_7 := python_operators.py
py_file_8 := python_controlflow.py
py_file_9 := python_match.py
py_file_10 := python_loop.py
py_file_11 := python_nestedloops.py 

.PHONY: all info git run1 run2 run3 run4 run5 run6 run7 run8 run9 run10 run11	

info:
	@printf "$(YELLOW)$(NL)Available rules:$(RESET)$(NL)"
	@echo "  all         - Display this information"
	@echo "  info        - Display this information"
	@echo "  run1        - Run $(py_file_1)"
	@echo "  run2        - Run $(py_file_2)"
	@echo "  run3        - Run $(py_file_3)"
	@echo "  run4        - Run $(py_file_4)"
	@echo "  run5        - Run $(py_file_5)"
	@echo "  run6        - Run $(py_file_6)"
	@echo "  run7        - Run $(py_file_7)"
	@echo "  run8        - Run $(py_file_8)"
	@echo "  run9        - Run $(py_file_9)"
	@echo "  run10       - Run $(py_file_10)"
	@echo "  run11       - Run $(py_file_11)"
	@echo "  git         - Commit changes with prefix"
	
	@printf "$(BLUE)$(NL)Usage:$(RESET)$(NL)"
	@echo "  make run1   - Runs $(py_file_1)"
	@echo "  make run2   - Runs $(py_file_2)"
	@echo "  make run3   - Runs $(py_file_3)"
	@echo "  make run4   - Runs $(py_file_4)"
	@echo "  make run5   - Runs $(py_file_5)"
	@echo "  make run6   - Runs $(py_file_6)"
	@echo "  make run7   - Runs $(py_file_7)"
	@echo "  make run8   - Runs $(py_file_8)"
	@echo "  make run9   - Runs $(py_file_9)"
	@echo "  make run10  - Runs $(py_file_10)"
	@echo "  make run11  - Runs $(py_file_11)"
	@echo "  make git MSG=\"your message\" - Commit with prefix"

check_container:
	@docker ps | grep $(CON_NAME) > /dev/null || (printf "$(RED)Error: Container $(CON_NAME) is not running. Run 'make all' in the project directory first.$(RESET)$(NL)"; exit 1)

git:
	@if [ -z "$(MSG)" ]; then \
		printf "$(RED)Error: Please provide a commit message using MSG=\"your message\"$(RESET)$(NL)"; \
		exit 1; \
	fi
	@git add .
	@git commit -m '$(GIT_COMMIT_PREFIX): $(MSG)'
	@printf "$(GREEN)Module-level changes committed with message: $(GIT_COMMIT_PREFIX): $(MSG)$(RESET)$(NL)"
	@git push
	@printf "Module-level changes pushed to remote repository$(NL)"

run1: check_container
	@docker exec $(CON_NAME) python /app/Module_1/$(py_file_1)

run2: check_container
	@docker exec $(CON_NAME) python /app/Module_1/$(py_file_2)

run3: check_container
	@docker exec $(CON_NAME) python /app/Module_1/$(py_file_3)

run4: check_container
	@docker exec $(CON_NAME) python /app/Module_1/$(py_file_4)

run5: check_container
	@docker exec -it $(CON_NAME) python /app/Module_1/$(py_file_5)

run6: check_container
	@docker exec -it $(CON_NAME) python /app/Module_1/$(py_file_6)

run7: check_container
	@docker exec $(CON_NAME) python /app/Module_1/$(py_file_7)

run8: check_container
	@docker exec $(CON_NAME) python /app/Module_1/$(py_file_8)

run9: check_container
	@docker exec $(CON_NAME) python /app/Module_1/$(py_file_9)

run10: check_container
	@docker exec $(CON_NAME) python /app/Module_1/$(py_file_10)

run11: check_container
	@docker exec $(CON_NAME) python /app/Module_1/$(py_file_11)

# Completed Module 1