#Problema 11

def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

entrada = input("Ingresa una palabra o frase: ")
if es_palindromo(entrada):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
