"""Jamie Garcia CYOP 300 Section 6381 Project 4"""

import re
import numpy as np


def check_phone(phone_number):
    """Validates phone number"""
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    if re.match(pattern, phone_number):
        return True
    return None


def check_zipcode(zipcode):
    """Validates zip code"""
    pattern = r"^\d{5}-\d{4}$"
    if re.match(pattern, zipcode):
        return True
    else:
        return False


def matrix_input():
    """Prompts the user for input"""
    print("Enter your first 3x3 matrix:")
    matrix1 = np.array([[int(x) for x in input().split()] for _ in range(3)])

    print("Enter your second 3x3 matrix:")
    matrix2 = np.array([[int(x) for x in input().split()] for _ in range(3)])

    return matrix1, matrix2


def perform_operation(matrix1, matrix2, operation):
    """choose operation"""
    if operation == "a":
        result = matrix1 + matrix2
    elif operation == "b":
        result = matrix1 - matrix2
    elif operation == "c":
        result = np.matmul(matrix1, matrix2)
    elif operation == "d":
        result = matrix1 * matrix2
    else:
        print("Invalid operation selected.")
        return None

    print("The results are:\n", result)
    print("The Transpose is:\n", result.T)
    print("The row and column mean values of the results are:")
    print("Row:", [round(row.mean(), 2) for row in result])
    print("Column:", [round(col.mean(), 2) for col in result.T])

    return result


def main():
    """main function"""
    print("***************** Welcome to the Python Matrix Application***********")

    while True:
        print("Do you want to play the Matrix Game?")
        play_game = input("Enter Y for Yes or N for No: ")
        if play_game.lower() == "n":
            print("*********** Thanks for playing Python Numpy ***************")
            break

        # Get phone number and zip code
        while True:
            phone_number = input("Enter your phone number (XXX-XXX-XXXX): ")
            if check_phone(phone_number):
                break
            print("Your phone number is not in correct format. Please renter:")

        while True:
            zipcode = input("Enter your zip code+4 (XXXXX-XXXX): ")
            if check_zipcode(zipcode):
                break
            print("Your zip code is not in correct format. Please renter:")

        # Get matrix inputs
        matrix1, matrix2 = matrix_input()

        # Select and perform matrix operation
        while True:
            print("Select a Matrix Operation from the list below:")
            print("a. Addition")
            print("b. Subtraction")
            print("c. Matrix Multiplication")
            print("d. Element by element multiplication")
            operation = input()
            if operation in ["a", "b", "c", "d"]:
                perform_operation(matrix1, matrix2, operation)
                break
            else:
                print("Invalid operation selected. Please try again.")


if __name__ == "__main__":
    main()

