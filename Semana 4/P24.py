#Problema 24
#Calcular la suma de una serie numérica.

def sum_series(n, formula):
 
    return sum(formula(i) for i in range(1, n + 1))


formula = lambda i: 1 / i
resultado = sum_series(n , formula)
print(f"La suma de la serie es: {resultado}")
