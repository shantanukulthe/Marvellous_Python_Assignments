"""
File:        Assignment11_7.py
Author:      Shantanu Kulthe
Date:        19/05/2025
Description: This file create python application to print pattern
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
i = 0
j = 0
def pattern(no):
    global i,j
    if(i<no):
        
        if(j<=i):
            print(" * ",end=" ")
            j = j + 1
            pattern(no)
        else:    
            print('\n')    
            i = i + 1
            j = 0
            pattern(no)    

def main():

    print("enter number")
    no = int(input())

    pattern(no)

if __name__ == "__main__":
    main()    
