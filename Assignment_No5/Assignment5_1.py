"""
File:        Assignment5_1.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file Accept tow number from user and perform Arithmetic operation
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def Addition(no1,no2):
    return no1 + no2

def Difference(no1,no2):
    icnt = 0
    i =no2
    j =no1
    if(no1 < no2):
        i = no1
        j = no2
    
    while (j != i):
        icnt = icnt +1
        i=i+1
    return icnt


def Product(no1,no2):
    return no1 * no2

def Division(no1 ,no2):
    return no1 / no2

def main():

    print("enter first number ")
    no1 = int(input())

    print("enter second number ")
    no2 = int(input())

    Add = Addition(no1,no2)
    print("Addition is :",Add)

    count = Difference(no1,no2)
    print("Difference is :",count)

    product = Product(no1,no2)
    print("Product is :",product)

    div = Division(no1,no2)
    print("Division is :",div)


if __name__ == "__main__":
    main()    
