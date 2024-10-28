frase = (input("introdueix una frase: "))

posicio_b1 = frase.count("b")
posicio_c1 = frase.count("c")

if posicio_b1 > posicio_c1:
    print("hi ha mes b")
else:
    print("hi ha mes c")



