''' Jamie Garcia CYOP 300 Week 5 Discussion '''

print("Welcome to my discussion 1 post")
print("This program just takes two user input numbers and does a simple math calculation")

while True:
    try:
        answer1 = float(input("Please enter your first number: "))
        break
    except ValueError:
        print("Please enter a number")

while True:
    try:
        answer2 = float(input("Please enter your second number: "))
        break
    except ValueError:
        print("Please enter a number")

print("The two numbers added together is" , answer1 + answer2)
print("The two numbers subtracted are" , answer1 - answer2)
print("The two numbers divided is" , answer1 / answer2)
print("The two numbers  multiplied together is" , answer1 * answer2)