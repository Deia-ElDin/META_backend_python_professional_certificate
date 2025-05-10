import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import print_separator, print_file_header

print_file_header("7-python_args.py")

def sum_of(a, b):
    return a + b

print ("sum_of(1, 2): ", sum_of(1, 2))

# print ("sum_of(1, 2, 3): ", sum_of(1, 2, 3)) # error

print_separator()

def sum_of(*args):
    print ("args: ", args)
    sum = 0
    for num in args:
        sum += num
    return sum

print ("sum_of(1, 2, 3): ", sum_of(1, 2, 3))
