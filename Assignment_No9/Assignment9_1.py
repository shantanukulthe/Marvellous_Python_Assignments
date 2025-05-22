"""
File:        Assignment9_1.py
Author:      Shantanu Kulthe
Date:        19/05/2025
Description: This file create three thread which display 1 to 5 after interval of 1 second
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import threading
import time

def Display(no):
    for i in range(1,no+1):
        print(i)


def main():

    print("enter number")
    no = int(input())

    T1 = threading.Thread(target=Display,args=(no,))
    T2 = threading.Thread(target=Display,args=(no,))
    T3 = threading.Thread(target=Display,args=(no,))

    T1.start()
    time.sleep(1)
    T2.start()
    time.sleep(1)
    T3.start()
    T1.join()
    T2.join()
    T3.join()
    print("main thread end")

if __name__ == "__main__":
    main()    
