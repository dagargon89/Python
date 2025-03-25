cantidad = int(input("¿Cuántos números deseas sumar? "))
suma = 0

for i in range(cantidad):
    numero = float(input(f"Introduce el número {i + 1}: "))
    suma += numero

print(f"La suma total es: {suma}")
