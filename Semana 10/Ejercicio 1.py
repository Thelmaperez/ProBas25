# solicitar el texto a el usuario
texto = input("Ingresa un texto: ").lower()

# eliminar puntuación
puntuacion = ".,;:!?()[]{}\"'"
for simbolo in puntuacion:
    texto = texto.replace(simbolo, "") # → remplaza por una cadena vacia

# se dividen las palabras
palabras = texto.split()

# cuenta las palabras
total_palabras = len(palabras)

# elimina palabras repetidas y las cuenta
palabras_unicas = set(palabras)
cantidad_unicas = len(palabras_unicas)

#  se usa diccionario
frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

palabra_frecuente = max(frecuencia, key=frecuencia.get)
frecuencia_maxima = frecuencia[palabra_frecuente]

#  resumen
print("\nResumen del análisis:")
print(f"Total de palabras: {total_palabras}")
print(f"Cantidad de palabras únicas: {cantidad_unicas}")
print("\nFrecuencia de cada palabra:")
for palabra, cantidad in frecuencia.items():
    print(f"{palabra}: {cantidad}")
print(f"\nLa palabra más frecuente es '{palabra_frecuente}' con {frecuencia_maxima} apariciones.")
