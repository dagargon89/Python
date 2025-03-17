inicio = int(input("Ingresa el número inicial: "))
fin = int(input("Ingresa el número final: "))

numero = inicio
while numero <= fin:
    if numero % 2 != 0:
        print(numero)
    numero += 1
