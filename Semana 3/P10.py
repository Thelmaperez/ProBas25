#Problema 10

print("Leer, escribir y modificar un archivo de texto")


with open('archivo.txt', 'w') as archivo:
    archivo.write('Hola a todos.\n')
    archivo.write('esto es python.\n')


print("Contenido del archivo:")
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
with open('archivo_.txt', 'a') as archivo:
    archivo.write('La línea ha sido agregada.\n')
print("\nContenido leído línea por línea:")
with open('archivo.txt', 'r') as archivo:
    for linea in archivo:
        print(linea.strip()) 