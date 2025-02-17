# the import random line imports the library "random" to be used within this code
import random
# The .sample method returns a new list containing elements from the population while leaving the original population unchanged.
# the range function allows me choose a number between the constraints I have given which is 1 and 51 (1 and 50)
# the number 6 at the end provides the number of samples from the range to be picked.
random_numbers = random.sample(range(1,51),6)
print("Your lottery numbers are:", random_numbers)

# help(random)
