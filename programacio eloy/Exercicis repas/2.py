temperatura = []

for i in range(7):
    temperatures = float(input(f"Introdueix la temperatura del dia {i+1}: "))
    temperatura.append(temperatures)

maxima = max(temperatura)
minima = min(temperatura)
mitjana = sum(temperatura) / len(temperatura)

print(maxima)
print(minima)
print(mitjana)