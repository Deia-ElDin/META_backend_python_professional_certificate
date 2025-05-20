def sum_of(a, b):
    return a + b

print ("sum_of(1, 2): ", sum_of(1, 2))

# print ("sum_of(1, 2, 3): ", sum_of(1, 2, 3)) # error

print("\n--------------------------------\n")

def sum_of(*args):
    print ("args: ", args)
    sum = 0
    for num in args:
        sum += num
    return sum

print ("sum_of(1, 2, 3): ", sum_of(1, 2, 3))
