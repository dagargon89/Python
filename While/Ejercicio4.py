suma = 0
continuar = "n"

while continuar.lower() != "s":
    try:
        numero = float(input("Ingrese un número: "))
        suma += numero
        continuar = input("Presione 'S' para terminar o cualquier tecla para continuar: ")
    except ValueError:
        print("Por favor ingrese un número válido")

print(f"La suma total es: {suma}")
