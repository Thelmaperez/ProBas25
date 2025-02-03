#Problema 4

print("Secuencia de Fibonacci")

def fibonacci(n):
    secuencia_fib=[0,1]
    for i in range(2, n):
      secuencia_fib.append(
         secuencia_fib[i-1] +
         secuencia_fib[i-2])
    return secuencia_fib
print(fibonacci(8))