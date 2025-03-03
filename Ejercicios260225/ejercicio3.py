# Definir una lista de bandas de power metal
bandas_power_metal = ['Helloween', 'Blind Guardian', 'Stratovarius', 'Rhapsody of Fire', 'Sonata Arctica']

# Mostrar la lista actual
print("Lista actual de bandas de power metal:")
print(bandas_power_metal)

# Pedir al usuario que ingrese la posición y el nombre de la banda para agregar a la lista
posicion = int(input("Ingresa la posición donde deseas agregar la nueva banda: "))
banda = input("Ingresa el nombre de la nueva banda: ")

# Verificar si la posición está dentro del rango de la lista
if 0 <= posicion <= len(bandas_power_metal):
    # Agregar la nueva banda en la posición especificada
    bandas_power_metal.insert(posicion, banda)
    print("Lista actualizada de bandas de power metal:")
    print(bandas_power_metal)
else:
    print("Posición fuera del rango de la lista.")
