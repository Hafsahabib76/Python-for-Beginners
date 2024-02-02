# Python program to make a simple calculator.

print("*********** Calculator ***********")

# infinite loop to make the calculator keep running
while True:
    print("**********************************")
    print("Options:")
    print("Enter 'a' for Addition")
    print("Enter 'b' for Subtraction")
    print("Enter 'c' for Multiplication")
    print("Enter 'd' for Division")
    print("Enter 'e' for Modulus")
    print("Enter 'f' for Floor Value")
    print("Enter 'g' for Power")
    print("Enter 'h' for Square Root")
    print("Enter '0' to Exit")
    print("**********************************")
    option = input("Select an option: ")

    if option in ("a", "b", "c", "d", "e", "f", "g", "h"):
        # Math operations which required two inputs
        if option in ("a", "b", "c", "d", "e"):

            # two user input: num1 and num2
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Addition
            if option == "a":
                addition = num1 + num2
                print("Addition result:", addition)

            # Subtraction
            elif option == "b":
                subtraction = num1 - num2
                print("Subtraction result:", subtraction)

            # Multiplication
            elif option == "c":
                multiplication = num1 * num2
                print("Multiplication result:", multiplication)

            # Division
            elif option == "d":
                # Condition to check and handle if the denominator value of the division containing 0.
                if num2 == 0:
                    print("Cannot divide by zero")
                # else perform division calculation
                else:
                    division = num1 / num2
                    print("Division result:", division)

            # Modulus
            elif option == "e":
                # Condition to check and handle if the denominator value of the division containing 0.
                if num2 == 0:
                    print("Cannot divide by zero")
                # else perform division calculation to get modulus
                else:
                    modulus = num1 % num2
                    print("Modulus result:", modulus)

        # Math operations which required single input
        else:

            # single user input of a number
            num = float(input("Enter the number: "))

            # Floor
            if option == "f":
                floor = num // 1
                print("Floor result:", floor)

            # Power
            if option == "g":
                power = num ** 2
                print("Power result:", power)

            # Square Root
            if option == "h":
                sqr = num ** 0.5
                print("Square Root result:", sqr)

    # Option to exit the calculator
    elif option == '0':
        print("Exit from the Calculator. Thankyou! for using it.")
        break

    # Invalid option message
    else:
        print("Invalid option. Please select a valid option.")