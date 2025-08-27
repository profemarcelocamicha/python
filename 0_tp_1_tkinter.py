import tkinter as tk
from tkinter import simpledialog, messagebox
import csv
import random
from faker import Faker

fake = Faker()
contactos = []

# === FUNCIONES ===

def agregar_contacto():
    nombre = simpledialog.askstring("Agregar contacto", "Ingrese nombre:")
    telefono = simpledialog.askstring("Agregar contacto", "Ingrese teléfono:")
    email = simpledialog.askstring("Agregar contacto", "Ingrese email:")
    if nombre and telefono and email:
        contacto = {"nombre": nombre, "telefono": telefono, "email": email}
        contactos.append(contacto)
        messagebox.showinfo("Éxito", "Contacto agregado con éxito.")

def mostrar_contactos():
    texto.delete("1.0", tk.END)  # Limpiar área de texto
    if not contactos:
        texto.insert(tk.END, "⚠️ No hay contactos cargados.\n")
    else:
        texto.insert(tk.END, "=== LISTA DE CONTACTOS ===\n")
        for i, c in enumerate(contactos, start=1):
            texto.insert(tk.END, f"{i}. {c['nombre']} - {c['telefono']} - {c['email']}\n")

def buscar_contacto():
    nombre = simpledialog.askstring("Buscar contacto", "Ingrese el nombre:")
    if not nombre:
        return
    for c in contactos:
        if c["nombre"].lower() == nombre.lower():
            messagebox.showinfo("Contacto encontrado", f"{c['nombre']} - {c['telefono']} - {c['email']}")
            return
    messagebox.showwarning("No encontrado", "El contacto no existe.")

def generar_contactos_falsos():
    cantidad = random.randint(3, 10)
    for _ in range(cantidad):
        contacto = {
            "nombre": fake.name(),
            "telefono": fake.phone_number(),
            "email": fake.email()
        }
        contactos.append(contacto)
    messagebox.showinfo("Éxito", f"Se generaron {cantidad} contactos falsos.")

def guardar_csv():
    with open("contactos.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "telefono", "email"])
        escritor.writeheader()
        escritor.writerows(contactos)
    messagebox.showinfo("Éxito", "Contactos guardados en contactos.csv")

def cargar_csv():
    try:
        with open("contactos.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                contactos.append(dict(fila))
        messagebox.showinfo("Éxito", "Contactos cargados desde contactos.csv")
    except FileNotFoundError:
        messagebox.showwarning("Error", "No se encontró el archivo contactos.csv")

# === INTERFAZ GRÁFICA ===
ventana = tk.Tk()
ventana.title("Agenda de Contactos")
ventana.geometry("500x400")

# Frame de botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(side="left", padx=10, pady=10)

btn1 = tk.Button(frame_botones, text="Agregar contacto", width=20, command=agregar_contacto)
btn1.pack(pady=5)
btn2 = tk.Button(frame_botones, text="Mostrar contactos", width=20, command=mostrar_contactos)
btn2.pack(pady=5)
btn3 = tk.Button(frame_botones, text="Buscar contacto", width=20, command=buscar_contacto)
btn3.pack(pady=5)
btn4 = tk.Button(frame_botones, text="Generar falsos", width=20, command=generar_contactos_falsos)
btn4.pack(pady=5)
btn5 = tk.Button(frame_botones, text="Guardar en CSV", width=20, command=guardar_csv)
btn5.pack(pady=5)
btn6 = tk.Button(frame_botones, text="Cargar desde CSV", width=20, command=cargar_csv)
btn6.pack(pady=5)

# Área de texto para mostrar contactos
texto = tk.Text(ventana, wrap="word")
texto.pack(side="right", expand=True, fill="both", padx=10, pady=10)

ventana.mainloop()
