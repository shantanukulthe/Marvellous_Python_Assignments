"""
File:        Assignment21_3.py
Author:      Shantanu Kulthe
Date:        13/06/2025
Description: This Application to display running process name and id from user
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import psutil         
import os
import sys
def DisplayProcess(DirName):
    if not os.path.exists(DirName):
        os.mkdir(DirName)

    filename = "Marvellous.log"
    filename = os.path.join(DirName,filename)
    fobj = open(filename,"w")



    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=(['pid','name']))
        fobj.write(str(info) + "\n")


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
            DisplayProcess(DirName)            
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
