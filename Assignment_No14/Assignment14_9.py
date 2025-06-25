"""
File:        Assignment14_9.py
Author:      Shantanu Kulthe
Date:        02/06/2025
Description: This file OOP concept to write application to use __eq__ functionality
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

class Product:
    def __init__(self,val1,val2):
        self.name = val1
        self.price = val2

    def __eq__(self,other):
        if self.price == other:
            return True
        else:
            return False

def main():

    obj1 = Product("bike",20000)
    obj2 = Product("car",20000)

    if obj1 == obj2:
        print("product are same")
    else:
        print("product are not same")    
    
if __name__ == "__main__":
    main()    
