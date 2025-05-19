"""
File:        Assignment7_2.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file take one list from user and use map function on it  
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""


def Double(Data):
    sum = 1
    sum = Data * 2
    return sum


def main():
    print("enter the size")
    size = int(input())
    Data = []
    print("enter the element")
    for i in range(size):
        Data.append(int(input()))

    MData = list(map(Double,Data))

    print(MData)
if __name__ == "__main__":
    main()