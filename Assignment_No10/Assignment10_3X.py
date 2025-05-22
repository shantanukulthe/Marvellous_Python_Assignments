"""
File:        Assignment10_3.py
Author:      Shantanu Kulthe
Date:        22/05/2025
Description: This file create python application which use FMR to perform task
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

from FMR import filterX,mapX,reduceX
def Display(Data):
    if(Data >= 70) and (Data <= 90):
        return True
    else:
        return False     

def Increase(Data):
    sum = 0
    sum = Data + 10
    return sum

def product(Data,sum):
    sum = Data * sum
    return sum

def main():

    print("enter size")
    size = int(input())

    Data = []

    print("enter the element")
    for i in range(size):
        Data.append(int(input()))


    FData = list(filterX(Display,Data))
    print(FData)    
    MData = list(mapX(Increase,FData))
    print(MData)
    RData = reduceX(product,MData)
    print(RData)

if __name__ == "__main__":
    main()    
