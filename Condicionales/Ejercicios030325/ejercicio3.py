PI = 3.14159

figura = input("Elige una figura para calcular el área (C para círculo, T para triángulo): ").upper()

if figura == "C":
    radio = float(input("Ingresa el radio del círculo: "))
    area_circulo = PI * radio ** 2
    print(f"El área del círculo es: {area_circulo}")
elif figura == "T":
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    area_triangulo = (base * altura) / 2
    print(f"El área del triángulo es: {area_triangulo}")
else:
    print("Opción no válida")
