#Problema 2

from fractions import Fraction
from decimal import Decimal
a = 4 #int(input("Ingrese el Primer numero: ))
b = 2 #int(input("Ingrese segundo numero: "))

print("adición = ",a + b)
print("sustracción = ",a - b)
print("multiplicación = ",a * b)
print("división = ", Fraction(Decimal(a) / Decimal(b)))
      