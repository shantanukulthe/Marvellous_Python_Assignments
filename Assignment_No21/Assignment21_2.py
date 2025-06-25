"""
File:        Assignment21_2.py
Author:      Shantanu Kulthe
Date:        13/06/2025
Description: This Application to display running process name and id from user
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import psutil         

def DisplayProcess(name):
    print("Information of current running process are:")

    for proc in psutil.process_iter(['pid','name']):
        if(proc.info['name'] == name):
            print(proc.info)


def main():

    print("enter process name :")
    name = input()

    DisplayProcess(name)    

if __name__ == "__main__":
    main()    
