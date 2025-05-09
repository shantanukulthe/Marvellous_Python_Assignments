"""
File:        Assignment1_10.py
Author:      Shantanu Kulthe
Date:        08/05/2025
Description: This file Accept String from user and display lenght  
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def stringlen(str):# This function accept the string and use inbuild function and print string length
    if(str == None):
        print("Invalid input")
    stringlen = len(str)
    print("string length is :",stringlen)

def main(): # defination of main function which  take input from user and calculate length on it (call stringlen function which use inbuild function)
    print("enter the number :")
    name = input()

    if(name == None):
        print("Invalid input")

    icnt = 0

    for i in name:
        icnt = icnt + 1
        
    print("String Lenght is :",icnt) 
    # second approch 
    stringlen(name)   

    
if __name__ == "__main__": # starter (main function call)
    main()


