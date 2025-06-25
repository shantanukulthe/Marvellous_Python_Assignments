"""
File:        Assignment22.py
Author:      Shantanu Kulthe
Date:        13/06/2025
Description: This Application to 
Interpreter: PVM (Python Virtual Machine)
Platform:    Windows
"""
import hashlib 
import os
import sys
import time
import schedule
import smtplib
import ssl
from email.message import EmailMessage 

def sendMail(filename,receive):
    # pass
    send  = "shantanukulthe3@gmail.com"
    receive = receive
    password = "rvby nito xhou uojq"

    subject = "Duplicate File remove"
    msg = EmailMessage()
    msg['From'] = send
    msg['To']   = receive
    msg['subject'] = subject

    
    fobj = open(filename,"rb")
    data = fobj.read()

    msg.add_attachment(data,maintype = "application ",subtype = "octet-stream",filename=filename)

    create = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com",465,context=create)
    server.login(send,password)
    server.send_message(msg)

def ChecksumValue(fname):

    fobj = open(fname,"rb")
    hobj = hashlib.md5()
    data = fobj.read(1024)

    while(len(data)>0):
        hobj.update(data)
        data = fobj.read(1024)

    return hobj.hexdigest()    

    

def DisplayProcess(DirName,receive):

    iret = os.path.isdir(DirName)

    if iret == False:
        exit()
    
    timestamp = time.ctime()
    Dirname = "MarvellousLog"
    
    if not os.path.exists(Dirname):
        os.mkdir(Dirname)
    
    filename  = "Marvellous%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")
    filename = os.path.join(Dirname,filename)
    
    fobj = open(filename,"w")
    
    Duplicate = {}
    
    for Foldername,subFolderNames,FileNames in os.walk(DirName):
        for fname in FileNames:
            fname = os.path.join(Foldername,fname)
            Checksum = ChecksumValue(fname)

            if(Checksum in Duplicate):
                Duplicate[Checksum].append(fname)
                fobj.write(str(fname) + "\n")
                os.remove(fname) 
            else:
                Duplicate[Checksum] = [fname]
                  
    sendMail(filename,receive)

def main():
    
    Border = "-"*86
    print(Border)
    print("----------------------------Marvellous Automation-------------------------------------")
    print(Border)

    if (len(sys.argv)== 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This Application is used to perform ----")
            print("This is the Automation Script")
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the give script as:")
            print("Script Name.py Argument1 Argument2 ")
        else:   
            file = sys.argv[1]
            
            fobj = open(file, "r")
            data = fobj.read().splitlines()

            DirName = data[0]
            timer   = int(data[1])
            receive = data[2]
            
            schedule.every(timer).minutes.do(lambda:DisplayProcess(DirName,receive)) 
            while True:
                schedule.run_pending()
                time.sleep(1) 
    else:
        print("Invalid command line Arguments")
        print(" Use given Flag")
        print("--h : Use to display the Help")
        print("--u : Use to display the usage")            

    print(Border)
    print("---------------------Tankyou for using our script-------------------------------------")
    print("----------------------------Marvellous Automation-------------------------------------")
    print(Border)

if __name__ == "__main__":
    main()    
