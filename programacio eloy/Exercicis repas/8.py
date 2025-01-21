numeros = [float(input(f"Introdueix el número {i+1}: ")) for i in range(10)]
mitjana = sum(numeros) / len(numeros)
mes_proper = min(numeros, key=lambda x: abs(x - mitjana))
print(f"La mitjana és {mitjana:.2f} i el número més proper és {mes_proper}.")
