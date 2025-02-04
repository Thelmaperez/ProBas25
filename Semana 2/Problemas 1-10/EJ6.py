#Problema 6

print("Calcular interés compuesto")


def interes_compuesto(P, r, n, t):
    A = P * (1 + r/n)**(n*t)  
    return A

capital_inicial = float(input("Introduce el capital inicial:"))
tasa_interes = float(input("Introduce la tasa de interés anual (en porcentapor ejemplo, 4 para 4%): ")) / 100
capitalizacion_anual = int(input("Introduce el número de veces que se capitaliza al año (por ejemplo, 1 para anual): "))
tiempo = float(input("Introduce el tiempo en años: "))

monto_final = interes_compuesto(capital_inicial, tasa_interes, capitalizacion_anual, tiempo)

print(f"\nEl monto final después de {tiempo} años es: {monto_final:.2f}")


