lista = []
cantidad = int(input("¿Cuántos elementos desea agregar? "))

for i in range(cantidad):
    elemento = input(f"Ingrese el elemento {i+1}: ")
    lista.append(elemento)

print("La lista final es:", lista)
