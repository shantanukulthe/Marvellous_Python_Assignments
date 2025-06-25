"""
File:        Assignment16_3.py
Author:      Shantanu Kulthe
Date:        09/06/2025
Description: This Application open file and display words line and character in it 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import os
def CreateFile(filename):
    icnt = 0
    charcount = 0
    linecount = 0
    fobj = open(filename,"r")

    data = fobj.read()
    
    for char in data:
        icnt = icnt + 1
        if(((char >= 'a') and (char <= 'z')) or ((char >= 'A') and (char <= 'Z'))):
            charcount = charcount + 1
        if char == '\n':
            linecount = linecount + 1

    if ((len(data) > 0) and (data[-1] != '\n')):
        linecount = linecount + 1    

    print(icnt)
    print(charcount)
    print(linecount)
    fobj.close()
   

def main():

    print("enter the file name :")
    filename = input()

    CreateFile(filename)    

if __name__ == "__main__":
    main()    
