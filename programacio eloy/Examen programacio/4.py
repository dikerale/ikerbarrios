numero_de_productes = 0
preu_limitat = 20
preu = 0

while True:
    productes = float(input("Introdueix el preu dels teus productes(deix la linia en blanc per poder parar el codi)"))
    if productes > preu_limitat:
        numero_de_productes == 1
        productes == preu

    elif productes > preu_limitat:
        print("has arribat al preu limit")
    else:
        cost_total = preu / numero_de_productes
        print(f"el porcentatges final dels productes introduits es: {cost_total}")
       