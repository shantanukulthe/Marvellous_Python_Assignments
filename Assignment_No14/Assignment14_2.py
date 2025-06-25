"""
File:        Assignment14_2.py
Author:      Shantanu Kulthe
Date:        02/06/2025
Description: This file OOP concept to write application to print area and perimeter of rectangle
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""


class Rectangle:

    def __init__(self,val1,val2):
        self.length = val1
        self.width = val2

    def Area(self):
        area =  self.length * self.width
        return area

    def Perimeter(self):
        perimeter =  2*(self.length * self.width)
        return perimeter    

def main():

    print("Enter length")
    length = int(input())

    print("Enter width")
    width = int(input())

    obj = Rectangle(length,width)

    iret = obj.Area()

    print("area of rectangle is :",iret)

    
    iret = obj.Perimeter()

    print("Perimeter of rectangle is :",iret)

    
if __name__ == "__main__":
    main()    
