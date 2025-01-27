#print("Actividades salón")

v1=10000

v1 -=2

if v1 <= 0:
    if v1 >= 99:
        print("Dentro del if")
        print("Aun dentro del if")

#print("salí")

#nombre = input()

#print("Tu nombre es: ",nombre)

#casting
#numero = int(float(input("Ingrese un numero: ")))

#print(numero)
"""
edad=-1
añoactual = 2025
añonacimiento = int(input("Ingresa año de nacimiento: "))
edad = añoactual - añodenacimiento

print("Tienes", edad,"años")
print("Tienes %.32f años"% edad)
"""

#Actividad 1:

print("Hola Mundo")

#Actividad 2:
from fractions import Fraction
from decimal import Decimal 
a = 1 #int(input("Ingrese el primer numero: "))
b = 5 #int(input("Ingrese el segundo numero: "))

print("adición = ",a + b)
print("sustracción = ",a - b)
print("multiplicación = ",a * b)
print("división = ", Fraction(Decimal(a) / Decimal(b)))

