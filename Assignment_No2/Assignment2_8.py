"""
File:        Assignment2_8.py
Author:      Shantanu Kulthe
Date:        15/05/2025
Description: This file Accept Number from User and print the pattern accordingly
Example -: 
1

1 2

1 2 3

1 2 3 4

1 2 3 4 5
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

# This function get number from main function and print pattern 
def pattern(no):
    for i in range(no):
        var = 1
        for j in range(no):
            if(j<=i):
                print(var,end=" ")  
                var = var + 1
        print("\n")    

    

# accept one number from user and pass to function name pattern 
def main():
    print("Enter the number")
    no = int(input())

    if no == 0:
        print("Invalid Input ")
        return

    pattern(no)

# Starter or entry point function call
if __name__ == "__main__":
    main()