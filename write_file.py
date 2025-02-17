# Creating a new file or opening it for appending
file = open('pelican.txt', 'a')
file.close()  # Close immediately since it's not used afterward

# Appends the first sentence
with open('pelican.txt', 'a') as file_handle:
    file_handle.write("A wonderful bird is the pelican\n")

# Appends the second sentence in a new 'with' block
with open('pelican.txt', 'a') as file_handle:
    file_handle.write("His bill holds more than his belican\n")

# The \n is need to make each text on a new line
lines = ["He can take in his beak, \n", "Enough food for a week,\n", "But I'm damned if I see how the helican. \n"]
with open('pelican.txt', 'a') as file_handle:
    file_handle.writelines(lines)
