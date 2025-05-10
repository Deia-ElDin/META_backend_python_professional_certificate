include common.mk

.PHONY: git

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
