"""
File:        Assignment15_1.py
Author:      Shantanu Kulthe
Date:        09/06/2025
Description: This Application accept file from user and check weather its in DIR or not
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import os
def CheckFile(filename):

    iret = os.path.exists(filename)

    if(iret == True):
        print("File is there in Directory")
    else:
        print("File does not exist in this directory ")    


def main():

    print("enter the file name :")
    filename = input()
    CheckFile(filename)

if __name__ == "__main__":
    main()    
