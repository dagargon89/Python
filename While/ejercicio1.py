valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))

while valor2 <= valor1:
    valor2 = float(input("El segundo valor debe ser mayor. Ingrese nuevamente: "))

print(f"Valores válidos: {valor1} y {valor2}")
