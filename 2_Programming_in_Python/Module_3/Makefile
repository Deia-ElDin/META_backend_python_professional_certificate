include ../../common.mk

py_file_1  := 1-python_algorithm.py
py_file_2  := 2-python_pure_vs_traditional_functions.py
py_file_3  := 3-string_reversal.py
py_file_4  := 4-python_map_filter.py
py_file_5  := 5-python_comprehension.py
py_file_6  := 6-python_test1.py	
py_file_7  := 7-python_class_basic.py
py_file_8  := 8-python_class_init.py
py_file_9  := 9-python_class_practice_payment_info.py
py_file_10 := 10-python_class_inheritance.py
py_file_11 := 11-python_class_abstract.py
py_file_12 := 12-python_test2.py
py_file_13 := 13-python_mro.py

.PHONY: all info git run1 run2 run3 run4 run5 run6 run7 run8 run9 run10 run11 run12 run13

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
	@echo "  run11       - Run $(py_file_11)"
	@echo "  run12       - Run $(py_file_12)"	
	@echo "  run13       - Run $(py_file_13)"
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
	@echo "  make run12  - Runs $(py_file_12)"
	@echo "  make run13  - Runs $(py_file_13)"
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

run5: check_container
	@docker exec $(CON_NAME) python $(C2_M3)$(py_file_5)

run6: check_container
	@docker exec $(CON_NAME) python $(C2_M3)$(py_file_6)

run7: check_container
	@docker exec $(CON_NAME) python $(C2_M3)$(py_file_7)

run8: check_container
	@docker exec $(CON_NAME) python $(C2_M3)$(py_file_8)

run9: check_container
	@docker exec $(CON_NAME) python $(C2_M3)$(py_file_9)

run10: check_container
	@docker exec $(CON_NAME) python $(C2_M3)$(py_file_10)	

run11: check_container
	@docker exec -it $(CON_NAME) python $(C2_M3)$(py_file_11)

run12: check_container
	@docker exec $(CON_NAME) python $(C2_M3)$(py_file_12) 

run13: check_container
	@docker exec $(CON_NAME) python $(C2_M3)$(py_file_13)