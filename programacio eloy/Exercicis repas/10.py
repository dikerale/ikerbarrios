import random

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lletres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cominado = numeros + lletres

contrasenya = random.choices(cominado, k=8)

print(*contrasenya)