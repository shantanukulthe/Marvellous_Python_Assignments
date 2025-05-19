"""
File:        Assignment5_2.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file Accept 3 number from user and check largest of it
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def LargestNumber(no1,no2,no3):
    if no1 > no2 and no1 > no3:
        return no1
    elif no2 > no1 and no2 > no3:
        return no2
    else :
        return no3    

def main():

    print("enter First number")
    no1 = int(input())
    print("enter Second number")
    no2 = int(input())
    print("enter Third number")
    no3 = int(input())

    iret = LargestNumber(no1,no2,no3)
    print("Largest Number is :",iret)


if __name__ == "__main__":
    main()    
