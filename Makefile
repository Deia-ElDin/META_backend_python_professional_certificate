PYTHON_IMAGE := python
NODE_IMAGE := node:lts-alpine

# ANSI color sequences for bold text
COLOR_RESET    := \033[0m
COLOR_RED      := \033[1;31m
COLOR_GREEN    := \033[1;32m
COLOR_YELLOW   := \033[1;33m

KEEP_IMAGE_REF := $(PYTHON_IMAGE)* $(NODE_IMAGE) $(NEXT_IMAGE)

.PHONY: pull-imgs py-img node-img fclean

all:
	@printf "$(COLOR_YELLOW)Available rules:$(COLOR_RESET)\n"
	@echo "  py-img    - Pull the Python image"
	@echo "  node-img  - Pull the Node.js image"
	@echo "  pull-imgs - Pull both Python and Node.js images"
	@echo "  fclean    - Remove all containers, images, networks, and volumes (except built-in networks)"

py-img:
	@docker pull $(PYTHON_IMAGE)

node-img:
	@docker pull $(NODE_IMAGE)

pull-imgs: py-img node-img

fclean:
	@printf "$(COLOR_RED)WARNING: 'make fclean' will delete ALL Docker resources (containers, images, networks, volumes).$(COLOR_RESET)\n"; \
	read -p "Proceed with FULL cleanup? [y/N] " ans; \
	if [ "$$ans" != "y" ]; then printf "$(COLOR_GREEN)Aborted fclean.$(COLOR_RESET)\n"; exit 0; fi; \
	docker stop $$(docker ps -aq); \
	docker rm   $$(docker ps -aq); \
	docker rmi  $$(docker images -q); \
	docker network rm $$(docker network ls -q); \
	docker volume rm  $$(docker volume ls -q)