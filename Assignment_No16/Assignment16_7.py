"""
File:        Assignment16_7.py
Author:      Shantanu Kulthe
Date:        09/06/2025
Description: This Application to display name of student whos marks are more than 75
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import os
def display(filename):
    words = ""
    fobj = open(filename,"r")

    while True:
        
        data = fobj.readline()
        if not data:
            break
        words = ""
        number = 0    
        for ch in data:
            if ch != " " and ch != '\n':
                words = words + ch
            elif ch <= '0' and ch >= '9':
                number = number + ch 
                
        if(number >= 75):
            print(data)           
def main():

    print("enter the file name :")
    filename = input()

    display(filename)    

if __name__ == "__main__":
    main()    
