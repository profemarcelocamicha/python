# Agenda de contactos con selección de localidad

contactos = []
localidades = ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "Salta"]

def mostrar_menu():
    print("\n--- MENÚ AGENDA ---")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Salir")

def seleccionar_localidad():
    print("\nSeleccione localidad:")
    for i, loc in enumerate(localidades, start=1):
        print(f"{i}. {loc}")
    
    while True:
        try:
            opcion = int(input("Ingrese el número de la localidad: "))
            if 1 <= opcion <= len(localidades):
                return localidades[opcion - 1]
            else:
                print("❌ Opción inválida, intente nuevamente.")
        except ValueError:
            print("❌ Debe ingresar un número válido.")

def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    localidad = seleccionar_localidad()

    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "localidad": localidad
    }
    contactos.append(contacto)
    print("✅ Contacto agregado con éxito!")

def mostrar_contactos():
    if not contactos:
        print("No hay contactos cargados.")
    else:
        print("\n--- LISTA DE CONTACTOS ---")
        for i, c in enumerate(contactos, start=1):
            print(f"{i}. {c['nombre']} - {c['telefono']} - {c['email']} - {c['localidad']}")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        mostrar_contactos()
    elif opcion == "3":
        print("👋 Saliendo del programa...")
        break
    else:
        print("❌ Opción inválida, intente nuevamente.")
