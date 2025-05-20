'''
    Python Scope types:
        - Local
        - Enclosing
        - Global
        - Built-in

    together they form the LEGB rule

    the puropse  of scope is to protect the variable from being changed by accident

    built-in:
        - functions that are built into python
        - print, len, max, min, etc.
'''

my_glbal = 10

def fn1():
    local_var = 5
    enclosing_var = 20
    def fn2():
        print ("Access the Enclosing variable inside fn2: ", enclosing_var)

    fn2()

    print ("Acccess the Global variable: ", my_glbal)

fn1()

print ("Access the Global variable: ", my_glbal)
# print ("Access the Local variable: ", local_var)
# print ("Access the Enclosing variable: ", enclosing_var)

print("\n--------------------------------\n")