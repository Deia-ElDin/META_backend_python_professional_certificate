import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import print_separator, print_file_header

print_file_header("3-python_list.py")

list1 = [1, 2, 3, 4, 5]

list2 = ['A', 'B', 'C']

list3 = ['Hello', 1, True, 40.22]


print ("list1: ", list1)
print ("list2: ", list2)
print ("list3: ", list3)

print ("list1[0]: ", list1[0])
print ("list1[1]: ", list1[1])

print ("list1[-1]: ", list1[-1])
print ("list1[-2]: ", list1[-2])

print ("list1[0:2]: ", list1[0:2])
print ("list1[1:]: ", list1[1:]) # from index 1 to the end
print ("list1[:3]: ", list1[:3]) # from the start to index 3 excluding 3

list1[0] = 100

print ("list1: ", list1)

print_separator()

list4 = list1 + list2

print ("list4: ", list4)

list5 = list1 * 3

print ("list5: ", list5)

list6 = [0] * 4 # create a list with 4 zeros

print ("list6: ", list6)

print_separator()

list7 = [1, [2, 3, 4], 5]

print ("list7: ", list7)

print ("list7[1]: ", list7[1])

print ("list7[1][2]: ", list7[1][2])


print_separator()

list8 = [1, 2, 3, 4, 5]

list8.append(6) # add an element to the end of the list

print ("list8: ", list8)

list8.insert(0, 100) # insert an element at a specific index

print ("list8: ", list8)

list8.remove(100) # remove an element by value

print ("list8: ", list8)

list8.pop() # remove the last element

print ("list8: ", list8)

list8.pop(0) # remove the element at index 0

print ("list8: ", list8)

print ("list 8: ", *list8) # unpack the list    

print ("list 8 with a separator: ", list7, list8 , sep=" - ")

for num in list8:
    print ("num: ", num)

list8.clear() # remove all elements from the list

print ("list8: ", list8)


