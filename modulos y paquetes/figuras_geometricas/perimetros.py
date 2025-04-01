import math

PI=math.pi

def perimetroCuadrado(lado):
    return lado*4

def perimetroRectangulo(base,altura):
    return base*2+altura*2

def perimetroCirculo(radio):
    return 2*PI*radio

def perimetroTriangulo(lado):
    return lado*3

def perimetroTrapecio(baseMenor,baseMayor,ladoa, ladoc):
    return baseMenor+baseMayor+ladoa+ladoc

def perimetroRombo(lado):
    return lado*4