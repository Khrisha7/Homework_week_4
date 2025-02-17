# this first line opens the file in read mode
# slurping reads the entire file in one gulp
bird_file = open("pelican.txt", "r").read()
print(bird_file)

# the data type is a string
print(type(bird_file))

# turns the pelican file into a list confirmed by the type function
bird_file_list = open('pelican.txt', 'r').read().splitlines()
print(bird_file_list)
print(type(bird_file_list))

# using a loop to iterate over and print the contents of the file
for line in open('pelican.txt', 'r'):
    print(line[:-1])