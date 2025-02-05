import random

def iniciar_joc(): # utilitzo aquesta funcio per poder iniciar el joc i que no es puguin introduir nombres imparells
    print("Benvingut al meu joc del Memory.")
    while True:
        try:
            parelles = int(input("Introdueix les parelles que vols jugar: "))
            if parelles % 2 == 0:
                return parelles
            else:
                print("Les parelles han de ser un numero parell")
        except ValueError:
            print("No pots introduir lletres")
    

def generar_parelles(parelles): # Utilitzo aquesta funcio per poder crear les cartes del meu joc i poder barrejarles per poder jugar
    numero_cartes = parelles * parelles
    numero_parelles = numero_cartes // 2
    lletres = ["pizza", "macarronos", "amanida", "pollastre", "sopa", "yogurt", "hamburguesa", "kebab"] * 2
    random.shuffle(lletres)
    
    cartes = lletres[:numero_parelles * 2]
    random.shuffle(cartes)
    return cartes

def mostrar_tauler(parelles):  # Modificat per retornar la matriu
    m = [["X" for _ in range(parelles)] for _ in range(parelles)]
    return m


def mostrar_matriu(m): #Aquesta funcio l'utilitzo per quan la matriu es generi ho separo cada espai amb |
    for fila in m:
        print(" | ".join(fila))

def actualitzar_estat(tauler, posicio1, posicio2, cartes):  # La funció accepta tuples per posicions
    fila1, columna1 = posicio1
    fila2, columna2 = posicio2
    if cartes[fila1 * len(tauler) + columna1] == cartes[fila2 * len(tauler) + columna2]:
        tauler[fila1][columna1] = cartes[fila1 * len(tauler) + columna1]
        tauler[fila2][columna2] = cartes[fila2 * len(tauler) + columna2]
    else:
        tauler[fila1][columna1] = "X"  # Torna les cartes a "X" si no són iguals
        tauler[fila2][columna2] = "X"


def jugar():
    parelles = iniciar_joc()
    cartes = generar_parelles(parelles)
    tauler = mostrar_tauler(parelles) 
    
    while True:
        mostrar_matriu(tauler) 
        try:
            fila1, columna1 = map(int, input("Introdueix les files i les columnes de la primera parella d'aquesta manera 0 0: ").split())
            fila2, columna2 = map(int, input("Introdueix les files i les columnes de la segona parella d'aquesta manera 0 0: ").split())

            if tauler[fila1][columna1] != "X" or tauler[fila2][columna2] != "X":
                print("Aquestes cartes ja han estat revelades.")
                continue  

            actualitzar_estat(tauler, (fila1, columna1), (fila2, columna2), cartes)  # Actualitza l'estat del tauler
            
        except ValueError:
            print("Introdueix be la parella que vols escollir (tal i com en el format que demano).")
        
        if guanyar(tauler):  
            print("Enhorabona ets un geni")
            break

        

def guanyar(tauler):
    return all(cart != "X"for fila in tauler for cart in fila)  


# Cridar la funció jugar() per començar el joc
jugar()
  