file = open('pelican.txt', 'r')
read_line = file.read()
print(type(read_line))
print(read_line)

# Open the file in read mode
with open('pelican.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()

# Count the number of lines
line_count = len(lines)

print("Lines in the file as a list:")
print(lines)
print("\nNumber of lines:", line_count)

# Open the file in read mode
with open('pelican.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Strip any leading/trailing whitespace and check if the line is not empty
        c_line = line.strip()
        if c_line:  # Only print non-blank lines
            print(c_line)
