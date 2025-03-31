# Lista para almacenar los contactos
agenda = []

def agregar_contacto(nombre, numero, correo):
    """Agrega un nuevo contacto a la agenda."""
    contacto = (nombre, numero, correo)
    agenda.append(contacto)
    print(f"Contacto {nombre} agregado correctamente.")

def buscar_contacto(nombre):
    """Busca un contacto por nombre e imprime sus detalles."""
    for contacto in agenda:
        if contacto[0].lower() == nombre.lower():
            print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")
            return
    print("Contacto no encontrado.")

def listar_contactos():
    """Lista todos los contactos en orden alfabético."""
    if not agenda:
        print("La agenda está vacía.")
        return
    agenda_ordenada = sorted(agenda, key=lambda x: x[0].lower())
    print("\nLista de contactos:")
    for contacto in agenda_ordenada:
        print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")

agregar_contacto("Ana", "123456789", "ana@example.com")
agregar_contacto("Maria", "987654321", "maria@example.com")
agregar_contacto("karla", "456789123", "Karla@example.com")

print("\nBuscando a Ana:")
buscar_contacto("Ana")

print("\nContactos ordenados:")
listar_contactos()
