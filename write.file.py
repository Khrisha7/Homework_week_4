# this is creating a file handle to open and append to a file called pelican.txt
# open function creates the file if it doesn't exist
# the 'a' ensures it is in append mode so data is added to the file instead of writing over it
bird_file = open('pelican.txt', 'a')

# i have created a new variable for the first line
# i have used the .write method to add this line and when you use this method it returns the number of characters added to the file
first_line = bird_file.write("A wonderful bird is the pelican\n")
print(first_line)

second_line = bird_file.write("His bill holds more than his belican\n")
print(second_line)

# lines is a variable for the list
# the square brackets show this is list
# the \n ensures each one appears on a new line
# the .writelines writes each string from lines variable to the file
lines = ["He can take in his beak,\n", "Enough food for a week, \n", "But I'm damned if I see how the helican.\n"]
new_lines = bird_file.writelines(lines)
print(new_lines)


