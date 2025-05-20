'''
    Comprehensions in Python are a way to create a new sequence from an already existing sequence.

    There are four main types of comprehensions in Python: 
        1- List comprehension 
        2- Dictionary comprehension 
        3- Set comprehension 
        4- Generator comprehension
'''

'''
    List comprehension

        [ <expression> for x in <sequence> if <condition> ] 
            - The expression is the value returned by the comprehension.
            - The for x in <sequence> is the loop that iterates over the sequence.
            - The if <condition> is the optional condition that the items in the sequence must meet.
'''

print ("List comprehension: \n")

data = [2,3,5,7,11,13,17,19,23,29,31]
# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)  

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)
    
print("\n--------------------------------\n")

''' 
    Dictionary comprehension

        dict = { key:value for key, value in <sequence> if <condition> } 

        Dictionary comprehension takes one or two lists as input and creates a dictionary out of it. 
'''

print ("Dictionary comprehension: \n")

# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number} # ** is the power operator
print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dic   t)

print("\n--------------------------------\n")

'''
    Set comprehension
        The set comprehension deals with the set data type and it's very similar to list comprehension. 
        The only key difference is the use of curly brackets for sets instead of square brackets as in lists. 
        
        { <expression> for x in <sequence> if <condition> } 
'''

print ("Set comprehension: \n")

set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)

print("\n--------------------------------\n")


'''
    Generator comprehension
        Generator comprehensions are also very similar to lists with the variation of using curved brackets
        instead of square brackets. They are also more memory efficient as compared to list comprehensions. 
        ( <expression> for x in <sequence> if <condition> ) 
'''

print ("Generator comprehension: \n")

data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)

print("Generator object: ", gen_obj)
print("Type of generator object: ", type(gen_obj))

for items in gen_obj:
    print(items, end = " ")

'''
    List comprehensions have been a relatively recent development but it does not necessarily mean 
    they are more efficient. Comprehensions have gained popularity primarily for providing cleaner code 
    readability and ease of use. They also provide some added advantages such as 
    providing filtering using if else conditions.

    List comprehensions also provide direct return of a list as compared to map() function 
    that returns a map object. It is mainly the clarity that has made list comprehensions popular, 
    but map() functions are still arguably a better choice when it comes to the use of larger sequences.
'''