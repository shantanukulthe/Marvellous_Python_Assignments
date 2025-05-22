"""
File:        Assignment2_2.py
Author:      Shantanu Kulthe
Date:        14/05/2025
Description: This file Accept Number from User and print pattern
Example-:
 *   *   *   *   *

 *   *   *   *   *

 *   *   *   *   *

 *   *   *   *   *

 *   *   *   *   *
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
# accept one number main print the pattern accordingly 
def pattern(no):

    for i in range(no):
        for j in range(no):
            print(" * ", end = " ")
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