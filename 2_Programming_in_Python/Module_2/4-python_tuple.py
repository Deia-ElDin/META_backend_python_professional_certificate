import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import print_separator, print_file_header

print_file_header("4-python_tuple.py")

my_tuple = (1, 2, 3, 4, 5)

print ("my_tuple: ", my_tuple)

my_tuple2 = ("Hello", "World", "Python")

print ("my_tuple2: ", my_tuple2)

my_tuple3 = (1, "Hello", True, 40.22)

print ("my_tuple3: ", my_tuple3)

my_tuple4 = () # empty tuple

print ("my_tuple4: ", my_tuple4)

my_tuple5 = (1,) # tuple with one element

print ("my_tuple5: ", my_tuple5)
print ("type of my_tuple5: ", type(my_tuple5))

my_tuple6 = (1) # this is not a tuple, it's an integer

print ("my_tuple6: ", my_tuple6)
print ("type of my_tuple6: ", type(my_tuple6))

print_separator()

my_tuple7 = 0, 1, 3, 2, 'Hello', 4, True, True, False, False, False

print ("my_tuple7: ", my_tuple7) 

print ("my_tuple7[0]: ", my_tuple7[0])
# print ("modify the tuple: ", my_tuple7[0] = 100) # error    

print ("type of my_tuple7: ", type(my_tuple7)) # yet the best practice is to use parentheses
print ("type of my_tuple7[0]: ", type(my_tuple7[0]))

print ("my_tuple7.count(False): ", my_tuple7.count(False))

# return the index of the first occurrence of the value
# yet it will return first occurance of 1 ot True cuz True is 1 in Python (which will be index 1)
print ("my_tuple7.index(True): ", my_tuple7.index(True)) 

# same thing here will return index 0 because 0 = False
print ("my_tuple7.index(False): ", my_tuple7.index(False))

# but this will return index 6 because we start searching from index 2 and we didn't face any value = 1 yet 3, 2 , 'Hello' or 4 are truthy values
# so if we are looking for True we are not looking for truthy values, we are specifically looking for True or 1 
print ("my_tuple7.index(True, 2): ", my_tuple7.index(True, 2))

print_separator()

my_tuple8 = (1, 2, 3, 4, 5)

print ("my_tuple8: ", my_tuple8)

print ("tetsing access by idx: ", my_tuple8[0])
# print ("testing chaning my_tuple8[0] to 100: ", my_tuple8[0] = 100) # error
print ("type of my_tuple8: ", type(my_tuple8))

my_list = list(my_tuple8)
print ("Chaning my_tuple8 to a list: the new type is: ", type(my_list), ", Value: ", my_list)
