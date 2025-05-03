.PHONY: fclean
.PHONY: install_py

KEEP_IMAGE_REF := python*

install-py:
	@docker pull python

fclean:
	-@docker stop $(docker ps -aq)
	-@docker rm $(docker ps -aq)
	-@docker rmi $(docker images -q -f "reference!=${KEEP_IMAGE_REF}")
	-@docker network rm $(docker network ls -q)
	-@docker volume rm $(docker volume ls -q)


