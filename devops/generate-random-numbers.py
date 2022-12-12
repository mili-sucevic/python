import random

# generate random numbers
numbers = []
for _ in range(1000):
    number = random.randint(1, 1000)
    numbers.append(number)

# write the numbers to a file
with open("numbers.txt", "w") as f:
    for number in numbers:
        f.write(str(number) + "\n")

