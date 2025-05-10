include ../../common.mk

py_file_1 := 1-python_functions.py
py_file_2 := 2-python_scope.py
py_file_3 := 3-python_list.py
py_file_4 := 4-python_tuple.py
py_file_5 := 5-python_sets.py
py_file_6 := 6-python_dictionaries.py
py_file_7 := 7-python_args.py
py_file_8 := 8-python_kwargs.py
py_file_9 := 9-python_test1.py
py_file_10 := 10-python_error_exceptions.py

.PHONY: all info git run1 run2 run3 run4 run5 run6 run7 run8 run9 run10 run11	

.DEFAULT_GOAL := info

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
	@echo "  make run10   - Runs $(py_file_10)"
	@echo "  make git MSG=\"your message\" - Commit with prefix$(NL)"

git:
	@if [ -z "$(MSG)" ]; then \
		printf "$(RED)Error: Please provide a commit message using MSG=\"your message\"$(RESET)$(NL)"; \
		exit 1; \
	fi
	@git add .
	@git commit -m '2nd Course - Programming in Python - Module 2: $(MSG)'
	@printf "$(GREEN)Module-level changes committed with message: 2nd Course - Programming in Python - Module 2: $(MSG)$(RESET)$(NL)"
	@git push
	@printf "$(YELLOW)Module-level changes pushed to remote repository$(RESET)$(NL)"

run1: check_container
	@docker exec $(CON_NAME) python $(C2_M2)$(py_file_1)

run2: check_container
	@docker exec $(CON_NAME) python $(C2_M2)$(py_file_2)

run3: check_container
	@docker exec $(CON_NAME) python $(C2_M2)$(py_file_3)

run4: check_container
	@docker exec $(CON_NAME) python $(C2_M2)$(py_file_4)

run5: check_container
	@docker exec $(CON_NAME) python $(C2_M2)$(py_file_5)

run6: check_container
	@docker exec $(CON_NAME) python $(C2_M2)$(py_file_6)

run7: check_container
	@docker exec $(CON_NAME) python $(C2_M2)$(py_file_7)

run8: check_container
	@docker exec $(CON_NAME) python $(C2_M2)$(py_file_8)

run9: check_container
	@docker exec -it $(CON_NAME) python $(C2_M2)$(py_file_9)

run10: check_container
	@docker exec -it $(CON_NAME) python $(C2_M2)$(py_file_10)
