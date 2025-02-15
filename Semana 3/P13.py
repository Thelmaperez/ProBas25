#Problema 13

def conversor():
    temperatura = input("ingresa la temperatura con su respectiva unidad" )
    unidad = temperatura[-1].upper()
    grados = float(temperatura[:-1])

    if unidad == "C":
        temperatura_conv = round(grados * (9/5) + 32,2)
        print(f"{grados}°{unidad} es quivalente a ({temperatura_conv}°F")
    else:
        temperatura_conv = round((grados - 32) * (5/9), 2)
        print(f"{grados}°{unidad} es equivalente a {temperatura_conv}°C")

conversor()
