def kilometros_a_millas(km):
    return km * 0.621371

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def litros_a_galones(litros):
    return litros * 0.264172

def main():
    while True:
        print("\nConversor de Unidades")
        print("1. Kilómetros a millas")
        print("2. Celsius a Fahrenheit")
        print("3. Litros a galones")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            km = float(input("Ingrese kilómetros: "))
            print(f"{km} km = {kilometros_a_millas(km)} millas")
        
        elif opcion == "2":
            c = float(input("Ingrese grados Celsius: "))
            print(f"{c}°C = {celsius_a_fahrenheit(c)}°F")
        
        elif opcion == "3":
            litros = float(input("Ingrese litros: "))
            print(f"{litros} L = {litros_a_galones(litros)} galones")
        
        elif opcion == "4":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()