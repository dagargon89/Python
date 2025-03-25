print("Calculadora básica")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

operacion = input("Seleccione la operación (1-4): ")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

match operacion:
    case "1":
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    case "2":
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    case "3":
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    case "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Error: No se puede dividir por cero")
    case _:
        print("Operación no válida")
