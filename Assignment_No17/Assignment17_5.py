"""
File:        Assignment17_5.py
Author:      Shantanu Kulthe
Date:        10/06/2025
Description: This Application to display Namaste every 9am using shedule
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import schedule
import time
def display():
    print("Namaste...")
    
def main():

    schedule.every().day.at("21:00").do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()    
