include common.mk

.PHONY: all info build clean fclean re git

.DEFAULT_GOAL := all

all:
	@make build
	@make clean
	@docker run -d --name $(CON_NAME) -v "$(PWD):/app" $(IMG_NAME) tail -f /dev/null
	@printf "$(GREEN)$(NL)Container $(CON_NAME) is running in detached mode$(RESET)$(NL)"
	@make info

info:
	@printf "$(YELLOW)$(NL)Available rules:$(RESET)$(NL)"
	@echo "  all         - Build the container for the whole certificate, clean it if it exists and run the container"
	@echo "  info        - Display this information"
	@echo "  clean       - Remove the container"
	@echo "  fclean      - Remove the container and image"
	@echo "  re          - Remove everything and start fresh"
	@echo "  git         - Commit Professional Certificate-level changes with prefix"

	@printf "$(BLUE)$(NL)Usage:$(RESET)$(NL)"
	@echo "  make all    - Build, clean and run the container"
	@echo "  make info   - Display this information"
	@echo "  make clean  - Remove the container"
	@echo "  make fclean - Remove the container and image"
	@echo "  make re     - Remove everything and start fresh"
	@echo "  make git MSG=\"your message\" - Commit Professional Certificate-level changes with prefix$(NL)"

build:
	@docker build -t $(IMG_NAME) .

clean:
	@docker rm -f $(CON_NAME) 2>/dev/null || true
	@printf "$(YELLOW)$(NL)Container $(CON_NAME) removed (if it existed).$(RESET)$(NL)"

fclean: clean
	@docker rmi -f $(IMG_NAME) 2>/dev/null || true
	@printf "$(YELLOW)$(NL)Image $(IMG_NAME) removed (if it existed).$(RESET)$(NL)"

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


