"""
File:        Assignment6_7.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file used take 5 input from user and serach for largest one 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def largest(no1,no2,no3,no4,no5):
    val = no1

    if (no2 > val):
        val = no2
    if(no3 > val):
        val = no3
    if(no4 > val):
        val = no4
    if(no5 > val):
        val = no5
    return val
def main():
    print("Enter First number")
    no1 = int(input())
    print("Enter Second number")
    no2 = int(input())
    print("Enter Third number")
    no3 = int(input())
    print("Enter Four number")
    no4 = int(input())
    print("Enter Five number")
    no5 = int(input())

    iret = largest(no1,no2,no3,no4,no5)
    print("larger number is ",iret)
if __name__ == "__main__":
    main()    
