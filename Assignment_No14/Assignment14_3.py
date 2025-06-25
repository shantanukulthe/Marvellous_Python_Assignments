"""
File:        Assignment14_3.py
Author:      Shantanu Kulthe
Date:        02/06/2025
Description: This file OOP concept to write application to print book details 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""


class Book:

    def __init__(self,val1):
        self.__price = val1

    def Get(self):
        return self.__price

    
    def Set(self,newPrice):
        self.__price = newPrice
        return self.__price
            

def main():

    print("Enter Price of book")
    price = int(input())

    obj = Book(price)

    iret = obj.Get()
    print("price is :",iret)
    
    print("price to be set:")
    setprice = int(input())
    
    iret = obj.Set(setprice)
    print("price is :",iret)

    
if __name__ == "__main__":
    main()    
