#Problema 18

#a*X**2 + b*x + c = 0
# a, b, c
from math import sqrt

def resolver_ecuacion(a, b, c):
    dete = b**2 - 4*a*c

    if dete > 0:
        x_1 = -b + sqrt(b**2 - 4*a*c) / (2*a)
        x_2 = -b - sqrt(b**2 - 4*a*c) / (2*a)
        return x_1, x_2
    elif dete == 0:
     x_1 = -b / (2*a)
     return (x_1,)
    else:
        return tuple()
    
print(resolver_ecuacion(1, 0, 1))

