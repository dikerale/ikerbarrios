import os

ruta = os.getcwd()

llista = []

filename = 'ikerbarrios.txt'


def afegir():
    nou = {}
    nou['nom']= input("Nom: ")
    nou['cognom']= input("Cognom: ")
    llista.append(nou)
def mostar():
    pass
def exportar():
    with open(filename) as f_obj:
        lines = f_obj.readlines()
    for line in lines:
        usuari = line.rstrip().split()
        dict = {}
        dict['nom']= usuari[0]
        dict['cognom']= usuari[1]
        llista.append(dict)

def importar():
    pass
def sortir():
    exit()

while True:
    print("1-Afegir, 2-Mostar, 3-exportar, 4-importar, 5-sortir")

    opcions = int(input("Introdueix el el numero del que vulguis fer"))

    if opcions == "1":
        afegir()
    if opcions == "2":
        mostar()
    if opcions == "3":
        exportar()
    if opcions == "4":
        importar()
    if opcions == "5":
        sortir()