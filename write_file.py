# Open the file 'pelican.txt' in append mode ('a') using the 'with' statement.
# 'with' ensures the file is automatically closed when the block finishes executing, even if an error occurs.
# This prevents resource leaks and file corruption.

# the With open (("pelican.txt", "a") as file:
    # Opens pelican.txt in append mode ('a').
    # If the file does not exist, it is created.
    # If the file already exists, new content is added to the end without overwriting previous data.
with open("pelican.txt", "a") as file:
    # The .write() method writes a string to the file.
    # It does NOT add a newline automatically, so we need to include '\n' at the end of each line.
    file.write("A wonderful bird is the pelican,\n")  # Appends the first line
    print("First line written to file: A wonderful bird is the pelican,")  # Print confirmation


    file.write("His bill holds more than his belican.\n")  # Appends the second line
    print("Second line written to file: His bill holds more than his belican.")  # Print confirmation

    # Create a list containing multiple lines of text
    # Each string in the list ends with '\n' to ensure proper line breaks when written to the file.
    lines = [
        "He can take in his beak,\n",
        "Enough food for a week,\n",
        "But I’m damned if I see how the helican.\n"
    ]

    # The writelines() method writes multiple lines to the file in one go.
    # Unlike write(), it does not automatically insert newlines between elements,
    # so we must include '\n' in each string within the list.
    file.writelines(lines)
print("Additional lines written to file:", lines)  # Print confirmation

# At this point, 'with' has automatically closed the file.
# Closing the file ensures all changes are saved and prevents accidental data loss or corruption.
