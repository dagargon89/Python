cateto1 = float(input("Introduce el primer cateto: "))
cateto2 = float(input("Introduce el segundo cateto: "))

if cateto1 <= 0 or cateto2 <= 0:
    print("Error")
else:
    hipotenusa = (cateto1**2 + cateto2**2) ** 0.5
    print(f"La hipotenusa es: {hipotenusa}")
