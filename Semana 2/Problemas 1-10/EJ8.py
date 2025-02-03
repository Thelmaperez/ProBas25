#Problema 8

print("calcular área y circunferencia de un circulo")

import math

def calcular_circulo():
    radio = float(input("Ingresa el radio del círculo: "))
    
    # Calcular el área
    area = math.pi * radio ** 2
    
    # Calcular la circunferencia
    circunferencia = 2 * math.pi * radio
    
    print(f"El área del círculo es: {area:.2f}")
    print(f"La circunferencia del círculo es: {circunferencia:.2f}")

# Llamar a la función
calcular_circulo()
