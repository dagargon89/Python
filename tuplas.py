'''Las tuplas son una estructura de datos que permite almacenar varios
 elementos de forma ordenada. A diferencia de las listas, las tuplas son 
 inmutables, es decir, no se pueden modificar una vez creadas. Las tuplas 
 se crean utilizando paréntesis y los elementos 
se separan por comas. Por ejemplo:
tupla = (1, 2, 3, 4, 5)
print(tupla)'''

tuplasFrutas = ('Kiwi', 'Fresa', 'Sandía')

print(tuplasFrutas)


lista = list(tuplasFrutas)
print(type(lista))
print(lista)

'''
Funcionan casi todos los metods de las listas, pero no se pueden modificar
tuplasFrutas[1] = 'Manzana' #Error
'''