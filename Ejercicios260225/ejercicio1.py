
# Definir una lista de ejemplo
listaPokemon = ['Pikachu', 'Charmander', 'Squirtle', 'Bulbasaur', 'Jigglypuff']

# Pedir al usuario que ingrese el índice del elemento que desea conocer
indice = int(input("Ingresa el índice del elemento que deseas conocer: "))

# Verificar si el índice está dentro del rango de la lista
if 0 <= indice < len(listaPokemon):
    # Mostrar el valor del elemento en el índice dado
    print(f"El valor del elemento en el índice {indice} es {listaPokemon[indice]}")
else:
    # Mostrar un mensaje de error si el índice está fuera del rango
    print("Índice fuera del rango de la lista.")
