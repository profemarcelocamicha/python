import tkinter as tk
from tkinter import messagebox
import csv

def guardar(nombre, apellido, telefono):
    if nombre.strip() == "" or apellido.strip() == "" or telefono.strip() == "":
        messagebox.showwarning("Campos vacíos", "Debe completar todos los campos antes de guardar.")
    else:
        with open('datos_usuarios.csv', 'a', newline='', encoding='utf-8') as archivo:
            campos = ['nombre', 'apellido', 'telefono']
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writerow({
                "nombre": nombre,
                "apellido": apellido,
                "telefono": telefono
            })
        messagebox.showinfo("Guardado", "Datos guardados en datos_usuarios.csv")
        limpiar_campos()

def limpiar_campos():
    """Vacía todos los campos de texto."""
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_nombre.focus()  # vuelve el cursor al primer campo

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Saludo con nombre y apellido")
ventana.geometry("600x400")
ventana.resizable(False, False)

# Etiquetas y campos de texto
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_apellido = tk.Label(ventana, text="Apellido:")
label_apellido.pack(pady=5)
entry_apellido = tk.Entry(ventana)
entry_apellido.pack()

label_telefono = tk.Label(ventana, text="Teléfono:")
label_telefono.pack(pady=5)
entry_telefono = tk.Entry(ventana)
entry_telefono.pack()

# Botones
boton_guardar = tk.Button(
    ventana,
    text="Guardar",
    command=lambda: guardar(entry_nombre.get(), entry_apellido.get(), entry_telefono.get())
)
boton_guardar.pack(pady=50)

# Iniciar loop de la ventana
ventana.mainloop()

