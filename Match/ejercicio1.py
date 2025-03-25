seccion = input("¿En qué sección desea sentarse (A/B/C/D)? ").upper()
cantidad = int(input("¿Cuántos boletos desea comprar? "))

match seccion:
    case "A":
        precio = 750
    case "B":
        precio = 500
    case "C":
        precio = 350
    case "D":
        precio = 250
    case _:
        precio = 0

total = precio * cantidad

if precio != 0:
    print(f"El total de su compra es: ${total}")
else:
    print("Sección no válida")
