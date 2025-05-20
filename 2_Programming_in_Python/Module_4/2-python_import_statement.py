import sys

sys.path.insert(1, r'/Users/dehamad/Desktop/meta_python/2_Programming_in_Python/Module_4/test_import_statement.py') 
import test_import_statement

from math import sqrt, factorial as f 

import math as m # aliace naming

print(test_import_statement.names)

print("\n--------------------------------\n")

print("sqrt = ", str(sqrt(9)))

print("\n--------------------------------\n")

print("cos = ", str(m.cos(0)))

print("\n--------------------------------\n")

print("f = ", str(f(10)))