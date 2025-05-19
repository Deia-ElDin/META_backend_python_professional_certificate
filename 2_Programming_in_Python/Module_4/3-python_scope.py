import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import print_separator, print_file_header

print_file_header("3-python_scope.py")



def d():
    animal = "elephant"

    def e():
        nonlocal animal 
        animal = "giraffe"
        print("Inside nested function: " + animal)
    
    print("Before calling function: " + animal)
    e()
    print("After calling function: " + animal)

animal = "camel"
d()
print("Global animal: " + animal)