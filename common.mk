# Color definitions
YELLOW   := \033[1;33m
GREEN    := \033[1;32m
BLUE     := \033[1;34m
RED      := \033[1;31m
RESET    := \033[0m
NL       := \n

# Docker configuration
IMG_NAME := meta_professional_certificate_img
CON_NAME := meta_professional_certificate_con 

# Course 2 - Programming in Python path
C2_M1 := 2_Programming_in_Python/Module_1/
C2_M2 := 2_Programming_in_Python/Module_2/

check_container:
	@docker ps | grep $(CON_NAME) > /dev/null || (printf "$(RED)Error: Container $(CON_NAME) is not running. Run 'make all' in the project directory first.$(RESET)$(NL)"; exit 1)
