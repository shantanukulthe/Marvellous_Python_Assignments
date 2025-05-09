"""
File:        Assignment1_3.py
Author:      Shantanu Kulthe
Date:        08/05/2025
Description: This file Accept two  number from user and perform Addition on That 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

def Add(value1,value2):                             # defination of Add function which accept two number and perform addition on that 
    if((value1 == None) or (value2 == None)):
        print("User has Given Wrong Input")
    sum = value1 + value2
    return sum

def main():                                          # defination of main function which take two number and pass it to function Add  
    print("Enter First Number")
    no1 = int(input())
    print("Enter Second Number")
    no2 = int(input())

    result = Add(no1,no2)
    print("Addition of two number is: ",result)

if __name__ == "__main__":                           # starter function mian()
    main()
