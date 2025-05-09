'''
    Type casting is the process of converting one data type to another.
    Common type casting functions:
    1. int() - converts to integer
    2. float() - converts to float
    3. str() - converts to string
    4. list() - converts to list
    5. tuple() - converts to tuple
    6. set() - converts to set
    7. dict() - converts to dictionary
'''

x = 10
float_x = float(x)
print("Integer to Float:", x, "->", float_x)

y = 3.14
int_y = int(y)
print("Float to Integer:", y, "->", int_y)

str_num = "123"
int_num = int(str_num)
print("String to Integer:", str_num, "->", int_num)

# String to Float
str_float = "3.14"
float_num = float(str_float)
print("String to Float:", str_float, "->", float_num)

# Integer to String
num = 42
str_num = str(num)
print("Integer to String:", num, "->", str_num)

# Float to String
pi = 3.14159
str_pi = str(pi)
print("Float to String:", pi, "->", str_pi)

# Boolean conversion
print("\nBoolean conversions:")
print("int(True) =", int(True))
print("int(False) =", int(False))
print("float(True) =", float(True))
print("float(False) =", float(False))
print("str(True) =", str(True))
print("str(False) =", str(False))

# List to String
my_list = [1, 2, 3]
list_str = str(my_list)
print("\nList to String:", my_list, "->", list_str)

# String to List (of characters)
text = "Python"
char_list = list(text)
print("String to List:", text, "->", char_list) 