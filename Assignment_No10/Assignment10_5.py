"""
File:        Assignment10_4.py
Author:      Shantanu Kulthe
Date:        22/05/2025
Description: This file create python application which use FMR to perform task
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

from  functools import reduce
def PrimeChck(Data):
    if(Data % 2 == 0):
        return False
    return True     

def Multiply(Data):
    sum = 0
    sum = Data * 2
    return sum

def GreaterNumber(Data,sum):
    if(sum < Data):
        sum = Data
    
    return sum




def main():

    print("enter size")
    size = int(input())

    Data = []

    print("enter the element")
    for i in range(size):
        Data.append(int(input()))


    FData = list(filter(PrimeChck,Data))
    print(FData)    
    MData = list(map(Multiply,FData))
    print(MData)
    RData = reduce(GreaterNumber,MData)
    print(RData)

if __name__ == "__main__":
    main()    
