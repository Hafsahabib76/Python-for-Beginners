# User input for the number to generate the pattern
num = int(input("Enter a number to generate pattern: "))

# Outer loop that iterate from 1 till the user input number
for i in range(1, num + 1):
    # Inner loop that iterate from 1 till the current value of the outer loop variable 'i'
    for j in range(1, i + 1):
        # Print the current value of 'i' followed by a space, without moving to the next line
        print(i, end=" ")
    # Move to the next line to start a new row in the pattern
    print('')