treballadors = [

    {"Nom": "Marc", 
    "Edat": 28 ,
    "Salari": 1500 },


    {"Nom": "Anna", 
    "Edat": 22 ,
    "Salari": 1400 },

    {"Nom": "Maria", 
    "Edat": 40 ,
    "Salari": 2000 },

    {"Nom": "Jaume", 
    "Edat": 41 ,
    "Salari": 1800 },

    {"Nom": "Manel", 
    "Edat": 18 ,
    "Salari": 1200 },

    {"Nom": "Rosa", 
    "Edat": 49 ,
    "Salari": 1800 },
    ]

def llistar_treballadors(treballadors):
    print(f"Nom     Edat    Salari")
    for i in treballadors:
        print(i["Nom"]+"\t" + str(i["Edat"])+ "\t" + str(i["Salari"]))

def llistar_noms(treballadors):

    for treball in treballadors:
        print(treball["Nom"])

def afegir_treballadors(treballadors):
    
    nou = {}
    nou['Nom'] = input("Nom: ")
    nou['Edat'] = int(input("Edat: "))
    nou['Salari'] = int(input("Salari: "))
    treballadors.append(nou)

def salari_alt():
    max = 0
    for treb in treballadors:
        if treb['Salari'] > max:
            max = treb['Salari']
            print(f"Max Salari: {max}")
        
def menors():
    cont = 0
    for treb in treballadors:
        if treb ['Edat'] < 35:
            cont += 1
            print(f"{cont}")

while True:
    opcio = (input("Llistar 1, noms 2, afegir 3, salari 4, menors 5: "))

    if opcio == "1":
        llistar_treballadors(treballadors)
    elif opcio == "2":
        llistar_noms(treballadors)
    elif opcio == "3":
        afegir_treballadors(treballadors)
    elif opcio == "4":
        salari_alt()
    elif opcio == "5":
        menors()
    





