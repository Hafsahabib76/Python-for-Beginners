import airthmetic

# Welcome Statement
print("Welcome to the Airthmetic Calculator!")

# infinite loop to make the calculator keep running
while True:
    # Operation statements
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Exponentiation")
    print("0. Exit")

    # Taking User Choice
    choice = int(input("Enter your choice (1/2/3/4/5/6/7) and 0 to Exit: "))

    if choice in (1, 2, 3, 4, 5, 6, 7):
        # two user input: firstNum and secondNum
        firstNum = int(input("Enter the first number: "))
        secondNum = int(input("Enter the second number: "))

        # if choice 1, perform addition operation
        if choice == 1:
            result = airthmetic.addition(firstNum, secondNum)
            print("Result:", firstNum, "+", secondNum, "=", result)

        # if choice 2, perform subtraction operation
        elif choice == 2:
            result = airthmetic.subtraction(firstNum, secondNum)
            print("Result:", firstNum, "-", secondNum, "=", result)

        # if choice 3, perform multiplication operation
        elif choice == 3:
            result = airthmetic.multiplication(firstNum, secondNum)
            print("Result:", firstNum, "*", secondNum, "=", result)

        # if choice 4, perform division operation
        elif choice == 4:
            result = airthmetic.division(firstNum, secondNum)
            if result is not None:
                print("Result:", firstNum, "/", secondNum, "=", result)

        # if choice 5, perform floor division operation
        elif choice == 5:
            result = airthmetic.floor(firstNum, secondNum)
            if result is not None:
                print("Result:", firstNum, "//", secondNum, "=", result)

        # if choice 6, perform modulus operation
        elif choice == 6:
            result = airthmetic.modulus(firstNum, secondNum)
            if result is not None:
                print("Result:", firstNum, "%", secondNum, "=", result)

        # if choice 7, perform subtraction operation
        elif choice == 7:
            result = airthmetic.exponentiation(firstNum, secondNum)
            print("Result:", firstNum, "**", secondNum, "=", result)

        # take input (Yes/No) from the user want to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (Yes/no): ")
        # if no
        if another_calculation.lower() != "yes":
            print("Goodbye!")
            break

    # Option to exit the calculator
    elif choice == 0:
        print("Goodbye!")
        break

    # Invalid option message
    else:
        print("Invalid option. Please select a valid option.")