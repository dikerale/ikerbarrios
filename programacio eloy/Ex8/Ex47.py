cadena = input("")

caracter = input("")

while len(caracter) != 1:
    caracter = input("Error, introdueix un sol caracter")

caracter2 = input("")

while len(caracter2) != 1:
    caracter2 = input("Error, introdueix un sol caracter")


  
cadena_nova = cadena.replace(caracter, caracter2)

print(cadena_nova)