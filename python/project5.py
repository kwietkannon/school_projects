"""Jamie Garcia SDEV 300 Section 6380"""
import sys

def population():
    print("for Population of April 1, type a: ")
    print("for population of July 1, type b: ")
    print("To change Population, type c: ")
    print("To exit the column, type d: ")
    while True:
        user_option = str(input("Select the column you want to analyze: "))
        if user_option == 'a':
            print("a")
        elif user_option == 'b':
            print("b")
        elif user_option == 'c':
            print("c")
        elif user_option == 'd':
            print("d")
        else:
            print("That is not a useable choice. Please try again: ")
    
        
def housing():
    print("F in the chat")

def main():
    """main function"""
    print("Welcome to the Python Data Analysis App")
    print("what file would you like to analyze: ")
    print("For population data, type 1: ")
    print("For Housing data, type 2: ")
    print("To exit the program, type 3: ")
    
    while True:
        user_input = str(input("please type your selection: "))
        if user_input == '1':
            print("You have selected Population data")
            population()
        elif user_input == '2':
            print("You have selected Housing Data")
            housing()
        elif user_input == '3':
            print("Thanks for using my program!")
            sys.exit()
        else:
            print("You did pick a usable selection, please enter a number from the list: ")
        

if __name__ == "__main__":
    main()