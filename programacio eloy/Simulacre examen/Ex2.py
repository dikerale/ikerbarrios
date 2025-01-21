#2. Algorisme que sumi tots els números parells compresos entre 2 i 100.

sumar  = 0
for i in range(2, 101, 2):
    sumar += i
print(f"Aquesta es la suma dels nombres parells entre el 2 i 100: {sumar}")