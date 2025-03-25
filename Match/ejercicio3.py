cantidad = float(input("Ingrese la cantidad en centímetros: "))
opcion = input("Elija la conversión (m/km/mi): ")

match opcion.lower():
    case "m":
        resultado = cantidad / 100
        print(f"{cantidad} cm son {resultado} metros")
    case "km":
        resultado = cantidad / 100000
        print(f"{cantidad} cm son {resultado} kilómetros")
    case "mi":
        resultado = cantidad / 160934
        print(f"{cantidad} cm son {resultado} millas")
    case _:
        print("Opción no válida. Use m, km o mi")
