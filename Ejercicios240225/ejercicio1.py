''' 
pide a un usuario que ingrese una frase y una letra, 
y muestra cuantas veces aparece la letra en la frase
'''
frase = input("Ingresa una frase: ").lower()

letra = input("Ingresa una letra: ").lower()

contador = frase.count(letra)

print(f"La letra '{letra}' aparece {contador} veces en la frase.")
