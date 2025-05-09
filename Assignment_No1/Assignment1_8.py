"""
File:        Assignment1_8.py
Author:      Shantanu Kulthe
Date:        08/05/2025
Description: This file Accept number from user and display * on console 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def Display(value): # defination of Display which accept Number and display *  
    
    if(value == None):
        print("Number is not valid")

    i = 0
    while(i<value):
        print("*",end =" ")
        i= i + 1


def main(): # defination of main function which  take input from user and function call (Display)
    print("enter the number :")
    no = int(input())

    Display(no)

    
if __name__ == "__main__": # starter (main function call)
    main()
