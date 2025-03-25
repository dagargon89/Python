#division entre cero
try:
    v1 = float(input("Ingrese un número: "))
    v2 = float(input("Ingrese otro número: "))
    division = v1/v2
    print("La división es: ", division)
except ZeroDivisionError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")
