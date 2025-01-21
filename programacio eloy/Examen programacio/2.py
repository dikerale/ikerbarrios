while True:
    paraules = (input("Introdueix algunes paraules: "))

    if paraules == " ":
        print("Error, no has introduit cap caracter (has d'introduir al menos una paraula)")
   
    else:
        contar = len(paraules.split())
        print(contar)
