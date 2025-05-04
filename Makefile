PYTHON_IMAGE := python
NODE_IMAGE := node:lts-alpine

KEEP_IMAGE_REF := $(PYTHON_IMAGE)* $(NODE_IMAGE) $(NEXT_IMAGE)

.PHONY: all fclean pull-imgs py-img node-img

all: pull-imgs

py-img:
	@docker pull $(PYTHON_IMAGE)

node-img:
	@docker pull $(NODE_IMAGE)

pull-imgs: py-img node-img

fclean:
	-@docker stop $(docker ps -aq)
	-@docker rm $(docker ps -aq)
	-@docker rmi $(docker images -q $(foreach img,${KEEP_IMAGE_REF},-f "reference!=$(img)"))
	-@docker network rm $(docker network ls -q)
	-@docker volume rm $(docker volume ls -q)
