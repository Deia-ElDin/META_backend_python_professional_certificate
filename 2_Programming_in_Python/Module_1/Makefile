COLOR_YELLOW   := \033[1;33m
COLOR_GREEN    := \033[1;32m
COLOR_BLUE     := \033[1;34m
COLOR_RESET    := \033[0m
NL 			   := \n

IMG_NAME := 2nd_course_1st_module_img
CON_NAME := 2nd_course_1st_module_con

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

.PHONY: all info build clean fclean re git \
	run1 run2 run3 run4 run5 run6 run7 run8 run9 run10 

all:
	@make build
	@make clean
	@docker run -d --name $(CON_NAME) -v "$(PWD):/app/Module_1" $(IMG_NAME) tail -f /dev/null
	@printf "$(COLOR_GREEN)$(NL)Container $(CON_NAME) is running in detached mode$(COLOR_RESET)$(NL)"
	@make info

info:
	@printf "$(COLOR_YELLOW)$(NL)Available rules:$(COLOR_RESET)$(NL)"
	@echo "  all         - Build, clean and run the container"
	@echo "  info        - Display this information"
	@echo "  clean       - Remove the container"
	@echo "  fclean      - Remove the container and image"
	@echo "  re          - Remove everything and start fresh"
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
	
	@printf "$(COLOR_BLUE)$(NL)Usage:$(COLOR_RESET)$(NL)"
	@echo "  make all    - Build, clean and run the container"
	@echo "  make info   - Display this information"
	@echo "  make clean  - Remove the container"
	@echo "  make fclean - Remove the container and image"
	@echo "  make re     - Remove everything and start fresh"
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
	@echo "  make git MSG=\"your message\" - Commit with prefix"

build:
	@docker build --quiet -t $(IMG_NAME) .

clean:
	@docker rm -f $(CON_NAME) 2>/dev/null || true

fclean: clean
	@docker rmi -f $(IMG_NAME) 2>/dev/null || true

re: fclean all

git:
	@if [ -z "$(MSG)" ]; then \
		printf "$(COLOR_RED)Error: Please provide a commit message using MSG=\"your message\"$(COLOR_RESET)$(NL)"; \
		exit 1; \
	fi
	@git add .
	@git commit -m "2nd Course - Programming in Python - Module 1: $(MSG)"
	@printf "$(COLOR_GREEN)Changes committed with message: 2nd Course - Programming in Python - Module 1: $(MSG)$(COLOR_RESET)$(NL)"
	@git push
	@printf "$(COLOR_GREEN)Changes pushed to remote repository$(COLOR_RESET)$(NL)" 

run1:
	@docker exec $(CON_NAME) python $(py_file_1)

run2:
	@docker exec $(CON_NAME) python $(py_file_2)

run3:
	@docker exec $(CON_NAME) python $(py_file_3)

run4:
	@docker exec $(CON_NAME) python $(py_file_4)

run5:
	@docker exec -it $(CON_NAME) python $(py_file_5)

run6:
	@docker exec -it $(CON_NAME) python $(py_file_6)

run7:
	@docker exec -it $(CON_NAME) python $(py_file_7)

run8:
	@docker exec -it $(CON_NAME) python $(py_file_8)

run9:
	@docker exec -it $(CON_NAME) python $(py_file_9)

run10:
	@docker exec -it $(CON_NAME) python $(py_file_10)

