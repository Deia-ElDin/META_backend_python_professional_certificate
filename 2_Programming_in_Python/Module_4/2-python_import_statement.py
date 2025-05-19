import sys
import os
import numpy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import print_separator, print_file_header

sys.path.insert(1, r'/Users/dehamad/Desktop/meta_python/2_Programming_in_Python/Module_4/test_import_statement.py') 
import test_import_statement

from math import sqrt, factorial as f 

import math as m # aliace naming


print_file_header("python_import_statement.py")


print(test_import_statement.names)

print_separator()

print("sqrt = ", str(sqrt(9)))

print_separator()

print("cos = ", str(m.cos(0)))

print_separator()

print("f = ", str(f(10)))