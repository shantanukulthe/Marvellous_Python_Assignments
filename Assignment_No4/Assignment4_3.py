"""
File:        Assignment4_3.py
Author:      Shantanu Kulthe
Date:        15/05/2025
Description: This file Accept list from User and perform FMR(Filter,Map,Reduce) 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
from functools import reduce

def Check(Data):
    Result = []
    if(Data >= 70) and (Data <= 90):
        Result.append(Data)

    return Result        
    
def Increment(Data):
    sum = 0
    sum = Data + 10

    return sum

def Multi(Data,sum):
    sum = sum * Data
    return sum
    
# accept one number from user and pass to Power
def main():
    print("enter the size ")
    size = int(input()) 

    Data = list()

    print("enter the element")

    for no in range(size):
        Data.append(int(input()))

    FData = list(filter(Check,Data))
    print(FData)

    MData = list(map(Increment,FData))
    print(MData)

    RData = reduce(Multi,MData)
    print(RData)
# Starter or entry point function call
if __name__ == "__main__":
    main()