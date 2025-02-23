#Problema 25
#Generar y analizar histogramas de datos

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = np.random.normal(loc=50, scale=15, size=1000)  # Media=50, Desviación=15, 1000 datos


plt.figure(figsize=(8, 5))
sns.histplot(data, bins=20, kde=True, color='blue', edgecolor='black', alpha=0.7)

plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma de Datos con Curva de Densidad')


plt.show()
