vector = [int(input(f"introdueix el numero {i+1} ")) for i in range(15)]

parells = 0 
senars = 0

for numero in vector:
    if numero %2 == 0:
        parells +=1
    else:
        senars +=1
print(f"Has introduit {senars}numeros senars i {parells} numeros parells")





