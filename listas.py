'''
Las listas son un tipo de dato que permite almacenar varios valores 
en una misma variable.
Las listas son mutables, lo que significa que pueden ser modificadas 
después de su creación.
Para crear una lista se utilizan corchetes [] y se separan los valores
con comas.

ejemplo:
thislist = ["apple", "banana", "cherry"]
print(thislist)

Ejemplo de lista anidada:
thislist = ["apple", ["banana", ["cherry"]]]
print(thislist)
'''

# Sintaxis
alumnos = ['David', 'Alan', 'Naomi', 'Fernanda', 'Daniel', 'Criss']
print(alumnos)
print('***********************************************************************')
print(alumnos[0:6])# si no conocemos la longitud de la lista podemos usar slicing dejando el valor inicial y :
print(alumnos[::2])# podemos usar slicing con saltos
print('***********************************************************************')
# Metodos
print(alumnos.index('Naomi'))# metodo index para buscar un valor en la lista y saber su posicion
print(alumnos.count('David'))# metodo count para saber cuantas veces se repite un valor en la lista
print('***********************************************************************')
# Agregar elementos
alumnos.append('Cynthia')# metodo append para agregar un valor al final de la lista
print(alumnos)
alumnos.insert(2, 'Goku')# metodo insert para agregar un valor en una posicion especifica, lleva 2 argumentos, la posicion y el valor
print(alumnos)
print('***********************************************************************')
# Eliminar elementos
alumnos.pop()# metodo pop para eliminar un valor de la lista, lleva como argumento la posicion del valor a eliminar, si no tiene elementos elimina el ultimo    
print(alumnos)
alumnos.remove('Goku')# metodo remove para eliminar un valor de la lista, lleva como argumento el valor a eliminar
print(alumnos)
del alumnos[0]# podemos usar la palabra reservada del para eliminar un valor de la lista
print(alumnos)
print('***********************************************************************')
# Editar elementos
alumnos[2] = 'Milk'# podemos editar un valor de la lista asignando un nuevo valor a la posicion
print(alumnos)

print('***********************************************************************')
# metodos extras
alumnos.reverse()# metodo reverse para invertir la lista
print(alumnos)
alumnos.sort()# metodo sort para ordenar la lista
print(alumnos)