"""
File:        Assignment1_7.py
Author:      Shantanu Kulthe
Date:        08/05/2025
Description: This file display Weather number is Divisible by 5 or not 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def Divisible(value): # defination of Divisible which accept Number and display weather number is divisible by 5 or not 
    
    if(value == None):
        print("Number is not valid")

    if((value % 5) == 0):
        return True
    else:
        return False 


def main(): # defination of main function which  take input from user and function call (Divisible)
    print("enter the number :")
    no = int(input())

    iret = Divisible(no)

    if(iret == True):
        print("Number is Divisible by 5")
    else:
        print("Number is not Divisible by 5")
    
if __name__ == "__main__": # starter (main function call)
    main()
