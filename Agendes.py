import json, re, os

ruta = os.getcwd()
arxiu = 'json.json'

regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
agenda = []



def afegir():
    while True:
        try:
            noms = input("Introdueix el nom: ")
            telf = input("Introdueix el telf: ")
            
            email = ""
            while not re.search(regex, email):  # Canviem la condició perquè el bucle funcioni correctament
                email = input("Introdueix el Mail: ")
            newsletter_entrada = input("Voldries entar a newsletter? (si/no): ").lower()
            newsletter = newsletter_entrada == "si"
            
            try: 
                id = agenda[-1]["id"] + 1
            except (IndexError, KeyError):
                id = 0
            
            contacte = {"id": id, "Nom": noms, "telefon": telf, "mail": email, "newsletter": newsletter}
            agenda.append(contacte)
            print("Contacte afegit a la perfeccio")
            
            break  # Afegim el break aquí perquè surti del bucle després d'afegir un contacte correcte

        except ValueError:
            print("Error")

def mostrarContacte(contacte):    
    print(f"{contacte['id']: <10}{contacte['Nom']: <15}{contacte['telefon']: <20}{contacte['mail']: <25}{'Si' if contacte.get('newsletter', False) else 'No'}")

def mostrarAgenda():
    print(f"{'ID': <10}{'Nom': <15}{'Telefon': <20}{'Mail': <25}{'Newsletter'}")
    print("-" * 80)
    
    for contacte in agenda:
        mostrarContacte(contacte)
def cercarContacte():

    while True:
        busqueda = input("Introdueix el nom que vulguis cercar: ").lower()
    
        trobar = False

        for contacte in agenda:
            if busqueda.lower() == contacte["Nom"]:
                print(f"{contacte['id']: <10}{contacte['Nom']: <15}{contacte['telefon']: <20}{contacte['mail']: <25}{'Si' if contacte.get('newsletter', False) else 'No'}")
                print(f"{'ID': <10}{'Nom': <15}{'Telefon': <20}{'Mail': <25}{'Newsletter'}")
                trobar = True
        
        if not trobar:
            print("\nAquest nom no està dins de l'agenda.")

       
        repetir = input("\nVols cercar un altre contacte? (Si/No): ").lower()
        if repetir != "si":
            break
def modificar():
    if not agenda:
        print("L'agenda està buida. No hi ha contactes per modificar.")
        return

   
    mostrarAgenda()
    
    try:
        id_modificar = int(input("\nIntrodueix l'ID del contacte a modificar: "))
        
        
        contacte = next((c for c in agenda if c["id"] == id_modificar), None)

        if not contacte:
            print(f"No s'ha trobat cap contacte amb ID {id_modificar}.")
            return

        print("\nDeixa el camp en blanc per mantenir el valor actual.\n")

        
        nou_nom = input(f"· Nom ({contacte['Nom']}): ").lower() or contacte['Nom']
        nou_telefon = input(f"· Telèfon ({contacte['telefon']}): ").lower() or contacte['telefon']
        nou_mail = input(f"· Mail ({contacte['mail']}): ").lower() or contacte['mail']

        
        while nou_mail and not re.match(regex, nou_mail):
            print("El correu electrònic no és vàlid. Torna a introduir-lo.")
            nou_mail = input(f"· Mail ({contacte['mail']}): ") or contacte['mail']

        nou_newsletter = input(f"· Newsletter (Si/No) ({'Si' if contacte['newsletter'] else 'No'}): ").lower()
        if nou_newsletter == "":
            nou_newsletter = contacte["newsletter"]
        else:
            nou_newsletter = True if nou_newsletter == "si" else False

        
        contacte.update({
            "Nom": nou_nom,
            "telefon": nou_telefon,
            "mail": nou_mail,
            "newsletter": nou_newsletter
        })

        print("\nContacte modificat correctament!")

    except ValueError:
        print("Error: Has d'introduir un ID vàlid.")
  
def esborrar():
    if not agenda:
        print("L'agenda està buida. No hi ha contactes per esborrar.")
        return
    mostrarAgenda()
    try:
        esborrar_contacte = int(input("\nIntrodueix l'ID del contacte a modificar: "))

        for k in agenda:
            if k["id"] == esborrar_contacte:
                confirmar = input("Estas segur d'esborrar el contacte (Si/No): ").lower()
                if confirmar == "si":
                    agenda.remove(k)
                    print("Contacte esborrat a la perfeccio")
    except ValueError:
        print("Has posat un ID invalid")

def exportar():
    if not agenda:
        print("L'agenda està buida. No hi ha res a exportar.")
        return

    try:
        with open(arxiu, 'w', encoding="utf-8") as f_obj:
            json.dump(agenda, f_obj, indent=4, ensure_ascii=False)
        print("Contactes exportats correctament a 'json.json'.")

    except Exception as e:
        print(f"Error en exportar: {e}")

    
def importar():
    if not os.path.exists(arxiu):
        print("No s'ha trobat cap fitxer d'agenda per importar.")
        return

    try:
        with open(arxiu, 'r', encoding="utf-8") as f_obj:
            agenda = json.load(f_obj)
        print("Contactes importats correctament!")

    except json.JSONDecodeError:
        print("Error: El fitxer JSON està buit o té un format incorrecte.")
    except Exception as e:
        print(f"Error en importar: {e}")
def sortir():
    print("Sortint del programa")
    exit()
    

def menu():
    print("\nAgenda")
    print("1- Afegir Contacte")
    print("2- Mostrar Agenda")
    print("3- Cercar Contacte")
    print("4- Modificar Contacte")
    print("5- Esborrar Contacte")
    print("6- Exportar Contacte")
    print("7- Importar Contacte")
    print("8- Sortir")

    opcions = input("Introdueix el nº d'algunes de les opcions: ")

    if opcions == "1":
        afegir()
    elif opcions == "2":
        mostrarAgenda()
    elif opcions == "3":
        cercarContacte()
    elif opcions == "4":
        modificar()
    elif opcions == "5":
        esborrar()
    elif opcions == "6":
        exportar()
    elif opcions == "7":
        importar()
    elif opcions == "8":
        sortir()
    else:
        print("Escull algunes de les opcions")
while True:
    menu()

