"""
File:        Assignment3_1.py
Author:      Shantanu Kulthe
Date:        14/05/2025
Description: This file Accept List from user and perform Addition on that 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
# This function gets call from main function which accept list from main function and perform 
# addition on values there in list and return summantion
def Addition(Data):

    if not Data:
        print("Not Valid Datas")
        return
    sum = 0

    for no in range(len(Data)):
        sum = sum + Data[no]

    return sum        


 # main function take list from user and send that list to addition function
 # which return value into result and we display that on output console
def main():              

    print("Enter no of element")
    size = int(input())

    if(size <=  0):
        print("You Have enter wrong size")
        return 
    Data = []

    print("enter the elemnt")

    for no in range(size):
        # iret = int(input())
        Data.append(int(input()))
    
    if not Data:
        print("You have entered wrong List")
        return

    result  = Addition(Data)

    print("Addition is :",result)


 # Starter or entery point function 
if __name__ == "__main__": 
    main()   