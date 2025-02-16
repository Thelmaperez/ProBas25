#Problema 17

def insertarPila(pila, elemento):
    pila.append(elemento)

def eliminarPila(pila):
    if pila:  # Verifica si la pila no está vacía
        pila.pop()  # Elimina el último elemento

if __name__ == "__main__":
    estupila = list()
    insertarPila(estupila, 1)
    print(estupila)
    insertarPila(estupila, "mi pelo")
    print(estupila)
    insertarPila(estupila, "ideota")
    print(estupila)
    eliminarPila(estupila)
    print(estupila)  

