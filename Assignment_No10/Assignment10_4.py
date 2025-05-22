"""
File:        Assignment10_4.py
Author:      Shantanu Kulthe
Date:        22/05/2025
Description: This file create python application which use FMR to perform task
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

from  functools import reduce
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


    FData = list(filter(ChckEven,Data))
    print(FData)    
    MData = list(map(Square,FData))
    print(MData)
    RData = reduce(Addition,MData)
    print(RData)

if __name__ == "__main__":
    main()    
