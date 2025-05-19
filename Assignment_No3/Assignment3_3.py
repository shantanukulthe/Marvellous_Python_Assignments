"""
File:        Assignment2_3.py
Author:      Shantanu Kulthe
Date:        14/05/2025
Description: This file Accept List from user return minimum number from list  
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

# This function gets call from main function which accept list from main function and find Minimum value from  list and return that value
def Minimum(Data):

    if not Data:
        print("Not Valid Datas")
        return
        
    imin = Data[0]
    for no in range(len(Data)):
        if imin > Data[no]:
            imin = Data[no]

    return imin        
        
 # main function take list from user and send that list to Minimum function
 # which return value into imin and we display that on output console
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

    if not Data:
        print("You have entered wrong List")
        return

    print("entered Data is :",Data)

    imin = Minimum(Data)

    print("Minimum number is :",imin)


 # Starter or entery point function 
if __name__ == "__main__":
    main()