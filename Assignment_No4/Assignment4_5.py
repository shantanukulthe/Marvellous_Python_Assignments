"""
File:        Assignment4_5.py
Author:      Shantanu Kulthe
Date:        15/05/2025
Description: This file Accept list from User and perform FMR(Filter,Map,Reduce) Prime number and its addition 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
from FMR import filterX,mapX,reduceXX
def CheckPrime(Data):
    if(Data % 2 == 0):
        return False
    return True    

def Multi(Data):
    sum = 0
    sum = Data * 2

    return sum

def Maximum(Data,imax):
    if(imax < Data):
        imax = Data
    return imax    
    

def Minimum(Data,imin):
    if(imin > Data):
        imin = Data
    return imin        
# accept one number from user and pass to Power
def main():
    print("enter the size ")
    size = int(input()) 

    Data = list()

    print("enter the element")

    for no in range(size):
        Data.append(int(input()))

    FData = list(filterX(CheckPrime,Data))
    print(FData)

    MData = list(mapX(Multi,FData))
    print(MData)

    RData = reduceXX(Maximum,MData)
    print(RData)

    RData1 = reduceXX(Minimum,MData)
    print(RData1)
# Starter or entry point function call
if __name__ == "__main__":
    main()