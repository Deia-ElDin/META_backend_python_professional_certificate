'''
    1- Numeric
        1. Integer
        2. Float
        3. Complex Number
    2- Sequence
        1. String
        2. List 
        3. Tuples
    3- Dictionary 
    4- Boolean
    5- Set
'''

# Numbers
integer_num = 10
float_num = 3.14
complex_num = 1 + 2j

print("Integer:", integer_num)
print("Float:", float_num)
print("Complex:", complex_num)

# Strings
single_quoted = 'Hello'
double_quoted = "World"
multi_line = """This is a
multi-line string"""

print("\nStrings:")
print(single_quoted)
print(double_quoted)
print(multi_line)

# Lists
my_list = [1, 2, 3, "Python", True]
print("\nList:", my_list)
print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Slicing:", my_list[1:3])

# Tuples
my_tuple = (1, 2, 3, "Python", True)
print("\nTuple:", my_tuple)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Dictionaries
my_dict = {
    "name": "Python",
    "version": 3.9,
    "is_awesome": True
}
print("\nDictionary:", my_dict)
print("Name:", my_dict["name"])
print("Version:", my_dict["version"])

# Sets
my_set = {1, 2, 3, 3, 4, 4, 5}  # Duplicates are removed
print("\nSet:", my_set)

# Boolean
is_true = True
is_false = False
print("\nBoolean values:")
print("True:", is_true)
print("False:", is_false)

# None
empty_value = None
print("\nNone value:", empty_value)