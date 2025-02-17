# What is going on here?
# As tup is a string, the len function return the length of the string which in this case is 5
tup = 'Hello'
print(len(tup))

# Due to the , after the word hello this change tup to a tuple with one element, so if we were to add another word after the comma, our tup variable would have two elements
tup = 'Hello',
print(len(tup))
