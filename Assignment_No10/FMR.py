def filterX(Task,Data):
    result = []

    for i in Data:
        iret = Task(i)
        if(iret == True):
            result.append(i)
    return result        

def mapX(Task,Data):
    result = []

    for i in Data:
        iret = Task(i)
        result.append(iret)
    return result            

def reduceX(Task,Data):
    result = 1

    for i in Data:
        result = Task(i,result)
    return result   
