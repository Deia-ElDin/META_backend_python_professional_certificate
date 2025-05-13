import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import print_separator, print_file_header

print_file_header("9-python_class_practice_payment_info.py")



class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet"
        
nathan = Payslips("Nathan", "no", 1000)
roger = Payslips("Roger", "no", 3000)

print(nathan.status(), "\n", roger.status())

nathan.pay()

print("\nAfter payment: \n" + nathan.status(), "\n", roger.status())