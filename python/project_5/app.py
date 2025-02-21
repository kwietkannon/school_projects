'''Jamie Garcia CYOP 300 Section 6381'''

import sys
import pandas as pd
import matplotlib.pyplot as plt

print("Welcome to the Python Data Analysis App")

def pop_data():
    '''function to pull population data'''
    print("a. Population April 1st: ")
    print("b. Population July 1st: ")
    print("c. Change Population: ")
    print("d. Exit Column: ")
    answer = input("Please select the column to analyze: ")

    while True:
        if answer.lower() == 'a':
            analyze_pop('Pop Apr 1')
        elif answer.lower() == 'b':
            analyze_pop('Pop Jul 1')
        elif answer.lower() == 'c':
            analyze_pop('Change Pop')
        elif answer.lower() == 'd':
            break
        else:
            print("That is not an option. Input choice: ")
            answer = input("Please select the column to analyze: ")

def house_data():
    '''function to pull housing data'''
    while True:
        print("This is the list of columns to analyze")
        print("a. Age")
        print("b. BEDRMS")
        print("c. BUILT")
        print("d. NUNITS")
        print("e. ROOMS")
        print("f. WEIGHT")
        print("g. UTILITY")
        print("h. Exit Column")
        answer = input("Please enter a column: ")

        if answer.lower() == 'a':
            analyze_house('AGE')
        elif answer.lower() == 'b':
            analyze_house('BEDRMS')
        elif answer.lower() == 'c':
            analyze_house('BUILT')
        elif answer.lower() == 'd':
            analyze_house('NUNITS')
        elif answer.lower() == 'e':
            analyze_house('ROOMS')
        elif answer.lower() == 'f':
            analyze_house('WEIGHT')
        elif answer.lower() == 'g':
            analyze_house('UTILITY')
        elif answer.lower() == 'h':
            break
        else:
            print("that is not an option. Input choice: ")
            answer = input("Please enter a column: ")

def analyze_pop(column):
    '''function to analyze data from PopChange.csv'''
    pop_file = "PopChange.csv"
    df = pd.read_csv(pop_file)
    column_data = df[column]
    print("Selection: ", column)
    print("*Statistics*")
    print("Count: ", column_data.count())
    print("Mean: ", column_data.mean())
    print("Standard Deviation: ", column_data.std())
    print("Min: ", column_data.min())
    print("Max: ", column_data.max())

    plt.figure(figsize=(10,8))
    column_data.hist()
    plt.title(f"histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

    sys.exit()

def analyze_house(column):
    '''function to analyze data from housing.csv'''
    house_file = "Housing.csv"
    df = pd.read_csv(house_file)
    column_data = df[column]
    print("Selection: ", column)
    print("*Statistics*")
    print("Count: ", column_data.count())
    print("Mean: ", column_data.mean())
    print("Standard Deviation: ", column_data.std())
    print("Min: ", column_data.min())
    print("Max: ", column_data.max())

    plt.figure(figsize=(10,8))
    column_data.hist()
    plt.title(f"histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

    sys.exit()


def main():
    '''Main function'''
    while True:
        print("1. population Data: ")
        print("2. Housing Data")
        print("3. Exit the program")
        answer = input("Select the file you want to analyze: ")

        if answer.isdigit() and answer == '1':
            pop_data()
        elif answer.isdigit() and answer == '2':
            house_data()
        else:
            sys.exit()

if __name__ == "__main__":
    main()
