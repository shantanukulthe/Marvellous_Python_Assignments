"""
File:        Assignment1_9.py
Author:      Shantanu Kulthe
Date:        08/05/2025
Description: This file Accept number from user and display Even number (first 10) 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
def EvenNumber(value): # defination of EvenNumber which accept Number and display even numbers   
    
    if(value == None):
        print("Number is not valid")

    i = 1
    while(i<=value*2):
        if(i % 2 == 0):
            print(i,end=" ")
        i= i + 1


def main(): # defination of main function which  take input from user and function call (Even Numbers)
    print("enter the number :")
    no = int(input())

    EvenNumber(no)

    
if __name__ == "__main__": # starter (main function call)
    main()
