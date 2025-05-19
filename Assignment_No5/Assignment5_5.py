"""
File:        Assignment5_2.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file Accept number and check its even or odd number 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def ChckEvenOdd(no):
    if no % 2 == 0:
        return True
    else :
        return False    

def main():

    print("enter Number")
    no = int(input())

    iret = ChckEvenOdd(no)
    if iret == True:
        print("Number is even Number")
    else :
        print("Number is Odd Number")


if __name__ == "__main__":
    main()    
