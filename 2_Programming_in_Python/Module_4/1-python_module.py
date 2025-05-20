import sys
import os
import calendar

location = sys.path
for loc in location:
    print("location = ", loc)

leapdays = calendar.leapdays(2000, 2050)
print("leapdays = ", str(leapdays))

isitleap = calendar.isleap(2036)
print("isitleap = ", str(isitleap))