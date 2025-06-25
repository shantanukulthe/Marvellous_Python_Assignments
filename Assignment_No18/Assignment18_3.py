"""
File:        Assignment18_3.py
Author:      Shantanu Kulthe
Date:        10/06/2025
Description: This Application to check file and copy all contain from one file into another 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

import os
import sys
def CopyFileIntoAnother(filename):
    
    iret = os.path.exists(filename)

    if iret == True:
        fobj = open(filename,"r")
        fobj1 = open("Demo.txt","w")
        data = fobj.read()
        fobj1.write(data)
    else:
        print("file not exists in directory")    
    
def main():

    
    if (len(sys.argv)== 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This Application is used to perform ----")
            print("This is the Automation Script")
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the give script as:")
            print("Script Name.py Argument1 Argument2 ")
        else:
            filename = sys.argv[1]
            CopyFileIntoAnother(filename)
    else:
        print("Invalid command line Arguments")
        print(" Use given Flag")
        print("--h : Use to display the Help")
        print("--u : Use to display the usage")


    print("---------------------Tankyou for using our script-------------------------------------")
    print("----------------------------Marvellous Automation-------------------------------------")
    # CopyFileIntoAnother(filename)

if __name__ == "__main__":
    main()    
