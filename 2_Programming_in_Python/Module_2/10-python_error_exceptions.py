"""
    Error & Exceptions:

        Errors:
            - Syntax errors: caused by syntax errors
            - Runtime errors: caused by logic errors

        Exceptions:
            - Errors that are not detected at compile time
            - Errors that are detected at runtime
"""

def divide_by(a, b):
    return a / b

print(divide_by(40, 4))
# print(divide_by(40, 0))

print("\n--------------------------------\n")

try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
except Exception as e:
    print ("Soomething went wrong: ", e)
    print ("Error type: ", type(e))
    print ("Error class: ", e.__class__)