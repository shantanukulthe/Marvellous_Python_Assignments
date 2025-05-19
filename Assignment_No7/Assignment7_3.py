"""
File:        Assignment7_3.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file take one list from user and use map function on it  
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

def EvenNumber(Data):
    if (Data % 2 == 0):
        return Data


def main():
    print("enter the size")
    size = int(input())
    Data = []
    print("enter the element")
    for i in range(size):
        Data.append(int(input()))

    FData = list(filter(EvenNumber,Data))

    print(FData)
if __name__ == "__main__":
    main()