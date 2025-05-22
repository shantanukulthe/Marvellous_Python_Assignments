"""
File:        Assignment10_2.py
Author:      Shantanu Kulthe
Date:        22/05/2025
Description: This file create python application using lambda function for multiplication of two number
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
Multi = lambda A,B:A * B 
def main():

    print("enter first number")
    no1 = int(input())

    
    print("enter second number")
    no2 = int(input())

    iret = Multi(no1,no2)

    print("Multiplication of two Number is:",iret)

if __name__ == "__main__":
    main()    
