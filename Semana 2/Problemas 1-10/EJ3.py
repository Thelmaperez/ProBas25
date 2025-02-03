#Problema 3

print("Calcular el factorial de un numero")

numero = int(input("Ingresa un numero"))
fac = 1
if numero != 0:
  for i in range(1,numero+1):
   fac = fac*i
print("Factorial:", fac)
