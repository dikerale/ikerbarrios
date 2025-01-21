cadena = input("Introdueix una cadena de text: ")
caracter = (input("introdueix el caracter que vols veure: "))

while len(caracter) != 1:
    print("introdueix nomes un sol caracter")
    caracter = input("si has posat mes d'un caracter introdueix aqui un sol caracter: ")

caracter_a_contar = cadena.count(caracter)

print(f"{caracter} apareix {caracter_a_contar} vegades a la cadena.")



