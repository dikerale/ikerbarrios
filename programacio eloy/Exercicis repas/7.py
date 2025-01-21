frase = input("Introdueix una frase: ")

paraules = frase.split()

comptador = sum(1 for paraula in paraules if len(paraula) > 4)

print(f"La frase té {comptador} paraules amb més de 4 caràcters.")
