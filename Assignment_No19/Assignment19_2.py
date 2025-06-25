"""
File:        Assignment19_2.py
Author:      Shantanu Kulthe
Date:        10/06/2025
Description: This Application to change Extension of current existing directory 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import os
import sys
def ChangeExtension(DirName,extension1,extenison2):
    
    for FolderName,SubFolderNames,FileNames in os.walk(DirName):
        
        for fname in FileNames:
            fname = os.path.join(DirName,fname)
            if(fname.endswith(extension1)):
                base,_ = os.path.splitext(fname)
                nfname =  base + extenison2
                print(nfname)

            

def main():

    Border = "-"*86
    print(Border)
    print("----------------------------Marvellous Automation-------------------------------------")
    print(Border)

    if (len(sys.argv)== 4):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This Application is used to perform ----")
            print("This is the Automation Script")
        elif((sys.argv[2] == "--u") or (sys.argv[2] == "--U")):
            print("Use the give script as:")
            print("Script Name.py Argument1 Argument2 ")
        else:
            DirName = sys.argv[1]
            Extension1 = sys.argv[2]
            Extension2 = sys.argv[3]
            ChangeExtension(DirName,Extension1,Extension2)    
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
