"""
File:        Assignment1_6.py
Author:      Shantanu Kulthe
Date:        08/05/2025
Description: This file Accept number and check weather it is positive or naegative number or zero  
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def CheckNumber(value):# This function accept the number decide weather number is positive,negative or zero
    if(value == None):
        print("invalid input")
        return -1
    if(value > 0):
        print("Number is positive Number :",value)
    elif(value == 0):
        print("Number is Zero Number :",value)
    else:
        print("Number is Negative Number :",value)   

def main(): # defination of main function which  take input from user and pass that number to CheckNumber function
    print("enter the number :")
    no = int(input())
    CheckNumber(no)
    
if __name__ == "__main__": # starter (main function call)
    main()


