include ../project.mk

.PHONY: info git

.DEFAULT_GOAL := info

info:
	@printf "$(YELLOW)$(NL)Available rules:$(RESET)$(NL)"
	@echo "  info        - Display this information"
	@echo "  git         - Commit changes with prefix"
	
	@printf "$(BLUE)$(NL)Usage:$(RESET)$(NL)"
	@echo "  make info   - Display this information"
	@echo "  make git MSG=\"your message\" - Commit with prefix$(NL)"

git:
	@if [ -z "$(MSG)" ]; then \
		printf "$(RED)Error: Please provide a commit message using MSG=\"your message\"$(RESET)$(NL)"; \
		exit 1; \
	fi
	@git add .
	@git commit -m '3rd Course - Version Control - Module 3: $(MSG)'
	@printf "$(GREEN)Module-level changes committed with message: 3rd Course - Version Control - Module 3: $(MSG)$(RESET)$(NL)"
	@git push
	@printf "$(YELLOW)Module-level changes pushed to remote repository$(RESET)$(NL)"
