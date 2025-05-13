import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import print_separator, print_file_header
from abc import ABC, abstractmethod

print_file_header("11-python_class_abstract.py")



class SomeAbstractClass(ABC):
    @abstractmethod
    def someabstractmethod(self):
        pass 

class Employee(ABC):

    @abstractmethod
    def donate(self):
        pass

class Donation(Employee):
    def donate(self):
        a = input("How much would you like to donate: ")
        return a

amounts = []
john = Donation()
j = john.donate()
amounts.append(j)
    
peter = Donation()
p = peter.donate()
amounts.append(p)

print(amounts)