def calcular_estadisticas(args):
    numeros = sorted(args)  
    n = len(numeros)
    
    # Prom usando una función lambda
    promedio = (lambda nums: sum(nums) / len(nums) if nums else 0)(numeros)
    #Sacar mediana
    if n % 2 == 1:
        mediana = numeros[n // 2]
    else:
        mediana = (numeros[n // 2 - 1] + numeros[n // 2]) / 2

    # Desviación estándar
    varianza = sum((x - promedio) ** 2 for x in numeros) / (n - 1) if n > 1 else 0
    desviacion = varianza ** 0.5  

    return promedio, mediana, desviacion  

# Solicitar los números al usuario
numeros = list(map(float, input("Ingresa números separados por espacio: ").split()))
prom, med, desv = calcular_estadisticas(numeros)


print(f"Promedio: {prom:.2f}")
print(f"Mediana: {med:.2f}")
print(f"Desviación Estándar: {desv:.2f}")
