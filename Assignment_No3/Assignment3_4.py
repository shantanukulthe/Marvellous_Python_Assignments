"""
File:        Assignment2_4.py
Author:      Shantanu Kulthe
Date:        14/05/2025
Description: This file Accept List from user and One another number return frequency of that number into the list   
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

# This function gets call from main function which accept list from main function and find Minimum value from  list and return that value
def Frequency(Data,value):

    if not Data and value:
        print("Not Valid Datas")
        return

    icnt = 0
    for no in range(len(Data)):
        if Data[no] == value:
            icnt = icnt + 1

    return icnt        
        
 # main function take list from user and send that list to Minimum function
 # which return value into imin and we display that on output console
def main():

    print("enter the size of element")
    size = int(input())

    print("Enter number ")
    value = int(input())

    if(size <=  0) or (value <= 0):
        print("You Have enter wrong size")
        return 

    Data = list()
    print("enter the elements")

    for no in range(size):
        Data.append(int(input()))

    print("entered Data is :",Data)

    ifeq = Frequency(Data,value)

    print("Maximun number is :",ifeq)


 # Starter or entery point function 
if __name__ == "__main__":
    main()