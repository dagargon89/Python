'''
Los diccionarios son colecciones de elementos que se encuentran indexados.
Cada elemento de un diccionario está compuesto por una clave y un valor.
En Python, los diccionarios se pueden definir utilizando llaves {} o la función dict().
'''

persona = { 
    'nombre': 'Alan',
    'edad': 17,
    'colorFavorito': 'azul',
    'cursos': ['Python', 'JavaScript', 'C#']
}

print(persona) # Salida: {'nombre': 'Alan', 'edad': 17, 'colorFavorito': 'azul'}

#otra forma de definir un diccionario
persona2 = dict(nombre='David', edad=35, colorFavorito='verde', cursos = ['Python', 'JavaScript', 'C#'])
print(persona2) # Salida: {'nombre': 'David', 'edad': 35, 'colorFavorito': 'verde'}

#acceder a los elementos de un diccionario
print(persona['nombre']) # Salida: Alan
print(persona.get('dir','No encontrado')) # con get() se puede especificar un valor por defecto si la clave no existe

#agregar y editar elementos a un diccionario
persona['pais'] = 'México' 
print(persona) # Salida: {'nombre': 'Alan', 'edad': 17, 'colorFavorito': 'azul', 'pais': 'México'}
persona['nombre'] = 'Alan Turing'
print(persona) # Salida: {'nombre': 'Alan Turing', 'edad': 17, 'colorFavorito': 'azul', 'pais': 'México'}

#eliminar elementos de un diccionario
persona.pop('colorFavorito')
print(persona) # Salida: {'nombre': 'Alan Turing', 'edad': 17, 'pais': 'México'}
del persona['edad']
print(persona) # Salida: {'nombre': 'Alan Turing', 'pais': 'México'}

#metodos extra
print(persona2.keys()) # Salida: dict_keys(['nombre', 'edad', 'colorFavorito', 'cursos'])
print(persona2.values()) # Salida: dict_values(['David', 35, 'verde', ['Python', 'JavaScript', 'C#']])
print(persona2.items()) # Salida: dict_items([('nombre', 'David'), ('edad', 35), ('colorFavorito', 'verde'), ('cursos', ['Python', 'JavaScript', 'C#'])])