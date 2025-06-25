"""
File:        Assignment14_5.py
Author:      Shantanu Kulthe
Date:        02/06/2025
Description: This file OOP concept to write application to print Bank details 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""


class Bank:

    def __init__(self,val1,val2,val3):
        self.accountNo = val1
        self.name = val2
        self.balance = val3


    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        self.balance = self.balance - amount

    
    def DisplayBalance(self):
        print("account number :",self.accountNo)
        print("name of account holder :",self.name)
        print("balance :",self.balance)    

def main():
    print("Enter account number")
    accountnumber = int(input())

    print("Enter name of account holder")
    name = input()

    print("balance amount")
    balance = int(input())

    obj = Bank(accountnumber,name,balance)

    obj.DisplayBalance()

    print("enter deposit amount")
    depositamount = int(input())

    obj.deposit(depositamount)

    obj.DisplayBalance()

    print("enter withdraw amount")
    withdraw = int(input())

    obj.withdraw(withdraw)

    obj.DisplayBalance()

    
if __name__ == "__main__":
    main()    
