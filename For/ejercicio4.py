n = int(input("Ingrese la cantidad de alumnos: "))
calificaciones = []
suma = 0

for i in range(n):
    calificacion = float(input(f"Ingrese la calificación del alumno {i + 1}: "))
    calificaciones.append(calificacion)
    suma += calificacion

promedio = suma / n
print(f"\nLas calificaciones capturadas son: {calificaciones}")
print(f"El promedio de las calificaciones es: {promedio:.2f}")
