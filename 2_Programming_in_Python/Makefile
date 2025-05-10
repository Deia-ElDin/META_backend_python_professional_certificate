include ../common.mk

.PHONY: info git

.DEFAULT_GOAL := info

info:
	@printf "$(YELLOW)$(NL)Course-level Makefile:$(RESET)$(NL)"
	@echo "  git   - Commit course-level changes with a message"

	@printf "$(BLUE)$(NL)Usage:$(RESET)$(NL)"
	@echo "  make git MSG=\"your message\"$(NL)"

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
