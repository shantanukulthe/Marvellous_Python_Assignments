"""
File:        Assignment8_1.py
Author:      Shantanu Kulthe
Date:        19/05/2025
Description: This file create two thread and perform Addition of even and odd number 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import threading
def AddEven(no):
    sum = 0
    for i in range(1,no*2+1):
        if(i % 2 == 0):
            sum = sum + i
    print("Add even is :",sum)     

def AddOdd(no):
    sum = 0
    for i in range(1,no*2):
        if(i % 2 != 0):
            sum = sum + i
    print("Add Odd is :",sum) 

def main():

    print("enter Number")
    no = int(input())

    T1 = threading.Thread(target=AddEven,args=(no,))
    T2 = threading.Thread(target=AddOdd,args=(no,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("main thread end")

if __name__ == "__main__":
    main()    
