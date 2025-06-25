"""
File:        Assignment14_6.py
Author:      Shantanu Kulthe
Date:        02/06/2025
Description: This file OOP concept to write application to Arithmatic operations 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""


class Arithmatic:

    def __init__(self,val1,val2):
        self.no1 = val1
        self.no2 = val2


    def add(self):
        result = self.no1 + self.no2
        return result
    
    def sub(self):
        result = self.no1 - self.no2
        return result

    
    def multi(self):
        result = self.no1 * self.no2
        return result 

    
    def div(self):
        result = self.no1 / self.no2
        return result 

def main():
    print("Enter first number")
    no1 = int(input())

    print("Enter second number")
    no2 = int(input())

    obj = Arithmatic(no1,no2)

    iret = obj.add()
    print("Addition is :",iret)

    
    iret = obj.sub()
    print("substraction is :",iret)
    
    iret = obj.multi()
    print("multiplication is :",iret)
    
    iret = obj.div()
    print("division is :",iret)

if __name__ == "__main__":
    main()    
