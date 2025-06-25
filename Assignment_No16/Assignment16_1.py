"""
File:        Assignment16_1.py
Author:      Shantanu Kulthe
Date:        09/06/2025
Description: This Application create file and store name of student in it 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import os
def CreateFile(filename):

    fobj = open(filename,"w")

    fobj.write("Suresh \n")
    fobj.write("Mahesh \n")
    fobj.write("Gullu \n")
    fobj.write("chullu \n")
    fobj.write("Sotay \n")

    fobj.close()
   

def main():

    print("enter the 1st file name :")
    filename = input()

    CreateFile(filename)    

if __name__ == "__main__":
    main()    
