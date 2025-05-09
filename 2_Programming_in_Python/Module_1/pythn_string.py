 # This is a comment

# Variables
x = 5
y = "Hello"

# Print statement
print(x)
print(y)

# Basic arithmetic
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Integer Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# String operations
name = "Python"
print("String length:", len(name))
print("First character:", name[0])
print("Last character:", name[-1])
print("Substring:", name[0:3])

# Boolean operations
is_true = True
is_false = False
print("AND:", is_true and is_false)
print("OR:", is_true or is_false)
print("NOT:", not is_true)

# If statement
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# For loop
print("\nFor loop example:")
for i in range(3):
    print(f"Count: {i}")

# While loop
print("\nWhile loop example:")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1