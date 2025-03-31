# Paradigma Imperativo: Uso de estructuras de control
def suma_imperativa(lista):
    suma = 0
    for num in lista:
        if num > 0:  # Condicional
            suma += num  # Acumulador
    return suma
def obtener_lista():
    return [1, -2, 3, 4, -5]

def imprimir_resultado(resultado):
    print(f"La suma de los valores positivos es: {resultado}")

# Paradigma Modular
def modulo_operaciones():
    lista = obtener_lista()
    resultado = suma_imperativa(lista)
    imprimir_resultado(resultado)

# Paradigma Orientado
class Calculadora:
    def __init__(self, valores):
        self.valores = valores

    def suma_positivos(self):
        return sum(num for num in self.valores if num > 0)


if __name__ == "__main__":
   
    modulo_operaciones()

    
    calc = Calculadora([1, -2, 3, 4, -5])
    print(f"La suma con POO es: {calc.suma_positivos()}")