def afegir():
    numero = int(input("Introdueix el numero que vulguis: "))
    llista.append(numero)

def esborrar():
    numero = int(input("Introdueix el numero que vulguis: "))
    if numero in llista:
        llista.remove(numero)
    else:
        print("Aquest numero no esta a la llista")

def llista_funcio():
    print("llista", llista)
    
def sortir():
    exit()

llista = []

while True:
    print("1-Afegir, 2-Esborrar 3-llista, 4-Sortir")

    opcions = input("Tria alguna de les opcions: ")

    if opcions == "1":
        afegir()
    if opcions == "2":
        esborrar()
    if opcions == "3":
        llista_funcio()
    if opcions == "4":
        print("Sortint del joc")
        sortir()
        break