n = int(input("¿Cuántos números desea ingresar?: "))
pares = 0
impares = 0
lista_pares = []
lista_impares = []

for i in range(n):
    numero = int(input(f"Ingrese el número {i+1}: "))
    while numero < 0:
        numero = int(input("Por favor ingrese un número positivo: "))
    
    if numero % 2 == 0:
        pares += 1
        lista_pares.append(numero)
    else:
        impares += 1
        lista_impares.append(numero)

print(f"\nResultados:")
print(f"Números pares: {lista_pares}")
print(f"Cantidad de números pares: {pares}")
print(f"\nNúmeros impares: {lista_impares}")
print(f"Cantidad de números impares: {impares}")
