#Problema 11

print("Verificar si una cadena de un palíndromo")

def es_palindromo(cadena):
 cadena = cadena.lower()
 return cadena == cadena[::-1]

print(es_palindromo("uva"))

