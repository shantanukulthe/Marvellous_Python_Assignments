"""
File:        Assignment2_9.py
Author:      Shantanu Kulthe
Date:        15/05/2025
Description: This file Accept Number from User and count digits 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

# This function get number from main function and count digit in it 
def CountDigit(no):
    icnt = 0
    while (no != 0):
        digit = no % 10
        icnt = icnt + 1
        no = no // 10   # integer Divition "//" N Floating Division "/"

    return  icnt
    

# accept one number from user and pass to function name CountDigit 
def main():
    print("Enter the number")
    no = int(input())

    if no == 0:
        print("Invalid Input ")
        return

    sum = CountDigit(no)

    print("Count of digit is :",sum)

# Starter or entry point function call
if __name__ == "__main__":
    main()