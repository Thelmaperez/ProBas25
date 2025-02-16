#Problema 20
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def main():
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print("Lista de ejemplo:", lista)
    objetivo = int(input("Ingrese el número a buscar: "))
    
    print("Seleccione el método de búsqueda:")
    print("1. Búsqueda lineal")
    print("2. Búsqueda binaria (requiere lista ordenada)")
    
    opcion = int(input("Opción: "))
    
    if opcion == 1:
        resultado = busqueda_lineal(lista, objetivo)
    elif opcion == 2:
        resultado = busqueda_binaria(lista, objetivo)
    else:
        print("Opción no válida.")
        return
    
    if resultado != -1:
        print(f"El número {objetivo} se encuentra en la posición {resultado}.")
    else:
        print("El número no está en la lista.")

if __name__ == "__main__":
    main()
