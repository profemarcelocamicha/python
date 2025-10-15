import tkinter as tk
from tkinter import messagebox

def saludar():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    if nombre.strip() == "" or apellido.strip() == "":
        messagebox.showwarning("Campos vacíos", "Por favor ingrese nombre y apellido.")
    else:
        mensaje = f"Hola, {nombre} {apellido}!"
        messagebox.showinfo("Saludo", mensaje)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Saludo con nombre y apellido")
ventana.geometry("600x400")

# Etiquetas y campos de texto
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_apellido = tk.Label(ventana, text="Apellido:")
label_apellido.pack(pady=5)
entry_apellido = tk.Entry(ventana)
entry_apellido.pack()

# Botones
boton_saludar = tk.Button(
    ventana,
    text="Saludar",
    command=saludar
)
boton_saludar.pack(pady=50)

# Iniciar loop de la ventana
ventana.mainloop()

