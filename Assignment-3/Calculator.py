# Addition function
def addition(num1, num2):
    return num1 + num2


# Subtraction function
def subtraction(num1, num2):
    return num1 - num2


# Multiplication function
def multiplication(num1, num2):
    return num1 * num2


# Division function
def division(num1, num2):
    if num2 == 0:
        print("Error: Division by zero")
    else:
        return num1 / num2


# Welcome Statement
print("Welcome to the Function Calculator!")

# infinite loop to make the calculator keep running
while True:
    # Operation statements
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Taking User Choice
    choice = int(input("Enter your choice (1/2/3/4/5): "))

    if choice in (1, 2, 3, 4):
        # two user input: firstNum and secondNum
        firstNum = float(input("Enter the first number: "))
        secondNum = float(input("Enter the second number: "))

        # if choice 1, perform addition operation
        if choice == 1:
            result = addition(firstNum, secondNum)
            print("Result:", firstNum, "+", secondNum, "=", result)

        # if choice 2, perform subtraction operation
        elif choice == 2:
            result = subtraction(firstNum, secondNum)
            print("Result:", firstNum, "-", secondNum, "=", result)

        # if choice 3, perform multiplication operation
        elif choice == 3:
            result = multiplication(firstNum, secondNum)
            print("Result:", firstNum, "*", secondNum, "=", result)

        # if choice 4, perform division operation
        elif choice == 4:
            result = division(firstNum, secondNum)
            if result is not None:
                print("Result:", firstNum, "/", secondNum, "=", result)

        # take input (Yes/No) from the user want to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (Yes/no): ")
        # if no
        if another_calculation.lower() != "yes":
            print("Goodbye!")
            break

    # Option to exit the calculator
    elif choice == 5:
        print("Goodbye!")
        break

    # Invalid option message
    else:
        print("Invalid option. Please select a valid option.")