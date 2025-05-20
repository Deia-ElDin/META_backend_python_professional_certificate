# Color definitions
YELLOW   := \033[1;33m
GREEN    := \033[1;32m
BLUE     := \033[1;34m
RED      := \033[1;31m
RESET    := \033[0m
NL       := \n

# Course paths
2nd_course := 2_Programming_in_Python

.PHONY: all info clean fclean re git

.DEFAULT_GOAL := all

all:
	@printf "$(GREEN)Starting containers for all courses...$(RESET)$(NL)"
	@make -C $(2nd_course) all
	@printf "$(GREEN)All course containers have been started!$(RESET)$(NL)"

info:
	@printf "$(YELLOW)$(NL)Available rules:$(RESET)$(NL)"
	@echo "  all         - Run all courses"
	@echo "  info        - Display this information"
	@echo "  clean       - Clean all projects"
	@echo "  fclean      - Remove all containers and images"
	@echo "  re          - Remove everything and start fresh"
	@echo "  git         - Commit Professional Certificate-level changes with prefix"

	@printf "$(BLUE)$(NL)Usage:$(RESET)$(NL)"
	@echo "  make all    - Run all courses"
	@echo "  make info   - Display this information"
	@echo "  make clean  - Clean all projects"
	@echo "  make fclean - Remove all containers and images"
	@echo "  make re     - Remove everything and start fresh"
	@echo "  make git MSG=\"your message\" - Commit Professional Certificate-level changes with prefix$(NL)"

clean:
	@make -C $(2nd_course) clean

fclean: clean
	@make -C $(2nd_course) fclean

re: fclean all

git:
	@if [ -z "$(MSG)" ]; then \
		printf "$(RED)Error: Please provide a commit message using MSG=\"your message\"$(RESET)$(NL)"; \
		exit 1; \
	fi
	@git add .
	@git commit -m 'Meta Back-End Developer Professional Certificate: $(MSG)'
	@printf "$(GREEN)Professional Certificate-level changes committed with message: Meta Back-End Developer Professional Certificate: $(MSG)$(RESET)$(NL)"
	@git push
	@printf "$(YELLOW)Professional Certificate-level changes pushed to remote repository$(RESET)$(NL)"


