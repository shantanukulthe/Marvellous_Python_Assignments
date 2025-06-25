"""
File:        Assignment20_1.py
Author:      Shantanu Kulthe
Date:        10/06/2025
Description: This Application to display checksum  
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import os
import sys
import hashlib
def CopyContent(DirName):

    for FolderName,SubFolderNames,FileNames in os.walk(DirName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            fobj = open(fname,"rb")
            hobj = hashlib.md5()
            buffer = fobj.read(1024)

            while(len(buffer)>0):
                hobj.update(buffer)
                buffer = fobj.read(1024)
            print(hobj.hexdigest())


            
def main():

    Border = "-"*86
    print(Border)
    print("----------------------------Marvellous Automation-------------------------------------")
    print(Border)

    if (len(sys.argv)== 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This Application is used to perform ----")
            print("This is the Automation Script")
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the give script as:")
            print("Script Name.py Argument1 Argument2 ")
        else:
            DirName = sys.argv[1]
            CopyContent(DirName)    
    else:
        print("Invalid command line Arguments")
        print(" Use given Flag")
        print("--h : Use to display the Help")
        print("--u : Use to display the usage")


    print(Border)
    print("---------------------Tankyou for using our script-------------------------------------")
    print("----------------------------Marvellous Automation-------------------------------------")
    print(Border)

    

if __name__ == "__main__":
    main()    
