"""
File:        Assignment15_5.py
Author:      Shantanu Kulthe
Date:        09/06/2025
Description: This Application accept  file name and string from user and calculate frequency in that  
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import os
def CheckFile(filename,string):
    word = ""
    icnt = 0
    iret = os.path.exists(filename)

    if(iret == False):
        print("File does not exist in this directory")
        exit()

    fobj = open(filename,"r")

    data = fobj.read()

    for i in data:
        if i != " " and i != "\n" and i != "\t":
            word = word + i
        else :
            if(word != ""):
                print(word)
                if (word == string):
                    icnt = icnt + 1
                word = ""
    if word != "":
        if(word == string):
            icnt = icnt + 1               
    return icnt        

def main():

    print("enter the 1st file name :")
    filename = input()
    
    print("enter string you want to serach:")
    string = input()

    iret = CheckFile(filename,string)

    print("Frequency of given string is :",iret)
    
if __name__ == "__main__":
    main()    
