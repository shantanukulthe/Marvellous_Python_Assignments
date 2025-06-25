"""
File:        Assignment17_1.py
Author:      Shantanu Kulthe
Date:        10/06/2025
Description: This Application to display Jay Ganesh every 2 second using shedule
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import schedule
import time
def display():

    print("Jay Ganesh....")
    
def main():

    schedule.every(2).seconds.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()    
