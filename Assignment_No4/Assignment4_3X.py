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
        return True

         
def Increment(Data):
    sum = 0
    sum = Data + 10

    return sum

def Multi(Data,sum):
    sum = sum * Data
    return sum

def filterX(Task,Data):
    Result = []
    for i in range(len(Data)):
        iret = Task(Data[i])
        if iret == True:
            Result.append(Data[i])
    return Result
  
def mapX(Task,Data):

    Result =[]

    for i in range(len(Data)):
        iret = Task(Data[i])
        Result.append(iret)

    return Result

def reduceX(Task,Data):
    result = 1
    for i in Data:
        result = Task(result,i)

    return result        
# accept one number from user and pass to Power
def main():
    print("enter the size ")
    size = int(input()) 

    Data = list()

    print("enter the element")

    for no in range(size):
        Data.append(int(input()))

    FData = list(filterX(Check,Data))
    print(FData)

    MData = list(mapX(Increment,FData))
    print(MData)

    RData = reduceX(Multi,MData)
    print(RData)

# Starter or entry point function call
if __name__ == "__main__":
    main()