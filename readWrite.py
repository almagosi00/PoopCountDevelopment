import os
from csv import writer
import string
import datetime
import operator

nameFileExtension = "PoopCount.csv"
nameFile = "PoopCount"
extension = ".csv"
separador = ';'
separadorNameFile = "_"
date_format = '%Y-%m-%d'
#formato -> nombre;fecha;hora

def add(name: string, date: datetime):

    os.path.isfile(nameFileExtension)

    with open(nameFileExtension, mode='a') as file:
        input = name + separador + str(date.date()) + separador + str(date.time()) +"\n"
        file.write(input)


def count():
    dictCount = dict()
    with open(nameFileExtension,mode='r') as file:
        rows = file.readlines()
        for row in rows:
            rowList = row.split(separador)
            if(rowList[0] in dictCount):
                
                dictCount.update({rowList[0]:dictCount.get(rowList[0]) + 1})
            else:
                dictCount.update({rowList[0]:1})
    output = ""
    dictOutput = dict( sorted(dictCount.items(), key=operator.itemgetter(1),reverse=True))
    for i in dictOutput:
        output = output + "\n" + i + " --> " + str(dictCount[i])
    return output
            


def clear(): #renombra el fichero
    newFileName = ""
    with open(nameFileExtension,mode='r') as file:
        rows = file.readlines()
        date = datetime.datetime.strptime(rows[len(rows)-1].split(separador)[1], date_format)
        newFileName = nameFile + separadorNameFile + str(date.month) + separadorNameFile + str(date.year) + extension
        
    os.rename(nameFileExtension,newFileName)