"""
File:        Assignment6_4.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file print Factorial of given number 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def Factorial(no):
    sum = 1
    for i in range(no,0,-1):
        sum = i * sum
    return sum 

def main():
    print("Enter the number")
    no = int(input())
    iret = Factorial(no)
    print("Factorial of number is :",iret)
    
if __name__ == "__main__":
    main()    
