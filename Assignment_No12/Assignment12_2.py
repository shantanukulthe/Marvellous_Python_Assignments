"""
File:        Assignment12_2.py
Author:      Shantanu Kulthe
Date:        31/05/2025
Description: This file OOP concept to calculate area,radius,circumference
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""


class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0


    def Accept(self,val1):
        self.radius = val1

    def calculateArea(self):
        self.area = Circle.PI * self.radius * self.radius

    def calculateCircumference(self):
        self.circumference =2 * Circle.PI  * self.radius    

    def Display(self):
        print("Area of circle is:",self.area)
        print("circumference of circle is:",self.circumference)
        

def main():
    obj1 = Circle()
    print("enter radius")
    no = int(input())
    obj1.Accept(no)
    obj1.calculateArea()
    obj1.calculateCircumference()
    obj1.Display()


if __name__ == "__main__":
    main()    
