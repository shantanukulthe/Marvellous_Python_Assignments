"""
File:        Assignment11_6.py
Author:      Shantanu Kulthe
Date:        19/05/2025
Description: This file create python application to calculate sum of 1 to N number of natural number  
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
sum = 0    
i = 0
def naturalNumber(no):
    global i, sum
    if no == 0:
        return False
    if(i <= no):
        sum = sum + i
        i = i + 1
        naturalNumber(no)
    return sum    


def main():

    print("enter number")
    no = int(input())

    iret = naturalNumber(no)

    print("Natural number sum is:",iret)

if __name__ == "__main__":
    main()    
