"""
File:        Assignment11_4.py
Author:      Shantanu Kulthe
Date:        19/05/2025
Description: This file create python application to calculate sum of x^n power 2,3 is 8
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
sum = 1
i = 0
def Power(no):
    global i,sum
    if(i<=no):
        sum = sum * no
        i = i + 1
        Power(no)
    return sum        

def main():

    print("enter number")
    no = int(input())

    iret = Power(no)

    print("Power Digit is:",iret)

if __name__ == "__main__":
    main()    
