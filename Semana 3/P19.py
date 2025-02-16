#Problema 19
import numpy as np

a, b = 0, 10
uniforme = np.random.uniform(a, b, 10)  
mu, sigma = 0, 1
normal = np.random.normal(mu, sigma, 10)  

n, p = 10, 0.5
binomial = np.random.binomial(n, p, 10)  

print("Uniforme:", uniforme)
print("Normal:", normal)
print("Binomial:", binomial)
