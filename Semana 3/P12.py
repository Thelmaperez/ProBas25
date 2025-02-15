#Problema 12

a = int(input("Ingresa un numero:  "))
b = int(input("ingresa un numero:  "))
c = int(input("ingresa un número:  "))
if a != b and a != c and b != c:
    if a > b :
        if a > c:
            print("el numero mayor es:",a)
        else:
            print("el numero mayor es: ",c)
    else:
        if b > c:
            print("el numero mayor es,", b)
        else:
            print("el numero mayor es:", c)
else:
    print("ingresa un 3 numeros diferentes")
