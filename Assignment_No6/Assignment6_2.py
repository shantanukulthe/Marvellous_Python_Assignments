"""
File:        Assignment6_2.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file print 1 to 100 sum of all even number 0n console
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
 

def main():
    print("Loop Starts")
    sum = 0
    i= 1
    while (i <= 100):
        if(i % 2 == 0):
            sum = sum + i
        i = i + 1
    print("Addition of all even number is :",sum)    

if __name__ == "__main__":
    main()    
