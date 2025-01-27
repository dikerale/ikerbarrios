import random
from emoji import emojize



pg = emojize(":zombie:")

m = [[], [], [], []]

def iniciar(m, pg):
    for i in range(4):
        for k in range(4):
            m[i].append(4)

iniciar(m, pg)


def persontage(pg):
    y = random.randint(0, 3)
    x = random.randint(0, 3)
    m[y][x]= pg
    return y, x

def mostrar_matriu():
    for llista in m:
        print(*llista)

def movement(x, y):

    moure = input("Apreta entre w, a, s o d per moure el persontge: ")

    m[y][x]= 4

    if moure == "a" and x-1 >= 0:
        x -= 1
        
    elif moure == "s" and y+1 <= 3:
        y += 1
        
    elif moure == "d" and x+1 <= 3:
        x += 1
    
        
    elif moure == "w" and y-1 >= 0:
        y -= 1

    else:
        print("No pots sortir dels limits del mapa")    
        
    m[y][x]= pg
    
    return y, x


y, x= persontage(pg)
mostrar_matriu()

while True:
    y, x = movement(x, y)
    mostrar_matriu()
    