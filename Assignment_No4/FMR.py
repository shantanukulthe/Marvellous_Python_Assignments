def filterX(Task,Data):
    Result = []
    for i in Data:
        iret = Task(i)
        if iret == True:
            Result.append(i)
    return Result
  
def mapX(Task,Data):

    Result =[]

    for i in Data:
        iret = Task(i)
        Result.append(iret)

    return Result

def reduceX(Task,Data):
    result = 1
    for i in Data:
        result = Task(result,i)

    return result      


def reduceXX(Task,Data):
    result = Data[0]
    for i in Data:
        result = Task(result,i)

    return result          