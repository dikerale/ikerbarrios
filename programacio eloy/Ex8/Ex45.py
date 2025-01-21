nom = input("introdueix el teu nom")

paraules = nom.split()

inicials = "".join([paraula[0].upper() for paraula in paraules])

print(f"les inicials son: {inicials}")


