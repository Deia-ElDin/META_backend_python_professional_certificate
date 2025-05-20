"""
    map(function, iterable)
    filter(function, iterable)

    the map take all objects in a list and applies a function to each object
    the filter take all objects in a list and applies a function to each object and returns a new list with the objects that return true
"""
menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def find_coffe(coffee):
    if coffee[0] == 'c':
        return coffee

map_coffee = map(find_coffe, menu)

print ("type of map_coffee: ", type(map_coffee))
print ("Object map_coffee: ", map_coffee)
for coffee in map_coffee:
    print ("Coffee item: ", coffee)

print("\n--------------------------------\n")

filter_coffee = filter(find_coffe, menu)

print ("type of filter_coffee: ", type(filter_coffee))
print ("Object filter_coffee: ", filter_coffee)
for coffee in filter_coffee:
    print ("Coffee item: ", coffee)



    