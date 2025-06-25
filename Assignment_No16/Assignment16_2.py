"""
File:        Assignment16_2.py
Author:      Shantanu Kulthe
Date:        09/06/2025
Description: This Application read file and display content 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import os
def CreateFile(filename):

    fobj = open(filename,"r")

    data = fobj.read()

    print(data)
    fobj.close()
   

def main():

    print("enter the 1st file name :")
    filename = input()

    CreateFile(filename)    

if __name__ == "__main__":
    main()    
