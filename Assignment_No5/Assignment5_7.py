"""
File:        Assignment5_2.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file Accept length and width and calculate are and perimeter
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def Area(length,width):
    Area = length * width
    return Area

def perimeter(length,width):
    perimeter = 2 *(length + width)
    return perimeter

def main():

    print("enter length")
    length = int(input())
    print("enter width")
    width = int(input())

    iret = Area(length,width)

    print("Area of Rectangle  is:",iret)

    iret = perimeter(length,width)
    print("Perimeter of Rectangle  is:",iret)


if __name__ == "__main__":
    main()    
