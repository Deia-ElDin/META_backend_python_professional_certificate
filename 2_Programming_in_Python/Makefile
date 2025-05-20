include project.mk

.PHONY: all info build clean fclean re git

.DEFAULT_GOAL := all

all:
	@make build
	@make clean
	@docker run -d --name $(CONTAINER) -v "$(CURDIR):/app" $(IMAGE) tail -f /dev/null
	@printf "$(GREEN)$(NL)Container $(CONTAINER) is running in detached mode$(RESET)$(NL)"
	@make info

info:
	@printf "$(YELLOW)$(NL)Available rules:$(RESET)$(NL)"
	@echo "  all         - Build the container for this project, clean it if it exists and run the container"
	@echo "  info        - Display this information"
	@echo "  clean       - Remove the container"
	@echo "  fclean      - Remove the container and image"
	@echo "  re          - Remove everything and start fresh"
	@echo "  git         - Commit course-level changes with prefix"

	@printf "$(BLUE)$(NL)Usage:$(RESET)$(NL)"
	@echo "  make all    - Build, clean and run the container"
	@echo "  make info   - Display this information"
	@echo "  make clean  - Remove the container"
	@echo "  make fclean - Remove the container and image"
	@echo "  make re     - Remove everything and start fresh"
	@echo "  make git MSG=\"your message\" - Commit course-level changes with prefix$(NL)"

build:
	@docker build -t $(IMAGE) .

clean:
	@docker rm -f $(CONTAINER) 2>/dev/null || true
	@printf "$(YELLOW)$(NL)Container $(CONTAINER) removed (if it existed).$(RESET)$(NL)"

fclean: clean
	@docker rmi -f $(IMAGE) 2>/dev/null || true
	@printf "$(YELLOW)$(NL)Image $(IMAGE) removed (if it existed).$(RESET)$(NL)"

re: fclean all

git:
	@if [ -z "$(MSG)" ]; then \
		printf "$(RED)Error: Please provide a commit message using MSG=\"your message\"$(RESET)$(NL)"; \
		exit 1; \
	fi
	@git add .
	@git commit -m '2nd Course - Programming in Python: $(MSG)'
	@printf "$(GREEN)Course-level changes committed with message: 2nd Course - Programming in Python: $(MSG)$(RESET)$(NL)"
	@git push
	@printf "$(YELLOW)Course-level changes pushed to remote repository$(RESET)$(NL)"
