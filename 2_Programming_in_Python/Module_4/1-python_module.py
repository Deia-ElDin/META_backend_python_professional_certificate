import sys
import os
import calendar
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import print_file_header

print_file_header("1-python_module.py")


location = sys.path

for loc in location:
    print("location = ", loc)

leapdays = calendar.leapdays(2000, 2050)
print("leapdays = ", str(leapdays))

isitleap = calendar.isleap(2036)
print("isitleap = ", str(isitleap))