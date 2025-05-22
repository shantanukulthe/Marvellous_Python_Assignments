"""
File:        Assignment2_1.py
Author:      Shantanu Kulthe
Date:        14/05/2025
Description: This file Accept Number two number from User and perform Addition substraction multiplication and Division
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import Arithmetic 


def main():

    print("Enter First number")
    value1 = int(input())

    print("Enter second number")
    value2 = int(input())

    result = Arithmetic.Add(value1,value2)
    print("Addition is :",result)

    result = Arithmetic.sub(value1,value2)
    print("Addition is :",result)

    result = Arithmetic.Multi(value1,value2)
    print("Addition is :",result)

    result = Arithmetic.Div(value1,value2)
    print("Addition is :",result)

if __name__ == "__main__":
    main()