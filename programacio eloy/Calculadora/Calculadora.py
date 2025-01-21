# Calculadora
def calcul_basic(operacio, num1, num2):

    if operacio == "+":
        suma= num1 + num2
        return suma
    elif operacio == "-":
        resta= num1 - num2
        return resta
    elif operacio == "*":
        multi= num1 * num2
        return multi
    elif operacio == "/":
        if  num2 == 0:
            return "no es pot divir per 0 maquina ;)"
        return num1 / num2



def eleva (base, exponent):
    resultat = base ** exponent
    return resultat 
    
   

