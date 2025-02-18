llista = []

def afegir():
    numero = int(input("Introdueix el nombre que vulguis: "))
    llista.append(numero)
def esborrar():
    borrar = int(input("Introdueix el numero que vols borrar: "))
    if borrar in llista:
        llista.remove(borrar)
    else:
        print("No esta a la llista")
def llistar():
    print("llista: ", llista)
def sortir():
    exit()

while True:

    print("1- Afegir, 2- Esborrar, 3- llistar, 4. sortir")

    opcio = int(input("Introdueix el numro que vulguis: "))

    if opcio == "1":
        afegir()
    if opcio == "2":
        esborrar()
    if opcio == "3":
        llistar()
    if opcio == "4":
        sortir()
        break