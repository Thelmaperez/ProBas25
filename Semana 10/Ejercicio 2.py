# Sistema de Inventario con Listas y Diccionarios

inventario = []

#  se hace funcion para agregar producto
def agregar_producto(nombre, categoria, precio, cantidad):
    producto = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "cantidad": cantidad 
        }
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado exitosamente.")

# funcion para eliminar producto
def eliminar_producto(nombre):
    global inventario
    inventario = [p for p in inventario if p["nombre"] != nombre]
    print(f"Producto '{nombre}' eliminado (si existía).")

# Función para buscar un producto por nombre
def buscar_producto(nombre):
    for p in inventario:
        if p["nombre"] == nombre:
            print("Información del producto:")
            print(f"Nombre: {p['nombre']}")
            print(f"Categoría: {p['categoria']}")
            print(f"Precio: {p['precio']}")
            print(f"Cantidad: {p['cantidad']}")
            return
    print(f"Producto '{nombre}' no encontrado.")

# Función para mostrar productos ordenados por precio
def mostrar_ordenado_por_precio():
    productos_ordenados = sorted(inventario, key=lambda x: x["precio"])
    print("\nProductos ordenados por precio (menor a mayor):")
    for p in productos_ordenados:
        print(f"{p['nombre']} - ${p['precio']} - {p['cantidad']} unidades")


agregar_producto("Manzana", "Fruta", 10, 50)
agregar_producto("Laptop", "Electrónica", 15000, 5)
agregar_producto("Cereal", "Alimentos", 80, 30)

buscar_producto("Laptop")
eliminar_producto("Cereal")
mostrar_ordenado_por_precio()

