"""
File:        Assignment14_1.py
Author:      Shantanu Kulthe
Date:        02/06/2025
Description: This file OOP concept to write application to print employe details 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""


class Employee:

    def __init__(self,val1,val2,val3):
        self.Name = val1
        self.Emp_id = val2
        self.Salary = val3

    def Display(self):
        print("Name of Employee :",self.Name)
        print("Epm_ID  :",self.Emp_id)
        print("Salary of Employee :",self.Salary)    

def main():

    print("Enter Name of employee")
    name = input()

    print("Enter Employee ID employee")
    Epm_ID = int(input())

    print("Enter Salary of employee")
    Salary = int(input())

    obj = Employee(name,Epm_ID,Salary)

    obj.Display()

    
if __name__ == "__main__":
    main()    
