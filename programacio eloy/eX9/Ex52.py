llista = []

while True:
    entrada = input("introdueix qualsevol numero, posa un 0 per poder acabar: ")

    if not entrada.isdigit():
        print("introdueix un numero valid: ")
        continue

    numero = int(entrada)

    if numero == 0:
        break

    llista.append(numero)

print("numeros introduits: ", *llista)

suma = sum(llista)
print("Aquesta es la suma:", suma)

quantitat = len(llista)

print("Aquesta es la quantitat de numeros: ", quantitat)


