import sys

sys.path.insert(1, r'/Users/dehamad/Desktop/meta_python/2_Programming_in_Python/Module_4/module_2.py') 
import module_2

from math import sqrt, factorial as f 

import math as m # aliace naming

print(module_2.names)

print("\n--------------------------------\n")

print("sqrt = ", str(sqrt(9)))

print("\n--------------------------------\n")

print("cos = ", str(m.cos(0)))

print("\n--------------------------------\n")

print("f = ", str(f(10)))