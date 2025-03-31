class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Precio: ${self.precio}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, precio, num_puertas):
        super().__init__(marca, modelo, año, precio)
        self.num_puertas = num_puertas

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de puertas: {self.num_puertas}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, precio, cilindrada):
        super().__init__(marca, modelo, año, precio)
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Cilindrada: {self.cilindrada}cc")


auto = Automovil("Toyota", "Corolla", 2022, 20000, 4)
moto = Motocicleta("Yamaha", "R1", 2021, 15000, 1000)

auto.mostrar_informacion()
print()
moto.mostrar_informacion()