"""
File:        Assignment17_4.py
Author:      Shantanu Kulthe
Date:        10/06/2025
Description: This Application to display Namaste every 9am using shedule
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import schedule
import time
def display():
    print("Do coding....")
    
def main():

    schedule.every(30).minutes.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()    
