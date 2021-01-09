from datetime import date
from datetime import datetime


def DataHora(argument):
    today = date.today()    
    if argument == "data1":
        return today.strftime("%d/%m/%Y")
    if argument == "data2":
        return today.strftime("%B %d, %Y")
    if argument == "data3":
        return today.strftime("%m/%d/%y")
    if argument == "data4":
        return today.strftime("%b-%d-%Y")
    
    now = datetime.now()
    if argument == "agora":
        return now
    if argument == "data":
        return now.date()
    if argument == "tempo":
        return now.time().replace(microsecond=0)
    if argument == "ano":
        return now.year
    if argument == "mes":
        return now.month
    if argument == "dia":
        return now.day
    if argument == "hora":
        return now.hour
    if argument == "segundo" or argument == "segundos" or argument =="s":
        return now.second
    if argument == "microsegundo" or argument == "microsegundos" or argument =="ms" :
        return now.microsecond
    
    return -1


def botao1():
    print("clicou")

if __name__ == '__main__':
    print("estou por aqui")
    print(DataHora("data1"))