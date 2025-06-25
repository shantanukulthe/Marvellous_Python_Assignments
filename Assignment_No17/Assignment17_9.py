"""
File:        Assignment17_9.py
Author:      Shantanu Kulthe
Date:        10/06/2025
Description: This Application to check mail 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import schedule
import time
import os
import imaplib


email = 'shantanukulthe3@gmail.com'
password = 'uwku kgdk fofd puxc'
IMAP_SERVER = 'imap.gmail.com'
def checkMail():

    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(email, password)
    mail.select("inbox")

    status,data = mail.search(None,"UNSEEN")

    if status == "OK":
        unread = data[0].split()
        print("U have unread mails",unread)
    else:
        print("No unread mails ")    

        
def main():

    schedule.every(1).second.do(checkMail)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()    


