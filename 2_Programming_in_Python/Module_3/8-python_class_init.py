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

print("\n--------------------------------\n")

class MyFirstClass():
    # print("Who wrote this?")
    index = "Author-Book"

    def __init__(self):
        print("Who wrote this?")  # Move the print statement into the constructor

    def hand_list(self, philosopher, book):
        print(self.index)
        print(philosopher + " wrote the book: " + book) 

my_first_class = MyFirstClass()
my_first_class.hand_list("Plato", "Republic")