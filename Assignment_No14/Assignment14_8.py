"""
File:        Assignment14_8.py
Author:      Shantanu Kulthe
Date:        02/06/2025
Description: This file OOP concept to write application to use super functionality
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

class Vehicle:

    def start(self):
        print("start function in vehicle")

class Car(Vehicle):

    def start(self):
        super().start()
        print("start function in car ")

def main():

    obj = Car()
    obj.start()

    
if __name__ == "__main__":
    main()    
