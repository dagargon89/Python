'''Realiza un programa que solicite al usuario dos números y realice las operaciones básicas de suma, resta, multiplicación y división.
Muestra los resultados de cada operación.'''
# Pedir al usuario que ingrese dos dígitos
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Realizar operaciones básicas
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2 if numero2 != 0 else "Indefinido (división por cero)"

# Mostrar los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
