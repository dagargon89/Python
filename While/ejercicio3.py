password = "abc123"
intentos = 3

while intentos > 0:
    intento = input("Ingresa la contraseña: ")
    if intento == password:
        print("¡Contraseña correcta! Acceso permitido")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Contraseña incorrecta. Te quedan {intentos} intentos")
        else:
            print("Has agotado todos tus intentos. Acceso bloqueado")
