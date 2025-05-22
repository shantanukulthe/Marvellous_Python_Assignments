"""
File:        Assignment9_4.py
Author:      Shantanu Kulthe
Date:        19/05/2025
Description: This file create python application which perfrom addition of 1 to 10 million number 
             create normal function ,thread and multiple process and count the time it take for execution 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import multiprocessing
import threading
import time

def Display(no):
    sum = 0
    for i in range(1,no+1):
        sum = sum + i
    print(sum)    

def main():

    print("enter number")
    no = int(input())

    start_time = time.time()
    Display(no)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time for normal function",execution_time)


    start_time = time.time()
    T1 = threading.Thread(target=Display,args=(no,))
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time for Thread function",execution_time)


    start_time = time.time()
    P1= multiprocessing.Process(target=Display,args=(no,))
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time for Multiprocessing function",execution_time)


    print("main thread end")

if __name__ == "__main__":
    main()    
