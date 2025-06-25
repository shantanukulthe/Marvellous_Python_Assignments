"""
File:        Assignment14_4.py
Author:      Shantanu Kulthe
Date:        02/06/2025
Description: This file OOP concept to write application to print student details 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""


class Student:

    SchoolName = "Marvellous"

    def __init__(self,val1,val2):
        self.name = val1
        self.rollNo = val2
    def changeSchoolName(self,schoolname):
        Student.SchoolName = schoolname

        
    def Display(self):
        print("name of student :",self.name)
        print("rollno of student :",self.rollNo)
        print("school name of student:",Student.SchoolName)    

def main():

    print("Enter name of student")
    name = input()
    print("Enter name of student")
    rollno = int(input())

    obj = Student(name,rollno)

    obj.Display()

    print("enter school name")
    schoolname = input()

    obj.changeSchoolName(schoolname)

    obj.Display()

    
if __name__ == "__main__":
    main()    
