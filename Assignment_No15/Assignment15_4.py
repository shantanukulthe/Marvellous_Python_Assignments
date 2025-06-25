"""
File:        Assignment15_4.py
Author:      Shantanu Kulthe
Date:        09/06/2025
Description: This Application accept two file name and compair content of that  
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import os
def CheckFile(filename1,filename2):

    iret = os.path.exists(filename1)

    if(iret == False):
        print("File does not exist in this directory")
        exit()
            
    
    iret = os.path.exists(filename2)

    if(iret == False):
        print("File does not exist in this directory")
        exit()
            
    fobj1 = open(filename1,"r")
    fobj2 = open(filename2,"r")

    if(fobj1.read() == fobj2.read()):
        return True
    else:
        return False    
    fobj1.close()
    fobj2.close()    


def main():

    print("enter the 1st file name :")
    filename1 = input()
    
    print("enter the 2nd file name :")
    filename2 = input()

    iret = CheckFile(filename1,filename2)
    
    if(iret == True):
        print("both files are same")
    else:
        print("bothe files are not same")    

if __name__ == "__main__":
    main()    
