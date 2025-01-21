frase = input("introdueix una frase: ")

espais = frase.replace(" ", "").lower()

if espais == espais [::-1]:
    print(f"la cadena si es un palindrom: {frase}")

else:
    print(f"la cadena no es un palindrom: {frase}")