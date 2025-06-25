"""
File:        Assignment18_5.py
Author:      Shantanu Kulthe
Date:        10/06/2025
Description: This Application to accept string from user and see weather its presnt in file or not and display frequnecy
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

import os
import sys
def CheckName(filename1,string):
    fobj = open(filename1,"r")
    count = 0
    word = ""
    data = fobj.read()
    for ch in data:
        if ch != " " and ch != "\n" and ch != "\t":
            word = word + ch
        else:
            if(word != ""):
                if(word == string):
                    count = count + 1
            word = ""                

    if(word == string):
        count = count + 1
    print(count)    

def main():

    print("enter the first file name :")
    filename = input()

    print("enter name u want to search:")
    string = input()

    CheckName(filename,string)

    
if __name__ == "__main__":
    main()    
