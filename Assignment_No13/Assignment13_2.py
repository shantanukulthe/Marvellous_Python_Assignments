"""
File:        Assignment13_2.py
Author:      Shantanu Kulthe
Date:        31/05/2025
Description: This file OOP concept to write application of Banking operations 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""


class BankAccount:

    ROI = 10.5

    def __init__(self,val1):
        self.Name = val1
        self.Amount = 0
        self.Time = 0
        self.interest = 0

    def Deposit(self,DepositeAmount):
        self.Amount = self.Amount + DepositeAmount

    def Withdraw(self,withdrawAmount):
        self.Amount = self.Amount - withdrawAmount    

    def CalculateInterset(self,years):
        self.Time = years
        self.interest = (self.Amount * BankAccount.ROI * self.Time)/100 

    def Display(self):
        print("Bank Account Holder Name :",self.Name)
        print("Total Amount :",self.Amount)
        print("ROI :",self.interest)


def main():

    print("Enter Account Holder Name")
    name = input()

    obj = BankAccount(name)
    print("Enter  Deposite Amount")
    amount = int(input())
    obj.Deposit(amount)
    print("enter withdrwa amount")
    withdrawAmt = int(input())
    obj.Withdraw(withdrawAmt)
    print("Enter Number of year")
    years = int(input())
    obj.CalculateInterset(years)

    obj.Display

    obj.Display()

if __name__ == "__main__":
    main()    
