def afegir(llista, numero):

    llista.append(numero)

def esborrar(llista, numero):

    if numero in llista:
        llista.remove(numero)
    else:
        print("Aquest numero no esta a la llista")

def llista_funcio(llista):
    print("llista", llista)
    
def Sortir():
    exit()

llista = []
numero = None

while True:
    print("1-Afegir, 2-Esborrar 3-llista, 4-Sortir")

    opcions = input("Tria alguna de les opcions: ")
    if opcions == "1":
        afegir_vari = int(input("Introdueix el numero que vulguis: "))
        afegir(llista, numero)
    if opcions == "2":
        esborrar()
    if opcions == "3":
        llista_funcio()

    if opcions == "4":
        print("Sortint del joc")
        Sortir()
        break
        
    
    

        


