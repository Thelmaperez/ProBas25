#Problema 22
#Simular el lanzamiento de un dado y una moneda

#moneda

import random as rnd

valor = rnd.random()

if valor > 0.50:
    print("la moneda cayó en águila")
else:
    print("la moneda cayó en sol")

#dado

dado = rnd.randint(1,6)

if dado == 1:
    print("uno")
if dado == 2: 
    print("dos")
if dado == 3:
    print("tres")
if dado == 4:
    print("cuatro")
if dado == 5:
    print("cinco")
if dado == 6:
    print("seis")


   
