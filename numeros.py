numero1 = 11
numero2 = 20

#operadores aritméticos
print(f'La suma es: {numero1 + numero2}') #suma output: 30
print(numero1 - numero2) #resta output: -10
print(numero1 * numero2) #multiplicación output: 200
print(numero1 / numero2)    #división output: 0.5
print(numero1 % numero2)   #módulo output: 10
print(numero1 ** numero2) #exponente output: 100000000000000000000
print(numero1 // numero2)   #división entera output: 0

#operadores  de comparación
print(numero1 == numero2) #igual a output: False
print(numero1 != numero2) #diferente de output: True
print(numero1 > numero2) #mayor que output: False
print(numero1 < numero2) #menor que output: True
print(numero1 >= numero2) #mayor o igual que output: False
print(numero1 <= numero2) #menor o igual que output: True

#operadores lógicos
print(numero1 < 5 and numero2 > 10) #and output: True
print(numero1 < 5 or numero2 > 10) #or output: True
print(not(numero1 < 5 and numero2 > 10)) #not output: False
print(not(numero1 < 5 or numero2 > 10)) #not output: False

#operadores de identidad
x = 5
y = 5
z = x
print(x is z) #is output: True