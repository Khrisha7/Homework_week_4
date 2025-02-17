# # lotto
import random

# numbers is specified to know how many lotto numbers we need
numbers = 6

# letting the loop run 6
for n in range(numbers):
    # generates a random integer between 1 and 50 (inclusive)
    print(random.randint(1,50))

# print(random.randint(1,50))