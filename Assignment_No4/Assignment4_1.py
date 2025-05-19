"""
File:        Assignment4_1.py
Author:      Shantanu Kulthe
Date:        15/05/2025
Description: This file Accept Number from User and Return Power of 2 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

# This function is lambda function which perform power of two and return its value 
Power = lambda A: A ** 2

# accept one number from user and pass to Power
def main():
    print("Enter the number")
    no = int(input())

    if no == 0:
        print("Invalid Input ")
        return

    sum = Power(no)

    print("Power of Number  is :",sum)

# Starter or entry point function call
if __name__ == "__main__":
    main()