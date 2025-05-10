# Color definitions
YELLOW   := \033[1;33m
GREEN    := \033[1;32m
BLUE     := \033[1;34m
RED      := \033[1;31m
RESET    := \033[0m
NL       := \n

# Docker configuration
IMG_NAME := course_2_programming_in_python_img
CON_NAME := course_2_programming_in_python_con

# Git messages
GIT_MSG_ERR := "$(RED)Error: Please provide a commit message using MSG=\"your message\"$(RESET)"
GIT_COMMIT_PREFIX := "2nd Course - Programming in Python"
GIT_COMMIT_MSG := "$(GREEN)Course-level changes committed with message: $(GIT_COMMIT_PREFIX): $(MSG)$(RESET)"
GIT_PUSH_MSG := "$(GREEN)Course-level changes pushed to remote repository$(RESET)"

.PHONY: all info build clean fclean re git

all:
	@make build
	@make clean
	@docker run -d --name $(CON_NAME) -v "$(PWD):/app" $(IMG_NAME) tail -f /dev/null
	@printf "%b%bContainer %s is running in detached mode%b%b" "$(GREEN)" "$(NL)" "$(CON_NAME)" "$(RESET)" "$(NL)"
	@make info

info:
	@printf "%b%bAvailable rules:%b%b" "$(YELLOW)" "$(NL)" "$(RESET)" "$(NL)"
	@echo "  all         - Build the container for the whole course, clean it if it exists and run the container"
	@echo "  info        - Display this information"
	@echo "  clean       - Remove the container"
	@echo "  fclean      - Remove the container and image"
	@echo "  re          - Remove everything and start fresh"
	@echo "  git         - Commit course-level changes with prefix"
	@printf "%b%bUsage:%b%b" "$(BLUE)" "$(NL)" "$(RESET)" "$(NL)"
	@echo "  make all    - Build, clean and run the container"
	@echo "  make info   - Display this information"
	@echo "  make clean  - Remove the container"
	@echo "  make fclean - Remove the container and image"
	@echo "  make re     - Remove everything and start fresh"
	@echo "  make git MSG=\"your message\" - Commit course-level changes with prefix"

build:
	@docker build -t $(IMG_NAME) .

clean:
	@docker rm -f $(CON_NAME) 2>/dev/null || true

fclean: clean
	@docker rmi -f $(IMG_NAME) 2>/dev/null || true

re: fclean all

git:
	@if [ -z "$(MSG)" ]; then \
		printf "%b%b" "$(GIT_MSG_ERR)" "$(NL)"; \
		exit 1; \
	fi
	@git add .
	@git commit -m '$(GIT_COMMIT_PREFIX): $(MSG)'
	@printf "%b%b" "$(GIT_COMMIT_MSG)" "$(NL)"
	@git push
	@printf "%b%b" "$(GIT_PUSH_MSG)" "$(NL)"
