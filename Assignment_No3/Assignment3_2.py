"""
File:        Assignment2_2.py
Author:      Shantanu Kulthe
Date:        14/05/2025
Description: This file Accept List from user return Maximun number from list  
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""

# This function gets call from main function which accept list from main function and find Maximum value from  list and return that value
def Maximun(Data):

    if not Data:
        print("Not Valid Datas")
        return
    
    imax = Data[0]
    for no in range(len(Data)):
        if imax < Data[no]:
            imax = Data[no]

    return imax        
        
 # main function take list from user and send that list to Maximun function
 # which return value into imax and we display that on output console
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

    imax = Maximun(Data)

    print("Maximun number is :",imax)


 # Starter or entery point function 
if __name__ == "__main__":
    main()