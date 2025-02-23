#Prolema 27
#Crear un conversor de unidades

def km_a_millas(km):
    return km*0.621371

km = 10
millas = km_a_millas(km)
print(f"{km} km son {millas:.2f}millas")