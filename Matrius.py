cont = 1
m = []  


for i in range(4):
    fila = []  
    for j in range(4):
        fila.append(cont)  
        cont += 1  
    m.append(fila)  
    cont -= 1


for fila in m:
    print(fila)