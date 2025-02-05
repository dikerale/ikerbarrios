import random
import string

matriu = []

def iniciar_joc():
    # Funció principal que controla el flux del joc.
    print("Benvingut al meu joc del Memory.")
    while True:
        try:
            parelles = int(input("Introdueix les parelles que vols jugar en la partida: "))
            if parelles < 4 or parelles > 5:
                print("Introdueix un nombre de parelles entre 1 i 10.")
            else:
                break
        except ValueError:
            print("Si us plau, introdueix un número vàlid.")

    caselles, generar_llista = generar_parelles(parelles)
    revelades = [False] * len(generar_llista)  # Estat de les caselles revelades

    while not ha_guanyat(revelades):
        mostrar_tauler(caselles, revelades)
        
        # Selecció de la primera casella
        casella1 = obtenir_casella(revelades, "Primera casella: ")
        caselles[casella1] = generar_llista[casella1]  # Revela temporalment la casella
        mostrar_tauler(caselles, revelades)  # Mostra el tauler amb la primera casella revelada

        # Selecció de la segona casella
        casella2 = obtenir_casella(revelades, "Segona casella: ")
        caselles[casella2] = generar_llista[casella2]  # Revela temporalment la casella
        mostrar_tauler(caselles, revelades)  # Mostra el tauler amb totes dues caselles revelades

        # Comprovació si les caselles coincideixen
        if revisar_parella(generar_llista, casella1, casella2):
            print("Parella trobada!")
            actualitzar_estat(revelades, casella1, casella2, True)
        else:
            print("No coincideixen. Intenta-ho de nou.")
            actualitzar_estat(caselles, casella1, casella2, False)

    print("Felicitats! Has trobat totes les parelles.")

def generar_parelles(parelles):
    # Genera les parelles d'elements, les barreja aleatòriament i inicialitza les caselles com a ocultes.
    generar_llista = list(string.ascii_uppercase[:parelles] * 2)
    random.shuffle(generar_llista)
    caselles = ["*"] * len(generar_llista)
    return caselles, generar_llista

def mostrar_tauler(caselles, revelades, tauler):
    # Mostra el tauler actual, revelant només les caselles que han estat descobertes.
    
    for i in range(caselles):
        for k in range(caselles):
            if revelades [i][k]:
                print(tauler[i][k], end=" ")
            else:
                print("?", end=" ")

def obtenir_casella(revelades, missatge):
    # Demana al jugador que introdueixi una casella vàlida que encara no estigui revelada.
    while True:
            casella = int(input(missatge))
            if casella < 0 or casella >= len(revelades):
                print("Introdueix un número dins el rang del tauler.")
            elif revelades[casella]:
                print("Aquesta casella ja està revelada. Tria una altra.")
            else:
                return casella

def revisar_parella(generar_llista, casella1, casella2):
    # Comprova si les dues caselles seleccionades són una parella coincident.
    return generar_llista[casella1] == generar_llista[casella2]

def actualitzar_estat(tauler, casella1, casella2, es_parella):
    # Actualitza l'estat del tauler: si no és una parella, les caselles tornen a estar ocultes.
    if not es_parella:
        tauler[casella1] = "*"
        tauler[casella2] = "*"

def ha_guanyat(revelades):
    # Comprova si totes les caselles han estat revelades, indicant que el joc s'ha acabat.
    return all(revelades)

# Iniciar el joc

iniciar_joc()