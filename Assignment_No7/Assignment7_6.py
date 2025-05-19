"""
File:        Assignment7_6.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file take one list from user and use filter functionality and find prime  number
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

def ChckPrime(Data):
    if(Data == 2):
        return True

    if( Data % 2 == 0) or (Data % 3 == 0):
        return False
    return True    

def main():
    print("enter the size")
    size = int(input())
    Data = []
    print("enter the element")
    for i in range(size):
        Data.append(int(input()))

    FData = list(filter(ChckPrime,Data))

    print(FData)
if __name__ == "__main__":
    main()