#Problema 5

print("Verificación de Número primo")

num=int(input("ingresa un número:"))
es_primo = True
for i in range(2, num):
  if num % i == 0:
    es_primo = False
    break
if es_primo :
  print("es primo.")
else:
  print("no es primo")
