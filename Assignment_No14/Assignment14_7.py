"""
File:        Assignment14_7.py
Author:      Shantanu Kulthe
Date:        02/06/2025
Description: This file OOP concept to write application to use super functionality
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

class Base:
    def __init__(self,val1,val2):
        self.name = val1
        self.age = val2
        print(self.name)
        print(self.age)

class Teacher(Base):

    def __init__(self,val1,val2):
        self.subject = "science"
        self.salary = 28000
        print(self.subject)
        print(self.salary)
        super().__init__(val1,val2)

def main():

    dobj = Teacher("shantanu",28)

    
if __name__ == "__main__":
    main()    
