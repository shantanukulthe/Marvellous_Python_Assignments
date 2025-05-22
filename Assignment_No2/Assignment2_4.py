"""
File:        Assignment2_4.py
Author:      Shantanu Kulthe
Date:        14/05/2025
Description: This file Accept Number from User and return Addition of Factors
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
# This function get number from main function which give factors of number and perform addition but and return sum of that 
def Factors(no):
    sum = 0
    for i in range(1,no):
        if no % i == 0:
            sum = sum + i
    return sum

# accept one number from user and pass to function name Factors
def main():
    print("Enter the number")
    no = int(input())

    if no == 0:
        print("Invalid Input ")
        return

    sum = Factors(no)
    print("Factorial is :",sum)


# Starter or entry point function call
if __name__ == "__main__":
    main()