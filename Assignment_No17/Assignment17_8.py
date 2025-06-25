"""
File:        Assignment17_8.py
Author:      Shantanu Kulthe
Date:        10/06/2025
Description: This Application to write take file backup everyhour
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import schedule
import time
import os

def FileBackup():

    filename = "MarvellousBackup.log"
    FolderName = "Backup"
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    filename = os.path.join(FolderName,filename)   

    fobj = open(filename,"w")

    fobj.write("backup Taken at"+time.ctime())
    
        
def main():

    schedule.every(1).minutes.do(FileBackup)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()    
