# Input number from the user
num = int(input("Enter a number: "))

print("Odd numbers from 1 to", num, "using 'for' loop")

# Use a for loop to generate odd numbers using range(start, end, steps) function
for i in range(1, num+1, 2):
    # print odd numbers
    print(i)

print("Odd numbers from 1 to", num, "using 'while' loop")

# Initialize a variable to start at 1
i = 1

# Use a while loop to generate odd numbers
while i <= num:
    # Print odd numbers
    print(i)
    # Increment i by 2 to move to the next odd number
    i += 2