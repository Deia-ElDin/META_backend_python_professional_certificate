COLOR_YELLOW   := \033[1;33m
COLOR_GREEN    := \033[1;32m
COLOR_BLUE     := \033[1;34m
COLOR_RESET    := \033[0m

IMG_NAME := 2nd_course_1st_module_img
CON_NAME := 2nd_course_1st_module_con

py_file_1 := python_syntax.py
py_file_2 := python_datatypes.py
py_file_3 := pythn_string.py
py_file_4 := python_typecasting.py

.PHONY: all info build clean run1 run2 run3 run4 fclean re

all:
	@make build
	@make clean
	@docker run -d --name $(CON_NAME) -v "$(shell pwd):/app/Module_1" $(IMG_NAME) tail -f /dev/null
	@printf "$(COLOR_GREEN)Container $(CON_NAME) is running in detached mode$(COLOR_RESET)\n"
	@make info

info:
	@printf "$(COLOR_YELLOW)Available rules:$(COLOR_RESET)\n"
	@echo "  run1   - Run python_syntax.py"
	@echo "  run2   - Run python_datatypes.py"
	@echo "  run3   - Run pythn_string.py"
	@echo "  run4   - Run python_typecasting.py"
	@echo "  clean  - Remove the container"
	@echo "  fclean - Remove the container and image"
	@echo "  re     - Remove everything and start fresh"
	@printf "$(COLOR_BLUE)Usage:$(COLOR_RESET)\n"
	@echo "  make run1 - Runs $(py_file_1)"
	@echo "  make run2 - Runs $(py_file_2)"
	@echo "  make run3 - Runs $(py_file_3)"
	@echo "  make run4 - Runs $(py_file_4)"
	
build:
	@docker build --no-cache -t $(IMG_NAME) .

clean:
	@docker rm -f $(CON_NAME) 2>/dev/null || true

run1:
	@docker exec $(CON_NAME) python $(py_file_1)

run2:
	@docker exec $(CON_NAME) python $(py_file_2)

run3:
	@docker exec $(CON_NAME) python $(py_file_3)

run4:
	@docker exec $(CON_NAME) python $(py_file_4)

fclean: clean
	@docker rmi -f $(IMG_NAME) 2>/dev/null || true

re: fclean all 