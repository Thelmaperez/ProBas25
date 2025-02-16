#Problema 16

cadena = input("ingresa una cadena de texto: ")
vocales = "aeiouAEIOU"
a = 0 
b = 0
for i in cadena :
   if ord(i) >= 65 and ord(i) <= 122:
     if i in vocales:
      a+=1  
   else:
      b+=1
        
print(f"vocales: {a}")      
print(f"consonantes: {b}")

