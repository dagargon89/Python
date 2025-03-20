def inicioCalculadora():
    print("Bienvenido a la calculadora")
    print("Seleccione la operación que desea realizar")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    opcion = int(input("Opción: "))
    return opcion
def suma():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
    print("**********************************************************")
def resta():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
    print("**********************************************************")
def multiplicacion():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
    print("**********************************************************")
def division():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    if num2 == 0:
        print("No se puede dividir entre 0")
    else:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
        print("**********************************************************")
def calculadora():
    opcion = inicioCalculadora()
    while opcion != 5:
        if opcion == 1:
            suma()
        elif opcion == 2:
            resta()
        elif opcion == 3:
            multiplicacion()
        elif opcion == 4:
            division()
        else:
            print("Opción inválida")
        opcion = inicioCalculadora()
    print("Gracias por usar la calculadora")
calculadora()
