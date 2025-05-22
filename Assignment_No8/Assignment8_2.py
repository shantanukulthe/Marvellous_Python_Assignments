"""
File:        Assignment8_1.py
Author:      Shantanu Kulthe
Date:        19/05/2025
Description: This file create two thread and perform even factors and odd factors summation 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import threading
def AddEvenFactor(no):
    sum = 0
    for i in range(1,no+1):
        if(no % i == 0) and (i % 2 == 0):
            sum = sum + i
    print("Add even factor is :",sum)     

def AddOddFactor(no):
    sum = 0
    for i in range(1,no):
        if(no % i == 0) and (i % 2 != 0):
            sum = sum + i
    print("Add Odd factor is :",sum) 

def main():

    print("enter Number")
    no = int(input())

    T1 = threading.Thread(target=AddEvenFactor,args=(no,))
    T2 = threading.Thread(target=AddOddFactor,args=(no,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("main thread end")

if __name__ == "__main__":
    main()    
