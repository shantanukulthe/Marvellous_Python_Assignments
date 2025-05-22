"""
File:        Assignment8_4.py
Author:      Shantanu Kulthe
Date:        19/05/2025
Description: This file create two thread which accept no from user and print number accordingly
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import threading
def Display(no):
    for i in range(1,no+1):
        print(i)

def DisplayRevers(no):
    for i in range(no,0,-1):
        print(i)
    
def main():

    print("enter Number")
    no = int(input())


    T1 = threading.Thread(target=Display,args=(no,))
    T2 = threading.Thread(target=DisplayRevers,args=(no,))

    T1.start()
    T1.join()
    print("waiting for T1")
    T2.start()
    T2.join()
    print("main thread end")

if __name__ == "__main__":
    main()    
