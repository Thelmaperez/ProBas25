def es_palindromo(texto):

    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

entrada = input("Ingresa una palabra o frase: ")
print("Es un palíndromo." if es_palindromo(entrada) else "No es un palíndromo.")
