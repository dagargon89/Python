numero = int(input("Introduce un número entero: "))

match numero % 2:
    case 0:
        print(f"El número {numero} es par")
    case 1:
        print(f"El número {numero} es impar")
