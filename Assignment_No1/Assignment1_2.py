"""
File:        Assignment1_2.py
Author:      Shantanu Kulthe
Date:        08/05/2025
Description: This file Accept number from user and find wheather given number is even or odd
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

def CheckNum(value1):                           # defination of CheckNum function accept number and check weather number is even and odd and return bool value 
    if(value1 == None):
        return False

    if((value1 % 2) == 0):
        return True
    else:
        return False       

def main():                                        # defination of main function which take number and pass it to function CheckNum  
    print("Enter the Number")
    no = int(input())

    iret = CheckNum(no)

    if(iret == True):                               # get rteun value i iret and if its true number is even and if its false its odd
        print("Number is Even number")
    else:
        print("Number is Odd number")

if __name__ == "__main__":                        # starter function mian()
    main()
