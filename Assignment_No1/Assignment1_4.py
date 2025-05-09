"""
File:        Assignment1_4.py
Author:      Shantanu Kulthe
Date:        08/05/2025
Description: This file display name on screen (console)
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def PrintNameOnScreen(str):          # defination of printNameonscreen function take string into str and print that string 5 times 
    
    if(str == None):
        print("String is empty")

    for i in range(5):
        print(str)


def main():                          # defination of main function which string and passing string to function 
    name = "Marvellous"
    PrintNameOnScreen(name)
    
if __name__ == "__main__":           # starter function mian()
    main()
