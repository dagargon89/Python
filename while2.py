import random

# Opciones del juego
opciones = ["piedra", "papel", "tijeras"]

# Bucle principal del juego
while True:
    # Pedir al jugador que ingrese su elección
    jugador = input("Elige piedra, papel o tijeras (o 'salir' para terminar): ").lower()
    
    if jugador == "salir":
        print("Gracias por jugar!")
        break
    
    if jugador not in opciones:
        print("Opción no válida. Intenta de nuevo.")
        continue
    
    # Elección de la computadora
    computadora = random.choice(opciones)
    print(f"Computadora elige: {computadora}")
    
    # Determinar el ganador
    if jugador == computadora:
        resultado = "Empate"
    elif (jugador == "piedra" and computadora == "tijeras") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijeras" and computadora == "papel"):
        resultado = "Jugador gana"
    else:
        resultado = "Computadora gana"
    
    print(f"Resultado: {resultado}")
