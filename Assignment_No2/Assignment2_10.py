"""
File:        Assignment2_10.py
Author:      Shantanu Kulthe
Date:        15/05/2025
Description: This file Accept Number from User and perform addition of digit present in it 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

# This function get number from main function and perform addition 
def AdditionDigit(no):
    sum = 0
    while (no != 0):
        digit = no % 10
        sum = sum + digit
        no = no // 10   # integer Divition "//" N Floating Division "/"

    return  sum
    

# accept one number from user and pass to function name AdditionDigit 
def main():
    print("Enter the number")
    no = int(input())

    if no == 0:
        print("Invalid Input ")
        return

    sum = AdditionDigit(no)

    print("Count of digit is :",sum)

# Starter or entry point function call
if __name__ == "__main__":
    main()