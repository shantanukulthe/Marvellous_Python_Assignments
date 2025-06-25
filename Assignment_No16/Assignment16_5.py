"""
File:        Assignment16_5.py
Author:      Shantanu Kulthe
Date:        09/06/2025
Description: This Application to read file and display only that line which contain more than five words
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import os
def display(filename):

    fobj = open(filename,"r")
   
    while True:
        line = fobj.readline()
        
        if not line:
            break
        words = ""
        count = 0
        for ch in line:
            if(ch != " " and ch != '\t' and ch != '\n'):
                words = words + ch
            else:
                if((words != " ") and (len(words) >= 5)):
                    count = count + 1
                words = ""

            # After loop, check last word also
        if(words != "" and len(words) >= 5):
            count = count + 1        
        if (count >= 1):
            print(line)


def main():

    print("enter the file name :")
    filename = input()

    display(filename)    

if __name__ == "__main__":
    main()    
