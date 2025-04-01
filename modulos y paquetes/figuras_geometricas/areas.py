import math

PI=math.pi

def areaCuadrado(lado):
    return lado*lado

def areaRectangulo(base, altura):
    return base*altura

def areaCirculo(radio):
    return PI*(radio**2)

def areaTriangulo(base,altura):
    return base*altura/2

def areaTrapecio(baseMenor, baseMayor, altura):
    return ((baseMenor+baseMayor)*altura)/2

def areaRombo(diagonalA, diagonalB):
    return (diagonalA*diagonalB)/2