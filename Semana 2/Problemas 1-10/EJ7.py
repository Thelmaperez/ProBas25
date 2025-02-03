#Problema 7

def verificar_numero():
    numero = int(input("Ingresa un número: "))
    
    # Verifica si es par o impar
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")

    # Verifica si es múltiplo de otro número
    otro_numero = int(input("Ingresa otro número para verificar si el primero es múltiplo de este: "))
    
    if otro_numero != 0:
        if numero % otro_numero == 0:
            print(f"{numero} es múltiplo de {otro_numero}.")
        else:
            print(f"{numero} no es múltiplo de {otro_numero}.")
    else:
        print("No se puede verificar múltiplos con cero.")

# Llamar a la función
verificar_numero()