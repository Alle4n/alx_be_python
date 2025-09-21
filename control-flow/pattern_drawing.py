# Drawing Patterns with Nested Loops

# Ask user for pattern size
size = int(input("Enter the size of the pattern: "))

# Use while loop for rows
row = 0
while row < size:
    # Use for loop for columns
    for col in range(size):
        print("*", end="")
    print()  # move to next line
    row += 1
