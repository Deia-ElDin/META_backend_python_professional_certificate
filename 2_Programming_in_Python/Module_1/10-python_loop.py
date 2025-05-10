my_str = "Hello, World!"

for char in my_str:
    print(char)

print("\n--------------------------------\n")

for i in range(10):
    print(i)

print("\n--------------------------------\n")

for i in range(10, 20):
    print(i)

print("\n--------------------------------\n")

favorites = ["Creme Brulee", "Apple Pie", "Churros", "Tiramisu", "Chocolate Cake"]

for dessert in favorites:
    print("I like ", dessert)

print("\n--------------------------------\n")

count = 0

while count < len(favorites):
    print("I like ", favorites[count])
    count += 1

print("\n--------------------------------\n")

for idx, dessert in enumerate(favorites):
    print(f"{idx}: {dessert}")

print("\n--------------------------------\n")

for dessert in favorites:
    if dessert == 'Churros1':
        print('Yes, one of my favorite desserts is', dessert)
        break
else:  # This else belongs to the for loop, not the if statement
    print('No sorry, not a dessert on my list')

print("\n--------------------------------\n")

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert) 

print("\n--------------------------------\n")

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert) 