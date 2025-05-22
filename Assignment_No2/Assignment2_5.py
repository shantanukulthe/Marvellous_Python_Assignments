"""
File:        Assignment2_5.py
Author:      Shantanu Kulthe
Date:        14/05/2025
Description: This file Accept Number from User and check number is prime or not 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
# This function get number from main function and check weather number is prime or not 
def ChckPrime(no):
    sum = 0
    for i in range(2,no):
        if no % i == 0:
            return False
    return True

# accept one number from user and pass to function name ChckPrime and take return value in ibool as boolean and check weather its true or false
def main():
    print("Enter the number")
    no = int(input())

    if no == 0:
        print("Invalid Input ")
        return

    ibool = ChckPrime(no)
    if(ibool == True):
        print("Number is Prime number")
    else:
        print("Number is not Prime")


# Starter or entry point function call
if __name__ == "__main__":
    main()