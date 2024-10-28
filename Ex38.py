contrasenya = "eureka"
contador = 0
while contador <3:
    intent = (input("esbrina la contrasenya: "))
    if intent == contrasenya:
        print(f"Correcte! El número era {contrasenya}.")
        break
    contador += 1
    print("no ho has esbrinat, torna a intentar")
if contador == 3:
    print("has esgotat els intents")
    