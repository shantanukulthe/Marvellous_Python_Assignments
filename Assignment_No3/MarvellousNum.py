def ChckPrime(value):
    for no in range(2, value):
        if(value % no == 0):
            return False
    return True

#This function get call from main as it accept the list and we fetch value from list using indexing value call ChckPrime function and send 
# value and check weather value is prime or not recive True or Value     
def ListPrime(Data):
    if not Data:
        print("Invalid Input")
        return
    sum = 0
    for no in range(len(Data)):
        iret = ChckPrime(Data[no])
        if(iret == True):
            sum = sum + Data[no]

    return sum               

