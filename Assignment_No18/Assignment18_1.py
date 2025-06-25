"""
File:        Assignment18_1.py
Author:      Shantanu Kulthe
Date:        10/06/2025
Description: This Application to check file in dirctory 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

import os
def CheckFile(filename):
    
    iret = os.path.exists(filename)

    if(iret == True):
        print("file exist in directory")
    else :
        print("file not exist in directory")    
    
def main():

    print("enter file name")
    filename = input()

    CheckFile(filename)

if __name__ == "__main__":
    main()    
