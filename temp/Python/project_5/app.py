'''Jamie Garcia CYOP 300 Section 6381'''

import csv
import sys
import pandas as pd
import numpy as np
import matplotlib.pylot as plt

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
            analyze_column('Population April 1')
        elif answer.lower() == 'b':
            analyze_column('Population July 1')
        elif answer.lower() == 'c':
            analyze_column('Change Population')
        elif answer.lower == 'd':
            break
        else:
            print("That is not an option. Input choice: ")

def house_data():
    '''function to pull housing data'''
    while True:
        print("This is the list of columns to analyze")
        print("a. Age")
        print("b. BEDRMS")
        print("c. BUILT")
        print("d. ROOMS")
        print("e. UTILITY")
        print("f. Exit Column")
        answer = input("Please enter a column: ")

        if answer.lower() == 'a':
            analyze_column('AGE')
        if answer.lower() == 'b':
            analyze_column('BEDRMS')
        if answer.lower() == 'c':
            analyze_column('BUILT')
        if answer.lower() == 'd':
            analyze_column('ROOMS')
        if answer.lower() == 'e':
            analyze_column('UTILITY')
        if answer.lower() == 'f':
            break
        else:
            print("that is not an option. Input choice: ")

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
        
        population_file = "PopChange.csv"
        housing_file = "Housing.csv"

        df = pd.read_csv(population_file)


if __name__ == "__main__":
    main()
