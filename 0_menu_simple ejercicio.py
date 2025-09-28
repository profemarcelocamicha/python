# Lista para guardar los contactos
contactos = []
mascotas = []

# === FUNCIONES ===

def agregar_contacto():
    nombre = input("Ingrese nombre: ")
    telefono = input("Ingrese teléfono: ")
    email = input("Ingrese email: ")
    contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    contactos.append(contacto)
    print("✅ Contacto agregado con éxito.\n")

def agregar_mascota():
    nombre = input("Ingrese nombre: ")
    raza = input("Ingrese raza: ")
    peso = input("Ingrese peso: ")
    mascota = {"nombre": nombre, "raza": raza, "peso": peso}
    mascotas.append(mascota)
    print("✅ Mascota agregado con éxito.\n")

def mostrar_contactos():
    if not contactos:
        print("⚠️  No hay contactos cargados.\n")
    else:
        print("\n👩👨🧑👧👦🧒== LISTA DE CONTACTOS ==👵👴🧓👩‍🦰👨‍🦰👩‍🦱👨‍🦱")
        for c in (contactos):
            print(c["nombre"], c["telefono"], c["email"])
        print()        

def mostrar_mascotas():
    if not mascotas:
        print("⚠️  No hay mascotas cargadas.\n")
    else:
        print("\n - 🐶🐕🐩 LISTA DE MASCOTAS 🐱🐈😻")
        for c in (mascotas):
            print(c["nombre"], c["raza"], c["peso"])
        print()        


# === PROGRAMA PRINCIPAL ===

def menu():
    while True:
        print("=== AGENDA  ===")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Agregar mascota")        
        print("4. Mostrar mascotas")        
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            mostrar_contactos()
        if opcion == "3":
            agregar_mascota()
        elif opcion == "4":
            mostrar_mascotas()            
        elif opcion == "0":
            print("👋  Saliendo del programa...")
            break
        else:
            print("⚠️  Opción no válida.\n")
# Ejecutar menú principal
menu()
