import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import print_file_header

print_file_header("13-python_mro.py")



"""
    mro: method resolution order

    There's many different ways to inherit from a class:
    1- Single / Simple inheritance: A class inherits from a single parent class.
    2- Multiple inheritance: A class inherits from multiple parent classes.
    3- Multilevel inheritance: A class inherits from a child class.
    4- Hierarchical inheritance: Multiple classes inherit from a single parent class.
    5- Hybrid inheritance: A combination of multiple inheritance and multilevel inheritance.

    The order in which a class inherits from a parent class is called the method resolution order (MRO).
    The MRO is the order in which Python looks for a method.
    The MRO is stored in the __mro__ attribute of the class.
    The MRO is used to resolve conflicts when a method is called on an object.

    Developer relay on algorithm to build the MRO:
    - Depth-first search
    - C3 linearization:
        - Adheres to Monotonicity.
        - Follows inheritance graph.
        - Visits super class after local class.

    - Methods arrtribute to find the MRO:   
        - __mro__
        - mro()
        - __class__.__mro__
"""

class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(A.mro())
print(B.mro())
print(C.mro())
