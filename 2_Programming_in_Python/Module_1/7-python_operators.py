print ("Sum = ", 2 + 2)
print ("Difference = ", 2 - 2)
print ("Product = ", 2 * 2)
print ("Quotient = ", 4.5 / 2)
print ("Remainder = ", 2 % 2)
print ("Exponent = ", 2 ** 3)
print ("Floor Division = ", 4.5 // 2)
print (type(4.5 // 2))

print ("\nLogical Operators")
a = False
b = False

if a and b:
    print ("Both a and b are true")
else:
    print ("At least one of a or b is false")

if a or b:
    print ("At least one of a or b is true")
else:
    print ("Both a and b are false")

c = True
d = True

if not c:
    print ("c is false")
else:
    print ("c is true")

if not d:
    print ("d is false")
else:
    print ("d is true")

if not(c and d):
    print ("c and d are false")
else:
    print ("c and d are true")



