my_set1 = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} # duplicate values are not allowed

print ("my_set1: ", my_set1)

print("\n--------------------------------\n")   

my_list1 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

my_set2 = set(my_list1)

print ("my_set2: ", my_set2)

my_set2.add(6)

print ("my_set2 after adding 6: ", my_set2)

my_set2.remove(6)

print ("my_set2 after removing 6: ", my_set2)

my_set2.add(7)

print ("my_set2 after adding 7: ", my_set2)

my_set2.discard(7) 

print ("my_set2 after discarding 7: ", my_set2)
 
my_set2.pop()  # remove and return an arbitrary element

my_set2.pop()

print ("my_set2 after popping: ", my_set2)

print("\n--------------------------------\n")

my_set3 = {1, 2, 3, 4, 5}

my_set4 = {4, 5, 6, 7, 8}

print ("my_set3: ", my_set3)
print ("my_set4: ", my_set4)

print ("my_set3 union my_set4: ", my_set3 | my_set4)
print ("my_set3 union my_set4 in a different way: ", my_set3.union(my_set4))

print ("my_set3 intersection my_set4: ", my_set3 & my_set4)
print ("my_set3 intersection my_set4 in a different way: ", my_set3.intersection(my_set4))

print ("my_set3 difference my_set4: ", my_set3 - my_set4)
print ("my_set3 difference my_set4 in a different way: ", my_set3.difference(my_set4))

print ("my_set3 symmetric difference my_set4: ", my_set3 ^ my_set4)
print ("my_set3 symmetric difference my_set4 in a different way: ", my_set3.symmetric_difference(my_set4))

my_set5 = {1, 2, 3}

print ("my_set5: ", my_set5)

print ("my_set5 is subset of my_set3: ", my_set5.issubset(my_set3)) # returns True if all elements of my_set5 are in my_set3

print ("my_set3 is superset of my_set5: ", my_set3.issuperset(my_set5))

print ("my_set5 is disjoint from my_set3: ", my_set5.isdisjoint(my_set3)) # returns True if the sets have no elements in common

print("\n--------------------------------\n")

my_set6 = {1, 2, 3, 4, 5}

print ("my_set6: ", my_set6)

# print ("my_set6[0]: ", my_set6[0]) 
# error: sets are unordered, so you cannot access elements by index
# the set is not a sequence, it doesn't containe an ordered elements inside

# print ("my_set6: ", my_set6)
