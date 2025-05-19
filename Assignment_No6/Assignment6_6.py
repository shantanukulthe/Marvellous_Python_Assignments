"""
File:        Assignment6_6.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file used tp print pattern
Example
 *

 *  *

 *  *  *

 *  *  *  *

 *  *  *  *  *
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def pattern(no):

    for i in range(no):
        for j in range(no):
            if(j<=i):
                print(" * ",end ="")
        print("\n")

def main():
    print("Enter the number")
    no = int(input())
    pattern(no)
    
if __name__ == "__main__":
    main()    
