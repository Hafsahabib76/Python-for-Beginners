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


# Floor Division function
def floor(num1, num2):
    if num2 == 0:
        print("Error: Division by zero")
    else:
        return num1 // num2


# Modulus (remainder) function
def modulus(num1, num2):
    if num2 == 0:
        print("Error: Division by zero")
    else:
        return num1 % num2


# Exponentiation function
def exponentiation(num1, num2):
    return num1 ** num2