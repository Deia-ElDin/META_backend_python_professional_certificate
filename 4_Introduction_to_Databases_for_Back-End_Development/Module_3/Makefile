include ../project.mk

.PHONY: info git

.DEFAULT_GOAL := info

info:
	@printf "$(YELLOW)$(NL)Available rules:$(RESET)$(NL)"
	@echo "  info        - Display this information"
	@echo "  git         - Commit changes with prefix"
	
	@printf "$(BLUE)$(NL)Usage:$(RESET)$(NL)"
	@echo "  make info   - Display this information"
	@echo "  make git msg=\"your message\" - Commit with prefix$(NL)"

git:
	@if [ -z "$(msg)" ]; then \
		printf "$(RED)Error: Please provide a commit message using msg=\"your message\"$(RESET)$(NL)"; \
		exit 1; \
	fi
	@git add .
	@git commit -m '4th Course - Introduction to Databases for Back-End Development - Module 3: $(msg)'
	@printf "$(GREEN)Module-level changes committed with message: 4th Course - Introduction to Databases for Back-End Development - Module 3: $(msg)$(RESET)$(NL)"
	@git push
	@printf "$(YELLOW)Module-level changes pushed to remote repository$(RESET)$(NL)"
