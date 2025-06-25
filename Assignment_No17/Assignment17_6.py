"""
File:        Assignment17_6.py
Author:      Shantanu Kulthe
Date:        10/06/2025
Description: This Application to write time to file
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import schedule
import time
from datatime import datatime
def display():
    filename = "Marvellous.txt"
    timestamp = datatime.now()
    fobj = open(filename,"w")
    fobj.write(str(timestamp))
    
def main():

    schedule.every(1).minutes.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()    
