#Problema 29 
#Generar y analizar datos estadısticos

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


data = np.random.normal(loc=50, scale=15, size=1000)  # Media=50, Desviación=15, 1000 datos


df = pd.DataFrame(data, columns=['Valores'])


media = np.mean(data)
mediana = np.median(data)
moda = stats.mode(data, keepdims=True)[0][0]  # Se obtiene la moda
desviacion = np.std(data)
varianza = np.var(data)
percentil_25 = np.percentile(data, 25)
percentil_75 = np.percentile(data, 75)


print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Desviación estándar: {desviacion:.2f}")
print(f"Varianza: {varianza:.2f}")
print(f"Percentil 25: {percentil_25:.2f}")
print(f"Percentil 75: {percentil_75:.2f}")


fig, axes = plt.subplots(1, 2, figsize=(12, 5))


sns.histplot(df['Valores'], bins=20, kde=True, color='blue', ax=axes[0])
axes[0].set_title("Histograma con Curva de Densidad")


sns.boxplot(x=df['Valores'], color='orange', ax=axes[1])
axes[1].set_title("Diagrama de Caja (Boxplot)")

plt.show()

