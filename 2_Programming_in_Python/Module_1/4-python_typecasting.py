'''
    Implicit typecasting:
        It is done automatically by the Python interpreter (complier).

    Explicit typecasting:
        It is done manually by the programmer.
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

str_float = "3.14"
float_num = float(str_float)
print("String to Float:", str_float, "->", float_num)

num = 42
str_num = str(num)
print("Integer to String:", num, "->", str_num)

pi = 3.14159
str_pi = str(pi)
print("Float to String:", pi, "->", str_pi)

print("\nBoolean conversions:")
print("int(True) =", int(True))
print("int(False) =", int(False))
print("float(True) =", float(True))
print("float(False) =", float(False))
print("str(True) =", str(True))
print("str(False) =", str(False))

my_list = [1, 2, 3]
list_str = str(my_list)
print("\nList to String:", my_list, "->", list_str)

text = "Python"
char_list = list(text)
print("String to List:", text, "->", char_list) 

# Error example
# my_str = "Hello, World!"
# my_int = (int(my_str))
# print("String to Integer:", my_str, "->", my_int)

