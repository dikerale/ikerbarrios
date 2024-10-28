frase = (input("introdueix una frase: "))

vocals = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for lletra in frase:
    if lletra in vocals:
        print(f"la primera lletra vocal és: {lletra}")
        break 