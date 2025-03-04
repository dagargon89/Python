lista_animes = ['Naruto', 'One Piece', 'Attack on Titan', 'My Hero Academia', 'Dragon Ball Z']

# Mostrar la lista actual con sus respectivos índices
print("Lista actual de animes:")
for indice, anime in enumerate(lista_animes):
    print(f"{indice}: {anime}")

# Pedir al usuario que ingrese la posición del elemento que desea modificar
posicion = int(input("Ingresa la posición del anime que deseas modificar: "))

# Verificar si la posición está dentro del rango de la lista
if 0 <= posicion < len(lista_animes):
    # Pedir al usuario que ingrese el nuevo nombre del anime
    nuevo_anime = input("Ingresa el nuevo nombre del anime: ")
    # Modificar el elemento en la posición especificada
    lista_animes[posicion] = nuevo_anime
    print("Lista actualizada de animes:")
    for indice, anime in enumerate(lista_animes):
        print(f"{indice}: {anime}")
else:
    print("Posición fuera del rango de la lista.")
