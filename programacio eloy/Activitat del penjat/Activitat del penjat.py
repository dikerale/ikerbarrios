# Activitat del penjat
from getpass import getpass

def iniciar_joc():
    print("Benvingut al meu joc del penjat")
    paraula = obtenir_paraula()
    vides, lletres_fallades, paraula_oculta = inicialitzar_estat(paraula)

    while True:
        mostrar_estat(paraula_oculta, lletres_fallades, vides)
        lletra = obtenir_lletra()
        
        # Es crida a actualitzar l'estat amb la lletra introduïda
        vides, paraula_oculta, lletres_fallades = actualitzar_estat(paraula, paraula_oculta, lletres_fallades, vides, lletra)

        # Comprovar si el jugador ha guanyat
        if ha_guanyat(paraula_oculta):
            mostrar_resultat(True, paraula)
            break
        elif vides == 0:
            mostrar_resultat(False, paraula)
            break
        
        # Es mostra el dibuix del penjat basat en les vides restants
        dibuixar_penjat(vides)

def obtenir_paraula():
    while True:
        paraula_oculta = getpass("Introdueix la paraula oculta: ").lower()
        if not paraula_oculta.isalpha():
            print("Has introduït caracters que no són vàlids per al joc, introdueix només lletres.")
        elif " " in paraula_oculta:
            print("No es poden posar espais, posa només lletres.")
        else:
            break
    return paraula_oculta

def inicialitzar_estat(paraula_oculta):
    longitut_paraula = len(paraula_oculta)
    paraula_oculta_estat = ["_"] * longitut_paraula  # Es crea una llista amb guions per representar la paraula
    lletres_fallades = []
    vides = 7
    return vides, lletres_fallades, paraula_oculta_estat

def mostrar_estat(paraula_oculta, lletres_fallades, vides):

    # La paraula oculta es mostra com una cadena separada per espais
    print("Paraula: " + " ".join(paraula_oculta))
    print(f"Lletres fallades: {', '.join(lletres_fallades)}")
    print(f"Vides Restants: {vides}")

def obtenir_lletra():
    while True:
        lletra = input("Posa la lletra que vulguis: ").lower()
        if len(lletra) != 1 or not lletra.isalpha():
            print("Error: introdueix una única lletra vàlida.")
        else:
            return lletra

def actualitzar_estat(paraula, paraula_oculta, lletres_fallades, vides, lletra):
    # Es comprova si la lletra és dins de la paraula
    if lletra in paraula:
        print(f"La lletra '{lletra}' està dins de la paraula. Molt bé")
        
        # Actualitza la paraula oculta amb les lletres encertades
        for i, caracter in enumerate(paraula):
            if caracter == lletra:
                paraula_oculta[i] = lletra
    else:
        if lletra not in lletres_fallades:
            print(f"La lletra '{lletra}' no està a la paraula. Tens una vida menys.")
            vides -= 1  # Resta una vida si la lletra no està
            lletres_fallades.append(lletra)  # Afegeix la lletra a les fallades
        else:
            print(f"La lletra '{lletra}' ja la vas intentar abans!")
    return vides, paraula_oculta, lletres_fallades

def ha_guanyat(paraula_oculta):
    # Comprova si encara queden guions a la paraula oculta
    return "_" not in paraula_oculta

def mostrar_resultat(guanyat, paraula):
    # Mostra un missatge diferent si el jugador guanya o perd
    if guanyat:
        print("Enhorabona has guanyat el joc del penjat")
        print(f"La paraula era: {paraula}")
    else:
        print("Has perdut, tens 0 vides.")
        print(f"La paraula era: {paraula}")

def dibuixar_penjat(vides):
    # Dibuix del penjat basat en el nombre de vides restants
    dibuix = [
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """
    ]
    print(dibuix[7 - vides])  # Tria el dibuix en funció de les vides


iniciar_joc()

