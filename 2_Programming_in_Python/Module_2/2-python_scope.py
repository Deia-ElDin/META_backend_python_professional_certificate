import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import print_separator, print_file_header

print_file_header("2-python_scope.py")

'''
    Python Scope types:
        - Local
        - Enclosing
        - Global
        - Built-in

    together they form the LEGB rule

    the puropse  of scope is to protect the variable from being changed by accident
'''

my_glbal = 10

def fn1():
    local_var = 5
    print ("Acccess the Global variable: ", my_glbal)

fn1()

print ("Access the Global variable: ", my_glbal)

print_separator()