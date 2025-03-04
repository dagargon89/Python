'''numero =float(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo.")
elif numero == 0:
    print("El número es cero.")
else:
    print("El número es negativo.")'''


#ejercicio
'''edad = int(input("Ingresa tu edad: "))
if edad > 0 and edad < 12:
    print("Eres un niño.")
elif edad >= 12 and edad < 18:
    print("Eres un adolescente.")
elif edad >= 18 and edad < 60:
    print("Eres un adulto.")
elif edad >= 60:
    print("Eres un adulto mayor.")
else:
    print("Edad no válida.")'''

#ejercicio2
# Definir usuario y contraseña correctos
'''USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "12345"

# Solicitar datos al usuario
usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

# Verificar credenciales
if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
    print("Inicio de sesión exitoso!")
elif usuario != USUARIO_CORRECTO:
    print("Usuario incorrecto")
elif contrasena != CONTRASENA_CORRECTA:
    print("Contraseña incorrecta")'''

#ejercicio3 puntos extra

invitados = ['David', 'Alan', 'Fernanda', 'Naomi', 'Luis', 'Criss', 'Daniel']

nombre = input("Ingresa tu nombre para verificar si estás en la lista de invitados: ")


if nombre.title() in invitados:
    print(f"¡Bienvenido/a {nombre}! Puedes pasar.")
elif nombre.title() not in invitados:
    print(f"Lo siento {nombre}, no estás en la lista de invitados.")
    edad = int(input("¿Cuál es tu edad?: "))
    if edad >= 18:
        invitados.append(nombre.title())
        print(f"Como eres mayor de edad, has sido agregado/a a la lista. ¡Bienvenido/a {nombre}!")
        print(f"Lista actualizada: {invitados}")
    else:
        print("Lo siento, al ser menor de edad debes retirarte.")