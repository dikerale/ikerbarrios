suma = 0
while True:
    cadena = int(input("Introdueix una cadena de numeros (introdueix un numero negatiu per poder acabar): "))
    if cadena < 0:
        break
    suma+=cadena
print(f"la suma total es: {suma}")


