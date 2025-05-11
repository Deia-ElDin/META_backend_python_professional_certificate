import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import print_separator, print_file_header

print_file_header("2-python_pure_functions.py")



my_list1 = [1, 2, 3]

# this is a traditional function, because it modifies the original list (global variable)
# this is a side effect, because it modifies the original list
def add_to_list(item):
    my_list1.append(item)
    return my_list1

print ("Traditional Function:")
my_new_list1 = add_to_list(4)
print ("my_list1 after appending: ", my_list1)
print ("my_new_list1 after appending: ", my_new_list1)

print_separator()

my_list2 = [1, 2, 3]

# this is a pure function, because it does not modify the original list (global variable)
# this is a pure function, because it does not have any side effects
def add_to_list(lst, item):
    new_lst = lst.copy()
    new_lst.append(item)
    return new_lst

print ("Pure Function:")
my_new_list2 = add_to_list(my_list2, 4)
print ("my_list2 after appending: ", my_list2)
print ("my_new_list2 after appending: ", my_new_list2)



