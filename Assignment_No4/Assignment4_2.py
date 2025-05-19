"""
File:        Assignment4_2.py
Author:      Shantanu Kulthe
Date:        15/05/2025
Description: This file Accept tow number from user and perform multiplication 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

# This function is lambda function which perform power of two and return its value 
Multi = lambda A , B: A * B

# accept one number from user and pass to Power
def main():
    print("Enter first number")
    no1 = int(input())
    print("Enter second number")
    no2 = int(input())


    if no1 == 0 and no2 == 0:
        print("Invalid Input ")
        return

    sum = Multi(no1,no2)

    print("Multiplication of digit is :",sum)

# Starter or entry point function call
if __name__ == "__main__":
    main()