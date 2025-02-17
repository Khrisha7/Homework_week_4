 # Open the file in read mode ('r') using the 'with' statement.
# 'with' ensures the file is automatically closed after reading, preventing resource leaks.
with open("pelican.txt", "r") as file:
    # The read() method is used to read the entire content of the file into a single string.
    content = file.read()

    # Print the type of the returned data.
    print("Data type of content:", type(content))

    #  Print the entire content of the file.
    print("\nFull content of pelican.txt:\n", content)

# Opening the file again, but this time read it as a list.
with open("pelican.txt", "r") as file:
    # The readlines() method reads the file line by line and stores each line as an element in a list.
    lines = file.readlines()

    # Print the type of the stored data
    print("\nData type of lines:", type(lines))  # Expected output: list

    # Print the number of items in the list (number of lines in the file).
    print("Number of lines in the file:", len(lines))

#Using a loop to iterate over the list and print each line, ensuring no blank lines are included.
print("\nContents of pelican.txt without blank lines:")
for line in lines:
    # Strip whitespace (including newlines) and check if the line is not empty.
    # line.strip() removes extra spaces and newlines.
    # if line.strip(): ensures only non-empty lines are printed.
    if line.strip():
        print(line.strip())
