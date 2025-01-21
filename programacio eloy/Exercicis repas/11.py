numero_edat = int(input("Introdueix el numero de vegades que vol introduir l'edat: "))
llista = []
for i in range(numero_edat):
    edats = int(input(f"introdueix la teva edat {i+1} vegades: "))
    if edats > 17:
        llista.append(edats)
contador = len(llista)
print(f"Son majors d'edat {contador} persona/es")


    


