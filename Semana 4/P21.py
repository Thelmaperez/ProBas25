#Problema 21
#Calcular el área y volumen de distintas figuras geométricas

import math

def area_circulo(radio):
    return math.pi * radio ** 2

def volumen_esfera(radio):
    return (4/3) * math.pi * radio ** 3

def area_rectangulo(base, altura):
    return base * altura

def volumen_prisma_rectangular(base, altura, profundidad):
    return base * altura * profundidad

def area_triangulo(base, altura):
    return (base * altura) / 2

def volumen_piramide(base, altura):
    return (1/3) * base * altura

def area_cuadrado(lado):
    return lado ** 2

def volumen_cubo(lado):
    return lado ** 3

def area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor + base_menor) * altura) / 2

def volumen_cilindro(radio, altura):
    return math.pi * radio ** 2 * altura


print("Área del círculo (radio=5):", area_circulo(5))
print("Volumen de la esfera (radio=5):", volumen_esfera(5))
print("Área del rectángulo (base=4, altura=7):", area_rectangulo(4, 7))
print("Volumen del prisma rectangular (base=4, altura=7, profundidad=10):", volumen_prisma_rectangular(4, 7, 10))
