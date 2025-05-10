import time

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0
for x in list1:  # runs a total of 9 times 
    count += 1
    for y in list2: # runs a tootal of 81 times
        count += 1

print(count)

print("\n--------------------------------\n")

for i in range(10):
    for j in range(10):
        print(0, end=" ")
    print()

print("\n--------------------------------\n")

start_timer = time.time()

for i in range(100):
    for j in range(10000):
        print(0, end=" ")
    print()

end_timer = time.time()

print(f"Time taken: {round(end_timer - start_timer, 3)} seconds")
