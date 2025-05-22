"""
File:        Assignment11_5.py
Author:      Shantanu Kulthe
Date:        19/05/2025
Description: This file create python application to calculate zero in digit 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
idigit = 0
icnt = 0
def countDigit(no):
    global idigit,icnt
    if(no != 0):
        digit = no % 10
        if(digit == 0):
            icnt = icnt + 1
        no = no // 10
        countDigit(no) 
    return icnt        
def main():

    print("enter number")
    no = int(input())

    iret = countDigit(no)

    print("zero count is:",iret)

if __name__ == "__main__":
    main()    
