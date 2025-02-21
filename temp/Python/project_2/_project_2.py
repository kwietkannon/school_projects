'''Jamie Garcia CYOP 300 6381 '''
# project 2

import string
import secrets
import math
from datetime import date
import sys

print("Welcome to my command line driven menu")
print("Please make a selection from the menu below to complete a task")
print("******************************************************************")
print("Generate Secure Password, type: a")
print("Calculate and format a Percentage, type: b")
print("How mand days from today until July 4, 2025, type: c")
print("Use the Law of Cosines to calculate the leg of a triangle, type: d")
print("Calculate the volume of a Right Circular Cylinder, type: e")
print("Exit program, type: f ")
print("******************************************************************")
ANSWER=str(input("Please make a seclection: "))


def sec_password():
    """function to prompt and create a secure password"""
    print("This option will create a secure password for you")
    length=int(input("Please enter how long you want the password to be: "))
    if isinstance(length, int):
        combination =(string.ascii_lowercase +
                    string.ascii_uppercase +
                    string.digits +
                    string.punctuation)

        password = ''.join(secrets.choice(combination) for i in range(length))
        print("the password generated is", password)
    else:
        print("That was not a valid number")
        length=int(input("Please enter how long you want the password to be: "))

def cal_and_format():
    """function to caluclate and format a percentage of a triangle"""
    print("This option will have you input a numberator and a denominator")
    print("It will also prompt for the number of decimal places you would like")
    numerator=float(input("please input the numberator: "))
    denominator=float(input("please input the denomiator: "))
    decimal=int(input("Please enter the number of decimal places: "))
    percent = "{{:.{}f}}".format(decimal).format(numerator/denominator)
    print("your input ends up with a percentage of", percent , "%")


def days_till_holiday():
    """function to calculate the days till July 4th 2025 from todays date"""
    print("this option calculates the days till July 4, 2025")
    today = date.today()
    holiday = date(2025, 7, 4)
    difference= holiday - today
    print("The days, from today, till the forth of July, 2025 is: ", difference.days)

def law_of_cosines():
    """function to show the law of cosines"""
    print("This function showcases the laws of cosines with an angel of 37 degrees")
    side_a=int(input("Please input the first side of this triangle: "))
    side_b=int(input("Please input the second side of this triangle: "))
    side_c=(math.sqrt(pow(side_a,2) + pow(side_b, 2) - 2 * side_a * side_b * math.cos(37)))
    print("the missing sides length is: ", side_c, ".")

def vol_of_circle():
    """function to calculate the volume of a right circular cylinder"""
    print("This function caluclates the volume of a right circular cylinder")
    radius=float(input("please input the radius of the right circular cylinder: "))
    height=float(input("Please input a height, in inches, for the right circular cylinder: "))
    volume= (math.pi * (radius**2)) * height
    print("the volume for this right cylinder is ", volume)


def exit_program():
    """function to exit the program"""
    print("thank you for using/visiting my program!")
    sys.exit()



while ANSWER in ("a", "b", "c", "d", "e"):
    if ANSWER == "a":
        sec_password()
        ANSWER=str(input("if you would like to continue please put in another option: "))
    elif ANSWER == "b":
        cal_and_format()
        ANSWER=str(input("if you would like to continue please put in another option: "))
    elif ANSWER == "c":
        days_till_holiday()
        ANSWER=str(input("if you would like to continue please put in another option: "))
    elif ANSWER == "d":
        law_of_cosines()
        ANSWER=str(input("if you would like to continue please put in another option: "))
    elif ANSWER == "e":
        vol_of_circle()
        ANSWER=str(input("if you would like to continue please put in another option: "))
    elif ANSWER == "f":
        exit_program()
    else:
        print("you did not input a letter within the given options: ")
        ANSWER=str(input("Please put in a correct option: "))

