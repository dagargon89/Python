
'''Pide al usuario que ingrese una frase y muestra la cantidad de palabras que tiene la frase.'''
frase = input("Ingresa una frase: ")

cantidad_palabras = len(frase.split())

print(f"La frase ingresada tiene {cantidad_palabras} palabras.")
