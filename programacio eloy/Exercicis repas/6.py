llistat = []
preus = []

while True:
    productes = input("introdueix tots el productes (posa la paraula fi per poder acabar): ")
    preu_producte = float(input("introdueix el preu del producte: "))
    if productes == "fi":
        break
    llistat.append(productes)
    preus.append(preu_producte)

for prod, preu in zip(llistat, preus):
    print(f"{prod}: {preu:.2f} €")





