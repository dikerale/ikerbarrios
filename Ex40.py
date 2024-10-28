import calendar
from datetime import datetime


def datavalida(dia, mes, any):
    try:
        data = datetime(year=any, month=mes, day=dia)
        return True
    except ValueError:
        return False


def mesnom(mes):
    mesos = ["gener", "febrer", "març", "abril", "maig", "juny", "juliol", "agost", "setembre", "octubre", "novembre", "desembre"]
    return mesos[mes - 1]


dia = int(input("Introdueix el dia: "))
mes = int(input("Introdueix el mes (1-12): "))
any = int(input("Introdueix l'any: "))

if datavalida(dia, mes, any):
    print(f"La data és: {dia} de {mesnom(mes)} de {any}")
else:
    print("Error: La data no és vàlida.")

