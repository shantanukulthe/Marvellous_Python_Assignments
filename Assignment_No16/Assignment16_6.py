"""
File:        Assignment16_6.py
Author:      Shantanu Kulthe
Date:        09/06/2025
Description: This Application to copy file contain from source to destination
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import os
def display(filename):

    fobj1 = open(filename,"r")
    fobj2 = open("destination.txt","w")

    data = fobj1.read()

    for i in data:
        fobj2.write(i)


def main():

    print("enter the file name :")
    filename = input()

    display(filename)    

if __name__ == "__main__":
    main()    
