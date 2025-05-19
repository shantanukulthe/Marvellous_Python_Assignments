"""
File:        Assignment6_5.py
Author:      Shantanu Kulthe
Date:        16/05/2025
Description: This file check weather number is prime or not 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def ChckPrime(no):
    if(no == 2):
        return True

    if(no % 2 == 0):
        return False
    else :
        return True 

def main():
    print("Enter the number")
    no = int(input())
    iret = ChckPrime(no)
    
    if iret == True:
        print("Number is Prime")
    else:
        print("Number is not Prime")
    
if __name__ == "__main__":
    main()    
