peliculas_terror = ['El Exorcista', 'Halloween', 'Pesadilla en Elm Street', 'El Resplandor', 'It']

# Mostrar la lista actual con sus respectivos índices
print("Lista actual de películas de terror:")
for indice, pelicula in enumerate(peliculas_terror):
    print(f"{indice}: {pelicula}")

# Preguntar al usuario si quiere eliminar elementos por índice o por nombre
opcion = input("¿Quieres eliminar una película por índice o por nombre? (indice/nombre): ").strip().lower()

if opcion == 'indice':
    # Pedir al usuario que ingrese el índice del elemento a eliminar
    indice = int(input("Ingresa el índice de la película que deseas eliminar: "))
    # Verificar si el índice está dentro del rango de la lista
    if 0 <= indice < len(peliculas_terror):
        # Eliminar el elemento en el índice dado
        pelicula_eliminada = peliculas_terror.pop(indice)
        print(f"La película '{pelicula_eliminada}' ha sido eliminada.")
    else:
        print("Índice fuera del rango de la lista.")
elif opcion == 'nombre':
    # Pedir al usuario que ingrese el nombre del elemento a eliminar
    pelicula = input("Ingresa el nombre de la película que deseas eliminar: ").strip()
    # Verificar si la película está en la lista
    if pelicula in peliculas_terror:
        # Eliminar el elemento por nombre
        peliculas_terror.remove(pelicula)
        print(f"La película '{pelicula}' ha sido eliminada.")
    else:
        print("La película no está en la lista.")
else:
    print("Opción no válida.")

# Mostrar la lista actualizada
print("Lista actualizada de películas de terror:")
for indice, pelicula in enumerate(peliculas_terror):
    print(f"{indice}: {pelicula}")
