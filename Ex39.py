llista = int(input("Introdueix un número, 0 per parar el programa: "))
acumulador = 0
count = 0
max = llista
min = llista

while llista != 0:
    
    acumulador += llista
    count += 1

    
    if llista > max:
        max = llista
    if llista < min:
        min = llista

    
    llista = int(input("Introdueix un número, 0 per parar el programa: "))


if count > 0:
    mitjana = acumulador / count
    print(f"numero maxim: {max}")
    print(f"numero minim: {min}")
    print(f"Mitjana: {mitjana:.2f}")
else:
    print("No s'ha introduït cap número vàlid.")



