import csv
import random
from faker import Faker

# Inicializamos Faker
fake = Faker('es_ES')

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
        print("\n=== LISTA DE CONTACTOS ===")
        for i, c in enumerate(contactos, start=1):
            print(f"{i}. {c['nombre']} - {c['telefono']} - {c['email']}")
        print()

def buscar_contacto():
    nombre = input("Ingrese el nombre a buscar: ")
    encontrado = False
    for c in contactos:
        if c["nombre"].lower() == nombre.lower():
            print(f"✅ Contacto encontrado: {c['nombre']} - {c['telefono']} - {c['email']}")
            encontrado = True
            break
    if not encontrado:
        print("❌ Contacto no encontrado.\n")

def generar_contactos_falsos():
    cantidad = random.randint(1000, 1200)
    for _ in range(cantidad):
        contacto = {
            "nombre": fake.name(),
            "apellido": fake.last_name(),            
            "telefono": fake.phone_number(),
            "email": fake.email(),
            "direccion": fake.address(),
            "edad": fake.random_int(min=0, max=100)              
        }
        contactos.append(contacto)
    print(f"✅ Se generaron {cantidad} contactos falsos.\n")

def guardar_csv():
    with open("contactos.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "apellido", "telefono", "email", "direccion", "edad"])
        escritor.writeheader()
        escritor.writerows(contactos)
    print("✅ Contactos guardados en contactos.csv\n")

def cargar_csv():
    try:
        with open("contactos.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                contactos.append(dict(fila))
        print("✅ Contactos cargados desde contactos.csv\n")
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo contactos.csv\n")

# === PROGRAMA PRINCIPAL ===
def menu():
    while True:
        print("=== AGENDA DE CONTACTOS ===")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Generar contactos falsos")
        print("5. Guardar en CSV")
        print("6. Cargar desde CSV")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            generar_contactos_falsos()
        elif opcion == "5":
            guardar_csv()
        elif opcion == "6":
            cargar_csv()
        elif opcion == "0":
            print("👋 Saliendo del programa...")
            break
        else:
            print("⚠️ Opción no válida.\n")

# Ejecutar menú principal
menu()
