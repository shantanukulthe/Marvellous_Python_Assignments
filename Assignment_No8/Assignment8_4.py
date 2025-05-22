"""
File:        Assignment8_4.py
Author:      Shantanu Kulthe
Date:        19/05/2025
Description: This file create three thread which accept string from user and check wheather string contain small,capital and digit 
             in it and return count
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import threading
import os
def SmallLetter(Data):
    print("Small Letter PID is :",os.getpid())
    icnt = 0
    for i in Data:
        if(i >= 'a') and (i <= 'z'):
            icnt = icnt + 1
    print("Small letter is :",icnt)         

def CapitalLetter(Data):
    print("Capital Letter PID is :",os.getpid())
    icnt = 0
    for i in Data:
        if(i >= 'A') and (i <= 'Z'):
            icnt = icnt + 1
    print("capital letter is :",icnt) 

def Digit(Data):
    print("Digit PID is :",os.getpid())
    icnt = 0
    for i in Data:
        if(i >= '0') and (i <= '9'):
            icnt = icnt + 1
    print("Digit is :",icnt)


def main():

    print("main PID is :",os.getpid())
    print("enter string")
    string = input()


    T1 = threading.Thread(target=SmallLetter,args=(string,))
    T2 = threading.Thread(target=CapitalLetter,args=(string,))
    T3 = threading.Thread(target=Digit,args=(string,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()
    print("main thread end")

if __name__ == "__main__":
    main()    
