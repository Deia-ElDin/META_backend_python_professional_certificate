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

print("\n--------------------------------\n")

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

print("\n--------------------------------\n")

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

"""
F → E → all of E’s parents (in order) → D → all of D’s parents (in order) → C → object
F → E → (B, C) → D (A, B) → C → object
Remove Dublicates 
F → E → B → C → D → A → object

But oops! That violates the parent order of D(A, B) — it says A must come before B, 
but here B came first (from E(B, C)).

So Python fixes that by reordering it to keep parent orders correct 
while still following the "first appearance wins" logic.

F → E → B → C → D → A → object
1 → 2 → 5 → 6 → 3 → 4 → object
F → E → D → A → B → C → object

What's the point of MRO?
    MRO = Method Resolution Order

    It's how Python decides which method to call when there's multiple inheritance.

    Without MRO, Python wouldn’t know which method to run when multiple classes,
    define the same function (.d(), .save(), .render()...)

    It's used for:
        1- Method overrides:
            Shows which class’s method is called when multiple define the same one.

        2- super() calls:
            Determines the next class super() should go to in multi-inheritance.

        3- Mixins:
            Helps control the order and behavior of reusable mixin classes.
"""

print("\n--------------------------------\n")

# Example 5
# 1. Guess the output for the following block of code and try running the code once you have a solution in mind:

class A:
    def b(self):
        return "Function inside A"

class B:
    pass

class C:
    def b(self):
        return "Function inside C"

class D(B, C, A):
    pass

class D(C):
    pass

"""
    D -> C 
    [<class '__main__.D'>, <class '__main__.C'>, <class 'object'>]
"""

d = D()
print(d.b())
print(D.mro())

print("\n--------------------------------\n")

# Example 6
# 2. Guess the output for the following block of code and try running the code once you have a solution in mind:

# class A:
#     def c(self):
#         return "Function inside A"

# class B(A):
#     def c(self):
#         return "Function inside B"

# class C(A,B):
#     pass

# class D(C):
#     pass


# d = D()
# print(d.a)
# print(D.mro())

"""
Error:
TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B
"""

print("\n--------------------------------\n")

# Example 7
# 3. Guess the output for the following block of code and try running the code once you have a solution in mind:

# class A:
#     pass

# class B(A):
#     pass

# class C(B):
#     pass


# c = C()
# print(c.a())

"""
Error:
AttributeError: 'C' object has no attribute 'a'
"""
