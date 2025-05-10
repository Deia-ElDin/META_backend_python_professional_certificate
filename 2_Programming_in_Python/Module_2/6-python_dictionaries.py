import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import print_separator, print_file_header

print_file_header("6-python_dictionaries.py")

my_dict1 = {"name": "Deia", "city": "Abu Dhabi"}

print ("my_dict1: ", my_dict1)

my_dict1["city"] = "Dubai"

print ("my_dict1 after changing city: ", my_dict1)

my_dict1["is_student"] = False

print ("my_dict1 after adding is_student: ", my_dict1)

my_dict1.pop("is_student")

print ("my_dict1 after popping is_student: ", my_dict1)

del my_dict1["city"]

print ("my_dict1 after deleting city: ", my_dict1)

my_dict1.clear()

print ("my_dict1 after clearing: ", my_dict1)

print_separator()

my_dict2 = {"name": "Deia", "city": "Abu Dhabi"}

print ("my_dict2: ", my_dict2)

for key, value in my_dict2.items():
    print (f"{key}: {value}")

print_separator()