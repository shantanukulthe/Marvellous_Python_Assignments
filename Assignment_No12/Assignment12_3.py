"""
File:        Assignment12_1.py
Author:      Shantanu Kulthe
Date:        31/05/2025
Description: This file OOP concept to calculate addition,substraction,multiplication,division
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""


class Arithmetic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self,val1,val2):
        self.value1 = val1
        self.value2 = val2

    def Addition(self):
        result= self.value1 + self.value2
        return result

    def substraction(self):
        if(self.value1 < 0):
            self.value1 = -self.value1
            
        result= self.value1 - self.value2
        return result

    def multiplication(self):
        result= self.value1 * self.value2
        return result

    def division(self):
        result= self.value1 / self.value2
        return result
  

def main():
    obj1 = Arithmetic()
    print("enter First number")
    no1 = int(input())
    print("enter second number")
    no2 = int(input())
    obj1.Accept(no1,no2)
    ret = obj1.Addition()
    print("Addition is :",ret)
    ret = obj1.substraction()
    print("Addition is :",ret)
    ret = obj1.multiplication()
    print("Addition is :",ret)
    ret = obj1.division()
    print("Addition is :",ret)


if __name__ == "__main__":
    main()    
