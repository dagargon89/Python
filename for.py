'''secuencia=range(1, 21, 4)
"""
This script demonstrates various uses of the `for` loop in Python, including iterating over ranges, lists, strings, and dictionaries.
It also includes an exercise that encrypts a user-input message by replacing each letter with a corresponding emoji from a predefined dictionary.
Functions and Features:
1. Iterating over a range of numbers with a step:
    - Prints a sequence of numbers from 1 to 20 with a step of 4.
2. Iterating over a list:
    - Prints each name in the list of students.
3. Iterating over a string:
    - Prints each character in the string "Hola, mundo!".
4. Iterating over a dictionary:
    - Prints each key-value pair in the dictionary of ages.
5. Encrypting a message:
    - Prompts the user to input a message.
    - Converts the message to lowercase.
    - Replaces each letter in the message with a corresponding emoji from the `abecedario` dictionary.
    - Prints the encrypted message with emojis.
"""
print(secuencia)

for numero in range(1, 21, 4):
    print(numero)

#listas

alumnos = ["Juan", "María", "Luis", "Ana", "Pedro"]

for alumno in alumnos:
    print(alumno)

#cadena de texto
mensaje = "Hola, mundo!"

for letra in mensaje:
    print(letra)

#diccionarios
edades = {"Juan": 25, "María": 19, "Luis": 30, "Ana": 22, "Pedro": 27}

for nombre, edad in edades.items():
    print(f"{nombre} tiene {edad} años")'''

#ejercicio

abecedario = {"a":"😭", "b":"🔥", "c":"💀", "d":"😵", "e":"😫", "f":"🙀", "g":"🐈", "h":"🐖", 
              "i":"🥪", "j":"🧀", "k":"📸", "l":"📟", "m":"👩‍⚕️", "n":"👩‍⚕️", "o":"🤢", "p":"🚽", 
              "q":"🏠", "r":"🔑", "s":"💯", "t":"💮", "u":"🌸", "v":"🇭🇰", "w":"🐉", "x":"🔮", 
              "y":"🧞", "z":"🧞" }

# proceso de cifrado
'''
Instrucciones
Capturar el mensaje y mostrar el mensaje con iconos'''

mensaje = input("Ingresa tu mensaje: ").lower()

mensajeEmoji = ""

for letra in mensaje:
    if letra in abecedario:
        mensajeEmoji += abecedario[letra]
    else:
        mensajeEmoji += letra
print(mensajeEmoji)   


