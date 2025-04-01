#ejercicio figuras geometricas, conocer area y perimetro
from figuras_geometricas.areas import areaCuadrado,areaRectangulo, areaCirculo, areaTriangulo, areaTrapecio, areaRombo
from figuras_geometricas.perimetros import perimetroCuadrado, perimetroRectangulo, perimetroCirculo, perimetroTriangulo, perimetroTrapecio, perimetroRombo

while True:
    print("FIGURAS GEOMETRICAS")
    print("Menu: ")
    print("1. Cuadrado")
    print("3. Circulo")
    print("4. Triangulo")
    print("5. Trapecio")
    print("6. Rombo")
    print("7. Salir")

    opcion=int(input("Selecciona la figura: "))

    match opcion:
        case 1:
            print("Seleccionaste cuadrado")
            print("Selecciona: ")
            print("1. area")
            print("2. perimetro")
            areayperimetro=int(input("Selecciona la opcion"))

            if areayperimetro==1:
                lado=int(input("Captura lado: "))
                print(f"El area del cuadrado es {areaCuadrado(lado)}")
            elif areayperimetro==2:
                lado=int(input("Captura lado: "))
                print(f"El perimetro del cuadrado es {perimetroCuadrado(lado)}")
            else:
                print("opcion invalida!!")
        case 2:
            print("Seleccionaste rectangulo")
            print("Selecciona: ")
            print("1. area")
            print("2. perimetro")
            areayperimetro=int(input("Selecciona la opcion"))

            if areayperimetro==1:
                base=int(input("Captura base: "))
                altura=int(input("Captura altura: "))
                print(f"El area del rectangulo es {areaRectangulo(base,altura)}")
            elif areayperimetro==2:
                base=int(input("Captura base: "))
                altura=int(input("Captura altura: "))
                print(f"El perimetro del rectangulo es {perimetroRectangulo(base,altura)}")
            else:
                print("opcion invalida!!")

        case 3:
            print("Seleccionaste circulo")
            print("Selecciona: ")
            print("1. area")
            print("2. perimetro")
            areayperimetro=int(input("Selecciona la opcion"))

            if areayperimetro==1:
                radio = float(input("Captura radio: "))
                print(f"El area del circulo es {areaCirculo(radio)}")
            elif areayperimetro==2:
                radio = float(input("Catura radio: "))
                print(f"El perimetro del circulo es {perimetroCirculo(radio)}")
            else:
                print("opcion invalida!!")
        case 4:
            print("Seleccionaste triangulo equilatero")
            print("Selecciona: ")
            print("1. area")
            print("2. perimetro")
            areayperimetro=int(input("Selecciona la opcion"))
            
            if areayperimetro==1:
                base = float(input("Captura base: "))
                altura = float(input("Captura altura: "))
                print(f"El area del triangulo es {areaTriangulo(base,altura)}")
            elif areayperimetro==2:
                lado1 = float(input("Captura lado: "))
                print(f"El perimetro del triangulo es {perimetroTriangulo(lado)}")
            else:
                print("opcion invalida!!")
        case 5:
            print("Seleccionaste trapecio")
            print("Selecciona: ")
            print("1. area")
            print("2. perimetro")
            areayperimetro=int(input("Selecciona la opcion"))
            
            if areayperimetro==1:
                baseMenor = float(input("Captura base menor: "))
                baseMayor = float(input("Captura base mayor: "))
                altura = float(input("Captura altura: "))
                print(f"El area del trapecio es {areaTrapecio(baseMenor,baseMayor,altura)}")
            elif areayperimetro==2:
                baseMenor = float(input("Captura base menor: "))
                baseMayor = float(input("Captura base mayor: "))
                ladoa = float(input("Captura lado a: "))
                ladoc = float(input("Captura lado c: "))
                print(f"El perimetro del trapecio es {perimetroTrapecio(baseMenor,baseMayor,ladoa,ladoc)}")
            else:
                print("opcion invalida!!")
        case 6:
            print("Seleccionaste rombo")
            print("Selecciona: ")
            print("1. area")
            print("2. perimetro")
            areayperimetro=int(input("Selecciona la opcion"))

            if areayperimetro==1:
                diagonalA = float(input("Captura diagonal A: "))
                diagonalB = float(input("Captura diagonal B: "))
                print(f"El area del rombo es {areaRombo(diagonalA,diagonalB)}")
            elif areayperimetro==2:
                lado = float(input("Captura lado: "))
                print(f"El perimetro del rombo es {perimetroRombo(lado)}")
            else:
                print("opcion invalida!!")
        case 7:
            print("Saliendo del programa....")
            break    
        case _:  
            print("Opcion incorrecta!!")  

