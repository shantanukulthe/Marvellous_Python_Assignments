"""
File:        Assignment12_1.py
Author:      Shantanu Kulthe
Date:        31/05/2025
Description: This file OOP concept related programing
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""


class Demo:

    Value = 10
    def __init__(self,val1,val2):
        self.no1 = val1
        self.no2 = val2


    def fun(self):
        print(self.no1)
        print(self.no2)

    def Gun(self):
        print(self.no1)
        print(self.no2)

def main():
    # print("enter first number")
    # no1 = int(input())

    # print("enter second number")
    # no2 = int(input())

    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.fun()
    obj1.Gun()

    obj2.fun()
    obj2.Gun()





if __name__ == "__main__":
    main()    
