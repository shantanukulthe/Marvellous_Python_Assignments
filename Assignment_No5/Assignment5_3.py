"""
File:        Assignment5_2.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file Accept age from user and check waether he/she is eligible to vote or not
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def Eligiblity(age):

    if age >= 18:
        return True
    else :
        return False    

def main():

    print("enter age")
    age = int(input())

    iret = Eligiblity(age)

    if(iret == True):
        print("Eligible to vote")
    else :
        print(" not Eligible to vote")  


if __name__ == "__main__":
    main()    
