"""
File:        Assignment7_1.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file take one number from user and send to lambda function with perform square and cube on that number 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""


square = lambda A: A ** 2

cube = lambda A: A ** 3


def main():
    print("enter the number")
    no = int(input())

    value = square(no)

    print("Square of Number is:",value)
    
    value = cube(no)

    print("cube of Number is:",value)

if __name__ == "__main__":
    main()