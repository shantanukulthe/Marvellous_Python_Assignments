"""
File:        Assignment10_1.py
Author:      Shantanu Kulthe
Date:        22/05/2025
Description: This file create python application which accept number from user and return power
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
Power = lambda A:A ** 2 
def main():

    print("enter number")
    no = int(input())

    iret = Power(no)

    print("Power of Number is:",iret)

if __name__ == "__main__":
    main()    
