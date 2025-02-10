import os
cwd = os.getcwd()

llista = []

filename = 'ikerbarrios.txt'

with open(filename) as f_obj:
 lines = f_obj.readlines()

for line in lines:
    usuari = line.rstrip().split()
    dict = {}
    dict['nom']= usuari[0]
    dict['cognom']= usuari[1]
    llista.append(dict)

print(*llista)