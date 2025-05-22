"""
File:        Assignment2_3.py
Author:      Shantanu Kulthe
Date:        14/05/2025
Description: This file Accept Number from User and factorial 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
# accept one number main print the pattern accordingly 
def Factorial(no):
    sum = 1
    for i in range(no,1,-1):
        sum = sum * i
    return sum

# accept one number from user and pass to function name Factorial
def main():
    print("Enter the number")
    no = int(input())

    if no == 0:
        print("Invalid Input ")
        return

    sum = Factorial(no)
    print("Factorial is :",sum)


# Starter or entry point function call
if __name__ == "__main__":
    main()