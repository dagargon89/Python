def encriptar(mensaje):
    abecedario = {"a": "😭", "b": "🔥", "c": "💀", "d": "😵", "e": "😫", "f": "🙀", "g": "🐈", "h": "🐖",
                  "i": "🥪", "j": "🧀", "k": "📸", "l": "📟", "m": "👩‍⚕️", "n": "👩‍⚕️", "o": "🤢", "p": "🚽",
                  "q": "🏠", "r": "🔑", "s": "💯", "t": "💮", "u": "🌸", "v": "🇭🇰", "w": "🐉", "x": "🔮",
                  "y": "🧞", "z": "🧞"}

    # Convertir el mensaje a minúsculas
    mensaje = mensaje.lower()

    mensajeEmoji = ""

    # Proceso de cifrado
    for letra in mensaje:
        if letra in abecedario:
            mensajeEmoji += abecedario[letra]
        else:
            mensajeEmoji += letra

    return mensajeEmoji  # Devuelve el mensaje cifrado


# Solicitar el mensaje al usuario
mensaje = input("Ingresa tu mensaje: ")

# Llamar a la función y guardar el resultado
mensaje_cifrado = encriptar(mensaje)

# Imprimir el mensaje cifrado
print(mensaje_cifrado)
