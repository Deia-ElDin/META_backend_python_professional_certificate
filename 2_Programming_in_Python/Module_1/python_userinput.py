print("Hello", "World", sep=" ", end="!\n")

num1 = 10
num2 = 12

sum = num1 + num2

print("Adding the value of {} and {} is {}".format(num1, num2, sum))
print("Adding the value of {0} and {1} is {2}".format(num1, num2, sum))
print("Adding the value of {a} and {b} is {sum}".format(a=num1, b=num2, sum=sum))
print("Adding the value of {b} and {a} is {sum}".format(a=num1, b=num2, sum=sum))

name = input("\nEnter your name: ")
age = input("Enter your age: ")

print("Hello", name, "you are", age, "years old")


num1 = input("\nEnter the first number: ")
num2 = input("Enter the second number: ")

sum = num1 + num2

print("\nThe concatenation of {} and {} is {}".format(num1, num2, sum))
print("the type of the concatenation is", type(sum))

sum = int(num1) + int(num2)
print("\nThe sum of {} and {} is {}".format(num1, num2, sum))
print("the type of sum is", type(sum))

