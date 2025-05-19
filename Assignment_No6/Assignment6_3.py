"""
File:        Assignment6_3.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file print table of given number
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def Table(no):
    sum = 0
    for i in range(1,11):
        sum = i * no
        print(sum)

def main():
    print("Enter the number")
    no = int(input())
    Table(no)
    
if __name__ == "__main__":
    main()    
