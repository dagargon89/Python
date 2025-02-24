# Ejemplos de tipos de datos en Python

# Entero (int)
numero_entero = 42
# print(f"Entero: {numero_entero}")

# Flotante (float)
numero_flotante = 3.14159
# print(f"Flotante: {numero_flotante}")

# Cadena de texto (str)
cadena_texto = "Hola, mundo!"
# print(f"Cadena de texto: {cadena_texto}")

# Booleano (bool)
booleano_verdadero = True
booleano_falso = False
# print(f"Booleano verdadero: {booleano_verdadero}")
# print(f"Booleano falso: {booleano_falso}")

# Lista (list)
lista_ejemplo = [1, 2, 3, 4, 5]
# print(f"Lista: {lista_ejemplo}")

# Tupla (tuple)
tupla_ejemplo = (1, 2, 3, 4, 5)
# print(f"Tupla: {tupla_ejemplo}")

# Conjunto (set): Colección desordenada de elementos únicos.
conjunto_ejemplo = {1, 2, 3, 4, 5}
# print(f"Conjunto: {conjunto_ejemplo}")

# Diccionario (dict): Colección de pares clave-valor, donde cada clave es única.
diccionario_ejemplo = {"clave1": "valor1", "clave2": "valor2"}
# print(f"Diccionario: {diccionario_ejemplo}")

# Conjunto inmutable (frozenset): Similar a un conjunto, pero sus elementos no pueden cambiarse después de su creación.
conjunto_inmutable = frozenset([1, 2, 3, 4, 5])
# print(f"Conjunto inmutable (frozenset): {conjunto_inmutable}")

# NoneType
valor_nulo = None
# print(f"NoneType: {valor_nulo}")

print(type(valor_nulo))
print(type(conjunto_inmutable))
print(type(diccionario_ejemplo))   # dict
print(type(conjunto_ejemplo))      # set
print(type(tupla_ejemplo))         # tuple
print(type(lista_ejemplo))         # list
print(type(booleano_falso))        # bool
print(type(booleano_verdadero))    # bool
print(type(cadena_texto))          # str
print(type(numero_flotante))       # float
print(type(numero_entero))         # int
