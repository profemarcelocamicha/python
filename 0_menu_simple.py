# Lista para guardar los contactos
contactos = []

# === FUNCIONES ===

def agregar_contacto():
    nombre = input("Ingrese nombre: ")
    telefono = input("Ingrese teléfono: ")
    email = input("Ingrese email: ")
    contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    contactos.append(contacto)
    print("✅ Contacto agregado con éxito.\n")

def mostrar_contactos():
    if not contactos:
        print("⚠️ No hay contactos cargados.\n")
    else:
        print("\n===================== LISTA DE CONTACTOS =======================")
        for c in (contactos):
            print(c["nombre"], c["telefono"], c["email"])
        print()        

# === PROGRAMA PRINCIPAL ===

def menu():
    while True:
        print("=== AGENDA DE CONTACTOS ===")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "0":
            print("👋 Saliendo del programa...")
            break
        else:
            print("⚠️ Opción no válida.\n")
# Ejecutar menú principal
menu()
