'''
Los conjuntos son colecciones de elementos únicos, es decir, no se pueden repetir.
En Python, los conjuntos se pueden definir utilizando llaves {} o la función set().
'''

conjuntoColores = {'rojo', 'verde', 'azul', 'amarillo', 'rojo'}
print(conjuntoColores) # Salida: {'verde', 'rojo', 'azul', 'amarillo'}

#acceder a los elementos de un conjunto
for color in conjuntoColores:
    print(color)

print('verde' in conjuntoColores) # Salida: True

#agregar elementos a un conjunto
conjuntoColores.add('naranja')
print(conjuntoColores) # Salida: {'verde', 'rojo', 'azul', 'naranja', 'amarillo'}

#eliminar elementos de un conjunto
conjuntoColores.remove('verde')
print(conjuntoColores) # Salida: {'rojo', 'azul', 'naranja', 'amarillo'}