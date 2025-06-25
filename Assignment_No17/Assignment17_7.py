"""
File:        Assignment17_7.py
Author:      Shantanu Kulthe
Date:        10/06/2025
Description: This Application to write time to file
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import schedule
import time
def displayLunchTime():
    print("Luch Time!")
    

def displayWrapUpWork():
    print("Wrap Up Work")
        
def main():

    schedule.every().day.at("13:00").do(displayLunchTime)
    schedule.every().day.at("18:00").do(displayWrapUpWork)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()    
