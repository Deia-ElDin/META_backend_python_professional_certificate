import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import print_separator, print_file_header


print_file_header("1-python_functions.py")

def sum(x, y):
    return x + y

print(sum(1, 2))

print_separator()

# bill = 175.00

# tax_rate = 15

# total_tax = (bill * tax_rate) / 100

# print("Total tax: ", total_tax)

# print_separator()

def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100, 2)

print("Total tax: ", calculate_tax(175.00, 15))
print("Total tax: ", calculate_tax(164.33, 22))

print_separator()

