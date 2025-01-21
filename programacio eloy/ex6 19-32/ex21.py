suma = 0
contador = 0

while contador < 5:
    nombre = int(input("Introdueix un nombre: "))
    if nombre % 2 != 0:
        suma += nombre
        contador += 1

print("La suma dels 5 primers nombres imparells és:", suma)
