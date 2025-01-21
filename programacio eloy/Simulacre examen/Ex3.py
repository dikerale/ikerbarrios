contrasenya = "1234"
suma = 0
nintents= 3


while suma <nintents:
    intent = (input("encerta la contrasenya: "))
    if intent == contrasenya:
        print(f"Vaya maquina ho has encertat.")
        break
    suma += 1
    print("Et queda un intent menys maquina")
if suma == nintents:
    print("No tens intens maquina")