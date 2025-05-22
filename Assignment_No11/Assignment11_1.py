"""
File:        Assignment11_1.py
Author:      Shantanu Kulthe
Date:        19/05/2025
Description: This file create python application to print number from 1 to N
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
i = 1
def Display(no):
    global i
    if(i <= no):
        print(i)
        i = i + 1
        Display(no)

def main():

    print("enter number")
    no = int(input())

    Display(no)

if __name__ == "__main__":
    main()    
