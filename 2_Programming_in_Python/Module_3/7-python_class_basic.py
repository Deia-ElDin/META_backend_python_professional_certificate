class MyClass:
    # pass # place holder for future code
    a = 5

    def hello(self):
        print ("Hello")

myc = MyClass()

print (MyClass.a)
print (myc.a)
print (myc.hello()) #

print("\n--------------------------------\n")

class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass

house = House()
print(house.num_rooms) # 5  
print(House.num_rooms) # 5

house.num_rooms = 7
print(house.num_rooms) # 7
print(House.num_rooms) # 5
# we did not change the class variable, we changed the instance variable

House.num_rooms = 9
print(house.num_rooms) # 7
print(House.num_rooms) # 9
# we changed the class variable, we changed the class variable for all instances

print("\n--------------------------------\n")

class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 7  # Class variable

    def __init__(self, address):
        self.address = address  # Instance variable

    def cost_evaluation(self):
        print(self.num_rooms)
        pass

# Create first instance
house1 = House("123 Main St")
print("Initial values:")
print("house1.num_rooms:", house1.num_rooms)  # 7
print("House.num_rooms:", House.num_rooms)    # 7

# Change class variable
House.num_rooms = 9
print("\nAfter changing class variable:")
print("house1.num_rooms:", house1.num_rooms)  # Still 7! (existing instance)
print("House.num_rooms:", House.num_rooms)    # 9 (class variable changed)

# Create new instance
house2 = House("456 Oak St")
print("\nNew instance created after change:")
print("house2.num_rooms:", house2.num_rooms)  # 9 (gets new value)
print("house1.num_rooms:", house1.num_rooms)  # Still 7 (unchanged)
print("House.num_rooms:", House.num_rooms)    # 9

