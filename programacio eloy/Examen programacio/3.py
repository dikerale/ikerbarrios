contrasenya = "benvingut"
contador = 0

while contador < 4:

    intent = (input("intenta esbrinar la contrasenya: "))

    if intent == contrasenya:
        print(f"Molt be has encertat la contrasenya {contrasenya}.")
        break

    contador += 1

    print("No ho has esbrinat, torna a intentar")

if contador == 4:
    print("has esgotat els intents, l'ordinador s'ha bloquejat")