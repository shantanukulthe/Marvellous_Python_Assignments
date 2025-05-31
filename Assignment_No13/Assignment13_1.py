"""
File:        Assignment12_1.py
Author:      Shantanu Kulthe
Date:        31/05/2025
Description: This file OOP concept to Display name of author and Books
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""


class BookStore:

    NoofBooks = 0
    def __init__(self,val1,val2):
        self.Name = val1
        self.Author = val2
        BookStore.NoofBooks = BookStore.NoofBooks + 1 

    def Display(self):
        print("Name of Book :",self.Name)
        print("Name of Author :",self.Author)
        print("Number of Books :",BookStore.NoofBooks)



def main():

    print("Enter name of Book")
    name = input()

    print("Enter Author of Book")
    author = input()

    obj = BookStore(name,author)

    obj.Display()

if __name__ == "__main__":
    main()    
