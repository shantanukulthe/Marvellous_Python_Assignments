"""
File:        Assignment19_3.py
Author:      Shantanu Kulthe
Date:        10/06/2025
Description: This Application to copy directory from one to another directory  
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import os
import sys
import shutil
def CopyContent(DirName,Extension):

    # DirName = os.path.exists(DirName)
    DirName1 = "Marvellous2Dir"
    if not os.path.exists(DirName1):
        os.mkdir(DirName1)  

    for FolderName,SubFolderNames,FileNames in os.walk(DirName):
        path = os.path.relpath(FolderName,DirName)
        print(path)
        dest_folder = os.path.join(DirName1,path)

        for fname in FileNames:
            src = os.path.join(FolderName,fname)
            dest = os.path.join(dest_folder,fname)
            # print(dest)
            shutil.copy2(src,dest)


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
            Extension = sys.argv[2]
            CopyContent(DirName,Extension)    
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
