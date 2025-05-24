include project.mk

.PHONY: info git

.DEFAULT_GOAL := info

info:
	@printf "$(YELLOW)$(NL)Available rules:$(RESET)$(NL)"
	@echo "  info        - Display this information"
	@echo "  git         - Commit course-level changes with prefix"

	@printf "$(BLUE)$(NL)Usage:$(RESET)$(NL)"
	@echo "  make info   - Display this information"
	@echo "  make git MSG=\"your message\" - Commit course-level changes with prefix$(NL)"

git:
	@if [ -z "$(MSG)" ]; then \
		printf "$(RED)Error: Please provide a commit message using MSG=\"your message\"$(RESET)$(NL)"; \
		exit 1; \
	fi
	@git add .
	@git commit -m '3rd Course - Version Control: $(MSG)'
	@printf "$(GREEN)Course-level changes committed with message: 3rd Course - Version Control: $(MSG)$(RESET)$(NL)"
	@git push
	@printf "$(YELLOW)Course-level changes pushed to remote repository$(RESET)$(NL)"
