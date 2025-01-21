numero = int(input("posa qualsevol numero: "))

es_parell = numero % 2 == 0

if es_parell:
    print(f"{numero} és un número parell: " )
else:
    print(f"{numero} és un número senar: " )