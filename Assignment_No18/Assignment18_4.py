"""
File:        Assignment18_4.py
Author:      Shantanu Kulthe
Date:        10/06/2025
Description: This Application to check file and copy all contain from one file into another 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

import os
import sys
def Compaire(filename1,filename2):
    fobj1 = open(filename1,"r")
    fobj2 = open(filename2,"r")

    if(fobj1.read() == fobj2.read()):
        print("Both files are same")
    else:
        print("files are different")    


def main():

    print("enter the first file name :")
    filename1 = input()

    print("enter the second file name :")
    filename2 = input()

    Compaire(filename1,filename2)

    
if __name__ == "__main__":
    main()    
