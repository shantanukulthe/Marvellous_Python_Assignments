"""
File:        Assignment5_2.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file Accept Temperature and convert it into Fahrenheit 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def Fahrenheit(no):
    F = (no * 9/5) + 32
    return F

def main():

    print("enter Number")
    no = int(input())

    iret = Fahrenheit(no)

    print("Tempareture Fahrenheit is:",iret)



if __name__ == "__main__":
    main()    
