"""
File:        Assignment16_4.py
Author:      Shantanu Kulthe
Date:        09/06/2025
Description: This Application to create file and place 10 number given by user in that file 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import os
def Numbersintofile(filename,data):

    fobj = open(filename,"w")

    for i in data:
        fobj.write(str(i)+"\n")

    fobj.close()    


def main():

    print("enter the file name :")
    filename = input()

    print("enter the size ")
    size = int(input())
    data = []
    for i in range(size):
        data.append(int(input()))


    Numbersintofile(filename,data)    

if __name__ == "__main__":
    main()    
