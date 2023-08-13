# FOR loop
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruits) # apple, banana, orange

# FOR loop with range
for number in range(1, 5):
    print(number) # 1, 2, 3, 4

# Equivalent to for(let i = 1; i < 5; i++) of JavaScript in Python
for i in range(len(fruits)):
    print(fruits[i]) # apple, banana, orange

# FOR loop with range and step
for number in range(1, 5, 2):
    print(number) # 1, 3

# FOR loop with range and step
for number in range(5, 1, -1):
    print(number) # 5, 4, 3, 2

# FOR loop with break
for number in range(1, 5):
    print(number) # 1, 2, 3, 4
    if number == 3:
        break

# FOR loop with continue
for number in range(1, 5):
    if number == 3:
        continue
    print(number) # 1, 2, 4

# FOR loop with else
for number in range(1, 5):
    print(number) # 1, 2, 3, 4
else:
    print("number is greater than 5")

# FOR loop with else and break
for number in range(1, 5):
    print(number) # 1, 2, 3, 4
    if number == 3:
        break
else:
    print("number is greater than 5")

# FOR loop with else and continue
for number in range(1, 5):
    if number == 3:
        continue
    print(number) # 1, 2, 4
else:
    print("number is greater than 5")

# WHILE loop
counter = 1
while counter <= 5:
    print(counter) # 1, 2, 3, 4, 5
    counter += 1

# WHILE loop with break
counter = 1
while counter <= 5:
    print(counter) # 1, 2, 3, 4
    if counter == 4:
        break
    counter += 1

# WHILE loop with continue
counter = 1
while counter <= 5:
    if counter == 4:
        counter += 1
        continue
    print(counter) # 1, 2, 3, 5
    counter += 1

# WHILE loop with else
counter = 1
while counter <= 5:
    print(counter) # 1, 2, 3, 4, 5
    counter += 1
else:
    print("counter is greater than 5")

