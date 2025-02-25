texto = 'hola python :)'

print(texto)
print(texto[3:13])#metodo de slicing
print(texto[1])
print(texto[0:14:2])#metodo de slicing con saltos
print("***********************************************************************")
print(len(texto))#metodo len para saber la longitud de la cadena
print("***********************************************************************")
print(texto.find('a'))#metodo find para buscar una subcadena ver su posicion
print("***********************************************************************")
print(texto.count('a'))#metodo count para contar cuantas veces se repite una subcadena
print("***********************************************************************")
print(texto.upper())#metodo upper para convertir a mayusculas
print("***********************************************************************")
print(texto.lower())#metodo lower para convertir a minusculas
print("***********************************************************************")
print(texto.capitalize())#metodo capitalize para convertir la primera letra en mayuscula
print("***********************************************************************")
print(texto.replace('hola','XXXX'))#metodo replace para reemplazar una subcadena por otra
print("***********************************************************************")
print(texto.isdigit())#metodo isdigit para saber si la cadena es un numero
print("***********************************************************************")
print(texto.isalpha())#metodo isalpha para saber si la cadena es alfabetica no tiene que teber espacios
print("***********************************************************************")
