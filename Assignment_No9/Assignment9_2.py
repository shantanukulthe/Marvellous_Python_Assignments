"""
File:        Assignment9_2.py
Author:      Shantanu Kulthe
Date:        19/05/2025
Description: This file create python program using multipleprocessing process to square list of number using multiple process
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import multiprocessing
import time

def Display(Data):
    sum = 1
    for i in Data:
        sum = i * i
        print("sqaure is :",sum)

def main():

    print("enter size")
    size = int(input())

    Data = []
    print("enter the element")
    for i in range(size):
        Data.append(int(input()))

    P1 = multiprocessing.Process(target=Display,args=(Data,))
    P2 = multiprocessing.Process(target=Display,args=(Data,))
    P3 = multiprocessing.Process(target=Display,args=(Data,))

    P1.start()
    P2.start()
    P3.start()
    P1.join()
    P2.join()
    P3.join()
    print("main thread end")

if __name__ == "__main__":
    main()    
