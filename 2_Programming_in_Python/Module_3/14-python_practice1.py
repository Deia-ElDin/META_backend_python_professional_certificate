import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import print_separator, print_file_header

print_file_header("15-python_practice1.py")



# Example 1
class A:
   def a(self):
       return "Function inside A"

class B:
    def a(self):
        return "Function inside B"

class C(B,A):
    pass

class D(A,B):
    pass

# Driver code
c = C()
print("printing a method from C class where it inherits from (B) first, then (A): ", c.a())
# Class C inherits from classes B and A. 
# When I don't find any function a() inside class C, 
# I should search for classes B and A and its important that I do it in that order.

d = D()
print("printing a method from D class where it inherits from (A) first, then (B): ", d.a())
# Class D inherits from classes A and B.
# When I don't find any function a() inside class D, 
# I should search for classes A and B and its important that I do it in that order.

print_separator()

# Example 2
class A:
    def b(self):
        return "Function inside A"

class B:
    def b(self):
        return "Function inside B"

class C(A, B):
    def b(self):
        return "Function inside C"
    pass

class D(C):
    pass

d = D()
print("printing a method from D class where it inherits from (C): ", d.b())
# Class D inherits from class C, which in turn inherits from classes A and B. 
# Class D accesses the immediate superclass of class D, 
# which is class C and resolves the value of the variable once it's found in that superclass.

print_separator()

# Example 3
class A:
    def c(self):
        return "Function inside A"

class B:
    def c(self):
        return "Function inside B"

class C(A, B):
    def c(self):
        return "Function inside C"

# class D(A, C):
#     pass

# d = D()
# print("printing a method from D class where it inherits from (A) first, then (C): ", d.c())

# Example 4
class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d())
print(F.mro())