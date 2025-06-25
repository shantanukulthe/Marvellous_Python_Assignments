"""
File:        Assignment21_1.py
Author:      Shantanu Kulthe
Date:        13/06/2025
Description: This Application to display running process name and id
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import psutil         
def main():

    print("Information of current running process are:")

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ['pid','name'])
        print(info)


if __name__ == "__main__":
    main()    
