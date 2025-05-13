import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import print_separator, print_file_header

print_file_header("8-python_class_init.py")



class Recipe():
    # def __new__(cls: type[self]) -> self: 
    #     pass 

    # def __init__(self) -> None:
    #     pass
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The " + self.dish + " has " + str(self.items) + \
              " and takes " + str(self.time) + " min to prepare")
        
pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 55)

print (pizza.items)
print (pasta.items)

print (pizza.contents())
print (pasta.contents())