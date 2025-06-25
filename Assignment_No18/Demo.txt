"""
File:        Assignment18_2.py
Author:      Shantanu Kulthe
Date:        10/06/2025
Description: This Application to check file in dirctory and if exist open for read 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

import os
def CheckFile(filename):
    
    iret = os.path.exists(filename)

    if iret == True:
        fobj = open(filename,"r")
        data = fobj.read()
        print(data)
    else:
        print("file not exists in directory")    
    
def main():

    print("enter file name")
    filename = input()

    CheckFile(filename)

if __name__ == "__main__":
    main()    
