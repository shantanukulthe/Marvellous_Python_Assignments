"""
File:        Assignment7_4.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file take one list from user and use reduce functionality and find product of all number
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
from functools import reduce

def Product(Data,sum):
    sum = Data * sum 
    return sum

def main():
    print("enter the size")
    size = int(input())
    Data = []
    print("enter the element")
    for i in range(size):
        Data.append(int(input()))

    RData = reduce(Product,Data)

    print(RData)
if __name__ == "__main__":
    main()