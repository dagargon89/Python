# Definir una lista de bandas de heavy metal
bandas_heavy_metal = ['Metallica', 'Iron Maiden', 'Black Sabbath', 'Judas Priest', 'Megadeth']

# Pedir al usuario que ingrese el nombre de una banda
banda = input("Ingresa el nombre de una banda de heavy metal: ")

# Verificar si la banda está en la lista y mostrar su índice
if banda in bandas_heavy_metal:
    indice = bandas_heavy_metal.index(banda)
    print(f"El índice de la banda '{banda}' es {indice}.")
else:
    print("La banda no está en la lista.")
