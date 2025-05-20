# Color definitions
YELLOW   := \033[1;33m
GREEN    := \033[1;32m
BLUE     := \033[1;34m
RED      := \033[1;31m
RESET    := \033[0m
NL       := \n

# Project-specific Docker configuration
PROJECT 	:= python_programming
IMAGE 		:= $(PROJECT)_img
CONTAINER	:= $(PROJECT)_container

# Module paths
M1 := Module_1/
M2 := Module_2/
M3 := Module_3/
M4 := Module_4/
M5 := Module_5/

check_container:
	@docker ps | grep $(CONTAINER) > /dev/null || (printf "$(RED)Error: Container $(CONTAINER) is not running. Run 'make all' in the project directory first.$(RESET)$(NL)"; exit 1)
