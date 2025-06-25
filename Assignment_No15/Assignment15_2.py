"""
File:        Assignment15_2.py
Author:      Shantanu Kulthe
Date:        09/06/2025
Description: This Application accept file name from user and read the content in that 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import os
def CheckFile(filename):

    iret = os.path.exists(filename)

    if(iret == False):
        print("File does not exist in this directory")
        exit()
            

    fobj = open(filename,"r")

    data = fobj.read()

    print(data)

    fobj.close()    


def main():

    print("enter the file name :")
    filename = input()
    CheckFile(filename)

if __name__ == "__main__":
    main()    
