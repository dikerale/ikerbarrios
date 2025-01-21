cadena = input("Introdueix una cadena de text: ")
vocals = ""  
for lletra in cadena:
    if lletra in "aeiouAEIOU":
        vocals += lletra  
print("Vocals en ordre invers:", vocals[::-1])  

