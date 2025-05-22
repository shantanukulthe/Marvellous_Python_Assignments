"""
File:        Assignment10_4.py
Author:      Shantanu Kulthe
Date:        22/05/2025
Description: This file create python application which use FMR to perform task
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

from FMR import filterX,reduceX,mapX
def ChckEven(Data):
    if(Data % 2 == 0):
        return True
    else:
        return False     

def Square(Data):
    sum = 0
    sum = Data * Data
    return sum

def Addition(Data,sum):
    sum = Data + sum
    return sum

def main():

    print("enter size")
    size = int(input())

    Data = []

    print("enter the element")
    for i in range(size):
        Data.append(int(input()))


    FData = list(filterX(ChckEven,Data))
    print(FData)    
    MData = list(mapX(Square,FData))
    print(MData)
    RData = reduceX(Addition,MData)
    print(RData)

if __name__ == "__main__":
    main()    
