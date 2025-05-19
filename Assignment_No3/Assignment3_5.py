"""
File:        Assignment2_5.py
Author:      Shantanu Kulthe
Date:        14/05/2025
Description: This file Accept List from user and check Prime number into it and perfom Addition   
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

 # main function take list from user and send that list to MarvellousNum module 
 # which return value into sum and we display that on output console

import MarvellousNum

def main():

    print("enter the size of element")
    size = int(input())

    if(size <=  0):
        print("You Have enter wrong size")
        return 

    Data = list()
    print("enter the elements")

    for no in range(size):
        Data.append(int(input()))

    sum =MarvellousNum.ListPrime(Data)

    print("Summation of prime number is :",sum)


 # Starter or entery point function 
if __name__ == "__main__":
    main()