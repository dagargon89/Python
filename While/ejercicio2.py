numero_secreto = 7
numero_usuario = int(input("Adivina el número (1-10): "))

while numero_usuario != numero_secreto:
    if numero_usuario > numero_secreto:
        numero_usuario = int(input("Es menor. Intenta otra vez: "))
    else:
        numero_usuario = int(input("Es mayor. Intenta otra vez: "))

print("¡Correcto! Has adivinado el número.")
