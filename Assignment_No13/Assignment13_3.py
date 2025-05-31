"""
File:        Assignment13_3.py
Author:      Shantanu Kulthe
Date:        31/05/2025
Description: This file OOP concept to write application of Banking operations 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""


class Number:

    def __init__(self,val1):
        self.value = val1

    def checkPrime(self):
        if(self.value % 2 == 0):
            return False
        else:
            return True    

    def CheckPerfect(self):
        sum = 0
        for i in range(1,self.value):
            if(self.value % i == 0):
                sum = sum + i
            if(self.value == sum):
                return True 
            else:
                return False            

    def Factors(self):
        for i in range(1,self.value):
            if(self.value % i == 0):
                print("Factors of number :",i)


    def sumFactor(self):
        sum = 0
        for i in range(1,self.value):
            if(self.value % i == 0):
                sum = sum + i

        return sum

def main():

    print("Enter Number")
    no = int(input())

    obj = Number(no)

    bret = obj.checkPrime()
    if(bret == True):
        print("Its prime Number")
    else:    
        print("Its not prime Number")

    bret = obj.CheckPerfect()
    if(bret == True):
        print("Its perfect Number")
    else:    
        print("Its not perfect Number")

    obj.Factors()
    
    ret = obj.sumFactor()
    print("Factorial sum is :",ret)

if __name__ == "__main__":
    main()    
