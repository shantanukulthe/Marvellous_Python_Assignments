"""
File:        Assignment1_5.py
Author:      Shantanu Kulthe
Date:        08/05/2025
Description: This file display range on console
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def PrintRange(value): # defination of PrintRange which accept Range and display it accordingly 
    
    if(value == None):
        print("Number is not valid")

    for i in range(10,0,-1):
        print(i,end = " ")


def main(): # defination of main function which contain function call (PrintRange)
    no = 10
    PrintRange(no)
    
if __name__ == "__main__": # starter (main function call)
    main()
